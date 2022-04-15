from math import modf


class IntervalPaces:
    def __init__(self) -> None:
        self.distances = [3000, 5000, 10000]
        self.jakobs_reference_times = {
            3000: 7 + 27 / 60,
            5000: 12 + 48 / 60,
            10000: 27 + 54 / 60,
        }
        self.jakobs_max_kph = {"3 min": 22, "6 min": 21}
        self.title_width = 60
        self.title_border = "="

    def _title(self, headline):
        return f" {headline} ".center(self.title_width, self.title_border)

    def _kph_to_km_pace(self, kph: float) -> str:
        """Convert kph float to min/km string"""
        pace = 60 / kph
        seconds, minutes = modf(pace)
        seconds *= 60
        return f"{int(minutes):02d}:{int(seconds):02d} min/km"

    def get_recent_race_record(self) -> float:
        """
        Prompt the user for two things
        1) Recent race distance
        2) Recent race PR
        """
        # 1: Select a race as reference
        print(self._title("Part 1 - Recent race distance"))
        choices = []
        prompt = "Select a race distance: "
        for i, dis in enumerate(self.distances):
            prompt += f"[{i}] {dis} m, "
            choices.append(i)
        prompt = prompt[:-2] + ": "
        choice = -1
        while choice not in choices:
            choice = int(input(prompt))
        distance = self.distances[choice]

        # 2: Provice race time
        print("\n")
        print(self._title(f"Part 2 - Provide your {distance} m PR"))
        minutes = -1
        while not (minutes >= 0):
            minutes = int(input("Race time minutes: "))
        seconds = -1
        while not seconds in range(0, 60):
            seconds = int(input("Race time seconds: "))
        your_time = minutes + seconds / 60

        return distance, your_time

    def get_max_interval_paces(self, factor: float) -> None:
        """Print all max paces from Jakob's refence times"""
        print("\n")
        print(self._title(f"Results"))
        for key, val in self.jakobs_max_kph.items():
            max_kph = factor * val
            print(f"Max {key} interval pace: {self._kph_to_km_pace(max_kph)}")

    def run(self) -> None:
        """Run full program to find max interval paces"""
        distance, your_time = self.get_recent_race_record()
        jakobs_time = self.jakobs_reference_times[distance]
        factor = jakobs_time / your_time
        self.get_max_interval_paces(factor)


if __name__ == "__main__":
    IntervalPaces().run()