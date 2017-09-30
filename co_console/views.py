from django.template.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
import subprocess

def console(request):
    context = {
        'STATIC_URL': settings.STATIC_URL
    }
    context.update(csrf(request))
    return render_to_response("console.html", context)

def console_post(request):
    command = request.POST.get("command")
    if command:
        try:
            data = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            data = e.output
        data = data.decode('utf-8')
        output = "%c(@olive)%" + data + "%c()"
    return HttpResponse(output)
