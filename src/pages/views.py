from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    output_str = f'<h1>Home View</h1><br> ' \
                 f'<h2>Request: {str(request)[1:-1]} </h2><br>' \
                 f'<h2>User: {request.user}</h2>'

    return HttpResponse(output_str)


def contact_view(request, *args, **kwargs):
    output_str = f'<h1>Contact View</h1><br> ' \
                 f'<h2>Request: {str(request)[1:-1]} </h2><br>' \
                 f'<h2>User: {request.user}</h2>'

    return HttpResponse(output_str)


def about_view(request, *args, **kwargs):
    output_str = f'<h1>About View</h1><br> ' \
                 f'<h2>Request: {str(request)[1:-1]} </h2><br>' \
                 f'<h2>User: {request.user}</h2>'

    return HttpResponse(output_str)


def social_view(request, *args, **kwargs):
    output_str = f'<h1>Social View</h1><br> ' \
                 f'<h2>Request: {str(request)[1:-1]} </h2><br>' \
                 f'<h2>User: {request.user}</h2>'

    return HttpResponse(output_str)