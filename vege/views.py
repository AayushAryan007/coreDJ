from django.shortcuts import render, redirect, get_object_or_404
from .models import Receipe
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def receipes(request):
    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        # Save to database
        Receipe.objects.create(
            user=request.user,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        print(f"Recipe '{receipe_name}' saved successfully!")
        return redirect('receipes')
    
    # Handle search
    search_query = request.GET.get('search', '')
    if search_query:
        queryset = Receipe.objects.filter(user=request.user, receipe_name__icontains=search_query)
    else:
        queryset = Receipe.objects.filter(user=request.user)
    
    context = {
        'receipes': queryset,
        'search_query': search_query
    }
    return render(request, 'receipes.html', context)


def edit_recipe(request, recipe_id):
    receipe = get_object_or_404(Receipe, id=recipe_id)
    
    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        # Update fields
        receipe.receipe_name = receipe_name
        receipe.receipe_description = receipe_description
        
        # Only update image if a new one is uploaded
        if receipe_image:
            receipe.receipe_image = receipe_image
        
        receipe.save()
        print(f"Recipe '{receipe_name}' updated successfully!")
        return redirect('receipes')
    
    context = {'receipe': receipe}
    return render(request, 'edit_receipe.html', context)


def delete_recipe(request, recipe_id):
    try:
        recipe = Receipe.objects.get(id=recipe_id)
        recipe.delete()
        print(f"Recipe '{recipe.receipe_name}' deleted successfully!")
    except Receipe.DoesNotExist:
        print(f"Recipe with id {recipe_id} not found")
    
    return redirect('receipes')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('receipes')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def register_page(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Here you would typically create the user
        user = User(username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        print(f"User '{username}' registered successfully!")
        return redirect('login')
    return render(request, 'register.html')