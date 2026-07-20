import time
from abc import ABC, abstractmethod
from typing import Dict, List


class ThirdPartyYouTubeLib(ABC):
    """
    The service interface defines common operations for both Real Subject and Proxy.
    As long as the client works with the service using this interface,
    you can pass it a proxy instead of the real service.
    """

    @abstractmethod
    def get_song_list(self) -> List[str]:
        pass

    @abstractmethod
    def get_song_info(self, song_id: str) -> str:
        pass


class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    """
    The Real Subject contains the core business logic.
    Usually, Real Subjects are capable of doing some useful work which may be very slow or sensitive.
    A Proxy can solve these issues without any changes to the Real Subject's code.
    """

    def get_song_list(self) -> List[str]:
        print("Connecting to YouTube API to fetch popular songs...")
        # Simulate network delay
        time.sleep(2)
        return ["Song A", "Song B", "Song C", "Song D"]

    def get_song_info(self, song_id: str) -> str:
        print(f"Connecting to YouTube API to fetch video info for ID: {song_id}...")
        # Simulate network delay
        time.sleep(1.5)
        return f"Video metadata for song ID {song_id} (Duration: 3:45, Views: 1.2M)"


class CachedYouTubeProxy(ThirdPartyYouTubeLib):
    """
    The Proxy has an interface identical to the Real Subject.
    It maintains a reference to the Real Subject and delegates the actual work to it.
    It can also manage the Real Subject's lifecycle, cache results, handle access control, etc.
    """

    def __init__(self, youtube_service: ThirdPartyYouTubeLib):
        self._youtube_service = youtube_service
        self._song_list_cache: List[str] = []
        self._song_info_cache: Dict[str, str] = {}

    def get_song_list(self) -> List[str]:
        if not self._song_list_cache:
            print("Proxy: Cache miss for song list. Fetching from service...")
            self._song_list_cache = self._youtube_service.get_song_list()
        else:
            print("Proxy: Cache hit for song list. Returning cached results.")
        return self._song_list_cache

    def get_song_info(self, song_id: str) -> str:
        if song_id not in self._song_info_cache:
            print(f"Proxy: Cache miss for song info (ID: {song_id}). Fetching from service...")
            self._song_info_cache[song_id] = self._youtube_service.get_song_info(song_id)
        else:
            print(f"Proxy: Cache hit for song info (ID: {song_id}). Returning cached results.")
        return self._song_info_cache[song_id]


def client_code(youtube_service: ThirdPartyYouTubeLib):
    """
    The client code works with all objects via the interface.
    This way, it doesn't care whether it receives a real service or a proxy.
    """
    # First call: cache will be empty, will fetch from real service
    print("--- Requesting list of songs (First time) ---")
    start_time = time.time()
    songs = youtube_service.get_song_list()
    print(f"Songs fetched: {songs}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds\n")

    # Second call: cache should hit, returns immediately
    print("--- Requesting list of songs (Second time) ---")
    start_time = time.time()
    songs_cached = youtube_service.get_song_list()
    print(f"Songs fetched: {songs_cached}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds\n")

    # Fetching details for a specific song
    song_id = "song_123"
    print(f"--- Requesting song details for {song_id} (First time) ---")
    start_time = time.time()
    info = youtube_service.get_song_info(song_id)
    print(f"Details: {info}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds\n")

    # Fetching details for the same song again
    print(f"--- Requesting song details for {song_id} (Second time) ---")
    start_time = time.time()
    info_cached = youtube_service.get_song_info(song_id)
    print(f"Details: {info_cached}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds\n")


if __name__ == "__main__":
    real_service = ThirdPartyYouTubeClass()

    print("========================================")
    print("Executing DIRECTLY on Real Service (No Proxy/Cache):")
    print("========================================")
    client_code(real_service)

    print("========================================")
    print("Executing WITH Cache Proxy:")
    print("========================================")
    proxy = CachedYouTubeProxy(real_service)
    client_code(proxy)
