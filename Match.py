from dataclasses import dataclass
from typing import List
from Outcome import Outcome

#
@dataclass
class Match:
    Match_id : str
    outcome : Outcome
    mental : str
    observation : List[str]
    analysis : List[str]