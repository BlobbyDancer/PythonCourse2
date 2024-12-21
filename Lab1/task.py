import doctest # TODO Написать 3 класса с документацией и аннотацией типов


class Music:
    def __init__(self, band_name: str, album_title: str, year: int):
        """
        Инициализация музыки с заданной группой, альбомом и годом выпуска.

        :param band_name: Название группы
        :param album_title: Название альбома
        :param year: Год выпуска альбома

        Пример:
        >>> music = Music("The Beatles", "Abbey Road", 1969)
        >>> music.band_name = 'The Beatles'
        >>> music.album_title = 'Abbey Road'
        >>> music.year = 1969
        """
        if year < 1900 or year > 1999:
            raise ValueError("Принимается только музыка XX века")

        self.band_name = band_name
        self.album_title = album_title
        self.year = year

    @staticmethod
    def sort_by_year(music_list1: List['Music']) -> List['Music']:
        """
        Функция которая сортирует альбомы по дате выхода

        :param music_list: Список объектов класса Music
        :return: Отсортированный список по году выпуска
        return sorted(music_list, key=lambda music: music.year)

        Примеры:
        >>> music1 = Music("The Beatles", "Abbey Road", 1969)
        >>> music2 = Music("Pink Floyd", "The Dark Side of the Moon", 1973)
        >>> music3 = Music("Led Zeppelin", "IV", 1971)
        >>> sorted_list = Music.sort_by_year([music1, music2, music3])
        >>> [music.album_title for music in sorted_list]
        ['Abbey Road', 'IV', 'The Dark Side of the Moon']
        """
        return sorted(music_list, key=lambda music: music.year)
        ...
    
    @staticmethod
    def sort_alphabetically(music_list2: List['Music']) -> List[str]:
        """
        Функция которая сортирует альбомы в алфавитном порядке

        :param music_list: Список объектов класса Music
        :return: Отсортированный по алфавиту список альбомов
        return sorted(music_list, key=lambda music: music.album_title)

        Примеры:
        >>> music1 = Music("The Beatles", "Abbey Road", 1969)
        >>> music2 = Music("Pink Floyd", "The Dark Side of the Moon", 1973)
        >>> music3 = Music("Led Zeppelin", "IV", 1971)
        >>> sorted_list = Music.sort_alphabetically([music1, music2, music3])
        >>> sorted_list
        ['Abbey Road', 'IV', 'The Dark Side of the Moon']
        """
        return sorted([music.album_title for music in music_list])
        ...


if __name__ == "__main__":
    doctest.testmod()


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги с названием, автором и количеством страниц.

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Пример:
        >>> book = Book("К востоку от рая", "Джон Стейнбек", 714)
        >>> book.title
        'К востоку от рая'
        >>> book.pages
        714
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_to_read: int = 10) -> str:
        """
        Метод для чтения книги, уменьшает количество оставшихся страниц.

        :param pages_to_read: Количество страниц для чтения
        :return: Строка с количеством прочитанных страниц

        Пример:
        >>> book = Book("К востоку от рая", "Джон Стейнбек", 714)
        >>> book.read(100)
        'Прочитано 100 страниц. Осталось 614 страниц.'
        """
        ...

    def get_info(self) -> str:
        """
        Метод для получения информации о книге.

        Пример:
        >>> book = Book("К востоку от рая", "Джон Стейнбек", 714)
        >>> book.get_info()
        'Книга: К востоку от рая, Автор: Джон Стейнбек, Страниц: 714'
        """
        return f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}"


    class Pond:
        def __init__(self, length: float, width: float, fish_type: str):
            """
            Инициализация пруда с заданной длиной, шириной и видом рыб, которые в нем обитают.

            :param length: Длина пруда в метрах
            :param width: Ширина пруда в метрах
            :param fish_type: вид рыб (карп, сом, окунь)

            Пример:
            >>> pond = Pond(15, 10.5, "карп")
            >>> pond.length
            15
            >>> pond.fish_type
            'карп'
            """
            if length <= 0 or width <= 0:
                raise ValueError("Длина и ширина пруда должны быть положительными числами.")
            if fish_type.lower() not in ["карп", "сом", "окунь"]:
                raise ValueError("В пруду могут быть только: карпы, сомы, окуни")

            self.length = length
            self.width = width
            self.fish_type = fish_type.lower()

        def area(self) -> float:
            """Метод для вычисления площади пруда."""
            return self.length * self.width

        def change_fish(self, new_fish: str) -> None:
            """
            Метод для изменения вида рыб в пруду.

            :param new_fish: Новый вид рыб

            Пример:
            >>> pond = Pond(15, 10.5, "карп")
            >>> pond.change_fish("сом")
            >>> pond.fish_type
            'сом'
            """
            ...
