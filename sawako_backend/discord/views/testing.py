import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from dataclasses.errors.responses import Responses
from discord.database.test.Test import Test
from discord.database.test.TestForm import TestForm


@csrf_exempt
def test(request):
    if request.method == 'POST':
        print(request.POST)

        form = TestForm(request.POST, request.FILES)

        print(form.is_valid())

        if form.is_valid():
            form.save(commit=True)

        return HttpResponse(Responses.E404, content_type='application/json')
    else:
        test = Test.objects.get(pk=1)
        data = {
            'image': test.image.url
        }
        return HttpResponse(json.dumps(data), content_type='application/json')