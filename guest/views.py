from django.shortcuts import render
from django.http import HttpResponse


def index(request, *args, **kwargs):
    return HttpResponse("<h1>Index</h1>")


def show(request, *args, **kwargs):
    return HttpResponse("<h1>Show</h1>")


def new(request, *args, **kwargs):
    return HttpResponse("<h1>New</h1>")


def create(request, *args, **kwargs):
    return HttpResponse("<h1>Create</h1>")


def edit(request, *args, **kwargs):
    return HttpResponse("<h1>Edit</h1>")


def update(request, *args, **kwargs):
    return HttpResponse("<h1>Update</h1>")


def destroy(request, *args, **kwargs):
    return HttpResponse("<h1>DELETE</h1>")
