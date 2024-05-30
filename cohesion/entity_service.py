from typing import Optional

from entity import Entity

bulk_create = [
    Entity("John Doe", Entity.EntityType.PERSON),
    Entity("Boaty McBoatface", Entity.EntityType.BOAT),
    Entity("The Big Company", Entity.EntityType.ORGANIZATION),
    Entity("The Small Company", Entity.EntityType.ORGANIZATION),
]

entities = {
    entity.id: entity
    for entity in bulk_create
}

def entity_by_id(id: int) -> Optional[Entity]:
    e = entities.get(id)

    if e is None:
        print(f"Entity {id} not found")
        return
    return e