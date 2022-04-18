from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from .forms import QuoteForm
from django.views.generic import CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class CreateQuote(SuccessMessageMixin, CreateView):
    model = models.Quote
    form_class = QuoteForm
    template_name = 'getservice/quote.html'
    success_message = "Solicitação de orçamento enviada com sucesso. Entraremos em contacto em breve"

class QuoteDetailView(DetailView):
    model = models.Quote






    #Get
        #form

    #POST:
        # -csrf_token
        # - validate
        # - save
        # - redirect to a success page
