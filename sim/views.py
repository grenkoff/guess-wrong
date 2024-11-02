import os

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.views import APIView
from . import models

from .models import SigninPage


@csrf_exempt
def sign_in(request):
    signin_view = SigninPage.get_instance()
    return render(request, 'sim/sign-in.html', {'signin_view': signin_view})


@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    print('Inside')
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
        )
    except ValueError:
        return HttpResponse(status=403)

    # In a real app, I'd also save any new user here to the database.
    # You could also authenticate the user here using the details from Google (https://docs.djangoproject.com/en/4.2/topics/auth/default/#how-to-log-a-user-in)
    request.session['user_data'] = user_data

    return redirect('pages:home')


def sign_out(request):
    del request.session['user_data']
    return redirect('pages:home')


@method_decorator(csrf_exempt, name='dispatch')
class AuthGoogle(APIView):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    def post(self, request, *args, **kwargs):
        try:
            user_data = self.get_google_user_data(request)
        except ValueError:
            return HttpResponse("Invalid Google token", status=403)

        email = user_data["email"]
        user, created = models.User.objects.get_or_create(
            email=email, defaults={
                "username": email, "sign_up_method": "google",
                "first_name": user_data.get("given_name"),
            }
        )

        # Add any other logic, such as setting a http only auth cookie as needed here.
        return HttpResponse(status=200)

    @staticmethod
    def get_google_user_data(request: HttpRequest):
        token = request.POST['credential']
        return id_token.verify_oauth2_token(
            token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
        )
