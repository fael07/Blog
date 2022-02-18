from ast import FunctionDef
from accounts.models import User
from ..forms.for_fields import set_slug
from django.contrib import auth
from ..utils.main import gets



def validate_login(request, process: dict):
    user_type, password = gets(request.POST, process['type'], 'password')
    filter_obj = {process['type']: user_type}
    
    user_for_login = User.objects.filter(**filter_obj).first()
    
    if user_for_login is None:
        return  {'status': 'invalid', 'errors': {process['type']: process['error_message']}}

    user = auth.authenticate(request, username=user_for_login.username, password=password)
    
    if user is not None:
        return {'status': 'valid', 'errors': {}, 'user': user}
    else:
        return {'status': 'invalid', 'errors': {'password': 'Senha incorreta'}}

def login(request, user):
    auth.login(request, user)

    
    
    
def create_user_with_email(fields: dict):
    new_user = User(
        username=fields['email'], name=fields['name'].title(),
        email=fields['email'], slug=set_slug(fields['name'])
    )
    new_user.set_password(fields['password'])
    new_user.save()
    
    
    
def check_password(request, current_password):
    current_password_value = request.POST.get(current_password)
    user = auth.authenticate(request, username=request.user.username, password=current_password_value)
    if user is not None:
        return {'status': 'valid', 'errors': {}}
    else:
        return {'status': 'invalid', 'errors': { current_password: 'Senha incorreta' }}


def change_password(request, new_password: str):
    new_password_value = request.POST.get(new_password)
    user = request.user
    user.set_password(new_password_value)
    user.save()


def logout(request):
    auth.logout(request)
    

def create_login_save(request, obj: dict):
    request.session['user_save'] = {}
    for key in obj.keys():
        match str(type(obj[key])):

            case "<class 'str'>":
                attribute_name = obj[key]
                request.session['user_save'][key] = getattr(request.user, attribute_name)
                
            case "<class 'function'>":
                get_atribute_function: function = obj[key]
                request.session['user_save'][key] = get_atribute_function(request.user)