from django.shortcuts import render
from django.db import IntegrityError, OperationalError
from .forms import ContactoForm

def guardar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)  # Crea una instancia del formulario con los datos del POST
        if form.is_valid():
            try:
                form.save()  # Guarda el contacto en la base de datos
                return render(request, 'success.html')  # Redirige a una página de éxito
            except IntegrityError:
                return render(request, 'error.html', {'error': 'Error de integridad. Verifica los datos ingresados.'})
            except OperationalError:
                return render(request, 'error.html', {'error': 'Problema con la base de datos. Intenta de nuevo más tarde.'})
            except Exception as e:
                return render(request, 'error.html', {'error': f'Ocurrió un error inesperado: {str(e)}'})
    else:
        form = ContactoForm()  # Crea un formulario vacío si no es un POST

    return render(request, 'formulario.html', {'form': form})  # Muestra el formulario
