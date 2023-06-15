// Ancestral Stories: In many African cultures, the art of storytelling is passed
//  down from generation to generation. Imagine you're creating an application that
//  records these oral stories and translates them into different languages. The
//  stories vary by length, moral lessons, and the age group they are intended for.
//  Think about how you would model `Story`, `StoryTeller`, and `Translator`
//  objects, and how inheritance might come into play if there are different types of
//  stories or storytellers.

class Story {
    constructor(length, moralLessons, ageGroup) {
        this.length = length;
        this.moralLessons = moralLessons;
        this.ageGroup = ageGroup;
    }
}

class Translator {
    translate(story, language) {
       this.story =story
       this.language=language
        return "Translated story";
    }
}

class Folklore extends Story {
    constructor(length, moralLessons, ageGroup, region) {
        super(length, moralLessons, ageGroup);
        this.region = region;
    }
}

class Mythology extends Story {
    constructor(length, moralLessons, ageGroup, deity) {
        super(length, moralLessons, ageGroup);
        this.deity = deity;
    }
}

class StoryTeller {
    constructor(name) {
        this.name = name;
    }

    tellStory(story) {
        this.story =story
        return "Telling story";
    }
}

class Grandparent extends StoryTeller {
    constructor(name) {
        super(name);
    }

    shareWisdom() {
        return "Sharing wisdom to children";
    }
}

class Storyteller extends StoryTeller {
    constructor(name, experienceYears) {
        super(name);
        this.experienceYears = experienceYears;
    }

    entertain() {
        return " audience listening";
    }
}


const folklore = new Folklore("long", ["Learnind1", "Learning2"], "petter", "kenya");
const translator = new Translator();
const translatedStory = translator.translate(folklore, "English");
console.log(translatedStory);

const grandparent = new Grandparent("Gloria");
const storytellingResult = grandparent.tellStory(folklore);
console.log(storytellingResult);

const professionalStoryteller = new Storyteller("mary", 8);
const entertainment = professionalStoryteller.entertain();
console.log(entertainment);



// **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.

class Recipe{
    constructor(  ingredients,preparationtime,cookingmethod, nutritional,food){
        this.ingredients =ingredients
        this.preparationtime=preparationtime
        this.cookingmethod =cookingmethod
        this.nutritional=nutritional
        this.food=food
    }

        cooks(){
              
            console.log(`the ${this.food} contaaint${this.ingredients} and take ${this.preparationtime} and ${this.cookingmethod} and has ${this.nutritional}`)   
            
   }
   
        }
           
   
   class MoroccanRecipe extends Recipe{
    constructor(  ingredients,preparationtime,cookingmethod, nutritional,food,taste){
           super( ingredients,preparationtime,cookingmethod, nutritional,food)
         
           this.taste=taste
   
       }
       tasting(){
       if ( `${this.food} is tasty `)
       console.log(`the ${this.food} contaaint${this.ingredients} is moroccanrep` )
        
   }
      
   }   
   class EthiopianRecipe extends Recipe{
    constructor(  ingredients,preparationtime,cookingmethod, nutritional,food){
           super( ingredients,preparationtime,cookingmethod, nutritional,food)
         
             this.taste=taste
   
       }
       tasting(){
       if ( `${this.food} is tasty `)
       console.log(`the ${this.food} contaaint${this.ingredients} is moroccanrep` )
        
   }
      
   }
   class NigerianRecipe extends Recipe{
    constructor(  ingredients,preparationtime,cookingmethod, nutritional,food){
           super( ingredients,preparationtime,cookingmethod, nutritional,food)
         
           this.taste=taste
   
       }
       tasting(){
       if ( `${this.food} is tasty `)
       console.log(`the ${this.food} contaaint${this.ingredients} is moroccanrep` )
        
   }
      
   }
      
   
   const foods = new Recipe("salt","3time","boiled","high","okra")
   console.log(stories)
   this.tasting
   const cookies=new MoroccanRecipe("yummy")
   console.log(cookies)
   
//**Wildlife Preservation:** You're a wildlife conservationist working on a
//  program to track different species in a national park. Each species has its own
//  characteristics and behaviors, such as its diet, typical lifespan, migration
//  patterns, etc. Some species might be predators, others prey. You'll need to
//  create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
//  these classes might relate to each other through inheritance.


class Wildlife{
    constructor(  animals,diet,lifespan, migration,pattern){
        this.animals =animals
        this.diet=diet
        this.lifespan=lifespan
        this.migration=migration
        this.pattern=pattern
    }

        working(){
              
            console.log(`the ${this.animals} contaaint${this.lifespan} and take ${this.migration} and ${this.diet} and has ${this.pattern}`)   
            
   }
   
        }

        class Species extends Wildlife{
            constructor(  animals,diet,lifespan, migration,pattern,species){
                   super(  animals,diet,lifespan, migration,pattern)
                   this.species=species
                  
               }
               longhair(){
               if ( `${this.hair}has ${this.lifespan} `)
               console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
           }
              
           }

           class Predator extends Wildlife{
            constructor(  animals,diet,lifespan, migration,pattern,species){
                   super(  animals,diet,lifespan, migration,pattern)
                   this.species=species
                  
               }
               longhair(){
               if ( `${this.hair}has ${this.lifespan} `)
               console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
           }
              
           }
           class Prey extends Wildlife{
            constructor(  animals,diet,lifespan, migration,pattern,species){
                   super(  animals,diet,lifespan, migration,pattern)
                   this.species=species
                  
               }
               longhair(){
               if ( `${this.hair}has ${this.lifespan} `)
               console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
           }
              
           }



           



// **African Music Festival:** You're in charge of organizing a Pan-African music
// festival. Many artists from different countries, each with their own musical style
// and instruments, are scheduled to perform. You need to write a program to
// manage the festival lineup, schedule, and stage arrangements. Think about how
// you might model the `Artist`, `Performance`, and `Stage` classes, and consider
// how you might use inheritance if there are different types of performances or
// stages.

class Music{
    constructor(  animals,diet,lifespan, migration,pattern){
        this.animals =animals
        this.diet=diet
        this.lifespan=lifespan
        this.migration=migration
        this.pattern=pattern
    }

        working(){
              
            console.log(`the ${this.animals} contaaint${this.lifespan} and take ${this.migration} and ${this.diet} and has ${this.pattern}`)   
            
   }
   
        }

        class Artist extends Music{
            constructor(  animals,diet,lifespan, migration,pattern,species){
                   super(  animals,diet,lifespan, migration,pattern)
                   this.species=species
                  
               }
               longhair(){
               if ( `${this.hair}has ${this.lifespan} `)
               console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
           }
              
           }

           class Performance extends Music{
            constructor(  animals,diet,lifespan, migration,pattern,species){
                   super(  animals,diet,lifespan, migration,pattern)
                   this.species=species
                  
               }
               longhair(){
               if ( `${this.hair}has ${this.lifespan} `)
               console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
           }
              
           }
           class Stage extends Music{
            constructor(  animals,diet,lifespan, migration,pattern,species){
                   super(  animals,diet,lifespan, migration,pattern)
                   this.species=species
                  
               }
               longhair(){
               if ( `${this.hair}has ${this.lifespan} `)
               console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
           }
              
           }




// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

class product{
    constructor( ){
        this.ingredients =ingredients
        this.preparationtime=preparationtime
        this.cookingmethod =cookingmethod
        this.nutritional=nutritional
        this.food=food
    }

        cooks(){
              
            console.log(`the ${this.food} contaaint${this.ingredients} and take ${this.preparationtime} and ${this.cookingmethod} and has ${this.nutritional}`)   
            
   }
   
        }
   


// Implement a class called Student with attributes for name, age, and grades (a
// list of integers). Include methods to calculate the average grade, display the
// student information, and determine if the student has passed (average grade >=
// 60). Create objects for the Student class and demonstrate the usage of these
// methods.

class Student{
    constructor(  ingredients,preparationtime,cookingmethod, nutritional,food){
        this.ingredients =ingredients
        this.preparationtime=preparationtime
        this.cookingmethod =cookingmethod
        this.nutritional=nutritional
        this.food=food
    }

        cooks(){
              
            console.log(`the ${this.food} contaaint${this.ingredients} and take ${this.preparationtime} and ${this.cookingmethod} and has ${this.nutritional}`)   
            
   }
   
        }


// Create a FlightBooking class that represents a flight booking system. Implement
// methods to search for available flights based on destination and date, reserve
// seats for customers, manage passenger information, and generate booking
// confirmations.

class FlightBooking{
    constructor(  ingredients,preparationtime,cookingmethod, nutritional,food){
        this.ingredients =ingredients
        this.preparationtime=preparationtime
        this.cookingmethod =cookingmethod
        this.nutritional=nutritional
        this.food=food
    }

        cooks(){
              
            console.log(`the ${this.food} contaaint${this.ingredients} and take ${this.preparationtime} and ${this.cookingmethod} and has ${this.nutritional}`)   
            
   }
   
        }


// Create a LibraryCatalog class that handles the cataloging and management of
// books in a library. Implement methods to add new books, search for books by
// title or author, keep track of available copies, and display book details.


class LibraryCatalog{
    constructor(  ingredients,preparationtime,cookingmethod, nutritional,food){
        this.ingredients =ingredients
        this.preparationtime=preparationtime
        this.cookingmethod =cookingmethod
        this.nutritional=nutritional
        this.food=food
    }

        cooks(){
              
            console.log(`the ${this.food} contaaint${this.ingredients} and take ${this.preparationtime} and ${this.cookingmethod} and has ${this.nutritional}`)   
            
   }
   
        }