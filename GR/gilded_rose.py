# now implement "Wine festival ticket"
# "Wine festival ticket" degrade in Value twice as fast as normal tickets
from abc import ABC, abstractmethod


class Ticket:
    def __init__(self, name, concert_countdown, value):
        self.name = name
        self.concert_countdown = concert_countdown
        self.value = value

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.concert_countdown, self.value)

GUNS = "Guns and Roses"
METALLICA = "Metallica 2003 collector ticket"
TECHNO = "Techno festival + backstage + VIP"
WINE_FESTIVAL = "Wine festival ticket"


class TicketProcessor(ABC):
    ticket: Ticket

    @abstractmethod
    def update_concert_countdown(self):
        pass

    @abstractmethod
    def update_value(self):
        pass


class DefaultProcessor(TicketProcessor):
    def __init__(self, ticket: Ticket):
        self.ticket = ticket

    def update_concert_countdown(self):
        self.ticket.concert_countdown = max(0, self.ticket.concert_countdown - 1)

    def update_value(self):
        if self.ticket.concert_countdown <= 0:
            self.ticket.value = max(0, self.ticket.value - 2)
        else:
            self.ticket.value = max(0, self.ticket.value - 1)


class MetallicaProcessor(TicketProcessor):
    def __init__(self, ticket: Ticket):
        self.ticket = ticket

    def update_concert_countdown(self):
        pass

    def update_value(self):
        pass


class GunsProcessor(DefaultProcessor):
    def __init__(self, ticket: Ticket):
        self.ticket = ticket

    def update_concert_countdown(self):
        super().update_concert_countdown()

    def update_value(self):
        self.ticket.value = min(50, self.ticket.value + 2)


class TechnoProcessor(TicketProcessor):
    def __init__(self, ticket: Ticket):
        self.ticket = ticket

    def update_concert_countdown(self):
        pass

    def update_value(self):
        if self.ticket.concert_countdown <= 0:
            self.ticket.value = 0
        elif self.ticket.concert_countdown <= 5:
            self.ticket.value = min(50, self.ticket.value + 3)
        elif self.ticket.concert_countdown <= 10:
            self.ticket.value = min(50, self.ticket.value + 2)
        else:
            self.ticket.value = min(50, self.ticket.value + 1)


class WineFestivalProcessor(TicketProcessor):
    def __init__(self, ticket: Ticket):
        self.ticket = ticket

    def update_concert_countdown(self):
        super().update_concert_countdown()

    def update_value(self):
        if self.ticket.concert_countdown <= 0:
            self.ticket.value = max(0, self.ticket.value - 4)
        else:
            self.ticket.value = max(0, self.ticket.value - 2)


def update_value(items: list[Ticket]) -> None:
    updater = {
        GUNS: GunsProcessor,
        METALLICA: MetallicaProcessor,
        TECHNO: TechnoProcessor, 
        WINE_FESTIVAL: WineFestivalProcessor
    }

    for item in items:
        processor = updater.get(item.name, DefaultProcessor)
        processor(item).update_concert_countdown()
        processor(item).update_value()
