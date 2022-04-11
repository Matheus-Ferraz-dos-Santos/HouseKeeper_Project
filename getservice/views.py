from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import QuoteForm
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
def GetIndexPage(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quote submitted successfully.')
            return render(request, 'getservice/success.html', {'form': QuoteForm(request.GET)})
        else:
            messages.error(request, "Invalid form submission.")
            messages.error(request, form.errors)
    else:

        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'getservice/quote.html', context={'form':form, 'submitted':submitted})
