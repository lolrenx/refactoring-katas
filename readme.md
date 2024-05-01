======================================
inspired by Gilded Rose Refactoring kata
https://github.com/emilybache/GildedRose-Refactoring-Kata
======================================

Helloasso is implementing a new tickets marketplace and the project has already started. Unfortunately our colleague Uncle Bob who coded the POC has moved on to new adventures.

Your task is to add the new feature to our system so that we can begin selling a new category of tickets. First an introduction to our system:

    - All tickets have a countdown value which denotes the number of days we have before the show
    - All tickets have a Value value which denotes how valuable the ticket is
    - At the end of each day our system lowers both values for every ticket

Pretty simple, right? Well this is where it gets interesting:

    - Once the sell by date has passed, Value degrades twice as fast (some collectors might still want the tickets, but the hype wears off quickly)
    - The Value of an ticket is never negative
    - "Guns and Roses" actually increases in Value the older it gets
    - The Value of an ticket is never more than 50
    - "Metallica", being a legendary ticket, never has to be sold or decreases in Value
    - "Techno festival + backstage + VIP", like Guns and Roses, increases in Value as its countdown value approaches;
    Value increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    Value drops to 0 after the concert

We have recently signed a promoter of wine festivals. This requires an update to our system:

    - "Wine festival ticket" degrade in Value twice as fast as normal tickets

Feel free to make any changes to the update_value function and add any new code as long as everything still works correctly. However, do not alter the Ticket class or tickets property as those belong to Uncle Bob will insta-rage and complain about you as he doesn't believe in shared code
ownership.

Just for clarification, a ticket can never have its Value increase above 50, however "Metallica" is a legendary ticket and as such its Value is 80 and it never alters.
