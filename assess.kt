// Ancestral Stories: In many African cultures, the art of storytelling is passed
//  down from generation to generation. Imagine you're creating an application that
//  records these oral stories and translates them into different languages. The
//  stories vary by length, moral lessons, and the age group they are intended for.
//  Think about how you would model `Story`, `StoryTeller`, and `Translator`
//  objects, and how inheritance might come into play if there are different types of
//  stories or storytellers.

fun main() {
    val folklore = Folklore("medium", listOf("Lesson 1", "Lesson 2"), "children", "West Africa")
    val translator = Translator()
    val translatedStory = translator.translate(folklore, "French")
    println(translatedStory)

    val grandparent = Grandparent("John")
    val storytellingResult = grandparent.tellStory(folklore)
    println(storytellingResult)

    val professionalStoryteller = ProfessionalStoryteller("Alice", 10)
    val entertainmentResult = professionalStoryteller.entertainAudience()
    println(entertainmentResult)
}



open class Story(val length: String, val moralLessons: List<String>, val ageGroup: String)

class Translator {
    fun translate(story: Story, language: String): String {
       
        return "the story is a long in ${language}"
    }
}


class Folklore(length: String, moralLessons: List<String>, ageGroup: String, val region: String) :
    Story(length, moralLessons, ageGroup)

class Mythology(length: String, moralLessons: List<String>, ageGroup: String, val deity: String) :
    Story(length, moralLessons, ageGroup)


open class StoryTeller(val name: String) {
    fun tellStory(story: Story): String {
        return "Telling story"
    }
}

class Grandparent(name: String) : StoryTeller(name) {
    fun shareWisdom(): String {
        return "Sharing wisdom"
    }
}

class ProfessionalStoryteller(name: String, val experienceYears: Int) : StoryTeller(name) {
    fun entertainAudience(): String {
        return "Entertaining audience"
    }
}



// **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.

















//**Wildlife Preservation:** You're a wildlife conservationist working on a
//  program to track different species in a national park. Each species has its own
//  characteristics and behaviors, such as its diet, typical lifespan, migration
//  patterns, etc. Some species might be predators, others prey. You'll need to
//  create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
//  these classes might relate to each other through inheritance.



open class Species(val diet: String, val lifespan: Int)

class Predator(diet: String, lifespan: Int, val huntingStyle: String) : Species(diet, lifespan)

class Prey(diet: String, lifespan: Int, val migrationPattern: String) : Species(diet, lifespan)



fun main (){
    val lion = Predator("Carnivore", 15, "Ambush hunting")
val zebra = Prey("Herbivore", 20, "Seasonal migration")

println("Lion:")
println("Diet: ${lion.diet}")
println("Lifespan: ${lion.lifespan}")
println("Hunting Style: ${lion.huntingStyle}")
println()

println("Zebra:")
println("Diet: ${zebra.diet}")
println("Lifespan: ${zebra.lifespan}")
println("Migration Pattern: ${zebra.migrationPattern}")
}

