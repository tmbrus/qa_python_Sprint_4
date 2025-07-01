import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # Тесты для add_new_book
    @pytest.mark.parametrize('name, expected', [
        ('Книга с нормальным названием', True),
        ('', False),  # пустое название
        ('Очень длинное название книги, которое явно больше 40 символов', False)
    ])
    def test_add_new_book(self, collector, name, expected):
        collector.add_new_book(name)
        assert (name in collector.books_genre) == expected

    # Тесты для set_book_genre
    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Несуществующий жанр')
        assert collector.get_book_genre('Гарри Поттер') == ''

    # Тесты для get_book_genre
    def test_get_book_genre(self, collector):
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''

    # Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Фантастическая книга')
        collector.set_book_genre('Фантастическая книга', 'Фантастика')
        collector.add_new_book('Еще фантастика')
        collector.set_book_genre('Еще фантастика', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    # Тесты для get_books_genre
    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Несуществующий жанр')
        assert collector.get_book_genre('Гарри Поттер') == ''

    # Тесты для get_books_for_children
    def test_get_books_for_children(self, collector):
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.add_new_book('Взрослая книга')
        collector.set_book_genre('Взрослая книга', 'Ужасы')
        assert 'Детская книга' in collector.get_books_for_children()
        assert 'Взрослая книга' not in collector.get_books_for_children()

    # Тесты для add_book_in_favorites
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    # Тесты для delete_book_from_favorites
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Книга для удаления')
        collector.add_book_in_favorites('Книга для удаления')
        collector.delete_book_from_favorites('Книга для удаления')
        assert 'Книга для удаления' not in collector.get_list_of_favorites_books()

    # Тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        assert len(collector.get_list_of_favorites_books()) == 2
