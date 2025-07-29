from django.contrib import admin
from django.urls import path
from product.views import students_list, course_list, create_studnet, student_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path("students/", students_list, name="students_list"),
    path("", students_list, name="students_root"),
    path("courses/", course_list, name="course_list"),
    path("students/create/", create_studnet, name="create_student"),
    path("students/<int:pk>/", student_detail, name="student_detail"),
]
