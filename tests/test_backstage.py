from GR.gilded_rose import (
    Ticket,
    update_value,
)

BACKSTAGE_PASSES = "Techno festival + backstage + VIP"


def test_backstage_passes_increase_value():
    ticket = Ticket(BACKSTAGE_PASSES, 11, 0)
    update_value([ticket])
    assert 1 == ticket.value


def test_backstage_passes_increase_value_by_2_when_sell_in_is_10_or_less():
    ticket = Ticket(BACKSTAGE_PASSES, 10, 0)
    update_value([ticket])
    assert 2 == ticket.value


def test_backstage_passes_increase_value_by_3_when_sell_in_is_5_or_less():
    ticket = Ticket(BACKSTAGE_PASSES, 5, 0)
    update_value([ticket])
    assert 3 == ticket.value


def test_backstage_passes_value_is_0_when_sell_in_is_0():
    ticket = Ticket(BACKSTAGE_PASSES, 0, 10)
    update_value([ticket])
    assert 0 == ticket.value
