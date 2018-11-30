from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import UsuarioForm, ServicioForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Usuario, Caso

def index(request):
    return render(request, 'navar/index.html')


# def create_usuario(request):
#     if request.method == 'POST':
#         usuario_form = UsuarioForm(request.POST)
#         if usuario_form.is_valid():
#             usuario_form = UsuarioForm(request.POST)  # Reload the profile form with the profile instance
#             usuario_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
#             usuario_form.save()  # Gracefully save the form
#     else:
#         usuario_form = UsuarioForm()
#     return render(request, 'navar/signup.html', {
#         'usuario_form': usuario_form
#     })
def create_usuario(request):
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        if usuario_form.is_valid():
            datos = usuario_form.cleaned_data
            nombres = datos.get('nombres')
            apellidos = datos.get('apellidos')
            cedula = datos.get('cedula')
            contrasena = datos.get('contraseña')
            especialidad =  datos.get('especialidad')
            habilidades = datos.get('habilidades')
            correo = datos.get('correo')
            telefono = datos.get('telefono')
            db_register = Usuario(nombres=nombres,apellidos=apellidos,cedula=cedula,contrasena=contrasena,especialidad=especialidad,habilidades=habilidades,correo=correo,telefono=telefono)
            db_register.save()
    else:
        usuario_form = UsuarioForm()
    return render(request, 'navar/signup.html', {
        'usuario_form': usuario_form
    })

def crear_solicitud(request):
    if request.method == 'POST':
        crear_servicio = ServicioForm(request.POST)
        if crear_servicio.is_valid():
            datos = crear_servicio.cleaned_data
            # especialista = request.user
            ips = datos.get('ips')
            sexo = datos.get('sexo')
            edad = datos.get('edad')
            artefacto_metalico = datos.get('artefacto_metalico')
            tiempo_entrega = datos.get('tiempo_entrega')
            diagnostico = models.TextField('diagnostico')
            procedimiento_q = models.TextField('procedimiento_q')
            etiologia_congenito = datos.get('etiologia_congenito')
            etiologia_oncologico = datos.get('etiologia_oncologico')
            etiologia_traumatico = datos.get('etiologia_traumatico')
            zona_superior = datos.get('zona_superior')
            zona_medio = datos.get('zona_medio')
            zona_inferior = datos.get('zona_inferior')
            zona_craneo = datos.get('zona_craneo')
            tiempo_agudo = datos.get('tiempo_agudo')
            tiempo_subagudo = datos.get('tiempo_subagudo')
            tiempo_cronico = datos.get('tiempo_cronico')
            diam_tornillo_1 = datos.get('diam_tornillo_1')
            diam_tornillo_2 = datos.get('diam_tornillo_2')
            diam_tornillo_3 = datos.get('diam_tornillo_3')
            diam_tornillo_4 = datos.get('diam_tornillo_4')
            diam_tornillo_otro = datos.get('diam_tornillo_otro')
            recesion_hueso = datos.get('recesion_hueso')
            margen_recesion = datos.get('margen_recesion')
            numero_sujeciones = datos.get('numero_sujeciones')
            incisiones_vias = models.TextField('incisiones_vias')
            planeamiento_q_v = datos.get('planeamiento_q_v')
            planeamiento_q_f = datos.get('planeamiento_q_f')
            biomodelo_pre_v = datos.get('biomodelo_pre_v')
            biomodelo_pre_f = datos.get('biomodelo_pre_f')
            biomodelo_pos_v = datos.get('biomodelo_pos_v')
            biomodelo_pos_f = datos.get('biomodelo_pos_f')
            guia_q_v = datos.get('guia_q_v')
            guia_q_f = datos.get('guia_q_f')
            implante_v = datos.get('implante_v')
            implante_f = datos.get('implante_f')
            observaciones = models.TextField('observaciones')
            db_register = Caso(ips=ips,sexo=sexo,edad=edad,artefacto_metalico=artefacto_metalico,tiempo_entrega=tiempo_entrega,diagnostico=diagnostico,procedimiento_q=procedimiento_q,etiologia_congenito=etiologia_congenito,etiologia_oncologico=etiologia_oncologico,etiologia_traumatico=etiologia_traumatico,
            zona_superior=zona_superior,zona_medio=zona_medio,zona_inferior=zona_inferior,zona_craneo=zona_craneo,tiempo_agudo=tiempo_agudo,tiempo_subagudo=tiempo_subagudo,tiempo_cronico=tiempo_cronico,diam_tornillo_1=diam_tornillo_1,diam_tornillo_2=diam_tornillo_2,diam_tornillo_3=diam_tornillo_3,
            diam_tornillo_4=diam_tornillo_4,diam_tornillo_otro=diam_tornillo_otro,recesion_hueso=recesion_hueso,margen_recesion=margen_recesion,numero_sujeciones=numero_sujeciones,incisiones_vias=incisiones_vias,planeamiento_q_v=planeamiento_q_v,planeamiento_q_f=planeamiento_q_f,
            biomodelo_pre_v=biomodelo_pre_v,biomodelo_pre_f=biomodelo_pre_f,biomodelo_pos_v=biomodelo_pos_v,biomodelo_pos_f=biomodelo_pos_f,guia_q_v=guia_q_v,guia_q_f=guia_q_f,implante_v=implante_v,implante_f=implante_f,observaciones=observaciones)
            db_register.save()
    else:
        crear_servicio = ServicioForm()
    return render(request, 'servicio/crear_servicio.html', {
        'crear_servicio': crear_servicio
    })


def usuario_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'navar/usuario.html', {'usuario': post})

@login_required
def registrar(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('usuario_detalle', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'navar/usuario_add.html', {'form': form})

@login_required
def usuario_editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('usuario_detalle', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'navar/usuario_editar.html', {'form': form})

@login_required
def usuario_eliminar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')