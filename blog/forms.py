from dal import autocomplete
from django import forms

from .models import *


class CommentCreateForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'comment'}))
    rating = forms.FloatField(label='Overall Rating')

    class Meta:
        model = Comment
        fields = ['content', 'rating']


class TagCreateForm(forms.ModelForm):
    tag = forms.CharField(label="Tags")

    class Meta:
        model = Comment
        fields = ['tag']


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='Title')
    content = forms.CharField(label='Content', widget=forms.Textarea)
    post_image = forms.ImageField(label='Photo')
    price = forms.IntegerField(label='Price')

    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image', 'price']
        widgets = {
            "tags": autocomplete.ModelSelect2Multiple(url='tags_autocomplete')
        }


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = [
            "start_date",
            "end_date",
            "category",
            "discount",
            "usage",
        ]
        widgets = {
            "start_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "end_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            "discount": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "usage": forms.DateInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }

    def clean(self):
        """
            - Check start_date can not be greater than end_date
            - Check for percentage-based coupon discount is not greater than 100%
        """
        start_date = self.cleaned_data.get("start_date", None)
        end_date = self.cleaned_data.get("end_date", None)

        if start_date > end_date:
            raise forms.ValidationError(
                "Start Date {} can not be greater than End Date {}.".format(
                    start_date, end_date)
            )

        coupon_category = self.cleaned_data.get("category", None)
        discount = self.cleaned_data.get("discount", None)

        if coupon_category == "P" and discount > 100.00:
            raise forms.ValidationError(
                "Discount can not be greater than 100 for percentage based coupon"
            )


class CheckCouponForm(forms.Form):
    Coupon = forms.CharField(max_length=18, widget=forms.TextInput(
        attrs={
            "class": "form-control coupon",
            "placeholder": "Coupon code",
        }),label='')
