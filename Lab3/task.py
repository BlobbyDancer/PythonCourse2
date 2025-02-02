class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        """Название книги (изменить нельзя)."""
        return self._name

    @property
    def author(self):
        """ Автор книги (изменить нельзя). """
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        """ Количество страниц. """
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """ Устанавливает количество страниц в книге. """
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = new_pages


    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"


class AudioBook:
    """ Класс аудиокниги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        """ Продолжительность книги. """
        return self._duration

    @duration.setter
    def duration(self, time):
        if not isinstance(time, (int,float)):
            raise TypeError("Продолжительность должна быть числом.")
        if time <= 0:
            raise ValueError("Продолжительность должна быть положительной.")
        self._duration = float(time)


    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.duration:.2f} часов"
