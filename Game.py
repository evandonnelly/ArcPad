from dataclasses import dataclass
from typing import List
from Session import Session
from Adjustment import Adjustment

@dataclass
class Game:
    game_title : str
    adjustmentList : List[Adjustment]
