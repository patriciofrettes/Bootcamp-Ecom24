from django.contrib.auth.models import AbstractUser
from django.db import models


# Definición del modelo de Usuario
class User(AbstractUser):
    # Este modelo extiende el modelo AbstractUser de Django, añadiendo campos adicionales
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)  # Imagen de perfil del usuario
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Saldo de dinero del usuario
    is_active = models.BooleanField(default=True)  # Estado del usuario (activo o no)

    def __str__(self):
        return self.username


class TransferReason(models.Model):
    # Razones por las cuales un usuario puede realizar una transferencia (ejemplo: pago, regalo, etc.)
    name = models.CharField(max_length=100)  # Nombre de la razón de la transferencia

    def __str__(self):
        return self.name

# Definición del modelo de Razón de Transferencia
# Definición del modelo de Transacción
class Transaction(models.Model):
    # Modelo que representa una transacción entre dos usuarios
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transactions')  # Usuario emisor
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transactions')  # Usuario receptor
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Monto de la transferencia
    reason = models.ForeignKey(TransferReason, on_delete=models.SET_NULL, null=True)  # Razón de la transferencia
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la transacción

    def __str__(self):
        return f"Transaction from {self.sender} to {self.receiver} of {self.amount}"

# Definición del modelo de Cuenta Favorita
class FavoriteAccount(models.Model):
    # Este modelo permite que un usuario marque otro como favorito
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')  # Usuario que marca la cuenta favorita
    favorite_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorited_by')  # Usuario marcado como favorito

    class Meta:
        unique_together = ('user', 'favorite_user')  # No permitir duplicados

    def __str__(self):
        return f"Favorite account: {self.user} -> {self.favorite_user}"


