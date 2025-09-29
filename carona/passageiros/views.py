# caronas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculo, Itinerario, SolicitacaoCarona
from .forms import ItinerarioForm, SolicitacaoForm

def criar_itinerario(request):
    if request.method == 'POST':
        form = ItinerarioForm(request.POST)
        if form.is_valid():
            itinerario = form.save(commit=False)
            itinerario.motorista = request.user
            itinerario.save()
            return redirect('detalhes_carona', pk=itinerario.pk)
    else:
        form = ItinerarioForm()
    return render(request, 'caronas/criar_itinerario.html', {'form': form})

def buscar_caronas(request):
    itinerarios = Itinerario.objects.filter(vagas_disponiveis__gt=0)
    return render(request, 'caronas/buscar_caronas.html', {'itinerarios': itinerarios})

def detalhes_carona(request, pk):
    itinerario = get_object_or_404(Itinerario, pk=pk)
    return render(request, 'caronas/detalhes_carona.html', {'itinerario': itinerario})

def solicitar_carona(request, pk):
    itinerario = get_object_or_404(Itinerario, pk=pk)
    if request.method == 'POST':
        SolicitacaoCarona.objects.create(itinerario=itinerario, colaborador=request.user)
        return redirect('buscar_caronas')
    return render(request, 'caronas/solicitar_carona.html', {'itinerario': itinerario})

def gerenciar_solicitacoes(request):
    solicitacoes = SolicitacaoCarona.objects.filter(itinerario__motorista=request.user)
    return render(request, 'caronas/gerenciar_solicitacoes.html', {'solicitacoes': solicitacoes})

def cancelar_carona(request, pk):
    solicitacao = get_object_or_404(SolicitacaoCarona, pk=pk, colaborador=request.user)
    solicitacao.delete()
    return redirect('buscar_caronas')
