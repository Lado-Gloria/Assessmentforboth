# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

class Ancestral_Stories:
    def __init__(self, story_title, age_group, moral_lessons):
        self.story_title = story_title
        self.age_group = age_group
        self.moral_lessons = moral_lessons
    def folk_tell_story(self):
        return f"Once upon a time, in a land far away, there was a {self.story_title}, a captivating tale that imparts valuable moral lessons to {self.age_group}."


class Story(Ancestral_Stories):
    def __init__(self, story_title, age_group, moral_lessons, length):
        super().__init__(story_title, age_group, moral_lessons)
        self.length = length
    def get_story(self):
   
     return f"Once upon a time, in a land of {self.story_title}, there lived a brave hero who embarked on a quest to save the kingdom from impending doom. This {self.length}-page story is filled with suspense, action, and important life lessons."

class Story_Teller(Ancestral_Stories):
    def __init__(self, story_title, age_group, moral_lessons, name_story_teller):
        super().__init__(story_title, age_group, moral_lessons)
        self.name_story_teller = name_story_teller
    def tell_story(self):
 
       return f"Welcome, dear listeners! I am {self.name_story_teller}, a skilled storyteller. Today, I will transport you to the magical world of {self.story_title}. Prepare to be captivated by the enchanting characters, moral teachings, and the power of imagination."

class Translator(Ancestral_Stories):
    def __init__(self, story_title, age_group, moral_lessons, language):
        super().__init__(story_title, age_group, moral_lessons)
        self.language = language
    def translate(self):
        return f"Behold, the tale of {self.story_title} translated into {self.language}! Through the art of translation, we bring this timeless story to a wider audience, spreading its profound moral lessons and cultural richness."

# Create an instance of Ancestral_Stories
ancestral_story = Ancestral_Stories("The Magical Forest", "Children", "Respect for Nature")
# Create an instance of Story
story = Story("The Hero's Journey", "Young Adults", "Courage, Perseverance", 100)
# Create an instance of Story_Teller
storyteller = Story_Teller("The Chronicles of Narnia", "All Ages", "Friendship, Imagination", "Lucy")
# Create an instance of Translator
# translator = Translator("Cinderella", "Children", "Kindness, Resilience", "French")
translator = Translator("The Lion King", "Children", "Courage, Identity", "Spanish")
# Access the methods of each class
print(ancestral_story.folk_tell_story())
print(story.get_story())
print(storyteller.tell_story())
print(translator.translate())

# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

# class Recipe :
#   def __int__(self, ingredients,preparationtime,cookingmethod, nutritional,food):
#         self.ingredients =ingredients
#         self.preparationtime=preparationtime
#         self.cookingmethod =cookingmethod
#         self.nutritional=nutritional
#         self.food=food
#   def cook(self):   
#       print(f"the {self.food} contaaint{self.ingredients} and take {self.preparationtime} and {self.cookingmethod} and has {self.nutritional}")   
      

# class MoroccanRecipe(Recipe):
#       def __int__(self, ingredients,preparationtime,cookingmethod, nutritional,food,taste):
#            super.__init__(self, ingredients,preparationtime,cookingmethod, nutritional,food)
#            self.taste=taste

#       def tasting(self):  
#        if {self.food} =={self.taste}: 
#         print(f"the {self.food}with {self.taste}is a moreccanRecipe") 

#        else:
#            print("it not a moroccanRecipe")
             
      
# class NigerianRecipe(Recipe):
#       def __int__(self, ingredients,preparationtime,cookingmethod, nutritional,food,slipery):
#            super.__init__(self, ingredients,preparationtime,cookingmethod, nutritional,food)
#            self.slipery =slipery

#       def tasty(self):  
#        if {self.food} =={self.slipery}: 
#         print(f"the {self.food}with {self.taste}is a nigerianRecipe")

#        else:
#            print("it not a nigerianRecipe")   
      
# class EthiopianRecipe(Recipe):
#       def __int__(self, ingredients,preparationtime,cookingmethod, nutritional,food,cookwell):
#            super.__init__(self, ingredients,preparationtime,cookingmethod, nutritional,food)
#            self.cookwell=cookwell

#       def cooking(self):  
#        if {self.food} =={self.cookwell}: 
#         print(f"the {self.food}with {self.cookwell}is a ethiopianRecipe") 

         
#        else:
#            print("it not a ethiopianRecipe")    
      
                
      

# foods =Recipe("salt","3time","boiled","high","okra",)
# ethopia=EthiopianRecipe("tast","4time","fufu","energy","long","onion")
# nigeriangirl=NigerianRecipe("sweet","5time","stewed","fried","tomatos","strength")
# morroccan=MoroccanRecipe("spicy","6time","baked","low","boo","pasted")
# print(foods.cook)
# print(ethopia.cooking)
# print(nigeriangirl.tasty)
# print(morroccan.tasting)




class Recipe:
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
        self.name = name
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        self.nutritional_info = nutritional_info
class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, special_ingredient):
        super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
        self.special_ingredient = special_ingredient

class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, spice_level):
        super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
        self.spice_level = spice_level

class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, complexity_level):
        super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
        self.complexity_level = complexity_level
        
class AfricanCuisine:
    def __init__(self):
        self.recipes = []
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
    def display_recipes(self):
        for recipe in self.recipes:
            print(f"Name: {recipe.name}")
            print(f"Ingredients: {', '.join(recipe.ingredients)}")
            print(f"Preparation Time: {recipe.preparation_time} minutes")
            print(f"Cooking Method: {recipe.cooking_method}")
            print(f"Nutritional Information: {recipe.nutritional_info}")
            if isinstance(recipe, MoroccanRecipe):
                print(f"Special Ingredient: {recipe.special_ingredient}")
            elif isinstance(recipe, EthiopianRecipe):
                print(f"Spice Level: {recipe.spice_level}")
            elif isinstance(recipe, NigerianRecipe):
                print(f"complexity_level: {recipe.complexity_level}")
            print()
# Instance:
african_cuisine = AfricanCuisine()
moroccan_recipe = MoroccanRecipe("Tagine", ["Chicken", "Onions", "Spices"], 60, "Slow cooking", "High in protein", "Ras el Hanout")
ethiopian_recipe = EthiopianRecipe("Doro Wat", ["Chicken", "Onions", "Berbere spice"], 90, "Stewing", "Spicy and flavorful", "Medium")
nigerian_recipe = NigerianRecipe("Jollof Rice", ["Rice", "Tomatoes", "Peppers"], 45, "One-pot cooking", "Delicious and filling", "Easy")
african_cuisine.add_recipe(moroccan_recipe)
african_cuisine.add_recipe(ethiopian_recipe)
african_cuisine.add_recipe(nigerian_recipe)
african_cuisine.display_recipes()


         

# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to
# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.


class Species:
    def __init__(self, diet, lifespan):
        self.diet = diet
        self.lifespan = lifespan

class Predator(Species):
    def __init__(self, diet, lifespan, hunting_style):
        super().__init__(diet, lifespan)
        self.hunting_style = hunting_style

class Prey(Species):
    def __init__(self, diet, lifespan, migration_pattern):
        super().__init__(diet, lifespan)
        self.migration_pattern = migration_pattern


lion = Predator("Carnivore", 15, "Ambush hunting")
zebra = Prey("Herbivore", 20, "Seasonal migration")

print("Lion:")
print("Diet:", lion.diet)
print("Lifespan:", lion.lifespan)
print("Hunting Style:", lion.hunting_style)
print()

print("Zebra:")
print("Diet:", zebra.diet)
print("Lifespan:", zebra.lifespan)
print("Migration Pattern:", zebra.migration_pattern)

class Species:
    def __init__(self, name, diet, lifespan):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan

class Predator(Species):
    def __init__(self, name, diet, lifespan, hunting_style):
        super().__init__(name, diet, lifespan)
        self.hunting_style = hunting_style

    def hunt_prey(self, prey):
        print(f"The {self.name} is hunting the {prey.name}!")
        if prey.diet == "Herbivore":
            return f"The {self.name} successfully hunted the {prey.name}!"
        else:
            return f"The {self.name} couldn't hunt the {prey.name} because it's not a herbivore!"

class Prey(Species):
    def __init__(self, name, diet, lifespan, migration_pattern):
        super().__init__(name, diet, lifespan)
        self.migration_pattern = migration_pattern

lion = Predator("Lions", "Carnivorous", 15, "Ambush hunting")
zebra = Prey("Zebra", "Herbivore", 20, "Seasonal migration")
gazelle = Prey("Gazelle", "Herbivore", 10, "No migration")

result1 = lion.hunt_prey(zebra)
result2 = lion.hunt_prey(gazelle)

print(result1)
print(result2) 



# story

class Story:
    def __init__(self, title, content, age_group):
        self.title = title
        self.content = content
        self.age_group = age_group


class StoryTeller:
    def __init__(self, name):
        self.name = name
        self.stories = []

    def add_story(self, story):
        self.stories.append(story)

    def tell_story(self, title):
        story = next((s for s in self.stories if s.title == title), None)
        if story:
            return {
                "title": story.title,
                "content": story.content,
                "age_group": story.age_group
            }
        else:
            return "Story not found."


class Translator:
    def __init__(self, language):
        self.language = language

    def translate_text(self, text, target_language):
        return f"{text} ({target_language})"

    def translate(self, story, target_language):
        translated_title = self.translate_text(story.title, target_language)
        translated_content = self.translate_text(story.content, target_language)
        translated_age_group = self.translate_text(story.age_group, target_language)

        return Story(translated_title, translated_content, translated_age_group)


class FolkTale(Story):
    def __init__(self, title, content, age_group, moral_lesson):
        super().__init__(title, content, age_group)
        self.moral_lesson = moral_lesson


# Instances
story1 = Story("The Elephant and the Hare", "Once upon a time...", "Children")
story2 = FolkTale("The Tortoise and the Hare", "In a forest...", "Children", "Slow and steady wins the race")

story_teller = StoryTeller("John")
story_teller.add_story(story1)
story_teller.add_story(story2)

story = story_teller.tell_story("The Lion and the Mouse")
if isinstance(story, str):
    print(story)  
else:
    print("Story:", story["title"])
    print("Content:", story["content"])
    print("Age Group:", story["age_group"])

translator = Translator("Spanish")
translated_story = translator.translate(story1, "Spanish")
print("Translated Story:")
print("Title:", translated_story.title)
print("Content:", translated_story.content)
print("Age Group:", translated_story.age_group)



# two

class Story:
    def __init__(self, title, content, age_group):
        self.title = title
        self.content = content
        self.age_group = age_group


class StoryTeller:
    def __init__(self, name):
        self.name = name
        self.stories = []

    def add_story(self, story):
        self.stories.append(story)

    def tell_story(self, title):
        for story in self.stories:
            if story.title == title:
                return {
                    "title": story.title,
                    "content": story.content,
                    "age_group": story.age_group
                }
        return "Story not found."


class Translator:
    def __init__(self, language):
        self.language = language

    def translate_story(self, text, target_language):
        return f"{text} ({target_language})"

    def translate(self, story, target_language):
        translated_title = self.translate_story(story.title, target_language)
        translated_content = self.translate_story(story.content, target_language)
        translated_age_group = self.translate_story(story.age_group, target_language)

        return Story(translated_title, translated_content, translated_age_group)


class FolkTale(Story):
    def __init__(self, title, content, age_group, moral_lesson):
        super().__init__(title, content, age_group)
        self.moral_lesson = moral_lesson


# Instances
story1 = Story("The Elephant and the Hare", "Once upon a time...", "Children")
story2 = FolkTale("The Tortoise and the Hare", "In a forest...", "Children", "Slow and steady wins the race")

story_teller = StoryTeller("John")
story_teller.add_story(story1)
story_teller.add_story(story2)

story = story_teller.tell_story("The Lion and the Mouse")
if isinstance(story, str):
    print(story)  # Story not found.
else:
    print("Story:", story["title"])
    print("Content:", story["content"])
    print("Age Group:", story["age_group"])

translator = Translator("Spanish")
translated_story = translator.translate(story1, "Spanish")
print("Translated Story:")
print("Title:", translated_story.title)
print("Content:", translated_story.content)
print("Age Group:", translated_story.age_group)





# 4
class Artist:
  def __init__(self, name, country, musical_style, instruments):
    self.name = name
    self.country = country
    self.musical_style = musical_style
    self.instruments = instruments
class Performance:
  def __init__(self, artist, stage, start_datetime, end_datetime):
    self.artist = artist
    self.stage = stage
    self.start_datetime = start_datetime
    self.end_datetime = end_datetime
class Stage:
  def __init__(self, name, capacity):
    self.name = name
    self.capacity = capacity
artist1 = Artist("Salif Keita", "Mali", "World", ["kora", "balafon"])
artist2 = Artist("Angelique Kidjo", "Benin", "Afropop", ["guitar", "vocals"])
artist3 = Artist("Tinariwen", "Algeria", "Tamazight folk", ["guitar", "vocals"])
stage1 = Stage("Main Stage", 10000)
stage2 = Stage("World Stage", 5000)
performances = [
  Performance(artist1, stage1, "2023-06-28T12:00:00", "2023-06-28T13:00:00"),
  Performance(artist2, stage2, "2023-06-28T14:00:00", "2023-06-28T15:00:00"),
  Performance(artist3, stage1, "2023-06-28T16:00:00", "2023-06-28T17:00:00"),
]
for performance in performances:
  print(f"{performance.artist.name} - {performance.stage.name} - {performance.start_datetime} - {performance.end_datetime}")


#   4

from datetime import datetime, timedelta

class Artist:
  def __init__(self, name, country, musical_style, instruments):
    self.name = name
    self.country = country
    self.musical_style = musical_style
    self.instruments = instruments

class Performance:
  def __init__(self, artist, stage, start_datetime, end_datetime):
    self.artist = artist
    self.stage = stage
    self.start_datetime = datetime.fromisoformat(start_datetime)
    self.end_datetime = datetime.fromisoformat(end_datetime)

  def get_duration(self):
    duration = self.end_datetime - self.start_datetime
    return duration

class Stage:
  def __init__(self, name, capacity):
    self.name = name
    self.capacity = capacity

artist1 = Artist("Salif Keita", "Mali", "World", ["kora", "balafon"])
artist2 = Artist("Angelique Kidjo", "Benin", "Afropop", ["guitar", "vocals"])
artist3 = Artist("Tinariwen", "Algeria", "Tamazight folk", ["guitar", "vocals"])

stage1 = Stage("Main Stage", 10000)
stage2 = Stage("World Stage", 5000)

performances = [
  Performance(artist1, stage1, "2023-06-28T12:00:00", "2023-06-28T13:00:00"),
  Performance(artist2, stage2, "2023-06-28T14:00:00", "2023-06-28T15:00:00"),
  Performance(artist3, stage1, "2023-06-28T16:00:00", "2023-06-28T17:00:00"),
]

for performance in performances:
  duration = performance.get_duration()
  end_time = performance.start_datetime + duration
  formatted_start = performance.start_datetime.strftime("%Y-%m-%d %H:%M:%S")
  formatted_end = end_time.strftime("%Y-%m-%d %H:%M:%S")
  print(f"{performance.artist.name} - {performance.stage.name} - Start: {formatted_start} - End: {formatted_end} - Duration: {duration}")

# 4

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


products = [
    Product("Apple", 0.5, 10),
    Product("Banana", 0.3, 15),
    Product("Orange", 0.4, 12)
]

total_value = 0
for product in products:
    if product.quantity > 0:
        total_value += product.price * product.quantity

print("Total value of all products:", total_value)

# 6

def student_information(name, age, grades):
    average_grade = sum(grades) / len(grades)
    has_passed = average_grade >= 60

    return {
        "name": name,
        "age": age,
        "grades": grades,
        "average_grade": average_grade,
        "has_passed": has_passed,
    }


def main():
    student1 = student_information("John Doe", 18, [80, 75, 90])
    student2 = student_information("Jane Doe", 19, [70, 85, 65])

  
    print(student1)

    print(student2)


if __name__ == "__main__":
    main()


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def cal_average_grade(self):
        if len(self.grades) == 0:
            return 0
        total_sum = sum(self.grades)
        return total_sum / len(self.grades)

    def student_who_passed(self):
        average_grade = self.cal_average_grade()
        return average_grade >= 60

    def highest_grade(self):
        highest_grade = max(self.grades)
        print("Highest Grade:", highest_grade)


students = [
    Student("Anne Kangu", 18, [80, 75, 90]),
    Student("Fei Faith", 19, [70, 85, 65]),
    Student("Alice Lizz", 20, [90, 80, 95])
]

for student in students:
    print("Name:", student.name)
    print("Age:", student.age)
    print("Grades:", student.grades)

    average_grade = student.cal_average_grade()
    print("Average Grade:", average_grade)

    passing_status = "Passed" if student.student_who_passed() else "Failed"
    print("Passing Status:", passing_status)
    print()



class Artist:
    def __init__(self, name, country, musical_style, instruments):
     self.name = name
     self.country = country
     self.musical_style = musical_style
     self.instruments = instruments
class Performance:
  def __init__(self, artist, stage, start_datetime, end_datetime):
    self.artist = artist
    self.stage = stage
    self.start_datetime = start_datetime
    self.end_datetime = end_datetime
class Stage:
  def __init__(self, name, capacity):
    self.name = name
    self.capacity = capacity
artist1 = Artist("Nyashinski", "Kenya", "love", ["malaika", "beautiful"])
artist2 = Artist("Christopher", "Jameican", "reggea", ["stay with", "weekrnd love"])
artist3 = Artist("Tatiana", "USA", "RNB", ["hopples", "never"])
stage1 = Stage("Main Stage", 10000)
stage2 = Stage("World Stage", 5000)
performances = [
  Performance(artist1, stage1, "2023-06-28T12:00:00", "2023-06-28T13:00:00"),
  Performance(artist2, stage2, "2023-06-28T14:00:00", "2023-06-28T15:00:00"),
  Performance(artist3, stage1, "2023-06-28T16:00:00", "2023-06-28T17:00:00"),
]
for performance in performances:
  print(f"{performance.artist.name} - {performance.stage.name} - {performance.start_datetime} - {performance.end_datetime}")



# python
class FlightBooking:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, destination, date):
        available_flights = []
        for flight in self.flights:
            if flight.destination == destination and flight.date == date:
                available_flights.append(flight)
        return available_flights

    def reserve_seat(self, flight, passenger_name, seat_number):
        if flight.is_seat_available(seat_number):
            flight.reserve_seat(passenger_name, seat_number)
            return True
        else:
            return False

    def get_passenger_info(self, flight, passenger_name):
        return flight.get_passenger_info(passenger_name)

    def generate_booking_confirmation(self, flight, passenger_name):
        passenger_info = self.get_passenger_info(flight, passenger_name)
        if passenger_info:
            confirmation = f"Booking Confirmation\nFlight: {flight.destination} ({flight.date})\nPassenger: {passenger_info}"
            return confirmation
        else:
            return "Passenger information not found."


class Flight:
    def __init__(self, destination, date, available_seats):
        self.destination = destination
        self.date = date
        self.available_seats = available_seats
        self.passengers = {}

    def is_seat_available(self, seat_number):
        return seat_number in self.available_seats

    def reserve_seat(self, passenger_name, seat_number):
        self.available_seats.remove(seat_number)
        self.passengers[passenger_name] = seat_number

    def get_passenger_info(self, passenger_name):
        return self.passengers.get(passenger_name, None)


booking_system = FlightBooking()

flight1 = Flight("New York", "2023-07-05", ["A1", "A2", "B1", "B2"])
flight2 = Flight("London", "2023-07-06", ["C1", "C2", "D1", "D2"])
booking_system.add_flight(flight1)
booking_system.add_flight(flight2)

available_flights = booking_system.search_flights("New York", "2023-07-05")
print("Available Flights:")
for flight in available_flights:
    print(flight.destination, flight.date)


if booking_system.reserve_seat(flight1, "John Doe", "A1"):
    print("Seat reserved successfully!")
else:
    print("Seat not available.")

passenger_info = booking_system.get_passenger_info(flight1, "John Doe")
print("Passenger Information:", passenger_info)

confirmation = booking_system.generate_booking_confirmation(flight1, "John Doe")
print(confirmation)


class PassengerDetails:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update_information(self, email, phone):
        self.email = email
        self.phone = phone


class FlightBooking:
    def __init__(self, destination, date, capacity):
        self.destination = destination
        self.date = date
        self.capacity = capacity
        self.passengers = []
        self.flights = []

    def search_flights(self, destination, date):
        available_flights = []
        for flight in self.flights:
            if flight.destination == destination and flight.date == date:
                available_flights.append(flight)
        return available_flights

    def reserve_seat(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        else:
            return False

    def manage_passenger_information(self, updated_passenger):
        for passenger in self.passengers:
            if passenger.name == updated_passenger.name:
                passenger.update_information(updated_passenger.email, updated_passenger.phone)
                return True
        return False

    def generate_booking_confirmation(self, passenger):
        for p in self.passengers:
            if p.name == passenger.name:
                return f"Booking confirmation for {p.name} on {self.date} to {self.destination}"
        return "Passenger not found"


flight_booking = FlightBooking("Tanzania", "2023-04-30", 90)
available_flights = flight_booking.search_flights("Uganda", "2022-03-20")
print(available_flights)

passenger1 = PassengerDetails("Nkatha", "nkatha@gmail.com")
reservation_status = flight_booking.reserve_seat(passenger1)
print(reservation_status)

passenger2 = PassengerDetails("Mily", "milly@gmail.com")
passenger2.update_information("milly@gmail.com", "1234567890")
update_status = flight_booking.manage_passenger_information(passenger2)
print(update_status)

booking_confirmation = flight_booking.generate_booking_confirmation(passenger1)
print(booking_confirmation)


