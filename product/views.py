from django.shortcuts import render
from product.models import Student, Course
from product.forms import StudentForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

def boolen_convertor(value):
    if value == "on":
        return True
    else :
        return False


# Create your views here.

def students_list(request):
    student_data = Student.objects.all()

    return render(request, "product/student_list.html", 
        context= {
            "students": student_data,
            "page_title": "Student Profile"
        }
    )

def student_detail(request, pk):
    student_data = Student.objects.get(pk=pk)

    return render(request, "product/student_detail.html", 
        context= {
            "student": student_data,
            "page_title": "Student Profile"
        }
    )

def course_list(request):

    courses_data = Course.objects.all()
    
    context = {
        'courses': courses_data,
        'page_title': "Courses List"
    }
    
    return render(request, 'product/course_list.html', context)

class CourseListView(ListView):
    model = Course
    template_name = "product/course_list.html"
    context_object_name = "courses"

class StudentDetailsView(DetailView):
    model = Student
    template_name = "product/student_detail.html"
    context_object_name = "student"

class StudentUpdateView(UpdateView):
    model = Student
    template_name = "product/create_student.html"
    context_object_name = "student"
    form_class = StudentForm
    success_url = reverse_lazy("students_list")


class StudentCreateView(CreateView):
    model = Student
    template_name = "product/create_student.html"
    context_object_name = "student"
    form_class = StudentForm
    success_url = reverse_lazy("students_list")


def create_studnet(request):

    context = {
        "page_title": "Create Student",
        "courses": Course.objects.all(),
        "form": StudentForm()
    }

    if request.method == "POST":
        data = request.POST
        files = request.FILES

        form = StudentForm(data=data, files=files)
        if form.is_valid():
            form.save()
            context["message"] = "Student created successfully"
            return render(request, "product/create_student.html", context)
        else:
            context["message"] = form.errors

        context["students"] = Student.objects.all()
        return render(request, "product/create_student.html", context)

    else :
        context["students"] = Student.objects.all()
        return render(request, "product/create_student.html", context)    


from django.views import View

class StudentView(View):
    def get(self, request):
        context = {
            "page_title": "Create Student",
            "courses": Course.objects.all(),
            "form": StudentForm()
        }
        return render(request, "product/create_student.html", context)

    def post(self, request):
        context = {
            "page_title": "Create Student",
            "courses": Course.objects.all(),
            "form": StudentForm()
        }
        data = request.POST
        files = request.FILES
        form = StudentForm(data=data, files=files)
        if form.is_valid():
            form.save()
            context["message"] = "Student created successfully"
            return render(request, "product/create_student.html", context)
        else:
            context["message"] = form.errors
        return render(request, "product/create_student.html", context)
    
    
