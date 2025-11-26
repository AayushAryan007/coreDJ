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


def delete_recipe(request, recipe_id):
    try:
        recipe = Receipe.objects.get(id=recipe_id)
        recipe.delete()
        print(f"Recipe '{recipe.receipe_name}' deleted successfully!")
    except Receipe.DoesNotExist:
        print(f"Recipe with id {recipe_id} not found")
    
    return redirect('receipes')