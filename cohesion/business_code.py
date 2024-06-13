import entity_service
from entity import Entity
import process_entity as p


def pre_process_entities() -> None:
    e_list = [
        entity_service.entity_by_id(i)
        for i in range(1, 7)
        if entity_service.entity_by_id(i)
    ]

    print("Starting to pre-process entities")

    for e in e_list:
        if e.entity_type == Entity.EntityType.ORGANIZATION:
            p.pre_process_organization(e)
        elif e.entity_type == Entity.EntityType.BOAT:
            p.pre_process_boat(e)
        else:
            p.pre_process_person(e)


def process_inanimate(e: Entity) -> None:
    print(f"processing {e} as an inanimate object")


def process_living(e: Entity) -> None:
    print(f"processing {e} as a living entity")


def process_inanimates(e_list: list[Entity]) -> None:
    print("Starting to process inanimate objects")
    for e in e_list:
        if e.entity_type in (Entity.EntityType.ORGANIZATION, Entity.EntityType.BOAT):
            process_inanimate(e)


if __name__ == "__main__":
    pre_process_entities()
    entity_list = [
        entity_service.entity_by_id(i)
        for i in range(1, 7)
        if entity_service.entity_by_id(i)
    ]
    process_inanimates(entity_list)
    print("starting to process living entities")
    for e in entity_list:
        if e.entity_type == Entity.EntityType.PERSON:
            process_living(e)

    print("done")