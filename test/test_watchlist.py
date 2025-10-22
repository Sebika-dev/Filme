from repository.watchlist_repository import WatchlistRepository
from service.watchlist_service import ServiceWatchlists
from domain.movie_domain import Movie
from repository.movie_repository import MovieRepository
from domain.watchlist_domain import Watchlist
from datetime import datetime
import os

def run_tests():
    print("Running tests")
    movie_repo = MovieRepository("movies_test_manual.txt")
    watchlist_repo = WatchlistRepository("watchlists_test_manual.txt")

    movie_repo.add(Movie(1, "Inception", datetime(2010, 7, 16), 8.8, ["Leonardo DiCaprio"]))
    movie_repo.add(Movie(2, "The Dark Knight", datetime(2008, 7, 18), 9.0, ["Christian Bale"]))
    movie_repo.add(Movie(3, "Interstellar", datetime(2014, 11, 7), 8.6, ["Matthew McConaughey"]))

    # Now, add movies to the watchlist
    watchlist_repo.add(Watchlist(1, 1, [1, 2]))  # Movies 1 and 2
    watchlist_repo.add(Watchlist(2, 2, [3]))  # Movie 3

    service = ServiceWatchlists(watchlist_repo, movie_repo)

    print("Test 1: Add movie to watchlist")
    service.add_movie_to_watchlist(1, 3)
    watchlist = next(wl for wl in watchlist_repo.get_all() if wl.watchlist_id == 1)
    assert 3 in watchlist.movie_ids, "Test 1 Failed: Movie not added correctly"
    print("Test 1 Passed!")

    print("Test 2: Edit watchlist")
    service.edit_watchlist(1, [2, 3])
    watchlist = next(wl for wl in watchlist_repo.get_all() if wl.watchlist_id == 1)
    assert watchlist.movie_ids == [2, 3], "Test 2 Failed: Watchlist not updated correctly"
    print("Test 2 Passed!")

    print("Test 3: Filter movies by actor")
    movies = service.filter_movies_by_actor("Leonardo DiCaprio")
    assert len(movies) == 1 and movies[0].title == "Inception", "Test 3 Failed: Incorrect filtering by actor"
    print("Test 3 Passed!")

    print("Test 4: Filter movies by IMDb rating")
    movies = service.filter_movies_by_imdb(8.7)
    assert len(movies) == 2, "Test 4 Failed: Incorrect filtering by IMDb rating"
    print("Test 4 Passed!")

    print("Test 5: Count movies by actor")
    count = service.count_movies_with_actor("Christian Bale")
    assert count == 1, "Test 5 Failed: Incorrect movie count by actor"
    print("Test 5 Passed!")

    print("Test 6: Calculate average IMDb for actor")
    average_rating = service.average_imdb_for_actor("Matthew McConaughey")
    assert abs(average_rating - 8.6) < 0.01, "Test 6 Failed: Incorrect average IMDb calculation"
    print("Test 6 Passed!")

    os.remove("movies_test_manual.txt")
    os.remove("watchlists_test_manual.txt")

    print("All tests passed successfully!")

run_tests()