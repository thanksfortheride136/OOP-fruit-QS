class Fruit:
	def __init__(self, name, color):
      		self.name = name
      		self.color = color

	def details(self):
    		print(f"My favorite {self.name} is {self.color}!")

apple = Fruit("Apple", "Red")
apple.details()