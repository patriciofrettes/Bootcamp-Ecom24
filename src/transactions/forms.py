from django import forms
from .models import TransferReason  # Solo importamos lo necesario de models

class TransferForm(forms.ModelForm):
    class Meta:
        model = None  # Inicialmente no se asigna el modelo

    def __init__(self, *args, **kwargs):
        # Aquí hacemos la importación local de Transaction
        from accounts.models import User
        from transactions.models import Transaction

        # Ahora asignamos el modelo a la clase Meta
        self.Meta.model = Transaction

        # Llenamos los queryset de los campos del formulario
        self.fields['receiver'].queryset = User.objects.all()  # Receptor: cualquier usuario
        self.fields['reason'].queryset = TransferReason.objects.all()  # Razón de la transferencia
        
        super().__init__(*args, **kwargs)

