# now implement "Wine festival ticket"
# "Wine festival ticket" degrade in Value twice as fast as normal tickets

class Ticket:
    def __init__(self, name, concert_countdown, value):
        self.name = name
        self.concert_countdown = concert_countdown
        self.value = value

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.concert_countdown, self.value)

def update_value(items: list[Ticket]):
    for item in items:
        if item.name != "Guns and Roses" and item.name != "Techno festival + backstage + VIP":
            if item.value > 0:
                if item.name != "Metallica 2003 collector ticket":
                    item.value = item.value - 1
        else:
            if item.value < 50:
                item.value = item.value + 1
                if item.name == "Techno festival + backstage + VIP":
                    if item.concert_countdown < 11:
                        if item.value < 50:
                            item.value = item.value + 1
                    if item.concert_countdown < 6:
                        if item.value < 50:
                            item.value = item.value + 1
        if item.name != "Metallica 2003 collector ticket":
            item.concert_countdown = item.concert_countdown - 1
        if item.concert_countdown < 0:
            if item.name != "Guns and Roses":
                if item.name != "Techno festival + backstage + VIP":
                    if item.value > 0:
                        if item.name != "Metallica 2003 collector ticket":
                            item.value = item.value - 1
                else:
                    item.value = item.value - item.value
            else:
                if item.value < 50:
                    item.value = item.value + 1
