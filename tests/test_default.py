from GR.gilded_rose import (
    Ticket,
    update_value,
)

GUNS = "Guns and Roses"

def test_ticket_doesnt_change_name():
    ticket = Ticket("foo", 0, 0)
    update_value([ticket])
    assert "foo" == ticket.name


def test_ticket_concert_countdown_decreases():
    ticket = Ticket("foo", 1, 0)
    update_value([ticket])
    assert 0 == ticket.concert_countdown


def test_ticket_value_decreases():
    ticket = Ticket("foo", 0, 1)
    update_value([ticket])
    assert 0 == ticket.value


def test_ticket_value_is_never_negative():
    ticket = Ticket("foo", 0, 0)
    update_value([ticket])
    assert 0 == ticket.value


def test_ticket_value_is_never_more_than_50():
    ticket = Ticket(GUNS, 0, 50)
    update_value([ticket])
    assert 50 == ticket.value


def test_ticket_value_degrades_twice_as_fast_after_concert_countdown():
    ticket = Ticket("foo", 0, 10)
    update_value([ticket])
    assert 8 == ticket.value
