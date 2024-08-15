class Missing(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.msg = args[0]


class Duplicate(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.msg = args[0]