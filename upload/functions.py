import os
import csv
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
    # p.save()
    return


def viewall():
    avenger = avengers.objects.values()
    dict={}
    dict['all'] = list(avenger)

    # for each in avenger:
    #     print(each.name, each.power)
    return dict