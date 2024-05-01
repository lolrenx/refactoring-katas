from GR.gilded_rose import (
    Ticket,
    update_value,
)

METALLICA = "Metallica 2003 collector ticket"


def test_metallica_countdown_doesnt_decrease():
    item = Ticket(METALLICA, 1, 0)
    update_value([item])
    assert 1 == item.concert_countdown


def test_item_metallica_value_doesnt_decrease():
    item = Ticket(METALLICA, 1, 80)
    update_value([item])
    assert 80 == item.value
