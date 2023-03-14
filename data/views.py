""" views file for the data app """
from django.shortcuts import render
from django.http import JsonResponse
from config.models import *


def view(request, subid, refid):
    data = Data.objects.filter(substance_id=subid, reference_id=refid)
    sub = Substances.objects.get(id=subid)
    ref = References.objects.get(id=refid)
    return render(request, "../templates/data/view.html", {'data': data, 'sub': sub, 'ref': ref})


def json(request, subid, refid):
    data = Data.objects.filter(substance_id=subid, reference_id=refid)
    sub = Substances.objects.get(id=subid)
    ref = References.objects.get(id=refid)
    output = {}
    output.update({'substance': sub.name})
    output.update({'reference': ref.citation})
    output.update({'data': []})
    for datum in data:
        d = {}
        d.update({'value': datum.pka_value})
        d.update({'type': datum.pka_type})
        d.update({'temperature (°C)': datum.temp})
        d.update({'remarks': datum.remarks})
        output['data'].append(d)
    return JsonResponse(output, safe=False)