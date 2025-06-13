import json
from carpark import Carpark
from display import Display, WeatherDisplay

with open("config.json") as f:
    config = json.load(f)

carpark = Carpark.from_config(config)

carpark.add_car("1ABC123")
carpark.add_car("2XYZ789")

display = Display()
display.show(f"Available Bays: {len(carpark.available_bays())}")

weather = WeatherDisplay()
weather.show("Expect rain at 6PM")

for bay in carpark.bays:
    print(bay)

# Test comment to trigger pull request
