from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect


def deleteUser(request):
    current_user = request.user
    username = current_user.username
    u = User.objects.get(username=username)
    if request.method == "POST":
        u.delete()
    return render(request, 'authentication/register.html')


def confirmDeleteUser(request):
    return render(request, 'dashboard/user_delete.html')
