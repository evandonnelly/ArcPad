from dataclasses import dataclass, field
import uuid

# Represents a standard warmup that you may repeat accross sessions
@dataclass
class Warmup:
    id : str = field(default_factory=lambda: str(uuid.uuid4()))
    title : str
    description : str
    total_sessions : int