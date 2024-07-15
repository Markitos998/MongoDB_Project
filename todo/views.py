from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ToDoItem
from .forms import ToDoItemForm
from bson.objectid import ObjectId
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

class AllToDos(ListView):
    template_name = "todo/index.html"
    context_object_name = 'todos'

    def get_queryset(self):
        return ToDoItem.objects.all()

class TodayToDos(ListView):
    template_name = "todo/today.html"
    context_object_name = 'todos'

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date=date.today())

class CreateToDoItem(CreateView):
    form_class = ToDoItemForm
    template_name = 'todo/create_todoitem.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        ToDoItem(
            text=form.cleaned_data['text'],
            due_date=form.cleaned_data['due_date']
        ).save()
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

class UpdateToDoItem(UpdateView):
    form_class = ToDoItemForm
    template_name = 'todo/update_todoitem.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return ToDoItem.objects.get(id=ObjectId(self.kwargs['pk']))

    def form_valid(self, form):
        obj = self.get_object()
        obj.text = form.cleaned_data['text']
        obj.due_date = form.cleaned_data['due_date']
        obj.save()
        return HttpResponseRedirect(self.success_url)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form = self.form_class(request.POST, initial={'text': obj.text, 'due_date': obj.due_date})
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        form = self.form_class(initial={'text': obj.text, 'due_date': obj.due_date})
        return render(request, self.template_name, {'form': form})

class DeleteToDoItem(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return ToDoItem.objects.get(id=ObjectId(self.kwargs['pk']))

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return HttpResponseRedirect(self.success_url)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
