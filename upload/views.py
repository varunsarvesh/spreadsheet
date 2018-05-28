from io import StringIO
import csv
import openpyxl

from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render

import spreadsheetupload
from upload import forms
from upload.functions import parse_file, viewall


def xlapp(request):
    return render(request, 'index.html')
    # return HttpResponse('Upload here')


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
        output = StringIO()
        w = openpyxl.Workbook(output)
        ws = w.create_sheet('sheet')

        # i=1
        for row in body:
            ws.append(row)
            # j=1
            # for value in row:
            #     ws.cell(row =i, column=j)
            #     j = j+1
            # i = i+1
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="newfile.xlsx"'
        w.save(response)
        return response
     return HttpResponse('uploaded')


def view(request):
    avenger = viewall()
    print(avenger)
    return render(request, 'view.html', {'avenger': avenger})
