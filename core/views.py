from django.shortcuts import render
from .models import BlogPost, Trainer, GroupLessons, MembershipPlan
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def personal_trainer(request):
    trainers = Trainer.objects.all()
    return render(request, 'personal_trainers.html', {'trainers': trainers})

def membership_plans(request):
    membership = MembershipPlan.objects.all()
    return render(request, 'membership_plans.html', {'membership': membership})

def roster(request):
    return render(request, 'roster.html')

def group_lessons(request):
    group_lessons = GroupLessons.objects.all()
    return render(request, 'group_lessons.html', {'group_lessons': group_lessons})

def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})
