from django.shortcuts import render
from django.views import View
from .models import User


class StudentViews(View):
    def get(self, request):
        search = request.GET.get("search_student")
        print(search)
        if search is None:
            students = User.objects.all()
            context = {
                "students": students,
            }
            print("succes")
            return render(request, "student.html", context)

        else:
            students = User.objects.filter(first_name__icontains=search)
            if students:
                context = {
                    "students": students,
                    "search_student": search
                }
                return render(request, "student.html", context)
            else:
                return render(request, "student.html")


class AboutStudentView(View):
    def get(self, request, id):
        student = User.objects.get(pk=id)
        return render(request, "full_data_student.html", {"student": student})
