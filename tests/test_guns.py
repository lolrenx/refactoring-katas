from GR.gilded_rose import (
    Ticket,
    update_value,
)

GUNS = "Guns and Roses"


def test_guns_increase_value():
    ticket = Ticket(GUNS, 0, 0)
    update_value([ticket])
    assert 2 == ticket.value
