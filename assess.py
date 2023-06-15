# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

class Story:
    def __init__(self, length, morallessons, agegroup):
        self.length = length
        self.morallessons = morallessons
        self.agegroup = agegroup

class Translator:
    def translate(self, story, language):
        self.story =story
        self.language =language
       
        return f"the {self.story} is in {self.language}"

class Folklore(Story):
    def __init__(self, length, moral_lessons, age_group, region):
        super().__init__(length, moral_lessons, age_group)
        self.region = region

class Mythology(Story):
    def __init__(self, length, moral_lessons, age_group, deity):
        super().__init__(length, moral_lessons, age_group)
        self.deity = deity

class StoryTeller:
    def __init__(self, name):
        self.name = name

    def tell_story(self, story):
        return "Telling story"

class Grandparent(StoryTeller):
    def __init__(self, name):
        super().__init__(name)

    def share_wisdom(self):
        return "Sharing wisdom"

class ProfessionalStoryteller(StoryTeller):
    def __init__(self, name, experience_years):
        super().__init__(name)
        self.experience_years = experience_years

    def entertain_audience(self):
        return "Entertaining audience"


folklore = Folklore("medium", ["Lesson 1", "Lesson 2"], "children", "West Africa")
translator = Translator()
translated_story = translator.translate(folklore, "French")
print(translated_story)

grandparent = Grandparent("John")
storytelling_result = grandparent.tell_story(folklore)
print(storytelling_result)

professional_storyteller = ProfessionalStoryteller("Alice", 10)
entertainment_result = professional_storyteller.entertain_audience()
print(entertainment_result)

# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

class Recipe :
  def __int__(self, ingredients,preparationtime,cookingmethod, nutritional,food):
        self.ingredients =ingredients
        self.preparationtime=preparationtime
        self.cookingmethod =cookingmethod
        self.nutritional=nutritional
        self.food=food
  def cook(self):   
      print(f"the {self.food} contaaint{self.ingredients} and take {self.preparationtime} and {self.cookingmethod} and has {self.nutritional}")   
      

class MoroccanRecipe(Recipe):
      def __int__(self, ingredients,preparationtime,cookingmethod, nutritional,food,taste):
           super.__init__(self, ingredients,preparationtime,cookingmethod, nutritional,food)
           self.taste=taste

      def tasting(self):  
       if {self.food} =={self.taste}: 
        print(f"the {self.food}with {self.taste}is a moreccanRecipe") 

       else:
           print("it not a moroccanRecipe")
             
      
class NigerianRecipe(Recipe):
      def __int__(self, ingredients,preparationtime,cookingmethod, nutritional,food,slipery):
           super.__init__(self, ingredients,preparationtime,cookingmethod, nutritional,food)
           self.slipery =slipery

      def tasty(self):  
       if {self.food} =={self.slipery}: 
        print(f"the {self.food}with {self.taste}is a nigerianRecipe")

       else:
           print("it not a nigerianRecipe")   
      
class EthiopianRecipe(Recipe):
      def __int__(self, ingredients,preparationtime,cookingmethod, nutritional,food,cookwell):
           super.__init__(self, ingredients,preparationtime,cookingmethod, nutritional,food)
           self.cookwell=cookwell

      def cooking(self):  
       if {self.food} =={self.cookwell}: 
        print(f"the {self.food}with {self.cookwell}is a ethiopianRecipe") 

         
       else:
           print("it not a ethiopianRecipe")    
      
                
      

foods =Recipe("salt","3time","boiled","high","okra",)
         


# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to
# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.
        
        