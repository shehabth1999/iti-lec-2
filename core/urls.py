from django.contrib import admin
from django.urls import path
from product.views import students_list, StudentUpdateView, CourseListView, StudentDetailsView, StudentCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("students/", students_list, name="students_list"),
    path("", students_list, name="students_root"),
    path("courses/", CourseListView.as_view(), name="course_list"),
    path("students/create/", StudentCreateView.as_view(), name="create_student"),
    path("students/update/<int:pk>/", StudentUpdateView.as_view(), name="update_student"),
    path("students/<int:pk>/", StudentDetailsView.as_view(), name="student_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)