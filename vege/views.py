from django.shortcuts import render, redirect
from .models import Receipe

# Create your views here.


def receipes(request):
    if request.method == 'POST':
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        # Debug: Print what we received
        # print(f"Name: {receipe_name}")
        # print(f"Description: {receipe_description}")
        # print(f"Image: {receipe_image}")
        # print(f"Image size: {receipe_image.size if receipe_image else 'No image'}")
        
        # Save to database
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        print(f"Recipe '{receipe_name}' saved successfully!")
        return redirect('receipes')
        

    queryset=Receipe.objects.all()
    context = {
        'receipes':queryset
    }
    return render(request, 'receipes.html', context)