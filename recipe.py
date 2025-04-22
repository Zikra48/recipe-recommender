class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = set(ingredients)
        self.steps = steps

    def matches(self, available_ingredients):
        return self.ingredients.issubset(set(available_ingredients))

    def __str__(self):
        return f"\n🍲 {self.name}\nIngredients: {', '.join(self.ingredients)}\nSteps: {self.steps}"
