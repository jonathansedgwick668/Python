import logging
import random

class BatteryTemperatureFormatter(logging.Formatter):
    def format(self, record):
        return f"{record.levelname} – {record.msg} C"

class BatteryTemperatureHandler(logging.FileHandler):
    def __init__(self, filename):
        super().__init__(filename)
        self.setFormatter(BatteryTemperatureFormatter())

logger = logging.getLogger("BatteryLogger")
logger.setLevel(logging.DEBUG)
logger.handlers = []

log_handler = BatteryTemperatureHandler("battery_temperature.log")
logger.addHandler(log_handler)

for _ in range(60):
    temp = round(random.uniform(20, 40), 1) 

    if temp < 20:
        logger.debug(temp)
    elif 30 <= temp <= 35:
        logger.warning(temp)
    elif temp > 35:
        logger.critical(temp)
    else:
        logger.info(temp)  # For 20–29.9°C range (not specified, but logically INFO)

