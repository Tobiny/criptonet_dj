from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Usuario o contraseña inválida'
        else:
            msg = 'Error al validar el formulario'

    return render(request, "usuarios/login.html", {"form": form, "msg": msg})


def editor_usuarios(user):
    return user.groups.filter(name='Editor de usuarios').exists()

@login_required
@user_passes_test(editor_usuarios)
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Usuario creado correctamente.'
            print()
            success = True

            # return redirect("/login/")

        else:
            msg = 'El formulario no es válido'
    else:
        form = SignUpForm()

    return render(request, "usuarios/register.html", {"form": form, "msg": msg, "success": success})
