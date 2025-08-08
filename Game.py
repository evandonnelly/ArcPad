from dataclasses import dataclass
from typing import List
from Session import Session
from Focus import Focus

# Reperesents a game title (ex. Rocket League, VALORANT, etc.)
@dataclass
class Game:
    game_title : str
    adjustmentList : List[Focus]
