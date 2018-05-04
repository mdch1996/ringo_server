from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .utills import post_data

from .forms import UserRegistrationForm, DeviceEditForm, UserEditForm, SwitchForm
from .models import Device, Ring, Switch


# def user_login(request):
#
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             print("--------uncleaned_data-------", form)
#             cd = form.cleaned_data
#             print("--------cleaned_data-------", cd)
#             user = authenticate(username=cd['username'], password=cd['password'])
#             print("--------authenticate-------", user)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     print("-----login(request, user)-------", login(request, user))
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#
#     return render(request, 'registration/login.html', {'form': form})


def register(request):
    print('----request.user----', request.user)
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        # print("request.POST", request.POST)
        # print("------user-form------", user_form)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # print("------user_form.save------", new_user)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Device.objects.create(user=new_user)
            return render(request,
                          'accounts/register_done.html',
                          {'new_user': new_user})
        else:
            messages.error(request, "you can'nt register!")
    else:
        user_form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'user_form': user_form})


@login_required()
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        device_form = DeviceEditForm(instance=request.user.device, data=request.POST)

        if user_form.is_valid() and device_form.is_valid():
            user_form.save()
            device_form.save()
            messages.success(request, "device updated successfully")
        else:
            messages.error(request, "error updating your device")
    else:
        user_form = UserEditForm(instance=request.user)
        device_form = DeviceEditForm(instance=request.user.device)
    return render(request, "accounts/edit.html", {'user_form': user_form, 'device_form': device_form})


@login_required()
def dashboard(request):
    ring_list = Ring.objects.filter(device__user__exact=request.user)
    switch_list = Switch.objects.filter(device__user__exact=request.user)
    device = Device.objects.get(user__exact=request.user)

    if request.method == 'POST':

        switch_form = SwitchForm(data=request.POST)
        if switch_form.is_valid():

            key = switch_form.cleaned_data['key']
            data = {
                "device": device.raspberry_pi_code,
                "key": key
            }
            print("-------data-------", data)
            post_status = post_data(device.ip, data)

            print("=======switch_status=======", post_status)
            print('-------switch_form------', switch_form)

            new_item = switch_form.save(commit=False)
            if post_status == 200:
                new_item.done = True

            new_item.device = device
            new_item.save()
            return render(request, "accounts/dashboard.html", {"ring_list": ring_list,
                                                               "switch_list": switch_list,
                                                               "switch_form": switch_form})
        else:
            messages.error(request, "your device ip isn't correct!")
    else:
        switch_form = SwitchForm()

    return render(request, "accounts/dashboard.html", {"ring_list": ring_list,
                                                       "switch_list": switch_list,
                                                       "switch_form": switch_form})
