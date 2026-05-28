class RandomizedSet:
    """
    Invariant: map must point value to value_index
    """

    def __init__(self):
        self.list = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.list.append(val)
            self.map[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            last_value = self.list[-1]
            [self.list[-1], self.list[self.map[val]]] = [
                self.list[self.map[val]],
                self.list[-1],
            ]
            self.list.pop()

            val_index = self.map[val]
            self.map[last_value] = val_index
            del self.map[val]
            return True
        return False

    def getRandom(self) -> int:
        if len(self.list) == 0:
            return False
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
