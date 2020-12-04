# Welcome to django-allauth-bs

Small app to use [django-allauth](https://github.com/pennersr/django-allauth) with bootstrap forms.

We simply override  the `as_p` method of all allauth forms, so we din't had to change templates or anything else.
Therefore we used our [django-forms-bs](https://github.com/InQuant/django-forms-bs) which simply adds an
`as_bootstrap()` method to django standard forms.

## Installation

`pip install git+https://github.com/InQuant/django-allauth-bs`


## Use / Configuration

1.  add `allauth-bs` below to `allauth` in `INSTALLED_APPS` settings.
1.  Set allauth form settings to
	```python
	ACCOUNT_FORMS = {
	    'login': 'allauth_bs.forms.BSLoginForm',
	    'signup': 'allauth_bs.forms.BSSignupForm',
	    'add_email': 'allauth_bs.forms.BSAddEmailForm',
	    'change_password': 'allauth_bs.forms.BSChangePasswordForm',
	    'set_password': 'allauth_bs.forms.BSSetPasswordForm',
	    'reset_password': 'allauth_bs.forms.BSResetPasswordForm',
	    'reset_password_from_key': 'allauth_bs.forms.BSResetPasswordKeyForm',
	    'disconnect': 'allauth_bs.forms.BSDisconnectForm',
	}
	```
1.  Extend your scss e.g. with:
	```scss
	button, input[type=submit] { @extend .btn, .btn-primary; }
	```
1.  Put a `account/base.html` which provides a `content` block below your apps template dir, e.g.:
	```html
	{# extend e.g. your own base.html menu and footer #}
	{% extends "base.html" %}

	{% block main %}
	  <div class="container">
		{% block content %}{% endblock %}
	  </div>
	{% endblock main %}
	```
