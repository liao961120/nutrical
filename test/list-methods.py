#%%
from nutrical import Rank, Table, Recipe, Ingredient as I

sources_of_protein = [
    I("Whey",            protein = 1000 * .8, dollars = 499),
    I("Casein",          protein =  907 * .8, dollars = 1200),
    I("Egg (7-11)",      protein = 6        , dollars = 10),
    I("Egg (raw)" ,      protein = 6        , dollars = 6),
    I("Tofu",            protein = 8.5 * 4  , dollars = 35),
    I("Dry milk",        protein = 7.8 * 81 , dollars = 789),
    I("Soy milk (7-11)", protein = 3.4 * 4  , dollars = 25),
]
Rank( sources_of_protein, by='dollars', protein=1 )



# %%
Table(sources_of_protein, tablefmt="html")
# %%
