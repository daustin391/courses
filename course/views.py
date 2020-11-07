from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def create(request):
    if request.method == "POST":
        pass
    else:
        return redirect("/")