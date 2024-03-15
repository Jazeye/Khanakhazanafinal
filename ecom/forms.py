from django import forms
from django.contrib.auth.models import User
from . import models
from django.core.exceptions import ValidationError


class CustomerUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain only letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain only letters.")
        return last_name

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['address', 'mobile', 'profile_pic']

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if len(mobile) != 10 or not mobile.isdigit():
            raise forms.ValidationError("Mobile number must be 10 digits.")
        return mobile

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile = forms.CharField(max_length=10)
    Address = forms.CharField(max_length=500)

    def clean_Mobile(self):
        mobile = self.cleaned_data.get('Mobile')
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be a 10-digit integer.")
        return mobile
#feedback form
def validate_name(value):
    if value and not value.isalpha():
        raise ValidationError("Name must contain only letters.")

class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].validators.append(validate_name)

    class Meta:
        model = models.Feedback
        fields = ['name', 'feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page

def validate_name(value):
    if not value.isalpha():
        raise ValidationError("Name must contain only letters.")

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30, validators=[validate_name])
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

