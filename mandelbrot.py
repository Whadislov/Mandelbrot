from dataclasses import dataclass
from math import log #to smooth out the banding artifacts

@dataclass
class MandelbrotSet:
    max_iterations: int
    escape_radius: float = 2.0

    def __contains__(self, c: complex) -> bool:
        return self.stability(c) == 1

    def stability(self, c: complex, smooth=False) -> float:
        value = self.escape_count(c, smooth) / self.max_iterations
        #when smoothing, the log can create negative values or values > 1
        if value < 0.0:
            return 0.0
        elif value > 1.0:
            return 1.0
        else:
            return value

    def escape_count(self, c: complex, smooth=False) -> int | float:
        z = 0
        for i in range(self.max_iterations):
            z = z ** 2 + c
            if abs(z) > 2:
                if smooth:
                    return i + 1 - log(log(abs(z))) / log(2)
                return i
        return self.max_iterations
    

