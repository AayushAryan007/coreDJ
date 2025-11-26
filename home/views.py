from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse("<h1>Hello, world!</h1>")
    people= [
      { 'name': "Alice", 'age': 30 },
      { 'name': "Bob", 'age': 25 },
      { 'name': "Charlie", 'age': 35 },
      { 'name': "Diana", 'age': 28 },
      { 'name': "Ethan", 'age': 32 },
      { 'name': "Fiona", 'age': 27 },
      { 'name': "George", 'age': 29 },
      { 'name': "Hannah", 'age': 31 },
      { 'name': "Ian", 'age': 26 },
      { 'name': "Jane", 'age': 33 },
    ]
     
    text = """
    <h1>People Information</h1>
    <p>Welcome to our comprehensive people information management system. This application provides a detailed database of individuals with their essential information including names and ages. Our platform is designed to help you efficiently manage and view detailed records of all people in our system. Whether you're looking for specific individuals or browsing through our complete database, our user-friendly interface makes it easy to find what you need. Each person in our system is carefully catalogued with accurate information to ensure data integrity and reliability. We maintain strict standards for data quality and regularly update our records. Our team is committed to providing you with the most accurate and up-to-date information available. You can easily search, filter, and organize the data according to your preferences. Our system is secure, efficient, and designed for optimal user experience. Thank you for using our people management system.</p>
    """
    
    
    context = {
        'people': people,
        'text': text,
        'page': 'Home',
    }
    
    return render(request, 'home/index.html', context)

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Success! Your form has been submitted.</h1>")


def about_page(request):
    context = {'page': 'About Us'}
    return render(request, 'home/about.html',context)
    
def contact_page(request):
    context = {'page': 'Contact Us'}
    return render(request, 'home/contact.html', context)