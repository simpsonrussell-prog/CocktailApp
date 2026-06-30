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

vesper_martini.make()