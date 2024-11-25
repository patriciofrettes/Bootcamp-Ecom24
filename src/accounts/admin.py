from django.contrib import admin

from .models import TransferReason

from .models import User, FavoriteAccount, Transaction

# Registra tus modelos en el panel de administración
admin.site.register(User)
admin.site.register(FavoriteAccount)
admin.site.register(Transaction)
admin.site.register(TransferReason)

