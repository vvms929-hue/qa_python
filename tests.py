import pytest
from main import BooksCollector


# фикстура
@pytest.fixture
def collector():
    return BooksCollector()


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):

        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # add_new_book
    @pytest.mark.parametrize(
        "name, is_added",
        [
            ("А", True),
            ("А" * 40, True),
            ("", False),
            ("А" * 41, False),
        ],
    )
    def test_add_new_book_name_length_boundary_values(self, collector, name, is_added):
        collector.add_new_book(name)
        assert (name in collector.get_books_genre()) == is_added

    # set_book_genre
    @pytest.mark.parametrize(
        "genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]
    )
    def test_set_book_genre_genre_from_list_genre_set(self, genre, collector):
        collector.add_new_book("Хоббит")
        collector.set_book_genre("Хоббит", genre)
        assert collector.get_book_genre("Хоббит") == genre

    # get_book_genre
    def test_get_book_genre_new_book_has_no_genre(self, collector):
        collector.add_new_book("Хоббит")
        assert collector.get_book_genre("Хоббит") == ""

    # get_books_with_specific_genre
    def test_get_books_with_specific_genre_returns_only_books_of_this_genre(
        self, collector
    ):
        collector.add_new_book("Облачный атлас")
        collector.add_new_book("Великий Гэтсби")
        collector.set_book_genre("Облачный атлас", "Фантастика")
        collector.set_book_genre("Великий Гэтсби", "Детективы")
        assert collector.get_books_with_specific_genre("Фантастика") == [
            "Облачный атлас"
        ]

    # get_books_genre
    def test_get_books_genre_returns_dict_with_book_and_genre(self, collector):
        collector.add_new_book("Облачный атлас")
        collector.set_book_genre("Облачный атлас", "Фантастика")
        assert collector.get_books_genre() == {"Облачный атлас": "Фантастика"}

    # get_books_for_children
    @pytest.mark.parametrize("genre", ["Фантастика", "Мультфильмы", "Комедии"])
    def test_get_books_for_children_genre_without_age_rating_book_in_list(
        self, genre, collector
    ):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", genre)
        assert collector.get_books_for_children() == ["Книга"]

    @pytest.mark.parametrize("genre", ["Ужасы", "Детективы"])
    def test_get_books_for_children_genre_with_age_rating_book_not_in_list(
        self, genre, collector
    ):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", genre)
        assert collector.get_books_for_children() == []

    # add_book_in_favorites
    def test_add_book_in_favorites_book_from_collection_added(self, collector):
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")
        assert "Дюна" in collector.get_list_of_favorites_books()

    # delete_book_from_favorites
    def test_delete_book_from_favorites_book_deleted(self, collector):
        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")
        collector.delete_book_from_favorites("Дюна")
        assert collector.get_list_of_favorites_books() == []

    # get_list_of_favorites_books
    def test_get_list_of_favorites_books_returns_all_favorites(self, collector):
        collector.add_new_book("Дюна")
        collector.add_new_book("Солярис")
        collector.add_book_in_favorites("Дюна")
        collector.add_book_in_favorites("Солярис")
        assert collector.get_list_of_favorites_books() == ["Дюна", "Солярис"]
