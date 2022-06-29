from subscriber import Subscriber


class Publisher:
    def __init__(self):
        self.__subscribers: list[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, data: str):
        for subscriber in self.__subscribers:
            subscriber.update(data)


