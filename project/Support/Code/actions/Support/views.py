from django.views.generic import View


class BaseView(View):
    tc = {} # template context
    rc = {} # request context