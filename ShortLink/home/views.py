from django.shortcuts import render, redirect,get_object_or_404
from .models import ShortenedURL


async def index(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        shortened_url = ShortenedURL.objects.create(original_url=original_url,)
        return redirect('shortened', pk=shortened_url.pk)
    else:
        return render(request,'index.html')



def shortened(request, pk):
    shortened_url = get_object_or_404(ShortenedURL, pk=pk)
    return redirect(shortened_url.original_url)