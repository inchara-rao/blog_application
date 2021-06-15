from django.forms import ModelForm
from .models import Create_article,register
from captcha.fields import CaptchaField



class article_form(ModelForm):
    class Meta:
        model= Create_article
        fields='__all__'


class register_form(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=register
        fields='__all__'