import media
import fresh_tomatoes

# initializing favorite movies
sw7 = media.Movie(
	"Star Wars: The Force Awakens",
	"An epic continuation of the Sci-Fi series",
	"https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
	"https://www.youtube.com/watch?v=sGbxmsDFVnE")
	
waterboy = media.Movie(
	"Waterboy",
	"A waterboy becomes the last hope for a struggling college football team",
	"https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Waterboy-poster-0.jpg/220px-Waterboy-poster-0.jpg",
	"https://www.youtube.com/watch?v=z8yv9eq5s14")
	
starship = media.Movie(
	"Starship Troopers",
	"A futuristic miltary takes on a planet of bugs",
	"https://upload.wikimedia.org/wikipedia/en/thumb/d/df/Starship_Troopers_-_movie_poster.jpg/220px-Starship_Troopers_-_movie_poster.jpg",
	"https://www.youtube.com/watch?v=Y07I_KER5fE")
	
goodburger = media.Movie(
	"Good Burger",
	"A wacky adventure of two unlikely friends working at a burger restaurant",
	"https://upload.wikimedia.org/wikipedia/en/thumb/c/c0/Good_Burger_film_poster.jpg/220px-Good_Burger_film_poster.jpg",
	"https://www.youtube.com/watch?v=rVTw5LK1zsQ")
	
wick = media.Movie(
	"John Wick",
	"After losing everything, a retired hitman comes to take everything",
	"https://upload.wikimedia.org/wikipedia/en/thumb/9/98/John_Wick_TeaserPoster.jpg/220px-John_Wick_TeaserPoster.jpg",
	"https://www.youtube.com/watch?v=2AUmvWm5ZDQ")
	
shaolin = media.Movie(
	"Shaolin Soccer",
	"Former kungfu masters apply their skills to soccer",
	"https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/ShaolinSoccerFilmPoster.jpg/220px-ShaolinSoccerFilmPoster.jpg",
	"https://www.youtube.com/watch?v=6FAaOwNnHTA")

# putting movie objects into a list
movies = [sw7, waterboy, starship, shaolin, goodburger, wick]

# uses fresh_tomatoes to create html page
fresh_tomatoes.open_movies_page(movies)
