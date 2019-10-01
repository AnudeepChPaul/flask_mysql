class Dictionize:
    def __init__(self, cursor):
        self.cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        row = self.cursor.__next__()
        return { description[ 0 ]: row[ col ]
                 for col, description in enumerate(self.cursor.description) }
