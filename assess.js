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
   
   
   
   