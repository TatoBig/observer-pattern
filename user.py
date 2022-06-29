from subscriber import Subscriber


class User(Subscriber):
    def __init__(self, name: str):
        self.__name: str = name

    def update(self, data: str) -> None:
        print(f'Hola {self.__name} ya hay un nuevo episodio de {data}')
