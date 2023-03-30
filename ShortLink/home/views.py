from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortenedURL
from asgiref.sync import sync_to_async
from .forms import ShortenURLForm
from django.contrib import messages
def create_short_url(original_url):
    shortened_url = ShortenedURL.create(original_url=original_url)
    return shortened_url

async def index(request):
    if request.method == 'POST':
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            shortened_url = await sync_to_async(create_short_url)(original_url)
            return await sync_to_async(render)(request, 'shortened.html', {
                'original_url': shortened_url.original_url,
                'shorted_url': 'http://easylink.pp.ua/' + shortened_url.shorted_url
            })
        else:
            messages.error(request, 'Please enter a valid URL.')
    else:
        form = ShortenURLForm()
    return await sync_to_async(render)(request, 'index.html', {'form': form})

@sync_to_async
def shortened(request, shorted_url):
    original_url = get_object_or_404(ShortenedURL, shorted_url=shorted_url).original_url
    return redirect(original_url)