from django.template.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
import subprocess
import sys


if len(settings.APPEND_PATH) > 0:
    sys.path.append(settings.APPEND_PATH)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def console(request):
    if get_client_ip(request) not in settings.CONSOLE_WHITELIST:
        return HttpResponse("Unauthorized.", status=403)
    context = {
        'STATIC_URL': settings.STATIC_URL
    }
    context.update(csrf(request))
    return render_to_response("console.html", context)


def console_post(request):
    command = request.POST.get("command")
    if command:
        command_exec = command.split(" ")[0]
        if not command_exec in settings.COMMAND_WHITELIST:
            data = "Command Only Support:\n"
            data += "\n".join(settings.COMMAND_WHITELIST)
        else:
            if command_exec in settings.COMMAND_MAPPING:
                command = command.replace(command_exec, settings.COMMAND_MAPPING[command_exec])
            try:
                data = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, cwd=settings.CONSOLE_CWD)
            except subprocess.CalledProcessError as e:
                data = e.output
        data = data.decode('utf-8')
        output = "%c(@olive)%" + data + "%c()"
    return HttpResponse(output)
