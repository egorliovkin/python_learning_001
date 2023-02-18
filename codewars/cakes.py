def cakes(recipe, available):
    # return min(available.get(k, 0) // recipe[k] for k in recipe)
    xs = [available[k] // recipe[k] for k in recipe.keys() if (k in available)]
    if len(xs) == len(recipe):
        return min(xs)
    else:
        return 0


def cakes2(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)


recipe1 = {"flour": 500, "sugar": 200, "eggs": 1}
available1 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe1, available1), 2, 'example #1')

recipe2 = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available2 = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe2, available2), 0, 'example #2')