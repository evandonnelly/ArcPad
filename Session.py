from dataclasses import dataclass
from datetime import datetime
from typing import List
from Match import Match
from Focus import Focus

# Represents you opening a game and beginning to play multiple matches
@dataclass
class Session:
    game_title : str
    warmup : str
    focus : Focus
    matchList : List[Match]