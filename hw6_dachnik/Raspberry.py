class Raspberry(object):
    states = {'Отсутствует', 'Цветение', 'Зеленая', 'Красная'}

    def __init__(self, index):
        self._index = index
        self._state_iterator = iter(self.states)
        self._state = next(self._state_iterator, None)

    def grow(self):
        self._state = next(self._state_iterator, 'Красная')

    def is_ripe(self):
        return self._state == 'Красная'