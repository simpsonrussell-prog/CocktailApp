class Cocktail():
    def __init__(self, name, ingredients = [], instructions = []):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    def __repr__(self):
        return f"{self.name}"
    def make(self):
        for instruction in self.instructions:
            input(f"{instruction}\nHit enter to continue\n")
        print("Serve, or drink and enjoy!")

martini = Cocktail("martini", ["gin", "vodka", "dry vermouth", "orange bitters", "lemon peel", "olives"], ["Add the vodka or gin, vermouth and bitters into a shaker", "Shake and pour into a glass with ice", "Garnish with lemon peel", "Skewer the olives and drop to the bottom of the glass"])
vesper_martini = Cocktail("Vesper Martini", ["90ml gin", "30ml vodka", "15ml Lillet Blanc", "Large, thin slice of lemon peel"], ["Place a coupe or martini glass in the freezer to chill.", "Fill the shaker with ice and shake vigorously for 20–30 seconds until the outside is ice-cold and frosty.", "Double strain the mixture into your chilled glass.", "Twist the lemon peel over the drink to express the oils, wipe the rim of the glass with the peel, and drop it in."])
mojito = Cocktail("mojito", ["Juice of 1 lime", "1tsp granulated sugar", "handful of mint leaves", "60ml white rum", "Soda water"], ["Muddle the lime juice, sugar and mint leaves in a small jug.", "Pour over the rum, stirring with a small handled spoon.", "Top up with soda water."])
margarita = Cocktail("margarita", ["ice", "50ml tequila", "25 ml lime juicd", "20ml triple sec", "salt", "lime wedges"], ["Sprinkle a few teaspoons of salt over the surface of a small plate or saucer. Rub one wedge of lime along the rim of a tumbler and then dip it into the salt so that the entire rim is covered.", "Fill a cocktail shaker with ice, then add the tequila, lime juice and triple sec. Shake until the outside of the shaker feels cold.", "Strain the mix into the prepared glass over fresh ice. Add a wedge of lime."])
white_russian = Cocktail("white russian", ["60ml vodka", "2 tbsp Kahlúa", "1 tbsp cream"], ["Mix together all the ingredients.", "Put some ice cubes in a small tumbler and pour the cocktail over the top."])

def decision():
    user_choice = input("Choose a cocktail that you would like to make:\n1: Margarita\n2: Martini\n3: Mojito\n4: Vesper Martini\n5: White Russian\n\nPlease enter the number of your choice >")
    if user_choice == "1":
        margarita.make
    elif user_choice == "2":
        martini.make
    elif user_choice == "3":
        mojito.make
    elif user_choice == "4":
        vesper_martini.make
    elif user_choice == "5":
        white_russian.make
    again = input("Would you like to make another cocktail? y/n\n> ")

decision()
