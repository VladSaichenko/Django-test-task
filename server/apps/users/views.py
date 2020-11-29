from allauth.socialaccount.models import SocialToken, SocialAccount
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    user = SocialAccount.objects.get(user=request.user)
    context = {
        'access_token': SocialToken.objects.get(account=user, account__provider='facebook')
    }
    return render(request, 'users/profile.html', context=context)
