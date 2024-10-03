from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import Relationship, User, Post, Like, Comment
from .forms import PostForm, CommentForm

def index(request):
    login_form = AuthenticationForm()
    signup_form = UserCreationForm()

    # Handle login form submission
    if 'login' in request.POST:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data.get('username'),
                password=login_form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')  # Success message
                return redirect('dashboard')  # Redirect to dashboard after login
            else:
                messages.error(request, 'No user found with this username or incorrect password.')  # Incorrect username or password
        else:
            messages.error(request, 'Invalid username or password.')  # General form error

    # Handle signup form submission
    elif 'signup' in request.POST:
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            messages.success(request, 'Sign up successful! You are now logged in.')  # Sign up success message
            return redirect('dashboard')  # Redirect to dashboard after sign-up
        else:
            messages.error(request, 'Invalid signup details.')  # General signup error

    return render(request, 'index.html', {
        'login_form': login_form,
        'signup_form': signup_form,
    })

def logout_view(request):
    messages.get_messages(request).used = True  # Clear previous messages
    auth_logout(request)
    messages.success(request, 'Sad to see you go!')
    return redirect('index')

def dashboard(request):
    user = request.user  # Get the currently logged-in user
    if not user.is_authenticated:
        return redirect('index') 
    print(f"User: {user.username}")
    '''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user  # Assign the post to the current user
            post.save()
            return redirect('dashboard')  # Redirect to the dashboard after the post is created
    else:
        form = PostForm()

    # Retrieve all posts from all users (or filter as needed)
    posts = Post.objects.all()

    return render(request, 'dashboard.html', {
        'user': user,
        'form': form,
        'posts': posts,  # Pass the posts to the template
    })
    '''
    if request.method == 'POST' and 'submit_post' in request.POST:
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = user
            post.save()
            return redirect('dashboard')

    # Handle comment submission
    elif request.method == 'POST' and 'submit_comment' in request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            comment = comment_form.save(commit=False)
            comment.user = user
            comment.post = post
            comment.save()
            return redirect('dashboard')

    # Handle like action
    elif request.method == 'POST' and 'like_post' in request.POST:
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        liked = Like.objects.filter(user=user, post=post).exists()

        if liked:
            Like.objects.filter(user=user, post=post).delete()  # Unlike
        else:
            Like.objects.create(user=user, post=post)  # Like
        return redirect('dashboard')

    else:
        post_form = PostForm()
        comment_form = CommentForm()

    posts = Post.objects.all()
    liked_posts = Like.objects.filter(user=user).values_list('post_id', flat=True)

    return render(request, 'dashboard.html', {
        'user': user,
        'post_form': post_form,
        'comment_form': comment_form,
        'posts': posts,
        'liked_posts': liked_posts,  # Pass liked posts for conditional rendering
    })

def user_list(request):
    user = request.user  # Get the currently logged-in user
    if not user.is_authenticated:
        return redirect('index') 
    # Exclude the logged-in user from the list of users
    users = User.objects.exclude(id=request.user.id)

    # Get a list of users the current user is following
    following = Relationship.objects.filter(follower=request.user).values_list('following', flat=True)

    return render(request, 'user_list.html', {
        'users': users,
        'following': following,
    })
def follow_unfollow(request, user_id):
    try:
        target_user = User.objects.get(id=user_id)
        # just for double checking though we removed the user from the list
        if request.user == target_user:
            # Prevent users from following themselves
            messages.warning(request, "You cannot follow yourself.")
            return redirect('user_list')

        # Check if the logged-in user is already following the target user
        relationship = Relationship.objects.filter(follower=request.user, following=target_user).first()

        if relationship:
            # If the relationship exists, unfollow
            relationship.delete()
            messages.success(request, f'You have unfollowed {target_user.username}.')
        else:
            # If no relationship exists, create a new follow
            Relationship.objects.create(follower=request.user, following=target_user)
            messages.success(request, f'You are now following {target_user.username}.')

        return redirect('user_list')

    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('user_list')


'''
# other stuff
from .forms import ReportForm

def map(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')  # Redirect to a list of reports
    else:
        form = ReportForm()
    return render(request, 'result.html', {'form': form})
'''
def map_view(request):
    return render(request, 'maps.html')
