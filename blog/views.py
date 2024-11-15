from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import *
from django.utils import timezone
from .forms import PostModelForm

def test1(request):
    #서비스 구현
    return HttpResponse('test1!')

def test2(request, id):
    print("타입 :",type(id))
    return HttpResponse(id)

def test3(request, year, mon, day):
    return HttpResponse(f'{year}년 {mon}월 {day}일')

# def list(request):
#     post_list = Post.objects.all()
#     titles = ''
#     for post in post_list:
#         titles += post.title
#     return HttpResponse(titles)


def list(request):
    post_list = Post.objects.all()
    search_key = request.GET.get("keyword")
    if search_key:
        post_list = Post.objects.filter(title__icontains=search_key)
    return render(request, 'blog/list.html', {'post_all':post_list, 'q':search_key})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment_list = post.comments.all()
    tag_list = post.tag.all()
    
    return render(request, "blog/detail.html", {'post':post, 'comment_all': comment_list, 'tag_list':tag_list})

def test4(request):
    d1 = timezone.now()
    var = """
    Miracles happen to only those who believe in them.
    Think like a man of action and act like man of thought.
    Courage is very important. Like a muscle, it is strengthened by use.
    Life is the art of drawing sufficient conclusions from insufficient premises.
    By doubting we come at the truth.
    A man that has no virtue in himself, ever envies virtue in others.
    When money speaks, the truth keeps silent.
    Better the last smile than the first laughter.
    """

    return render(request, 'blog/test4.html', {'score': 95, 'var':var, 'd1': d1})

def profile(request):
    user = User.objects.first()
    return render(request, 'blog/profile.html', {'user':user})

def tag_list(request, id):
    tag = Tag.objects.get(id=id)
    post_list = tag.post_set.all()
    return render(request, 'blog/list.html', {'post_all':post_list})

def test7(request):
    print('요청 방식 :', request.method)
    print('Get 방식으로 전달된 QueryString :', request.GET)
    print('Post방식으로 전달된 QueryString :', request.POST)
    print('업로드된 파일 :', request.FILES)
    return render(request, 'blog/form_test.html')

def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            print('======>',form.cleaned_data)
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect(post)
    else:
        form = PostModelForm()
        return render(request, 'blog/post_form.html', {'form':form})
    
    
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'blog/post_update.html', {'form':form})
    
def post_delete(request, id):
    post=get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list')
    else:
        return render(request, 'blog/post_delete.html', {'post':post}) 
    
    