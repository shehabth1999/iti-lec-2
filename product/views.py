from django.shortcuts import render
from product.models import Student, Course

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


def create_studnet(request):

    context = {
        "page_title": "Create Student",
        "courses": Course.objects.all()
    }

    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        age = data.get("age")
        email = data.get("email")
        is_active = boolen_convertor(data.get("is_active"))
        grade = data.get("grade")
        course_id = data.get("course")
        
        print(name, age, email, is_active, grade)
        
        # validate the data
        
        # create the data
        student = Student.objects.create(name=name, age=age, email=email, is_active=is_active, grade=grade, course_id=course_id)

        print("student.pk", student.pk)

        context["students"] = Student.objects.all()

        context["message"] = f"{name} created successfully"
        return render(request, "product/create_student.html", context)

    else :
        context["students"] = Student.objects.all()
        return render(request, "product/create_student.html", context)    
