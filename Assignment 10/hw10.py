"""
The whole point of this assignment is to simulate two musicians having a battle. To do this,
create two classes, an Instrument class (i.e. their instrument of choice)
and the Musician class (i.e. the musician using the instrument).

"""

import random


class Instrument:
    def __init__(self, model: str, brand: str, strength: float):
        self.model = model
        self.brand = brand
        self.strength = strength

    def does_break(self) -> bool:
        return random.random() < 0.5 * self.strength

    def __str__(self):
        return f"{self.brand} {self.model} ({self.strength * 100:.1f} / 100 strength)"

"""
Define a method for the Musician class called pick_instrument() that: 
- Accepts a single parameter, instrument_index, representing a location within the Musician object's 
instruments list. 
- Returns the Instrument object at location instrument_index.
    * If the value of instrument_index is larger than the size of instruments, this method will return 
    the last Instrument object in instruments.
    * instrument_index will have a default value of None. If the user chooses not to pass in a value for 
    instrument_index , pick_instrument() will return a random Instrument object from instruments.
    * If instruments is an empty list, return None.

"""

class Musician:
    def __init__(self, stage_name: str, instruments: list):
        self.stage_name = stage_name
        self.instruments = instruments
        self.number_of_instruments = len(instruments)

    def __str__(self):
        instrument_names = [f"{i.brand} {i.model} ({i.strength * 100:.1f} / 100 strength)" for i in self.instruments]
        return f"Musician object '{self.stage_name}', owning a {' '.join(instrument_names)}"

    def pick_instrument(self, instrument_index=None):
        if not self.instruments:
            return None

        if instrument_index is not None and instrument_index < self.number_of_instruments:
            return self.instruments[instrument_index]

        if instrument_index is None:
            return random.choice(self.instruments)

        return self.instruments[-1]

"""
Write a standalone function called get_name_of_battle_winner() , which will do the following:
- Accept two parameters, both of which you can assume will always be Musician objects. 
- The function will then pick a random Instrument object from each of the Musician objects in this duel. 
Be sure to check that each Musician object has at least one instrument. If either of them don't have any 
instruments, the other Musician automatically wins. 
- If both players don't have any instruments, return the string "NO CONTEST". 
- Finally, get_name_of_battle_winner() will first check which Instrument object's strength attribute is 
larger. Let's say musician A's instrument is stronger than musician B's. If so, our program will call 
musician A's Instrument object's does_break() method. If it returns True (that is, if it breaks), Musician 
B wins in an upset. Otherwise, musician A wins. If musician B's instrument was stronger than musician A's, 
we do the same process, but instead calling musician B's Instrument object's does_break() method. If both 
Instrument objects happen to have the same strength value, the winner will be decided by a 50/50 random 
coin-toss. 
- Whichever Musician wins, return their stage_name attribute.

"""

def get_name_of_battle_winner(musician1, musician2):
    # check if either musician has no instruments
    if not musician1.instruments:
        return musician2.stage_name
    elif not musician2.instruments:
        return musician1.stage_name

    # pick a random instrument for each musician
    instrument1 = musician1.pick_instrument()
    instrument2 = musician2.pick_instrument()

    # compare the strength of the two instruments
    if instrument1.strength > instrument2.strength:
        print(f"{musician1.stage_name} picked a {instrument1}!")
        print(f"{musician2.stage_name} picked a {instrument2}!")
        if instrument1.does_break():
            return musician2.stage_name
        else:
            return musician1.stage_name
    elif instrument1.strength < instrument2.strength:
        print(f"{musician1.stage_name} picked a {instrument1}!")
        print(f"{musician2.stage_name} picked a {instrument2}!")
        if instrument2.does_break():
            return musician1.stage_name
        else:
            return musician2.stage_name
    else:
        # 50/50 chance
        print("Both musician's instruments are the same strength. The winner will be decided by the whim of chance.")
        if random.random() < 0.5:
            return musician1.stage_name
        else:
            return musician2.stage_name


def main():
    danelectro = Instrument("Stock '59", "Danelectro", 0.25)
    fender_vi = Instrument("VI Bass", "Fender", 0.99)
    four_double_o_one = Instrument("4001C64 Bass", "Rickenbacker", 0.856)
    gear = [danelectro, fender_vi, four_double_o_one]
    # Let's say both musicians have access to the same gear
    sad_musician = Musician("Robert Smith", gear)
    less_sad_musician = Musician("Miki Berenyi", gear)
    # Testing the get_name_of_battle_winner method a few times
    number_of_duels = 10
    for duel_number in range(number_of_duels):
        winner_name = get_name_of_battle_winner(sad_musician,
                                                less_sad_musician)
        print(f"THE WINNER OF DUEL #{duel_number + 1} IS {winner_name}!", end="\n\n")


main()