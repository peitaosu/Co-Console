def help(request):
    data = """Co-Console is a Web-based Console.
About how to setup and use it, please get details from README.md."""
    return data

def ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_addr = x_forwarded_for.split(',')[0]
    else:
        ip_addr = request.META.get('REMOTE_ADDR')
    return ip_addr

CUSTOM_COMMAND = {
    "help": help,
    "ip": ip
}