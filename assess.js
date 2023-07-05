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
   this.tasting
   const cookies=new MoroccanRecipe("yummy")
   console.log(cookies)
   
//**Wildlife Preservation:** You're a wildlife conservationist working on a
//  program to track different species in a national park. Each species has its own
//  characteristics and behaviors, such as its diet, typical lifespan, migration
//  patterns, etc. Some species might be predators, others prey. You'll need to
//  create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
//  these classes might relate to each other through inheritance.


// class Wildlife{
//     constructor(  animals,diet,lifespan, migration,pattern){
//         this.animals =animals
//         this.diet=diet
//         this.lifespan=lifespan
//         this.migration=migration
//         this.pattern=pattern
//     }

//         working(){
              
//             console.log(`the ${this.animals} contaaint${this.lifespan} and take ${this.migration} and ${this.diet} and has ${this.pattern}`)   
            
//    }
   
//         }

//         class Species extends Wildlife{
//             constructor(  animals,diet,lifespan, migration,pattern,species){
//                    super(  animals,diet,lifespan, migration,pattern)
//                    this.species=species
                  
//                }
//                longhair(){
//                if ( `${this.hair}has ${this.lifespan} `)
//                console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
//            }
              
//            }

//            class Predator extends Wildlife{
//             constructor(  animals,diet,lifespan, migration,pattern,species){
//                    super(  animals,diet,lifespan, migration,pattern)
//                    this.species=species
                  
//                }
//                longhair(){
//                if ( `${this.hair}has ${this.lifespan} `)
//                console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
//            }
              
//            }
//            class Prey extends Wildlife{
//             constructor(  animals,diet,lifespan, migration,pattern,species){
//                    super(  animals,diet,lifespan, migration,pattern)
//                    this.species=species
                  
//                }
//                longhair(){
//                if ( `${this.hair}has ${this.lifespan} `)
//                console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
//            }
              
//            }



class Species {
    constructor(name ,diet, lifespan) {
        this.diet = diet;
        this.lifespan = lifespan;
        this.name =name
    }
}

class Predator extends Species {
    constructor(name,diet, lifespan, huntingStyle) {
        super(name,diet, lifespan);
        this.huntingStyle = huntingStyle;
    }

    huntPrey(prey) {

        console.log(`The ${this.name} is hunting the ${prey.name}!`);
        if (prey.diet === "Herbivore") {
            return `The ${this.name} successfully hunted the ${prey.name}!`;
        } else {
            return `The ${this.name} couldn't hunt the ${prey.name} because it's not a herbivore!`;
        }
    }
}

class Prey extends Species {
    constructor(name,diet, lifespan, migrationPattern) {
        super(name,diet, lifespan);
        this.migrationPattern = migrationPattern;
    }
}

const lion =new Predator("Lions","Canivorous",15,"Ambush hunting")
const zebra = new Prey("Zebra","Herbivore", 20, "Seasonal migration");
const gazelle = new Prey("gazelle","Herbivore", 10, "No migration");

const result1 = lion.huntPrey(zebra);
const result2 = lion.huntPrey(gazelle);

console.log(result1);
console.log(result2);


// **African Music Festival:** You're in charge of organizing a Pan-African music
// festival. Many artists from different countries, each with their own musical style
// and instruments, are scheduled to perform. You need to write a program to
// manage the festival lineup, schedule, and stage arrangements. Think about how
// you might model the `Artist`, `Performance`, and `Stage` classes, and consider
// how you might use inheritance if there are different types of performances or
// stages.

// class Music{
//     constructor(  animals,diet,lifespan, migration,pattern){
//         this.animals =animals
//         this.diet=diet
//         this.lifespan=lifespan
//         this.migration=migration
//         this.pattern=pattern
//     }

//         working(){
              
//             console.log(`the ${this.animals} contaaint${this.lifespan} and take ${this.migration} and ${this.diet} and has ${this.pattern}`)   
            
//    }
   
//         }

//         class Artist extends Music{
//             constructor(  animals,diet,lifespan, migration,pattern,species){
//                    super(  animals,diet,lifespan, migration,pattern)
//                    this.species=species
                  
//                }
//                longhair(){
//                if ( `${this.hair}has ${this.lifespan} `)
//                console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
//            }
              
//            }

//            class Performance extends Music{
//             constructor(  animals,diet,lifespan, migration,pattern,species){
//                    super(  animals,diet,lifespan, migration,pattern)
//                    this.species=species
                  
//                }
//                longhair(){
//                if ( `${this.hair}has ${this.lifespan} `)
//                console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
//            }
              
//            }
//            class Stage extends Music{
//             constructor(  animals,diet,lifespan, migration,pattern,species){
//                    super(  animals,diet,lifespan, migration,pattern)
//                    this.species=species
                  
//                }
//                longhair(){
//                if ( `${this.hair}has ${this.lifespan} `)
//                console.log(`the ${this.food} contaaint${this.ingredients} is ${this.species}` )
                
//            }
              
//            }




        //    4
        //Create an AnimalShelter class that holds only dogs and cats. The shel

        class Artist {
            constructor(name, country, musicalStyle, instruments) {
              this.name = name;
              this.country = country;
              this.musicalStyle = musicalStyle;
              this.instruments = instruments;
            }
          }
          
          class Performance {
            constructor(artist, stage, startTime, endTime) {
              this.artist = artist;
              this.stage = stage;
              this.startTime = startTime;
              this.endTime = endTime;
            }
          }
          
          class Stage {
            constructor(name, capacity) {
              this.name = name;
              this.capacity = capacity;
            }
          }
          
          class MainStage extends Stage {
            constructor(name, capacity, soundSystem) {
              super(name, capacity);
              this.soundSystem = soundSystem;
            }
          }
          
          class WorldStage extends Stage {
            constructor(name, capacity, decorations) {
              super(name, capacity);
              this.decorations = decorations;
            }
          }
          
          const artist1 = new Artist("Salif Keita", "Mali", "World", ["kora", "balafon"]);
          const artist2 = new Artist("Angelique Kidjo", "Benin", "Afropop", ["guitar", "vocals"]);
          const artist3 = new Artist("Tinariwen", "Algeria", "Tamazight folk", ["guitar", "vocals"]);
          
          const mainStage = new MainStage("Main Stage", 10000, "High-quality speakers");
          const worldStage = new WorldStage("World Stage", 5000, "Colorful banners");
          
          const performances = [
            new Performance(artist1, mainStage, "12:00 PM", "1:00 PM"),
            new Performance(artist2, worldStage, "2:00 PM", "3:00 PM"),
            new Performance(artist3, mainStage, "4:00 PM", "5:00 PM"),
          ];
          
          performances.forEach((performance) => {
            console.log(`${performance.artist.name} - ${performance.stage.name} - ${performance.startTime} to ${performance.endTime}`);
          });



// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values.

// class product{
//     constructor( ){
//         this.ingredients =ingredients
//         this.preparationtime=preparationtime
//         this.cookingmethod =cookingmethod
//         this.nutritional=nutritional
//         this.food=food
//     }

//         cooks(){
              
//             console.log(`the ${this.food} contaaint${this.ingredients} and take ${this.preparationtime} and ${this.cookingmethod} and has ${this.nutritional}`)   
            
//    }
   
//         }
   

        class Product {
            constructor(name, price, quantity) {
              this.name = name;
              this.price = price;
              this.quantity = quantity;
            }
          }
          

          const products = [
            new Product("Apple", 0.5, 10),
            new Product("Banana", 0.3, 15),
            new Product("Orange", 0.4, 12)
          ];
          
          let totalValue = 0;
          for (let i = 0; i < products.length; i++) {
            const product = products[i];
            if (product.quantity > 0) {
              totalValue += product.price * product.quantity;
            }
          }
          
        
          console.log("Total value of all products:", totalValue);

    class Products {
            constructor(name, price, quantity) {
              this.name = name;
              this.price = price;
              this.quantity = quantity;
            }
          }
          
          // Creating an array of Product instances
          const product = [
            new Product("Apple", 0.5, 10),
            new Product("Banana", 0.3, 15),
            new Product("Orange", 0.4, 12)
          ];
          
          // Calculating the total values using logical AND (&&) and logical OR (||) operators
          let totalValues = 0;
          for (let i = 0; i < products.length; i++) {
            const product = products[i];
            totalValue += (product.quantity > 0 && product.price > 0) ? (product.price * product.quantity) : 0;
          }
          
          // Printing the total value
          console.log("Total value of all products:", totalValue);



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


// question6
   class Students {
  constructor(name, age, grades) {
    this.name = name;
    this.age = age;
    this.grades = grades;
  }

  calculateAverageGrade() {
    let sum = 0;
    for (let i = 0; i < this.grades.length; i++) {
      sum += this.grades[i];
    }
    return sum / this.grades.length;
  }

  hasPassed() {
    const averageGrade = this.calculateAverageGrade();
    if (this.grades.length === 0) {
      return false;
    } else if (averageGrade >= 60 && this.grades.length >= 4) {
      return true;
    } else {
      return false;
    }
  }

  displayHighestGrade() {
    const highestGrade = Math.max(...this.grades);
    console.log("Highest Grade:", highestGrade);
  }
}

const students = [
  new Students("John Doe", 18, [80, 75, 90]),
  new Students("Jane Doe", 19, [70, 85, 65]),
  new Students("Alice Smith", 20, [90, 80, 95])
];

for (let student of students) {
  console.log("Student information:");
  console.log("Name:", student.name);
  console.log("Age:", student.age);
  console.log("Grades:", student.grades);
  const averageGrade = student.calculateAverageGrade();
  console.log("Average Grade:", averageGrade);

  const passingStatus = averageGrade >= 60 ? "Passed" : "Failed";
  console.log("Passing Status:", passingStatus);

  student.displayHighestGrade();

  console.log();
}


// 
// Create a FlightBooking class that represents a flight booking system. Implement
// methods to search for available flights based on destination and date, reserve
// seats for customers, manage passenger information, and generate booking
// confirmations.

class PassengerDetails {
  constructor(name, email) {
    this.name = name;
    this.email = email;
  }

  updateInformation(email, phone) {
    this.email = email;
    this.phone = phone;
  }
}

class FlightBooking {
  constructor(destination, date, capacity) {
    this.destination = destination;
    this.date = date;
    this.capacity = capacity;
    this.passengers = [];
    this.flights = [];
  }

  searchFlights(destination, date) {
    const availableFlights = [];
    for (const flight of this.flights) {
      if (flight.destination === destination && flight.date === date) {
        availableFlights.push(flight);
      }
    }
    return availableFlights;
  }

  reserveSeat(passenger) {
    if (this.passengers.length < this.capacity) {
      this.passengers.push(passenger);
      return true;
    } else {
      return false;
    }
  }

  managePassengerInformation(updatedPassenger) {
    for (const passenger of this.passengers) {
      if (passenger.name === updatedPassenger.name) {
        passenger.updateInformation(updatedPassenger.email, updatedPassenger.phone);
        return true;
      }
    }
    return false;
  }

  generateBookingConfirmation(passenger) {
    for (const p of this.passengers) {
      if (p.name === passenger.name) {
        return `Booking confirmation for ${p.name} on ${this.date} to ${this.destination}`;
      }
    }
    return "Passenger not found";
  }
}

const flightBooking = new FlightBooking("Tanzania", "2023-04-30", 90);
const availableFlights = flightBooking.searchFlights("Uganda", "2022-03-20");
console.log(availableFlights);

const passenger1 = new PassengerDetails("Nkatha", "nkatha@gmail.com");
const reservationStatus = flightBooking.reserveSeat(passenger1);
console.log(reservationStatus);

const passenger2 = new PassengerDetails("Mily", "milly@gmail.com");
passenger2.updateInformation("milly@gmail.com", "1234567890");
const updateStatus = flightBooking.managePassengerInformation(passenger2);
console.log(updateStatus);

const bookingConfirmation = flightBooking.generateBookingConfirmation(passenger1);
console.log(bookingConfirmation);