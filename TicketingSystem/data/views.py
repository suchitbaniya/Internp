from django.shortcuts import render
from .models import api_data
from .task import call_api
from .services import check_data
from django.http import JsonResponse
import requests
from django.core.paginator import Paginator
from .forms import SearchForm
from django.forms import Form, CharField
from django import forms
from django.db.models import Q 




    

def display_data_from_db(request):
  
    call_api()
    
    table_data = api_data.objects.all()
    #paginator call
    paginator = Paginator(table_data,12)
    page_number = request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    #initialize form to be passed to the views for the input field to be visible
    # need to be checked
    form = SearchForm(request.POST)
    context = {'page_obj': page_obj,'form':form}

    if request.method == "POST":
        # get the data from the form 
        form = SearchForm(request.POST)
        print(form)
        if form.is_valid():
            #get the value passed in the from
            keyword = form.cleaned_data['keyword']
            choice = form.cleaned_data['Filter_by']
            # print(choice)
            # print(keyword)

            #major logic
            #filter that searches the database with the presence of the keyword with 
            table_data = api_data.objects.filter(Q(E_ID__icontains=keyword)|Q(OLT_Hostname__icontains=keyword))#and so on for all the data fields in the model api_data
            # print("table_data",table_data)
            #data needs to be shown in the paginator again for which new paginator is introduced
            paginator = Paginator(table_data,12)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            # append the new page_obj which contains the search result regarding that keyword 
            context = {"page_obj":page_obj ,'form':form }
            # print(context)


            #render the context in table1.html with the new context that we got from the search keyword
            return (render(request,'table1.html',context))

    
    
    return render( request,'table1.html',context)


# def checking_data(request):
#      if request.method == 'GET':
#         check_data()
#         return JsonResponse({'message': 'Data checked successfully.'})
#      else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=400)


def email(request):
    return render(request, 'compose_email.html')

def report(request):
    return render(request, 'report.html')

def comment(request):
    return render(request, 'comment.html') 
def status(request):
    return render(request, 'status.html')

   
