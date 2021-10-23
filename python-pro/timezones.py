from datetime import datetime

# permite trabajar con timezones
import pytz


def city_time(city):
    city_time = pytz.timezone(city)
    city_date = datetime.now(city_time).strftime("%d/%m/%Y, %H:%M:%S")
    print(f"En la ciudad {city} son las: {city_date}")


if __name__ == "__main__":
    city_time("America/Bogota")
    city_time("America/Mexico_City")
    city_time("America/Caracas")

# bogota_timezone = pytz.timezone("America/Bogota")
# bogota_date = datetime.now(bogota_timezone)
# print("Bogota: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))
