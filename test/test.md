<div class="cell markdown">

## Installation

``` sh
pip install nutrical
```

## Usage

### Ingredients

</div>

<div class="cell code" execution_count="1">

``` python
from nutrical import Ingredient, Recipe

apple = Ingredient("apple", portion='160g', calories=80, protein=.5, fiber=1)
banana = Ingredient("banana", portion='80g', calories=70, protein=1, fiber=1.6)
peanut = Ingredient("peanut", portion='20g', calories=110, protein=5.7, fat=20, fiber=1.8)
milk = Ingredient("milk", portion="1 cup", calories=200, protein=3)
```

</div>

<div class="cell code" execution_count="2">

``` python
# Programmatic construction
data = {'name': 'hi', 'portion': '150g', 'dollar': 20, 'Soluble Fiber': 1}
Ingredient(**data)
```

<div class="output execute_result" execution_count="2">

    Nutrition      Value
    -------------  --------
    portion        150 gram
    dollar         20
    soluble fiber  1

</div>

</div>

<div class="cell code" execution_count="3">

``` python
# Nutritional values of 2 apples (summed)
2 * apple
```

<div class="output execute_result" execution_count="3">

    Nutrition    Value
    -----------  --------
    portion      320 gram
    calories     160
    protein      1.0
    fiber        2

</div>

</div>

<div class="cell markdown">

#### Change of basis

A new ingredient can be created from an old one by setting a new portion
size, as well as any `kwargs` (except `name`) used in the definition of
the ingredient. This makes it easy to caluate the nutritional values of
the same ingredient with a different portion size, such as for a larger
(or smaller) apple.

</div>

<div class="cell code" execution_count="4">

``` python
# A smaller apple
apple.to(portion='130g')
```

<div class="output execute_result" execution_count="4">

    Nutrition    Value
    -----------  ----------
    portion      130.0 gram
    calories     65.0
    protein      0.41
    fiber        0.81

</div>

</div>

<div class="cell markdown">

You might also want to know how large a portion is required to reach
intake of, say 3 grams of fiber. Simple, just supply fiber as the
parameter of the `.to()` method.

</div>

<div class="cell code" execution_count="5">

``` python
# How much to eat to reach 3g of fibers?
apple.to(fiber=3)
```

<div class="output execute_result" execution_count="5">

    Nutrition    Value
    -----------  ----------
    portion      480.0 gram
    calories     240.0
    protein      1.5
    fiber        3.0

</div>

</div>

<div class="cell markdown">

Different ingredients can be added together. For instance, the code
below calculates the nutritional values of apple milk.

</div>

<div class="cell code" execution_count="6">

``` python
# Apple milk nutritional values per 1g of protein
# Note that portion is (auto) discarded since 
# milk is measured in volume while apple in weights
(apple + milk).to(protein=1)
```

<div class="output execute_result" execution_count="6">

    Nutrition      Value
    -----------  -------
    fiber           0.29
    protein         1
    calories       80

</div>

</div>

<div class="cell markdown">

Adding together different ingredients to arrive at a new one might seem
a bit counter-intuitive. Indeed, that's why there's a `nutrical.Recipe`
class to represent recipes directly.

</div>

<div class="cell markdown">

### Recipes

</div>

<div class="cell code" execution_count="7">

``` python
# Create recipe from ingredients
recipe = Recipe("Fruit Cake", [
    1   * banana,   # 1 banana
    1.5 * peanut    # 1.5 servings of peanut butter
])
recipe
```

<div class="output execute_result" execution_count="7">

    <Recipe (Fruit Cake)>

    Ingredient    Portion
    ------------  ---------
    banana        80 gram
    peanut        30.0 gram

    Nutrition    Value
    -----------  ----------
    portion      110.0 gram
    fiber        4.3
    protein      9.55
    fat          30.0
    calories     235.0

</div>

</div>

<div class="cell markdown">

#### Some Recipe methods

</div>

<div class="cell code" execution_count="8">

``` python
recipe.add(1.5*apple)  # add 1 and a half apples to ingredient
recipe.rename("Cake")  # rename recipe
recipe.to(portion = '100gram')  # change of basis
```

<div class="output execute_result" execution_count="8">

    <Recipe (Cake)>

    Ingredient    Portion
    ------------  ----------
    banana        22.86 gram
    peanut        8.57 gram
    apple         68.57 gram

    Nutrition    Value
    -----------  ----------
    portion      100.0 gram
    fiber        1.66
    fat          8.57
    calories     101.43
    protein      2.94

</div>

</div>

<div class="cell markdown">

#### Import/Export

</div>

<div class="cell code" execution_count="9">

``` python
# Export nutritional values
recipe.export_csv("FruitCake.csv") 
recipe.export_xlsx("FruitCake.xlsx") 
```

</div>

<div class="cell code" execution_count="10">

``` python
from nutrical import import_recipe

# Import recipe from csv/excel
recipe = import_recipe("FruitCake.csv")
recipe
```

<div class="output execute_result" execution_count="10">

    <Recipe (FruitCake)>

    Ingredient    Portion
    ------------  ----------
    banana        80 gram
    peanut        30.0 gram
    apple         240.0 gram

    Nutrition    Value
    -----------  ----------
    portion      350.0 gram
    fiber        5.8
    fat          30.0
    calories     355.0
    protein      10.3

</div>

</div>
