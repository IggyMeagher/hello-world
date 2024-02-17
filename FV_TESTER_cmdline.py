import random


# Creating an array with fruits and vegetables, including specific types of apples.

fruits_and_vegetables = [
    "Apple - Granny Smith",
    "Apple - Fuji",
    "Apple - Honeycrisp",
    "Apple - Golden Delicious",
    "Apple - Gala",
    "Banana",
    "Orange - Valencia",
    "Orange - Navel",
    "Orange - Blood Orange",
    "Grapes - Red",
    "Grapes - Green",
    "Grapes - Concord",
    "Pear - Bartlett",
    "Pear - Bosc",
    "Pear - Anjou",
    "Strawberry",
    "Blueberry",
    "Raspberry",
    "Blackberry",
    "Watermelon",
    "Cantaloupe",
    "Honeydew Melon",
    "Tomato",
    "Cucumber",
    "Bell Pepper - Green",
    "Bell Pepper - Red",
    "Bell Pepper - Yellow",
    "Carrot",
    "Broccoli",
    "Cauliflower",
    "Lettuce - Iceberg",
    "Lettuce - Romaine",
    "Spinach",
    "Kale",
    "Onion - Yellow",
    "Onion - Red",
    "Onion - White",
    "Garlic",
    "Potato - Russet",
    "Potato - Red",
    "Potato - Yukon Gold",
    "Sweet Potato",
    "Zucchini",
    "Eggplant",
    "Mushroom - Button",
    "Mushroom - Portobello",
    "Mushroom - Shiitake",
    "Corn",
    "Peas",
    "Green Bean",
    "Chili Pepper - Jalapeno",
    "Chili Pepper - Habanero",
    "Chili Pepper - Serrano",
    "Lemon",
    "Lime",
    "Kiwi",
    "Pineapple",
    "Mango",
    "Peach",
    "Nectarine",
    "Apricot",
    "Cherry",
    "Plum",
    "Grapefruit",
    "Pomegranate",
    "Avocado",
    "Papaya",
    "Guava",
    "Durian",
    "Lychee",
    "Dragon Fruit",
    "Passion Fruit",
    "Tangerine",
    "Clementine",
    "Date",
    "Fig"
]

#print(len(fruits_and_vegetables))

class fruit_and_veg():
    def __init__(self, score, process):
        self.random_int = random.randint(0,76)
        self.score = score
        self.process = process

    def randomfv(self):


        random_fruit_or_veg = fruits_and_vegetables[self.random_int]

        print("what is", random_fruit_or_veg)
        answer = input('')

        if answer.lower() == random_fruit_or_veg.lower():
            self.score +=1
            print("your score is", self.score)
        else:
            self.score -=1
            print('not correct', self.score, 'is your score')
        if self.score == 20:
            self.process = False
            print('well done, you have completed the test with a score of', self.score,'/20')
        
            

is_process_running = True
current_score = 0

while is_process_running == True:
    random_fruit_and_veg = fruit_and_veg(current_score, is_process_running)
    random_fruit_and_veg.randomfv()
    current_score = random_fruit_and_veg.score








