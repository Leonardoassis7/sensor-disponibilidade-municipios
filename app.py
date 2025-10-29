from sensor.sensor import Sensor, SensorSites

def main():
    sensor = Sensor()
    resultados = sensor.verifica_sites()
    for codigo, info in resultados.items():
        print(f"{codigo} - {info['nome']}: {info['url']} => Status -> {info['status']}")

if __name__ == "__main__":
    main()