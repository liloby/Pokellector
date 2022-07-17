from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Move, Pokemon
from .forms import InteractionForm

from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemons_index(request):
    pokemons = Pokemon.objects.order_by('-level')
    latest_pokemon = Pokemon.objects.order_by('id').last
    return render(request, 'pokemons/index.html', { 'pokemons': pokemons, 'latest_pokemon': latest_pokemon})

def pokemons_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    interaction_form = InteractionForm()
    return render(request, 'pokemons/detail.html', {
         'pokemon': pokemon, 'interaction_form': interaction_form 
         })

def add_interaction(request, pokemon_id):
    form = InteractionForm(request.POST)
    if form.is_valid():
        new_interaction = form.save(commit=False)
        new_interaction.pokemon_id = pokemon_id
        pokemon = Pokemon.objects.get(id=pokemon_id)
        pokemon.level += 1
        pokemon.save()
        new_interaction.save()
    return redirect('detail', pokemon_id=pokemon_id)

class PokemonCreate(CreateView):
    pokemon = Pokemon.objects.all().count()
    model = Pokemon
    fields = '__all__'
    success_url = '/pokemons/'

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['name', 'description', 'type']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemons/'

class MoveList(ListView):
    model = Move

class MoveDetail(DetailView):
    model = Move

class MoveCreate(CreateView):
    model = Move
    fields = '__all__'

class MoveUpdate(UpdateView):
    model = Move
    fields = '__all__'

class MoveDelete(DeleteView):
    model = Move
    success_url = '/moves/'