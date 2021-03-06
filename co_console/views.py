from django.template.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
import os, sys, platform, subprocess

import commands

rt_env = os.environ.copy()
if len(settings.APPEND_PATH) > 0:
    if platform.system() == 'Darwin' or platform.system() == 'Linux':
        rt_env['PATH'] = ':'.join([':'.join(settings.APPEND_PATH), rt_env['PATH']])
    elif platform.system() == 'Windows':
        rt_env['PATH'] = ';'.join([';'.join(settings.APPEND_PATH), rt_env['PATH']])


def console(request):
    if commands.ip(request) not in settings.CONSOLE_WHITELIST:
        return HttpResponse('Unauthorized.', status=403)
    context = {
        'STATIC_URL': settings.STATIC_URL
    }
    context.update(csrf(request))
    return render_to_response('console.html', context)


def console_post(request):
    command = request.POST.get('command')
    if command:
        command_exec = command.split(' ')[0].split('.')[0]
        if not command_exec in settings.COMMAND_WHITELIST:
            data = 'Command Only Support:\n'
            data += '\n'.join(settings.COMMAND_WHITELIST)
        elif command_exec in settings.ARGS_REQUIRED and (len(command.split(' ')) < 2 or (len(command.split(' ')) == 2 and command.split(' ')[1] == '')):
            data = 'Command Arguments Required:\n'
            data += '\n'.join(settings.ARGS_REQUIRED)
        else:
            if command_exec in settings.COMMAND_MAPPING:
                command = command.replace(command_exec, settings.COMMAND_MAPPING[command_exec])
            if command_exec in commands.CUSTOM_COMMAND:
                data = commands.CUSTOM_COMMAND[command_exec](request)
            else:
                try:
                    data = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, env=rt_env, cwd=settings.CONSOLE_CWD)
                except subprocess.CalledProcessError as e:
                    data = e.output
        data = data.decode('utf-8')
        output = '%c(@olive)%' + data + '%c()'
    return HttpResponse(output)
