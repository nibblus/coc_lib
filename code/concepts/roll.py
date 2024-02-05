"""
    This file is part of tococyn.

    tococyn is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import math
import random
import re


def random_func(limit: int) -> int:
    """
    Generate a random number between 1 and limit
    :param limit: upper bound
    :return: random number between 1 and limit
    """
    return random.randint(1, limit)


class Die:
    """
    A die
    """

    def __init__(self, sides: int):
        if not isinstance(sides, int) or sides < 1:
            raise ValueError(f"Sides {sides} must be strict positive integer")
        self.sides = sides
        self._value = None

    def __repr__(self):
        return f"D{self.sides}"

    def value(self) -> int:
        """
        Generate a number for the die
        :return: Random roll
        """
        self._value = random_func(self.sides)
        return self._value


class Roll:
    """
    Representation of dice roll
    """

    def __init__(self, description: str = "D100"):
        self.description = description
        self.dice = []
        description = description.replace("-", "|-").replace("+", "|")
        terms = re.split(r'\|', description)
        terms = [term.split("D") for term in terms]
        for term in terms:
            if len(term) == 1:
                self.dice.append(Value(int(term[0])))
            elif len(term) == 2:
                l = 1 if len(term[0]) == 0 else int(term[0])
                for i in range(l):
                    self.dice.append(Die(int(term[1])))
        pass

    def roll(self) -> int:
        """
        Roll the die
        :return: random side of the die
        """
        total = 0
        for die in self.dice:
            r = die.value()
            total += die.value()
        return total


class Value:
    """
    Representation of a value
    """

    def __init__(self, value: int = 1):
        self._value = value

    def value(self) -> int:
        """

        :return:
        """
        return self._value


def test_random():
    COUNT = 10000000

    SEQUENCE_MAX = min(max(2, int(math.log10(COUNT)-2)),6)
    seq = ""
    die = Roll('D6')
    d = dict()
    s = dict()
    for _ in range(COUNT):
        roll = die.roll()
        """
        tel frequentie van waarde
        """
        count = d.get(roll, 0)
        count += 1
        d[roll] = count

        """
        tel frequentie van sequenties 
        """
        seq = f"{seq}{roll}"
        if len(seq) < SEQUENCE_MAX:
            continue
        if len(seq) > SEQUENCE_MAX:
            seq = seq[1:]
        count = s.get(seq, 0)
        count+=1
        s[seq] = count


    for x in sorted(d.keys()):
        print(f"{x} : {d[x]} => {d[x]*100/COUNT:.2f}%")

    for x in sorted(s.keys()):
        print(f"{x} : {s[x]} => {s[x]*100/COUNT:.2f}%")



if __name__ == "__main__":
    test_random()
