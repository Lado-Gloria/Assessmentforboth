# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.


class Storytelling:
    def __int__(self, length,morallessons,agegroup,story):
        self.length =length
        self.story=story
        self.morallessons =morallessons
        self.agegroup =agegroup
    def  storys(self):
        print( f"the {self.length}of the {self.story}depend on the{self.agegroup}") 

class Storys(Storytelling):
    def __init__(self, length,morallessons,agegroup,story,languages):
           super.__init__(self, length,morallessons,agegroup,story,)
           self.language=languages
           if story =="short" and story =="English":
             print( f"the {self.length}of the {self.story}depend on the{self.agegroup}") 

class StoryTeller(Storytelling):
     def __init__(self, length,morallessons,agegroup,story,storteller):
           super.__init__(self, length,morallessons,agegroup,story,)
           self.storyteller=storteller
           if story =="short" and story =="English":
             print( f"the {self.length}of the {self.story}depend on the{self.agegroup}" )



stories =Storytelling("long","entertainment","the child","children")
print(stories)



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
         



        
        