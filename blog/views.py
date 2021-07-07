
from pickle import FALSE
from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render ,get_object_or_404
from django.urls import reverse_lazy ,reverse
from django.views.generic import ListView ,DetailView ,CreateView ,UpdateView ,DeleteView
from . models import Post ,Category ,Comment
from .form import PostForm ,EditForm 
# Create your views here.

# def home(requlest):
#     return render(request ,'home.html',{})

class HomeView(ListView):
    model = Post 
    template_name ='home.html'
    ordering = ['-post_date']
    cats = Category.objects.all()

    def get_context_data(self,*args, **kwargs):
        cat_menu =  Category.objects.all()
        contex =super(HomeView,self).get_context_data(*args, **kwargs)
        contex ['cat_menu'] =cat_menu
        return contex


def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get("post_id")  )
    liked = False
    if post.likes.filter( id =request.user.id ).exists():
        post.likes.remove(request.user)
        liked = FALSE
    else :
        post.likes.add(request.user)
        liked = True
        
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Article_Detail.html'
 
    def get_context_data(self,*args, **kwargs):
        cat_menu =  Category.objects.all()
        contex =super(ArticleDetailView,self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post ,id = self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id= self.request.user.id).exists():
            liked =True

        contex ['total_likes'] =total_likes
        contex ['cat_menu'] =cat_menu
        contex['liked']  =liked 
        return contex

class AddPostView(CreateView):
    model = Post 
    form_class = PostForm
    template_name = 'add_post.html'
    # fields= '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name ="update_post.html"
    # fields =['title','title_Tag' ,'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields ='__all__'
    success_url = reverse_lazy('home')



def  CategoryView(request,cats):
    cats =cats.replace('-',' ')
    category_posts = Post.objects.filter(category=cats)
    return render(request , 'category.html',{'cats':cats.title(),'category_posts':category_posts})



def  CategoryViewList(request):
    category_list = Category.objects.all()
    return render(request , 'category_list.html',{'category_list':category_list})



def AddComment(request, pk):
    
    if request.method =='POST':
        bd= request.POST.get('comment')
        post = Post.objects.get(id =pk)
        comment =Comment(body=bd, post= post ,user = request.user )
        comment.save()
        
    return redirect(f'/artical/{pk}' )






