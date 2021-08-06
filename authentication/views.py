#!/usr/bin/env python
######################################################################
# (Kevin Mukuna, August 2021)
#
# Authentication script. The script below is used for registering
# users,validated users and login
######################################################################

import json
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import login
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import View
from validate_email import validate_email
from .forms import UserUpdateForm, ProfileUpdateForm
from .utils import account_activation_token


class RegistrationView(View):
    """
    registration view, a view is simple an http response
    :return http response
    each function gives a brief explanation
    """

    def get(self, request):
        """
        :param request: http request
        :return: http response
        """
        return render(request, 'authentication/register.html')

    def post(self, request):
        """
        this method is used for getting user data, validating it
        and creating an account.
        The method send the user an activation link after registration
        and wait till the link has been activated, before saving the user.
        else it return the page again.
        :param request: http request
        """
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        company_address = request.POST['company_address']
        company_name = request.POST['company_name']
        company_number = request.POST['company_number']
        company_reg = request.POST['company_reg']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'authentication/register.html', context)

                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    company_name=company_name,
                    company_address=company_address,
                    company_number=company_number,
                    company_reg=company_reg,

                )
                user.set_password(password)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                email_body = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }

                link = reverse('activate', kwargs={
                    'uidb64': email_body['uid'], 'token': email_body['token']})

                email_subject = 'Activate your account'

                activate_url = 'http://' + current_site.domain + link

                email = EmailMessage(
                    email_subject,
                    'Hi ' + user.username + ', Please the link below to activate your account \n' + activate_url,
                    'noreply@semycolon.com',
                    [email],
                )
                email.send(fail_silently=False)
                messages.success(request, f"An Account activation link has ben sent to {user.email}")
                return redirect('login')

        return render(request, 'authentication/register.html')


class EmailValidationView(View):
    """
    this method is used to validate emails as the user is
    typing or submit an email.
    The method is being called by ajax to see if a user with
    that specific username already exists, as they type
    """

    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry, this email is registered. Use another.'}, status=409)
        return JsonResponse({'email_valid': True})


class UsernameValidationView(View):
    """
    this method is used to validate username as the user is
    typing.
    The method is being called by ajax to see if a user with
    that specific email already exists, as they type
    """

    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry, this username is taken. Try another.'}, status=409)
        return JsonResponse({'username_valid': True})


class VerificationView(View):
    """
    validate account by sending users an email with token
    for activation this method is used to for generating
    new unique tokens
    """

    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login' + '?message=' + 'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')


def activate(request, uidb64, token):
    """
    :param request: self explanatory
    :param uidb64: json encoding base 64 format
    :param token: reset token being created using the
                  password reset token generator to
                  ensure unique password token
                  is generated everytime
    :return: redirect the pages to login once the
             user clicks on their link to send an email
             or throws in an error
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('authentication/activated_account.html')
        HttpResponse('Thank you for your email confirmation. you will be redirected in 2 seconds')
        return redirect('redirect')

        # return redirect('authentication/login.html')
    else:
        return HttpResponse('Activation link is invalid!')


def redirectpages(request):
    """redirect all 404 errors to this page--> i haven't modeled it yet"""
    return render(request, "authentication/redirect.html")


class LoginView(View):
    """
    the following class is used for logging in.
    The method are self explanatory
    :the get method is used when the page is requested
    :post method is used when the page is posted
     """

    def get(self, request):
        """get login page"""
        return render(request, 'authentication/login.html')

    def post(self, request):
        """validate login credentials"""
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +
                                     user.username + ' you are now logged in')
                    return redirect('profile-page')
                messages.error(
                    request, 'Account is not active,please check your email')
                return render(request, 'authentication/login.html')
            messages.error(
                request, 'Invalid credentials,try again')
            return render(request, 'authentication/login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'authentication/login.html')


class LogoutView(View):
    """logs the user out"""

    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')


def profile(request, username):
    """
    creating an instance of both
            userformUpdate and profileUpdateform
    storing in the current user details in
        u_form and p_form for profile
        picture within the first if condition
    this is so that the user can see the older
    credentials when they change to new,

    the 2nd if conditions saves the details if
    both forms are valid regardless of which form is changed

    :param request:
    :param username:
    :return: if updated redirect
    """

    if request.user.is_authenticated and username == request.user.username:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated')
                person = User.objects.get(username=username)
                return redirect('profile-page', person)
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'authentication/profile.html', context)
    else:
        person = User.objects.get(username=username)
        return render(request, 'authentication/profile.html', {'user': person})


def dashboard_profile(request, username):
    """
    creating an instance of both
            userformUpdate and profileUpdateform
    storing in the current user details in
        u_form and p_form for profile
        picture within the first if condition
    this is so that the user can see the older
    credentials when they change to new,

    the 2nd if conditions saves the details if
    both forms are valid regardless of which form is changed

    :param request:
    :param username:
    :return: if updated redirect
    """

    if request.user.is_authenticated and username == request.user.username:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated')
                person = User.objects.get(username=username)
                return redirect('dashboard_profile', person)
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'dashboard/dashboard_profile.html', context)
    else:
        person = User.objects.get(username=username)
        return render(request, 'dashboard/dashboard_profile.html', {'user': person})
