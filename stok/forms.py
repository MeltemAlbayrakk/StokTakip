from django import forms
from .models import Devices
from django.contrib.auth.models import User


class StokForm(forms.ModelForm):
    def __init__(self, user=None, **kwargs):
        super(StokForm, self).__init__(**kwargs)

        self.fields["worker"].queryset = User.objects.filter(is_staff=False)

    """Form for the image model"""

    class Meta:
        model = Devices
        fields = (
            "brand",
            "image",
            "description",
            "serialnum",
            "employee",
            "category",
            "status",
            "arrival_date",
            "exit_date",
            "department",
            "worker",
            
        )
