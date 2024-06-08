
from mon_module.hello import print_hello

from enum import Enum
# @COORDINATE
COORDINATE_A1 = "A1"
COORDINATE_A2 = "A2"
COORDINATE_A3 = "A3"
COORDINATE_B1 = "B1"
COORDINATE_B2 = "B2"
COORDINATE_B3 = "B3"
COORDINATE_C1 = "C1"
COORDINATE_C2 = "C2"
COORDINATE_C3 = "C3"

class COORDINATE(Enum):
    A1 = "A1"
    A2 = "A2"
    A3 = "A3"
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"
    C1 = "C1"
    C2 = "C2"
    C3 = "C3"
    C4 = 4 



if __name__ == "__main__":
    print_hello()
    # img = polynome.image(1.5)
    # print("polynome.image(1.5) =", img)
    # print(polynome.A)
    print(COORDINATE.A1)