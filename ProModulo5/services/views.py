from django.shortcuts import render, HttpResponseRedirect
from .models import Service
from .forms import ServiceForm
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import PedidoForm
from django.urls import reverse_lazy


class PedidoSuccess(TemplateView):
    template_name = 'services/pedido_success.html'

class ServiceCreatePedido(CreateView):
    form_class = PedidoForm
    template_name = 'services/pedido_cliente.html'
    success_url = reverse_lazy('services:success_pedido')

    def form_valid(self, form):
        pedido_nuevo = form.save(commit=False)
        pedido_nuevo.save()
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(ServiceCreatePedido, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


def _crea_diccionario(datos_pedido):
    diccionario ={}
    datos_pedido = datos_pedido[:-1]
    productos = datos_pedido.split('|')
    for producto in productos:
        detalle = producto.split('-')
        diccionario[detalle[0]] = int(detalle[1])
    return diccionario

def ver_detalle_pedido(request):
    pedido = list()
    if request.method == 'POST':
        datos_pedido = request.POST['datos_pedido']
        print(datos_pedido)
        productos = _crea_diccionario(datos_pedido)
        print(productos)
        total = 0
        for producto in productos.keys():
            cantidad = productos[producto]
            if cantidad > 0:
                dict_producto = {}
                service = Service.objects.get(pk=producto)
                dict_producto['id'] = service.id
                dict_producto['title'] = service.title
                dict_producto['sub_title'] = service.subtitle
                dict_producto['quantity'] = cantidad
                dict_producto['cost'] = service.pricing
                total += cantidad * int(service.pricing)
                pedido.append(dict_producto)
        #Se colocan las variables en session
        request.session['total_float']= float(total)
        request.session['detalle_pedido'] = pedido
    return render(request, 'services/detalle_pedido.html', {'pedido':pedido, 'total':total})


def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services':services})

@staff_member_required
def update(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST,request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/service_update_form.html', {'form':form})

@staff_member_required
def create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'services/service_form.html', {'form':form})
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form':form})