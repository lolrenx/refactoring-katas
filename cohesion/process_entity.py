from entity import Entity


def pre_process_organization(e: Entity) -> None:
    print(f"pre-processing {e} as an organization")

def pre_process_boat(e: Entity) -> None:
    print(f"pre-processing {e} as a boat")

def pre_process_person(e: Entity) -> None:
    print(f"pre-processing {e} as a person")
