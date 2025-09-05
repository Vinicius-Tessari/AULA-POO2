class Clock:
    def __init__(self, hour: int, minute: int):
        self.hour = hour % 24
        self.minute = minute % 60

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"
    
clock = Clock(9, 5)
print(clock)

    