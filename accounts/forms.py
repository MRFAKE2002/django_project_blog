from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomCreationsForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
        

class CustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')
        
