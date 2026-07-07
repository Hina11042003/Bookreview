from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from celery.result import AsyncResult
from .models import Book
from .forms import BookForm
from .tasks import send_book_added_email


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            user_email = form.cleaned_data['submitted_by_email']
            task = send_book_added_email.delay(book.title, book.author, user_email)
            request.session['pending_email_task'] = task.id
            messages.success(request, f'🎉 "{book.title}" has been added successfully!')
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    task_id = request.session.pop('pending_email_task', None)  # only shows right after creation
    return render(request, 'book/book_detail.html', {'book': book, 'task_id': task_id})


def check_email_status(request, task_id):
    result = AsyncResult(task_id)
    return JsonResponse({'status': result.status})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book-detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book-list')
    return render(request, 'book/book_confirm_delete.html', {'book': book})