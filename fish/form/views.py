from django.shortcuts import render
from django.views.decorators.http import require_safe

@require_safe
def index(request):
    return render(request, "index.html")

def custom_404(request, exception=None):
    return render(request, "404.html", status=404)
