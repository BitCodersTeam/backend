from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from dataclasses.errors.statuses import Status
from dataclasses.errors.responses import Responses
from discord.database.guild.GuildForm import GuildForm


@csrf_exempt
def add_guild(request):
    if request.method != 'POST':
        return JsonResponse(data=Responses.E400, status=Status.BadRequest)

    body = request.POST
    form = GuildForm(body)
    if form.is_valid():
        form.save(commit=True)

    return JsonResponse(data=Responses.O201)
