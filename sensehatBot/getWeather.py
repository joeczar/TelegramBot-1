from sense_hat import SenseHat

sense = SenseHat()


def getWeather(command):
    t = round(sense.get_temperature_from_pressure(), 1)
    h = round(sense.get_humidity(), 1)
    p = round(sense.get_pressure(), 1)

    switch = {
        'temperature': 'The temperature is %s' % t,
        'humidity': 'The humidity is %s' % h,
        "pressure": 'The pressure is %s' % p,
        'report': "Temperature {temp}\nHumidity {humid}\nPressure {press}".format(
            temp=t, humid=h, press=p),
    }
    return switch.get(command, 'I don\'t know %s' % command)
