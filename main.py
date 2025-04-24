from recipe import Recipe
from recipe_book import RecipeBook

book = RecipeBook()

# Sample Recipes
book.add_recipe(Recipe(
    "Omelette",
    ["egg", "salt", "pepper", "oil"],
    ["Crack the eggs.", "Add salt and pepper.", "Whisk.", "Fry in oil."]
))

book.add_recipe(Recipe(
    "Tomato Sandwich",
    ["bread", "tomato", "salt", "butter"],
    ["Slice tomato.", "Butter the bread.", "Add tomato.", "Sprinkle salt.", "Close sandwich."]
))

book.add_recipe(Recipe(
    "Fruit Salad",
    ["apple", "banana", "orange", "honey"],
    ["Chop all fruits.", "Mix them in a bowl.", "Drizzle honey on top."]
))

book.add_recipe(Recipe(
    "Grilled Cheese",
    ["bread", "cheese", "butter"],
    ["Butter the bread.", "Place cheese between slices.", "Grill until golden."]
))

book.add_recipe(Recipe(
    "Pasta",
    ["pasta", "salt", "water", "olive oil", "tomato sauce"],
    ["Boil water with salt.", "Add pasta.", "Cook until tender.", "Drain and mix with sauce."]
))

book.add_recipe(Recipe(
    "Peanut Butter Banana Toast",
    ["bread", "banana", "peanut butter"],
    ["Toast the bread.", "Spread peanut butter.", "Slice banana and place on top."]
))

book.add_recipe(Recipe(
    "Cucumber Salad",
    ["cucumber", "salt", "lemon juice", "pepper"],
    ["Slice cucumber.", "Add salt and pepper.", "Squeeze lemon juice.", "Toss well."]
))

# User input
fridge_items = input("Enter the items in your fridge (comma-separated): ").lower().split(',')

# Trim extra spaces
fridge_items = [item.strip() for item in fridge_items]

# Get matching recipes
matching = book.find_recipes(fridge_items)

if matching:
    print("\nYou can make the following recipes:")
    for recipe in matching:
        print(f"\n🍽️ {recipe.name}")
        print("Ingredients:", ', '.join(recipe.ingredients))
        print("Instructions:")
        for step in recipe.instructions:
            print(f"- {step}")
else:
    print("\nNo matching recipes found. Try adding more ingredients!")
