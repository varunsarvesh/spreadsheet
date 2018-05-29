from io import StringIO
import csv
import openpyxl

from django.core.exceptions import ValidationError
from django.http import HttpResponse, response
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

import spreadsheetupload
from upload import forms
from upload.functions import parse_file, export_xl


def xlapp(request):
    return render(request, 'index.html')
    # return HttpResponse('Upload here')


class Json(APIView):
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser, )

    def get(self):
        return Response({"data": "data"})


def upload(request):
    # with open('avengers.csv') as csvfile:
    #     parse_file(csvfile)
    form = forms.DocumentForm()
    return render(request, 'upload.html', {'form': form})


def uploading(request):
     if request.method == 'POST':
        # form = forms.DocumentForm(request.POST)
        file_name = 'docfile'
        wb = openpyxl.load_workbook(request.FILES[file_name])
        header = []
        body = []
        firstrow = 1
        wrksheet = wb.active
        print('-------')
        print(request.FILES[file_name].name)
        for row in wrksheet:
             list = []
             for ro in row:
                 list.append(ro.value)
             if firstrow == 1:
                 header.append(list)
             else:
                 body.append(list)
             firstrow = 0
        print(header)
        print(body)
        response = export_xl(body)
        return response
     return HttpResponse('uploaded')


def view(request):
    avenger = viewall()
    print(avenger)
    return render(request, 'view.html', {'avenger': avenger})
