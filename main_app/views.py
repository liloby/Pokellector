from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

class Pokemon:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, type, description, level):
    self.name = name
    self.type = type
    self.level = level
    self.description = description

pokemons = [
  Pokemon('Bulbasaur', 'Grass', 3, 'Cute grass first pokemon'),
  Pokemon('Charmander', 'Fire', 5, 'Feisty but adorable fire pokemon'),
  Pokemon('Squirtle', 'Water', 4, 'Portable infinite water generator')
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemons_index(request):
    return render(request, 'pokemons/index.html', { 'pokemons': pokemons })