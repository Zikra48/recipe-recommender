from recipe import Recipe
from recipe_book import RecipeBook

# Sample recipes
def create_sample_recipes():
    book = RecipeBook()
    book.add_recipe(Recipe(
        "Tomato Sandwich",
        ["bread", "tomato", "salt"],
        "Place sliced tomato on bread, sprinkle salt, and enjoy."
    ))
    book.add_recipe(Recipe(
        "Omelette",
        ["egg", "salt", "onion"],
        "Whisk eggs with salt and onion. Cook on pan until fluffy."
    ))
    book.add_recipe(Recipe(
        "Fried Rice",
        ["rice", "egg", "carrot", "soy sauce"],
        "Stir-fry cooked rice with veggies, egg, and soy sauce."
    ))
    return book

def main():
    print("🥕 Welcome to the Recipe Recommender!")
    ingredients = input("Enter the items you have in your fridge (comma separated):\n> ").lower().split(",")
    ingredients = [i.strip() for i in ingredients]

    recipe_book = create_sample_recipes()
    recommendations = recipe_book.recommend(ingredients)

    if recommendations:
        print("\n✅ You can make the following recipes:")
        for recipe in recommendations:
            print(recipe)
    else:
        print("\n❌ No matching recipes found. Try adding more ingredients.")

if __name__ == "__main__":
    main()
