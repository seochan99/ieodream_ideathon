from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignupForm(forms.Form):
    model = User

    def signup(self, request, user):
        profile = Profile()
        profile.user = user
        profile.save()
        user.save()
        return user

# 프로필사진을 업데이트할 때 사용자의 정보도 같이 업데이트 할 수 있도록 사용자정보에 대한 폼, 프로필에 대한 폼 생성
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name']


class ProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False) # 선택적으로 입력할 수 있음.
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']