from django import forms
from .models import Course, Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if Student.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Email already exists")
    #     return email

    # # def clean_age(self):
    # #     age = self.cleaned_data.get('age')
    # #     if age < 18:
    # #         raise forms.ValidationError("Age must be greater than 18")
    # #     if age > 100:
    # #         raise forms.ValidationError("Age must be less than 100")
    # #     return age

    # def clean(self):
    #     data = super().clean()  
    #     age = data.get('age')
    #     if age < 18:
    #         raise forms.ValidationError("Age must be greater than 18")
    #     if age > 100:
    #         raise forms.ValidationError("Age must be less than 100")
    #     return data
        
