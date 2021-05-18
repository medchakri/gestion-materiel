from frontoffice.models import materiel

from django import forms

class materielForm(forms.ModelForm):
    class Meta:
        model = materiel
        fields= '__all__'
        widgets = {
            'numSerie' : forms.TextInput(attrs={'class': 'form-control'}),
            'dateAchat': forms.DateInput(attrs={'class': 'form-control'}),
            'garantie' : forms.TextInput(attrs={'class': 'form-control'}),
            'lieuAchat' : forms.TextInput(attrs={'class': 'form-control'}),
            'prixAchat': forms.TextInput(attrs={'class': 'form-control'}),
            'marque': forms.TextInput(attrs={'class': 'form-control'}),
            'dateMaintenance': forms.DateInput(attrs={'class': 'form-control'}),
            'contrat' : forms.TextInput(attrs={'class': 'form-control'}),
            'lieuAffectation' : forms.TextInput(attrs={'class': 'form-control'})


        }

