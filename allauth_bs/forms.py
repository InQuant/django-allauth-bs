from allauth.account import forms as allauth_forms
from allauth.socialaccount.forms import DisconnectForm
from forms_bs.forms import BSForm


class AllAuthFormMixin(BSForm):
    def as_p(self):
        return self.as_bootstrap()


class BSLoginForm(allauth_forms.LoginForm, AllAuthFormMixin):
    pass


class BSSignupForm(allauth_forms.SignupForm, AllAuthFormMixin):
    pass


class BSAddEmailForm(allauth_forms.AddEmailForm, AllAuthFormMixin):
    pass


class BSChangePasswordForm(allauth_forms.ChangePasswordForm, AllAuthFormMixin):
    pass


class BSSetPasswordForm(allauth_forms.SetPasswordForm, AllAuthFormMixin):
    pass


class BSResetPasswordForm(allauth_forms.ResetPasswordForm, AllAuthFormMixin):
    pass


class BSResetPasswordKeyForm(allauth_forms.ResetPasswordKeyForm, AllAuthFormMixin):
    pass


class BSDisconnectForm(DisconnectForm, AllAuthFormMixin):
    pass
