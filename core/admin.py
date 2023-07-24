from django.contrib import admin

# Register your models here.

from .models import Trainer, MembershipPlan, GroupLessons, BlogPost, ContactForm, News


admin.site.register(Trainer)
admin.site.register(MembershipPlan)
admin.site.register(GroupLessons)
admin.site.register(BlogPost)
admin.site.register(ContactForm)
admin.site.register(News)

