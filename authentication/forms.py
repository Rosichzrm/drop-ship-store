from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(f'Пользователь с логином: {username} не зарегистрирован!!!')

        if not self.user.check_password(password):
            raise forms.ValidationError(f'Пароль указан не верно!!!')

class RegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'account__login--input'
        self.fields['username'].widget.attrs.update(placeholder='Username')
        self.fields['email'].widget.attrs.update(placeholder='Email Addres')
        self.fields['password'].widget.attrs.update(placeholder='Password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }