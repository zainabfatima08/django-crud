from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


class StudentCRUDView(View):
    model = None
    form_class = None  
    list_template = None 
    detail_template = None

    def get_queryset(self):
        return self.model.objects.all()
#READ
    def get(self, request, pk=None):

        if pk:
            obj = get_object_or_404(self.model, pk=pk)
            return render(
                request,
                self.detail_template,
                {'object': obj}
            )

        objects = self.get_queryset()
        form = self.form_class()
        return render(
            request,
            self.list_template,
            {'objects': objects, 'form': form}
        )
# CREATE 
    def post(self, request, pk=None):
        action = request.POST.get('action')

        if action == 'add':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
            return redirect('student_crud')
#UPDate
        if action == 'edit':
            obj_id = request.POST.get('object_id')
            obj = get_object_or_404(self.model, pk=obj_id)
            form = self.form_class(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            return redirect('student_crud')
#DELETE
        if action == 'delete':
            obj_id = request.POST.get('object_id')
            obj = get_object_or_404(self.model, pk=obj_id)
            obj.delete()
            return redirect('student_crud')

class CRUDView(StudentCRUDView):
    model = Student
    form_class = StudentForm
    list_template = 'students/student_list.html'