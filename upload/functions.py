import os
import csv
from io import StringIO

import openpyxl
from django.http import HttpResponse

from .models import sheet


def parse_file(csv_file, name: str):
    # reader = csv.reader(csv_file, delimiter=',')
    first_row = 1
    list = []
    # print(reader)
    for row in csv_file:
        # for i in row:
            print(row)

    #     if first_row ==1 :
    #         p = sheet(header=list(row))
    #     else:
    #         list.append(list(row))
    # p = sheet(details=list)
    # p = sheet(name=name)
    # p.savdef


def export_xl(body):
    output = StringIO()
    w = openpyxl.Workbook(output)
    ws = w.create_sheet('sheet')
    for row in body:
        ws.append(row)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="newfile.xlsx"'
    w.save(response)
    return response