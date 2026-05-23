from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ProfileCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        
        #  campos extras do Profile:
        fields = UserCreationForm.Meta.fields + ('email','curso')