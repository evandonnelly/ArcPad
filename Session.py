from dataclasses import dataclass
from datetime import datetime
from typing import List
from VOD import VOD

@dataclass
class Session:
    date : datetime
    warmup : str
    vodList : List[VOD]