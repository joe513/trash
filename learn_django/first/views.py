from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
import django.views.decorators.http as ht
from django.views.generic import *
from first.models import Sites


def main(request):
    typpe = request.is_secure()
    response = HttpResponse('Hello: %s ' % typpe)
    print(response.status_code, response.charset, response.reason_phrase)

    return response


class MyList(ListView):

    model = Sites
    context_object_name = 'sites'


class MyView(View):

    http_method_names = ['get', 'head']

