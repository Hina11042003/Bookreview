from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=2)
def send_book_added_email(self, book_title, book_author, recipient_email):
    try:
        send_mail(
            subject='Book added successfully',
            message=f'Hi! Your book "{book_title}" by {book_author} was saved successfully to the Book Review System.',
            from_email=None,
            recipient_list=[recipient_email],
            fail_silently=False,  # important: don't swallow errors
        )
        return f'Confirmation sent to {recipient_email} for "{book_title}"'
    except Exception as exc:
        logger.error(f"Failed to send email to {recipient_email}: {exc}")
        raise self.retry(exc=exc, countdown=10)