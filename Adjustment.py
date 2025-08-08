from dataclasses import dataclass
from typing import List
from Session import Session

@dataclass
class Adjustment:
    cue : str
    action : str
    sessionList : List[Session]
    number_of_sessions : int