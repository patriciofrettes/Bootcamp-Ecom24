from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout

from .models import User, FavoriteAccount, Transaction
from .forms import RegistrationForm, TransferForm, ProfileForm, Transaction

# Vista de registro de usuario
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Vista de login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'accounts/login.html')

# Vista de perfil
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige a la misma página para mostrar los cambios
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

# Vista para realizar transferencia
def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            sender = request.user
            receiver = form.cleaned_data['receiver']
            amount = form.cleaned_data['amount']
            reason = form.cleaned_data['reason']

            if sender.balance >= amount:
                sender.balance -= amount
                receiver.balance += amount
                sender.save()
                receiver.save()
                # Crear la transacción
                Transaction.objects.create(sender=sender, receiver=receiver, amount=amount, reason=reason)
                return redirect('history')  # Redirige al historial de transacciones
            else:
                return render(request, 'accounts/transfer.html', {'form': form, 'error': 'Saldo insuficiente'})
    else:
        form = TransferForm()
    return render(request, 'accounts/transfer.html', {'form': form})

# Vista de cuentas favoritas
def favorites(request):
    favorites = FavoriteAccount.objects.filter(user=request.user)
    return render(request, 'accounts/favorites.html', {'favorites': favorites})

# Vista del historial de transacciones
def history(request):
    transactions = Transaction.objects.filter(sender=request.user) | Transaction.objects.filter(receiver=request.user)
    return render(request, 'accounts/history.html', {'transactions': transactions})







