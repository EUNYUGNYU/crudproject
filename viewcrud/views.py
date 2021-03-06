from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request,'viewcrud/index.html')

def read(request):
    blogs=Blog.objects.all()
    return render(request,'viewcrud/funccrud.html',{'blogs':blogs})

def create(request):
    #새로운 데이터, 블로그 글 저장 ==POST
    if request.method == 'POST':
    #입력된 블로그 글들을 저장해라
        form=NewBlog(request.POST)
        if form.is_valid:
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()

        return redirect('home')

    # 글쓰기 페이지를 띄워주는 역할== GET(!=POST)
    else:
    #단순히 입력받을 수 있는 form을 띄워주라
        form = NewBlog()
        return render(request,'viewcrud/new.html', {'form':form})

def update(request,pk):
    #어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog=get_object_or_404(Blog, pk=pk)

    #해당하는 블로그 객체 번호에 맞는 입력공간
    form=NewBlog(request.POST, instance=blog) #객체는 위에 있는 블로그 객체

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'viewcrud/new.html', {'form':form})


def delete(request,pk):
    blog=get_object_or_404(Blog, pk=pk) #기본키명이 pk
    blog.delete()
    return redirect('home')


