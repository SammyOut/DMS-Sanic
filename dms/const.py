from enum import Enum


class EXTENSION_TIME(Enum):
    ELEVEN = 11
    TWELVE = 12


class EXTENSION_CLASS(Enum):
    GA = 0
    NA = 1
    DA = 2
    RA = 3
    FLOOR_2 = 4
    FLOOR_3_SCHOOL_SIDE = 5
    FLOOR_3_DORMITORY_SIDE = 6
    FLOOR_4_SCHOOL_SIDE = 7
    FLOOR_4_DORMITORY_SIDE = 8
    FLOOR_5 = 9
    FLOOR_3_WATER = 10


class GOINGOUT_STATUS(Enum):
    BEFORE = 0
    ING = 1
    AFTER = 2


class MUSIC_APPLY_WEEKDAY(Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6


class STAY_STATUS(Enum):
    FRI_OUT = 0
    SAT_OUT = 1
    SAT_IN = 2
    STAY = 3

