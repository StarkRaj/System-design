from abc import ABC, abstractmethod
from typing import Iterable

# --- Component ---
class FSNode(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def size(self) -> int:
        """Bytes for a file, sum of children for a directory."""

    @abstractmethod
    def render(self, indent: int = 0) -> str:
        """Return a printable tree representation."""


# --- Leaf ---
class File(FSNode):
    def __init__(self, name: str, size_bytes: int):
        super().__init__(name)
        self._size = size_bytes

    def size(self) -> int:
        return self._size

    def render(self, indent: int = 0) -> str:
        return f"{' ' * indent}- {self.name} ({self._size}B)"


# --- Composite ---
class Directory(FSNode):
    def __init__(self, name: str, children: Iterable[FSNode] = ()):
        super().__init__(name)
        self._children: list[FSNode] = list(children)

    def add(self, node: FSNode) -> None:
        self._children.append(node)

    def remove(self, node: FSNode) -> None:
        self._children.remove(node)

    def size(self) -> int:
        return sum(child.size() for child in self._children)

    def render(self, indent: int = 0) -> str:
        lines = [f"{' ' * indent}+ {self.name}/ ({self.size()}B)"]
        lines.extend(child.render(indent + 1) for child in self._children)
        return "\n".join(lines)


# --- Client (doesn't care about leaf vs composite) ---
if __name__ == "__main__":
    root = Directory("project", [
        File("README.md", 1200),
        Directory("src", [
            File("main.py", 3400),
            File("utils.py", 800),
        ]),
        Directory("tests", [
            File("test_main.py", 1500),
        ]),
    ])
    print(root.render())