from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course', 'age']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter student name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter email address',
                'required': True
            }),
            'course': forms.TextInput(attrs={
                'placeholder': 'Enter course name',
                'required': True
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter age',
                'min': 1,
                'max': 100,
                'required': True
            }),
        }
        
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'course': 'Course/Program',
            'age': 'Age (years)',
        }
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 5 or age > 100:
            raise forms.ValidationError("Age must be between 5 and 100")
        return age
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if self.instance.pk is None:
            if Student.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already registered")
        else:  
            if Student.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("This email is already registered")
        return email

