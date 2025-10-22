class Watchlist:
    def __init__(self, watchlist_id: int, user_id: int, movie_ids: list[int]):
        self.watchlist_id = watchlist_id
        self.user_id = user_id
        self.movie_ids = movie_ids

    @property
    def watchlist_id(self):
        return self._watchlist_id

    @watchlist_id.setter
    def watchlist_id(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("watchlist_id must be a non-negative integer.")
        self._watchlist_id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("user_id must be a non-negative integer.")
        self._user_id = value

    @property
    def movie_ids(self):
        return self._movie_ids

    @movie_ids.setter
    def movie_ids(self, value):
        if not isinstance(value, list) or not all(isinstance(movie_id, int) for movie_id in value):
            raise ValueError("movie_ids must be a list of integers.")
        self._movie_ids = value

    def __str__(self):
        return f"Watchlist[ID={self.watchlist_id}, User ID={self.user_id}, Movies={', '.join(map(str, self.movie_ids))}]"