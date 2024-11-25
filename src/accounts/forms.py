from django import forms
from .models import User, Transaction

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class TransferForm(forms.Form):
    receiver = forms.ModelChoiceField(queryset=User.objects.all())
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    reason = forms.ModelChoiceField(queryset=Transaction.objects.all())

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'profile_picture']

