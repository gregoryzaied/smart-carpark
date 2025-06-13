class Display:
    def show(self, message):
        print(f"[DISPLAY] {message}")

class WeatherDisplay(Display):
    def show(self, message):
        print(f"[WEATHER] {message}")
