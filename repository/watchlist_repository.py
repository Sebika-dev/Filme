from functools import reduce
from domain.watchlist_domain import Watchlist

class WatchlistRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.watchlists = []
        self.__load()

    def __save(self):
        with open(self.file_path, "w") as file:
            for watchlist in self.watchlists:
                movie_ids_str = ";".join(map(str, watchlist.movie_ids))
                file.write(f"{watchlist.watchlist_id},{watchlist.user_id},{movie_ids_str}\n")

    def __load(self):
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    watchlist_id, user_id, movie_ids = line.strip().split(",")
                    movie_ids_list = [int(movie_id) for movie_id in movie_ids.split(";") if movie_id]
                    self.watchlists.append(Watchlist(int(watchlist_id), int(user_id), movie_ids_list))
        except FileNotFoundError:
            self.watchlists = []

    def get_all(self):
        return self.watchlists

    def generate_id(self):
        return max((watchlist.watchlist_id for watchlist in self.watchlists), default=0) + 1

    def add(self, watchlist: Watchlist):
        self.watchlists.append(watchlist)
        self.__save()

    def filter_movies_by_imdb(self, movie_repo, min_rating: float):
        all_movie_ids = {movie_id for watchlist in self.watchlists for movie_id in watchlist.movie_ids}
        return list(filter(lambda movie: movie.imdb_rating > min_rating and movie.movie_id in all_movie_ids,
                           movie_repo.get_all()))

    def count_movies_with_actor(self, movie_repo, actor_name: str):
        all_movie_ids = {movie_id for watchlist in self.watchlists for movie_id in watchlist.movie_ids}
        movies_with_actor = filter(lambda movie: actor_name in movie.actors and movie.movie_id in all_movie_ids,
                                   movie_repo.get_all())
        return len(list(movies_with_actor))

    def average_imdb_for_actor(self, movie_repo, actor_name: str):
        all_movie_ids = {movie_id for watchlist in self.watchlists for movie_id in watchlist.movie_ids}
        relevant_movies = list(filter(lambda movie: actor_name in movie.actors and movie.movie_id in all_movie_ids,movie_repo.get_all()))
        if not relevant_movies:
            return 0.0

        total_rating = reduce(lambda acc, movie: acc + movie.imdb_rating, relevant_movies, 0.0)
        return total_rating / len(relevant_movies)