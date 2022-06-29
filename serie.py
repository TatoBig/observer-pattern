from publisher import Publisher


class Serie:
    def __init__(self, name: str):
        self.__name: str = name
        self.__episodes: list[str] = []
        self.__publisher: Publisher = Publisher()

    def add_episode(self, episode: str):
        self.__episodes.append(episode)
        self.__publisher.notify(f'{self.__name} - {episode}')

    @property
    def publisher(self):
        return self.__publisher
