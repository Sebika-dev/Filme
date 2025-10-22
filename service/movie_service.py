from datetime import datetime
from repository.movie_repository import MovieRepository
from domain.movie_domain import Movie

class service_movies:
    def __init__(self, repoMovie: MovieRepository):
        self.MovieRepository = repoMovie

    def add_movie(self, title: str, release_date: datetime, imdb_rating: float, actors: list):
        for movie in self.MovieRepository.get_all():
            if movie.title == title:
                raise ValueError("Movie already exists!")
        idNewMovie = self.MovieRepository.gen_id_movies()
        newMovie = Movie(idNewMovie, title, release_date, imdb_rating, actors)
        self.MovieRepository.add(newMovie)

    def remove_movie(self, idMovie: int):
        self.MovieRepository.delete(idMovie)

    def update_movie(self, updated_movie: Movie):
        self.MovieRepository.update(updated_movie)

    def get_movies(self):
        return self.MovieRepository.get_all()