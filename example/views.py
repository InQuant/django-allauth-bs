from allauth.account.forms import LoginForm
from django.shortcuts import render

from allauth_bs.forms import BSForm
from django import forms


class TestForm(BSForm):
    CHOICES = (
        ('yes', 'yes'),
        ('no', 'no'),
    )

    first_name = forms.CharField(help_text='Test', label='test', label_suffix='yo')
    last_name = forms.CharField(initial='test', label='test')
    c = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    t = forms.BooleanField()


def helloworld(request):
    form = TestForm()
    return render(request, 'example/test.html', context={
        'form': form
    })