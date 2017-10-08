from django.views.generic import View
from django.template.response import TemplateResponse
from Apps.GestionSeguroSalud.models import TipoSeguro
from Apps.GestionSeguroSalud.models import Seguro

# Vista
class TipoSeguroListView(View):
    def get(self, request):
        app_keys = []

        for tipoSeguro in TipoSeguro.objects.all():
            app_keys.append(Seguro.factory(tipoSeguro))

        context={
            'tiposeguro_list': app_keys                                     #TipoSeguro.objects.all()
        }
        return TemplateResponse(request, 'lista_TipoSeguro.html', context)