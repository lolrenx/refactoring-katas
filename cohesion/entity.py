from itertools import count
from enum import Enum
from dataclasses import dataclass, field

@dataclass
class Entity:
    class EntityType(str, Enum):
        PERSON = "PERSON"
        ORGANIZATION = "ORGANIZATION"
        BOAT = "BOAT"

    id: int = field(default_factory=count(start=1).__next__, init=False)
    name: str
    entity_type: EntityType

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.entity_type}"
