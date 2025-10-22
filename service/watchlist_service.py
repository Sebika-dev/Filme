class ServiceWatchlists:
    def __init__(self, watchlist_repo, movie_repo):
        self.watchlist_repo = watchlist_repo
        self.movie_repo = movie_repo

    def add_movie_to_watchlist(self, watchlist_id: int, movie_id: int):
        self.watchlist_repo.add_movie_to_watchlist(watchlist_id, movie_id)

    def edit_watchlist(self, watchlist_id: int, new_movie_ids: list[int]):
        self.watchlist_repo.edit_watchlist(watchlist_id, new_movie_ids)

    def filter_movies_by_actor(self, actor_name: str):
        return self.watchlist_repo.filter_movies_by_actor(self.movie_repo, actor_name)

    def filter_movies_by_imdb(self, min_rating: float):
        return self.watchlist_repo.filter_movies_by_imdb(self.movie_repo, min_rating)

    def count_movies_with_actor(self, actor_name: str):
        return self.watchlist_repo.count_movies_with_actor(self.movie_repo, actor_name)

    def average_imdb_for_actor(self, actor_name: str):
        return self.watchlist_repo.average_imdb_for_actor(self.movie_repo, actor_name)