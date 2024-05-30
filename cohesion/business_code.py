import entity_service
from entity import Entity


def process_organization(e: Entity) -> None:
    print(f"processing {e} as an organization")

def process_boat(e: Entity) -> None:
    print(f"processing {e} as a boat")

def process_person(e: Entity) -> None:
    print(f"processing {e} as a person")


def process_entities() -> None:
    e_list = [
        entity_service.entity_by_id(i)
        for i in range(1, 7)
        if entity_service.entity_by_id(i)
    ]

    for e in e_list:
        if e.entity_type == Entity.EntityType.ORGANIZATION:
            process_organization(e)
        elif e.entity_type == Entity.EntityType.BOAT:
            process_boat(e)
        else:
            process_person(e)


if __name__ == "__main__":
    process_entities()