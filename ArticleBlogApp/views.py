from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def homeview(request):
    article = Article.objects.all() 
    return render(request, 'home.html', {'articles':article})


def aboutview(request):
    return render(request, 'about.html')

def article_details(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        # Handle the case where no matching article is found, e.g., show an error message
        print("Article not found for slug:", slug)
        return HttpResponse("Article not found")
    return render(request, 'articlelist_detail.html', { 'article': article })



@login_required(login_url='/login/')
def createarticle_view(request):

    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to create a new article
            article = form.save(commit=False)
            article.writter = request.user  # Set the writer to the current user
            article.save()
            return redirect('Articlelist')  # Redirect to article detail page
    else:
        form = CreateArticle()
    
    return render(request, 'createarticle.html', {'form': form})