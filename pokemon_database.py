# Group Members: Nima & Kevin
"""A file for your implementation of the local database."""

from dataclasses import dataclass
from typing import List
from pokemon_api import *


@dataclass
class Pokemon:
    name: str
    attack: int
    defense: int
    num_types: int
    type1: str
    type2: str
    
def populate_database(pokemon_IDs: list[int]) -> str | int:
    for i in pokemon_IDs:
        name = get_pokemon_name(i)
        attack = get_pokemon_attack(name)
        defense = get_pokemon_defense(name)
        num_types = get_pokemon_num_types(name)
        type1 = get_pokemon_type1(name)
        type2 = get_pokemon_type2(name)
        
        
        
        
        
        