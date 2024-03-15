from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


user = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = user
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = user
        fields = UserChangeForm.Meta.fields
