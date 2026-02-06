from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView,UpdateView
from .models import Student
from .forms import StudentForm
from django.urls import reverse_lazy

# Create your views here.,

# CREATE

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

# READ

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'

# UPDATE

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')

#DELETE

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_detail_delete.html'
    success_url = reverse_lazy('student_list')