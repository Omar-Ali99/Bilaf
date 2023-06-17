from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from users_app.models import Store
from django.contrib.auth.decorators import login_required



# Create your views here.
def home_page(request: HttpRequest):

    return render(request, 'main_app/home_page.html')

def base_page(request: HttpRequest):

    return render(request, 'main_app/base.html')

def about_us(request : HttpRequest):
    return render(request, 'main_app/about_us.html')


def about_project(request : HttpRequest):
    return render(request, 'main_app/about_project.html')

def pick_delv_policies(request : HttpRequest):
    return render(request, 'main_app/pickup_delivery_policy.html')


def search(request:HttpRequest):
    search_phrase = request.GET.get("search", "")
    store = Store.objects.filter(store_name__icontains = search_phrase) or Store.objects.filter(category__icontains = search_phrase)

    selected_filter = request.GET.get('filter')  # Get the selected filter value from the request
    filtered_data = Store.objects.all()  # Fetch all data initially
    
    if selected_filter:
        filtered_data = filtered_data.filter(category=selected_filter)  # Apply filter based on selected value
        
    context = {
        'filtered_data': filtered_data,
        'selected_filter': selected_filter,
        'store': store,
    }
    
    return render(request, 'main_app/search.html', context)

