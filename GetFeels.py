from Twinter import run_twint


class Feels:
    def get_feels(self):
        feels = ""
        intel = run_twint(self)
        score = intel[0]
        sample = intel[1]

        if score in range(80, 101):
            feels = f"very happy"
        elif score in range(60, 80):
            feels = "happy"
        elif score in range(40, 60):
            feels = "relieved"
        elif score in range(20, 40):
            feels = "good"
        elif score in range(-20, 20):
            feels = "neutral"
        elif score in range(-40, -20):
            feels = "unamused"
        elif score in range(-60, -40):
            feels = "sad"
        elif score in range(-80, -60):
            feels = f"very sad"
        elif score in range(-101, -60):
            feels = "triggered"

        return [feels, score, sample]
