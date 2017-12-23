from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
import django.views.decorators.http as ht


def main(request):
    typpe = request.is_secure()
    response = HttpResponse('Hello: %s ' % typpe)
    print(response.status_code, response.charset, response.reason_phrase)

    return response
