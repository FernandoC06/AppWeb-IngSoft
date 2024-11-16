from django import forms
from .models import Reportes,Proyecto, Miembro, Task, Checklist

class ProyectForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'fechaInicio', 'fechaFin']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Reportes
        fields = ['title', 'area', 'category', 'content', 'image']

class AsignarRolForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['rol']
        labels = {'rol': 'Rol del miembro'}
        widgets = {
            'rol': forms.Select(choices=[
                (0, 'Sin asignar'),
                (1, 'Administrador'),
                (2, 'Gestor'),
                (3, 'Programador'),
            ]),
        }

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del checklist'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'start_date', 'end_date', 'completed']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la tarea'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la tarea'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
