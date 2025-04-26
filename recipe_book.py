from recipe import Recipe

class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def recommend(self, available_ingredients):
        matches = [r for r in self.recipes if r.matches(available_ingredients)]
        return matches
