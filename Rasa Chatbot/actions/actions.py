from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Movie Names by Genre
MOVIE_RECOMMENDATIONS = {
    "action": [
        "Mad Max: Fury Road", "John Wick", "Die Hard", "The Dark Knight", "Gladiator", 
        "The Avengers", "Mission: Impossible - Fallout", "Inception", "The Bourne Identity", 
        "The Matrix"
    ],
    "comedy": [
        "Superbad", "The Hangover", "Monty Python and the Holy Grail", "Step Brothers", 
        "Anchorman", "Groundhog Day", "21 Jump Street", "Ferris Bueller's Day Off", 
        "Dumb and Dumber", "The Grand Budapest Hotel"
    ],
    "drama": [
        "The Shawshank Redemption", "Forrest Gump", "The Godfather", "Fight Club", 
        "The Pursuit of Happyness", "Schindler's List", "A Beautiful Mind", "12 Angry Men", 
        "The Green Mile", "American Beauty"
    ],
    "romance": [
        "The Notebook", "Titanic", "Pride and Prejudice", "La La Land", "Notting Hill", 
        "500 Days of Summer", "Romeo + Juliet", "The Fault in Our Stars", "Before Sunrise", 
        "When Harry Met Sally"
    ],
    "horror": [
        "The Shining", "Get Out", "A Nightmare on Elm Street", "The Conjuring", "It", 
        "Hereditary", "The Exorcist", "The Ring", "Paranormal Activity", "Psycho"
    ],
    "thriller": [
        "Se7en", "Gone Girl", "Shutter Island", "The Sixth Sense", "Prisoners", 
        "The Silence of the Lambs", "Zodiac", "Memento", "Oldboy", "Fight Club"
    ],
    "sci-fi": [
        "Blade Runner", "The Matrix", "Star Wars: A New Hope", "Interstellar", "Inception", 
        "2001: A Space Odyssey", "The Terminator", "E.T. the Extra-Terrestrial", 
        "Minority Report", "Star Trek"
    ],
    "adventure": [
        "Indiana Jones: Raiders of the Lost Ark", "Pirates of the Caribbean", "The Lord of the Rings: The Fellowship of the Ring", 
        "The Hobbit: An Unexpected Journey", "Jurassic Park", "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", 
        "Avatar", "The Princess Bride", "King Kong", "Back to the Future"
    ],
    "fantasy": [
        "Harry Potter and the Sorcerer's Stone", "The Lord of the Rings: The Return of the King", 
        "The Chronicles of Narnia", "The Princess Bride", "Alice in Wonderland", 
        "The Wizard of Oz", "Stardust", "Pan's Labyrinth", "The Shape of Water", "Doctor Strange"
    ],
    "animation": [
        "Toy Story", "The Lion King", "Frozen", "Shrek", "Finding Nemo", 
        "Up", "The Incredibles", "Spirited Away", "Coco", "Zootopia"
    ]
}
# Returns the particular array of a genre by user request
class ActionRecommendMovies(Action):
    def name(self) -> Text:
        return "action_recommend_movies"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        genre = tracker.get_slot("genre")  # Get the genre from the slot
        
        if genre in MOVIE_RECOMMENDATIONS:
            movie_list = MOVIE_RECOMMENDATIONS[genre]
            movie_list_str = ", ".join(movie_list)  # Join the movie list as a string
            dispatcher.utter_message(text=f"Here are some {genre} movies you might like: {movie_list_str}")
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find any movies for that genre. Try another genre!")

        return []  #  return statement
