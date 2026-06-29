# ./domain/enums/source.py

from enum import StrEnum


class Source(StrEnum):
    INRIA = "Inria"
    BRGM = "BRGM"
    CEA = "CEA"
    IFPEN = "IFPEN"
    EURAXESS = "Euraxess"
    CNRS = "CNRS"
    ACADEMIC_POSITIONS = "Academic Positions"