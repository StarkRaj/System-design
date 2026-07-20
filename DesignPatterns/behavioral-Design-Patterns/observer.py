from abc import ABC, abstractmethod
from typing import List


# 1. The Observer Interface
class Subscriber(ABC):
    @abstractmethod
    def update(self, channel_name: str, video_title: str) -> None:
        pass


# 2. The Subject
class YouTubeChannel:
    def __init__(self, name: str):
        self.name = name
        self._subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)
        print(f"Subscriber added to '{self.name}'.")

    def unsubscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.remove(subscriber)
        print(f"Subscriber removed from '{self.name}'.")

    def notify(self, video_title: str) -> None:
        for subscriber in self._subscribers:
            subscriber.update(self.name, video_title)

    def upload_video(self, video_title: str) -> None:
        print(f"\n[{self.name}] Uploaded new video: '{video_title}'")
        self.notify(video_title)


# 3. Concrete Observers
class User(Subscriber):
    def __init__(self, username: str):
        self.username = username

    def update(self, channel_name: str, video_title: str) -> None:
        print(f"Notification to {self.username}: '{channel_name}' posted a new video -> '{video_title}'")


if __name__ == "__main__":
    # Create YouTube Channel (Subject)
    channel = YouTubeChannel("CodeCraft")

    # Create Users (Observers)
    user1 = User("Alice")
    user2 = User("Bob")

    # Users subscribe to channel
    channel.subscribe(user1)
    channel.subscribe(user2)

    # Channel uploads a video -> Notifications sent automatically
    channel.upload_video("Learn Observer Pattern in 5 Minutes")

    # One user unsubscribes
    print()
    channel.unsubscribe(user2)

    # Channel uploads another video -> Only Alice gets the notification
    channel.upload_video("Python Tips and Tricks")
