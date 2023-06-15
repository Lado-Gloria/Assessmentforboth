// Ancestral Stories: In many African cultures, the art of storytelling is passed
//  down from generation to generation. Imagine you're creating an application that
//  records these oral stories and translates them into different languages. The
//  stories vary by length, moral lessons, and the age group they are intended for.
//  Think about how you would model `Story`, `StoryTeller`, and `Translator`
//  objects, and how inheritance might come into play if there are different types of
//  stories or storytellers.


class Storytelling{
 constructor( length,morallessons,agegroup,story){
        this.length =length
        this.story=story
        this.morallessons =morallessons
        this.agegroup =agegroup
 }
     storys(){
        return `the ${this.length}of the ${this.story}depend on the${this.agegroup}` 
}

     }
        

class Storys extends Storytelling{
    constructor( length,morallessons,agegroup,story,languages){
        super(length,morallessons,agegroup,story,)
      
        this.languages=languages

    }
    stori(){
    if (story =="short" || story =="English")
    return `the ${this.length}of the ${this.story}depend on the${this.agegroup}` 
}
   
}   
class StoryTeller extends Storytelling{
    constructor(length,morallessons,agegroup,story,storteller){
        super(length,morallessons,agegroup,story,)
       
        this.storteller=storteller

    }
    stories(){
        if (story =="short" || story =="English")
        return `the ${this.length}of the ${this.story}depend on the${this.agegroup}` 
    }

}
   

const stories = new Storytelling("long","entertainment","the child","children")
console.log(stories)
const teller =new StoryTeller("mommy")
console.log(teller.stori(""))

console.log(this .stories)




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
   


// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

class product{
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