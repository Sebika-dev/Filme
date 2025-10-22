from domain.movie_domain import Movie
from datetime import datetime
from repository.movie_repository import MovieRepository
from service.movie_service import service_movies


def test_add_movie():
    test_file_path = "test_movies.txt"
    repo = MovieRepository(test_file_path)
    service = service_movies(repo)
    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    service.add_movie("Mama", release_date, 8.5, ["Tata"])
    all_movies = repo.get_all()

    assert len(all_movies) == 1
    assert all_movies[0].title == "Mama"
    assert all_movies[0].imdb_rating == 8.5
    assert "Tata" in all_movies[0].actors
    cleanup(test_file_path)


def test_get_all_movies():
    test_file_path = "test_movies.txt"
    repo = MovieRepository(test_file_path)
    service = service_movies(repo)

    release_date1 = datetime.strptime("01-01-2020", "%d-%m-%Y")
    release_date2 = datetime.strptime("01-01-2021", "%d-%m-%Y")

    service.add_movie("Mama", release_date1, 8.5, ["Tata"])
    service.add_movie("Venom", release_date2, 8.5, ["Ghita"])

    all_movies = repo.get_all()

    assert len(all_movies) == 2
    assert all_movies[0].title == "Mama"    
    assert all_movies[1].title == "Venom"
    cleanup(test_file_path)


def test_remove_movie():
    test_file_path = "test_movies.txt"
    repo = MovieRepository(test_file_path)
    service = service_movies(repo)

    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    service.add_movie("Mama", release_date, 8.5, ["Tata"])

    all_movies = repo.get_all()
    assert len(all_movies) == 1

    service.remove_movie(all_movies[0].movie_id)
    all_movies = repo.get_all()
    assert len(all_movies) == 0
    cleanup(test_file_path)


def test_update_movie():
    test_file_path = "test_movies.txt"
    repo = MovieRepository(test_file_path)
    service = service_movies(repo)

    release_date = datetime.strptime("01-01-2020", "%d-%m-%Y")
    service.add_movie("Mama", release_date, 8.5, ["Tata"])

    all_movies = repo.get_all()
    movie_to_update = all_movies[0]

    updated_movie = Movie(movie_to_update.movie_id, "Updated Movie", release_date, 9.0, ["Misu"])
    repo.update(updated_movie)
    all_movies = repo.get_all()

    assert len(all_movies) == 1
    assert all_movies[0].title == "Updated Movie"
    assert all_movies[0].imdb_rating == 9.0
    assert "Misu" in all_movies[0].actors
    cleanup(test_file_path)


def cleanup(file_path):
    import os
    if os.path.exists(file_path):
        os.remove(file_path)


if __name__ == "__main__":
    test_add_movie()
    print("test_add_movie passed")
    test_get_all_movies()
    print("test_get_all_movies passed")
    test_remove_movie()
    print("test_remove_movie passed")
    test_update_movie()
    print("test_update_movie passed")