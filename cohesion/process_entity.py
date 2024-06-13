from entity import Entity


def pre_process_organization(e: Entity) -> None:
    print(f"pre-processing {e.name} as an organization")
    print(f"{e.name} is of type {e.entity_type}")

def pre_process_boat(e: Entity) -> None:
    print(f"pre-processing {e.name} as a boat")
    print(f"{e.name} is of type {e.entity_type}")

def pre_process_person(e: Entity) -> None:
    print(f"pre-processing {e.name} as a person")
    print(f"{e.name} is of type {e.entity_type}")
