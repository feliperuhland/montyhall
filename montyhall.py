# coding: utf-8

import random


def montyhall(n=1, change_door=True):
    result_list = []
    for i in range(0, n):
        ds = DoorShow(change_door=change_door)
        result_list.append(ds.run())

    true_count = result_list.count(True)
    false_count = result_list.count(False)
    print('True: {} [{}]'.format(true_count, true_count / n * 100))
    print('False: {} [{}]'.format(false_count, false_count / n * 100))


def _create_doors():
    doors = []
    while len(doors) < 3:
        if len(doors) == 2 and not any(doors):
            doors.append(True)
            continue
        if any(doors):
            doors.append(False)
            continue
        doors.append(random.choice([True, False]))  # bool(random.getrandbits(1))
    return doors


class DoorShow(object):
    def __init__(self, change_door=True):
        self.doors = _create_doors()
        self.change_door = change_door
        self.first_choice = None
        self.second_choice = None

    def first_door(self):
        door_n = random.choice([0, 1, 2])
        self.first_choice = (door_n, self.doors[door_n])

    def second_door(self):
        if not self.change_door:
            return
        first_choice_index = [0, 1, 2].index(self.first_choice[0])
        alternatives = [0, 1, 2]
        alternatives.pop(first_choice_index)
        if self.doors[alternatives[0]]:
            self.second_choice = (alternatives[0], self.doors[alternatives[0]])
        else:
            self.second_choice = (alternatives[1], self.doors[alternatives[1]])

    def result(self):
        if self.change_door:
            return self.second_choice[1]
        return self.first_choice[1]

    def run(self):
        self.first_door()
        self.second_door()
        return self.result()
