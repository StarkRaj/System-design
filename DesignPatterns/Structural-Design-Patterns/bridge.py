from abc import ABC, abstractmethod

# Implementation Interface
class Device(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

# Concrete Implementation 1: TV
class TV(Device):
    def turn_on(self) -> None:
        print("TV: Powering on...")

    def turn_off(self) -> None:
        print("TV: Powering off...")

# Concrete Implementation 2: Radio
class Radio(Device):
    def turn_on(self) -> None:
        print("Radio: Powering on...")

    def turn_off(self) -> None:
        print("Radio: Powering off...")

# Abstraction
class Remote:
    def __init__(self, device: Device) -> None:
        self._device = device

    def turn_on(self) -> None:
        self._device.turn_on()

    def turn_off(self) -> None:
        self._device.turn_off()

# Refined Abstraction
class AdvancedRemote(Remote):
    def mute(self) -> None:
        print("AdvancedRemote: Muting device.")
        self._device.turn_off()

if __name__ == "__main__":
    print("--- Testing TV with Basic Remote ---")
    tv = TV()
    basic_tv_remote = Remote(tv)
    basic_tv_remote.turn_on()
    basic_tv_remote.turn_off()

    print("\n--- Testing Radio with Advanced Remote ---")
    radio = Radio()
    advanced_radio_remote = AdvancedRemote(radio)
    advanced_radio_remote.turn_on()
    advanced_radio_remote.mute()
