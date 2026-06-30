# create empty dictionary and list for management of cocktail menu
cocktail_dict = {}
cocktail_list = []

#logic to create new recipe
class Cocktail():
    def __init__(self, name, ingredients = [], instructions = []):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        cocktail_dict.update({name: self})
        cocktail_list.append(self)
    def __repr__(self):
        return f"{self.name}"
    def make(self):
        print(f"You will need the following ingredients:\n{self.ingredients}\n")
        for instruction in self.instructions:
            input(f"{instruction}\nHit enter to continue\n")
        print("Serve, or drink and enjoy!")

#starter list of cocktails
martini = Cocktail("martini", ["gin", "vodka", "dry vermouth", "orange bitters", "lemon peel", "olives"], ["Add the vodka or gin, vermouth and bitters into a shaker", "Shake and pour into a glass with ice", "Garnish with lemon peel", "Skewer the olives and drop to the bottom of the glass"])
vesper_martini = Cocktail("vesper martini", ["90ml gin", "30ml vodka", "15ml Lillet Blanc", "Large, thin slice of lemon peel"], ["Place a coupe or martini glass in the freezer to chill.", "Fill the shaker with ice and shake vigorously for 20–30 seconds until the outside is ice-cold and frosty.", "Double strain the mixture into your chilled glass.", "Twist the lemon peel over the drink to express the oils, wipe the rim of the glass with the peel, and drop it in."])
mojito = Cocktail("mojito", ["Juice of 1 lime", "1tsp granulated sugar", "handful of mint leaves", "60ml white rum", "Soda water"], ["Muddle the lime juice, sugar and mint leaves in a small jug.", "Pour over the rum, stirring with a small handled spoon.", "Top up with soda water."])
margarita = Cocktail("margarita", ["ice", "50ml tequila", "25 ml lime juicd", "20ml triple sec", "salt", "lime wedges"], ["Sprinkle a few teaspoons of salt over the surface of a small plate or saucer. Rub one wedge of lime along the rim of a tumbler and then dip it into the salt so that the entire rim is covered.", "Fill a cocktail shaker with ice, then add the tequila, lime juice and triple sec. Shake until the outside of the shaker feels cold.", "Strain the mix into the prepared glass over fresh ice. Add a wedge of lime."])
white_russian = Cocktail("white russian", ["60ml vodka", "2 tbsp Kahlúa", "1 tbsp cream"], ["Mix together all the ingredients.", "Put some ice cubes in a small tumbler and pour the cocktail over the top."])

#logic for user to add their own recipe
def add_drink():
    name = input("Please enter the name of your cocktail.\n> ")
    ingredient = "gas'n'air"
    ingredients = []
    while ingredient != "none":
        print(f"Your current list of ingredients contains {ingredients}.")
        ingredient = input("Please type another ingredient in here. If you have finished your list of ingredients, type none.\n> ")
        ingredients.append(ingredient)
    instruction = "breathe"
    instructions = []
    while instruction != "none":
        print(f"Your list of instructions is {instructions}.")
        instruction = input("Please type your next instruction here. If you have no further instructions, type 'none'.\n> ")
        instructions.append(instruction)
    name = Cocktail(name, ingredients, instructions)


#logic for user to choose a recipe or to add their own
def decision():
    user_choice = input(f"Please select a drink from the following list, or type 'new' to enter your own recipe.\n{cocktail_list}\n> ")
    if user_choice in cocktail_dict:
        user_choice_value = cocktail_dict[user_choice]
        user_choice_value.make()
    elif user_choice == "new":
        add_drink()
    else:
        print("I'm sorry, I didn't understand that. Please enter the name of the cocktail that you would like to make\n")
        decision()
    if input("Would you like to make another cocktail? y/n\n> ") == "y":
        decision()
    else:
        print("Thanks for using my cocktails app!")
        return

decision()

