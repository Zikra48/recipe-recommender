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
    "Mashed Potatoes",
    ["potatoes", "butter", "milk", "salt", "pepper"],
    ["Peel and boil the potatoes until tender.", "Mash the potatoes with butter and milk.", "Season with salt and pepper."]
))
book.add_recipe(Recipe(
    "Tomato Soup",
    ["tomato", "onion", "garlic", "olive oil", "vegetable broth", "salt", "pepper"],
    ["Sauté onions and garlic in olive oil.", "Add chopped tomatoes and vegetable broth.", "Simmer for 20 minutes.", "Blend the soup until smooth.", "Season with salt and pepper."]
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
book.add_recipe(Recipe(
    "Chocolate Brownies",
    ["flour", "cocoa powder", "sugar", "butter", "eggs", "vanilla extract", "baking powder", "chocolate chips"],
    ["Mix dry ingredients together.", "Add eggs, butter, and vanilla extract.", "Fold in chocolate chips.", "Bake at 350°F for 25-30 minutes."]
))
book.add_recipe(Recipe(
    "Grilled Chicken",
    ["chicken breasts", "olive oil", "garlic", "lemon juice", "salt", "pepper"],
    ["Marinate chicken breasts in olive oil, garlic, lemon juice, salt, and pepper for 30 minutes.", "Grill the chicken until cooked through."]
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
