# class Horror:
#     def __init__(self, movie, weapon, clothing):
#         self.movie = movie
#         self.weapon = weapon
#         self.clothing = clothing
#
#     def damage(self):
#         return 'inflict damage'
#
#     def walk(self):
#         return 'the character is moving'
#
#     def traps(self):
#         return 'sets traps'
#
#
# class Ghost(Horror):
#     def __init__(self, movie, weapon, clothing):
#         super().__init__(movie, weapon, clothing)
#         self.weapon = weapon
#
#     def battle(self):
#         return f'Released an {self._weapon}'


def solve(s):
    countUpper = 0
    countlower = 0
    for i in s:
        if i == i.upper():
            countUpper += 1
        else:
            countLower += 1
        if countUpper <= countLower:
            s = s.lower()
        else:
            s = s.upper()
            return s
