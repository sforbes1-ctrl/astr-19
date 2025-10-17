#coding journal1
#session 4
#creating a class about my favorite animal

#data numbers
class animal: 
		def __init__(self, name, length_arms, length_legs, num_eyes, has_tail, is_furry):
			self.name = name
			self.length_arms = length_arms
			self.length_legs = length_legs
			self.num_eyes = num_eyes
			self.has_tail = has_tail
			self.is_furry = is_furry

		def describe(self):
			print(f"animal name: {self.name}")
			print(f"average arm length: {self.length_arms}")
			print(f"average leg length: {self.length_legs}")
			print(f"number of eyes: {self.num_eyes}")
			print(f"has tail: {self.has_tail}")
			print(f"is furry: {self.is_furry}")

def main():
		penguin = animal("penguin", 19, 7, 2, True, False)
		penguin.describe()

if __name__ == "__main__":
		main()