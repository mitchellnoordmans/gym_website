from django.shortcuts import render, redirect
from .models import BlogPost, Trainer, GroupLessons, MembershipPlan, News
from .forms import ContactForm
from django.core.mail import EmailMessage
import os

def home(request):
    news_post = News.objects.all()
    return render(request, 'home.html', {'news_post': news_post})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the homepage after form submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def personal_trainer(request):
    trainers = Trainer.objects.all()
    return render(request, 'personal_trainers.html', {'trainers': trainers})

def membership_plans(request):
    memberships = MembershipPlan.objects.all()
    return render(request, 'membership_plans.html', {'memberships': memberships})

def roster(request):
    return render(request, 'roster.html')

def group_lessons(request):
    group_lessons = GroupLessons.objects.all()
    return render(request, 'group_lessons.html', {'group_lessons': group_lessons})

def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def about_location(request):
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')
    
    # Get a list of all image files in the directory
    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

    # Pass the list of image filenames to the template context
    context = {'image_files': image_files}
    return render(request, 'about_location.html', context)

def services_sauna(request):
    return render(request, 'services_sauna.html')

def services_fysiotherapy(request):
    return render(request, 'services_fysiotherapy.html')

def services_sportmassage(request):
    return render(request, 'services_sportmassage.html')