class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers"

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance) -> Distance:
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance) -> None:
        self.km += other.km

    def __add__(self, other: int) -> Distance:
        return Distance(self.km + other)

    def __iadd__(self, other: int) -> None:
        self.km += other

    def __mul__(self, other: Distance) -> Distance:
        return Distance(self.km * other.km)

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Distance) -> Distance:
        return Distance(self.km / other.km)

    def __truediv__(self, other: int) -> Distance:
        return Distance(self.km / other)

    def __lt__(self, other: Distance) -> bool:
        return self.km < other.km

    def __gt__(self, other: Distance) -> bool:
        return self.km > other.km

    def __le__(self, other: Distance) -> bool:
        return self.km <= other.km

    def __ge__(self, other: Distance) -> bool:
        return self.km >= other.km

    def __eq__(self, other: Distance) -> bool:
        return self.km == other.km

    def __lt__(self, other: int) -> bool:
        return self.km < other

    def __gt__(self, other: int) -> bool:
        return self.km > other

    def __le__(self, other: int) -> bool:
        return self.km <= other

    def __ge__(self, other: int) -> bool:
        return self.km >= other

    def __eq__(self, other: int) -> bool:
        return self.km == other
