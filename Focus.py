from dataclasses import dataclass, field
import uuid

# Represents the aspects of your gameplay that you wish to change
@dataclass
class Focus:
    id : str = field(default_factory=lambda: str(uuid.uuid4()))
    title : str
    cue : str
    action : str
    total_sessions : int