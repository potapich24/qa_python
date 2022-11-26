from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_name_in_the_dictionary(self):
        collector1 = BooksCollector()
        collector1.add_new_book('Что такое тестирование')
        assert 'Что такое тестирование' in collector1.get_books_rating()

    def test_set_book_rating_rating_of_a_nonexistent_book(self):
        collector2 = BooksCollector()
        collector2.add_new_book('Мост через вечнось')
        collector2.set_book_rating('Момо', 8)
        assert collector2.books_rating['Мост через вечнось'] != 8 and 'Момо' not in collector2.books_rating

    def test_get_book_rating_rating_by_name(self):
        collector3 = BooksCollector()
        collector3.add_new_book('Замок Броуди')
        assert collector3.books_rating.get('Замок Броуди') == collector3.get_book_rating('Замок Броуди')

    def test_get_books_with_specific_rating_selection_by_rating(self):
        collector4 = BooksCollector()
        collector4.add_new_book('Две жизни')
        collector4.set_book_rating('Две жизни', 10)
        collector4.add_new_book('Иллюзия')
        collector4.set_book_rating('Иллюзия', 10)
        collector4.add_new_book('Подземка')
        collector4.set_book_rating('Подземка', 5)

        assert collector4.get_books_with_specific_rating(10) == ['Две жизни', 'Иллюзия']

    def test_get_books_rating_dictionary_output(self):
        collector5 = BooksCollector()
        collector5.add_new_book('Динка')
        collector5.set_book_rating('Динка', 10)
        collector5.add_new_book('Хроники нарнии')
        collector5.set_book_rating('Хроники нарнии', 10)
        collector5.add_new_book('Подземка')
        collector5.set_book_rating('Подземка', 5)
        assert 'Динка' in collector5.get_books_rating() and 'Хроники нарнии' in collector5.get_books_rating() and 'Подземка' in collector5.get_books_rating()

    def test_add_book_in_favorites_can_not_add_one_book_twice(self):
        collector6 = BooksCollector()
        collector6.add_new_book('Иллюзия')
        collector6.add_book_in_favorites('Иллюзия')
        collector6.add_book_in_favorites('Иллюзия')
        assert len(collector6.favorites) == 1

    def test_delete_book_from_favorites_movie_deleted(self):
        collector7 = BooksCollector()
        collector7.add_new_book('Подземка')
        collector7.add_new_book('Хроники нарнии')
        collector7.add_book_in_favorites('Подземка')
        collector7.add_book_in_favorites('Хроники нарнии')
        collector7.delete_book_from_favorites('Подземка')
        assert 'Подземка' not in collector7.favorites and 'Хроники нарнии' in collector7.favorites

    def test_get_list_of_favorites_books_list_output(self):
        collector8 = BooksCollector()
        collector8.add_new_book('Подземка')
        collector8.add_book_in_favorites('Подземка')
        assert collector8.get_list_of_favorites_books() == ['Подземка']

