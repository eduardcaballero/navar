from django import forms
from .models import  Usuario,Caso
from django.forms import  Textarea, TextInput, NumberInput,Textarea

class UsuarioForm(forms.Form):
    nombres = forms.CharField(max_length=35)
    apellidos = forms.CharField(max_length=35)
    cedula = forms.CharField(max_length=15)
    especialidad =  forms.CharField(widget=forms.Textarea)
    contraseña = forms.CharField(widget=forms.PasswordInput)
    habilidades = forms.CharField(widget=forms.Textarea)
    correo = forms.EmailField()
    telefono = forms.CharField(max_length=10)

    class Meta:
        model = Usuario
        fields = ('nombres', 'apellidos', 'cedula', 'especialidad', 'contraseña','habilidades', 'correo', 'telefono' )

class ServicioForm(forms.Form):
    ips = forms.CharField(max_length=100)
    sexo = forms.CharField(max_length=1)
    edad = forms.CharField(max_length=3)
    artefacto_metalico = forms.BooleanField(required=False)
    tiempo_entrega = forms.CharField(max_length=3)
    diagnostico = forms.CharField(widget=forms.Textarea)
    procedimiento_q = forms.CharField(widget=forms.Textarea)
    etiologia_congenito = forms.BooleanField(required=False)
    etiologia_oncologico = forms.BooleanField(required=False)
    etiologia_traumatico = forms.BooleanField(required=False)
    zona_superior = forms.BooleanField(required=False)
    zona_medio = forms.BooleanField(required=False)
    zona_inferior = forms.BooleanField(required=False)
    zona_craneo = forms.BooleanField(required=False)
    tiempo_agudo = forms.BooleanField(required=False)
    tiempo_subagudo = forms.BooleanField(required=False)
    tiempo_cronico = forms.BooleanField(required=False)
    diam_tornillo_1 = forms.CharField(max_length=6)
    diam_tornillo_2 = forms.CharField(max_length=6)
    diam_tornillo_3 = forms.CharField(max_length=6)
    diam_tornillo_4 = forms.CharField(max_length=6)
    diam_tornillo_otro = forms.CharField(max_length=6)
    recesion_hueso = forms.BooleanField(required=False)
    margen_recesion = forms.CharField(max_length=6)
    numero_sujeciones = forms.CharField(max_length=2)
    incisiones_vias = forms.CharField(widget=forms.Textarea)
    planeamiento_q_v = forms.BooleanField(required=False)
    planeamiento_q_f = forms.BooleanField(required=False)
    biomodelo_pre_v = forms.BooleanField(required=False)
    biomodelo_pre_f = forms.BooleanField(required=False)
    biomodelo_pos_v = forms.BooleanField(required=False)
    biomodelo_pos_f = forms.BooleanField(required=False)
    guia_q_v = forms.BooleanField(required=False)
    guia_q_f = forms.BooleanField(required=False)
    implante_v = forms.BooleanField(required=False)
    implante_f = forms.BooleanField(required=False)
    observaciones = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Caso
        fields = ('ips','sexo','edad','artefacto_metalico','tiempo_entrega','diagnostico','procedimiento_q','etiologia_congenito','etiologia_oncologico','etiologia_traumatico',
        'zona_superior','zona_medio','zona_inferior','zona_craneo','tiempo_agudo','tiempo_subagudo','tiempo_cronico','diam_tornillo_1','diam_tornillo_2','diam_tornillo_3',
        'diam_tornillo_4','diam_tornillo_otro','recesion_hueso','margen_recesion','numero_sujeciones','incisiones_vias','planeamiento_q_v','planeamiento_q_f',
        'biomodelo_pre_v','biomodelo_pre_f','biomodelo_pos_v','biomodelo_pos_f','guia_q_v','guia_q_f','implante_v','implante_f','observaciones')