import pytest
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2, 'Неверное количество книг'
    
    def test_set_book_genre_add_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Детективы')
        assert collector.get_book_genre('Война и мир') == 'Детективы', "Такой жанр не найден"

    def test_get_book_genre_book_have_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Детективы')
        genre = collector.get_book_genre('Война и мир')
        assert genre == 'Детективы', "Ошибка получения жанра"

    def test_get_books_with_specific_genre_all_books_with_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Война и мир')
        collector.add_new_book('Искусство автотестов')
        collector.set_book_genre('Война и мир', 'Детективы')
        collector.set_book_genre('Искусство автотестов', 'Ужасы')
        books = collector.get_books_with_specific_genre('Детективы')
        assert 'Война и мир' in books, "Ошибка поиска по жанру"

    def test_get_books_genre_result_not_empty(self):

        collector = BooksCollector()

        all_books = collector.get_books_genre()
        assert all_books is not None, "Ошибка получения словаря книг"

    def test_get_books_for_children_children_books_separately(self):

        collector = BooksCollector()

        collector.add_new_book('Мультик')
        collector.set_book_genre('Мультик', 'Мультфильмы')
        children_books = collector.get_books_for_children()
        assert 'Мультик' in children_books, "Ошибка получения детских книг"

    @pytest.mark.parametrize('book_name', [
        'Война и мир',
        'Мультик',
        'Искусство автотестов'
    ])
    def test_add_and_delete_from_favorites_books_add_and_delete_from_favorites(self, book_name):

        collector = BooksCollector()

        collector.add_new_book(book_name)

        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites, "Ошибка добавления книги в избранное"
        
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.favorites, "Ошибка удаления книги из избранного"

    def test_get_list_of_favorites_books_list_not_empty(self):

        collector = BooksCollector()

        collector.add_book_in_favorites('Мультик')
        favorites = collector.get_list_of_favorites_books()
        assert favorites is not None, "Ошибка получения списка избранных книг"



