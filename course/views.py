from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course


def index(request):
    context = {"all_courses": Course.objects.all()}
    return render(request, "index.html", context)


def create(request):
    if request.method == "POST":
        errors = Course.objects.validate(request.POST)
        if not errors:
            Course.objects.create(name=request.POST["name"], desc=request.POST["desc"])
        else:
            for msg in errors.values():
                messages.error(request, msg)
    return redirect("/")


def destroy(request, course_id):
    this_course = Course.objects.get(id=course_id)

    if request.method == "GET":
        context = {"this_course": this_course}
        return render(request, "delete.html", context)

    elif request.method == "POST":
        if request.POST["confirm_delete"]:
            this_course.delete()

    return redirect("/")
