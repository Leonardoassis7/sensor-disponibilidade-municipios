import requests
from municipios.municipio import SensorSites

class Sensor:
    def __init__(self):
        self.sensor_sites = SensorSites()

    def verifica_sites(self):
        resultados = {}
        for codigo, dados in self.sensor_sites.lista.items():
            url = dados.get('url')
            if not url:
                resultados[codigo] = {'nome': dados.get('nome', ''), 'status': 'Sem URL'}
                continue
            try:
                response = requests.get(url, timeout=10)
                resultados[codigo] = {
                    'nome': dados.get('nome', ''),
                    'url': url,
                    'status': response.status_code
                }
            except requests.RequestException as e:
                resultados[codigo] = {
                    'nome': dados.get('nome', ''),
                    'url': url,
                    'status': f'Erro: {e}'
                }
        return resultados


if __name__ == '__main__':
    sensor = Sensor()
    resultados = sensor.verifica_sites()
    for codigo, info in resultados.items():
        print(f"{codigo} - {info['nome']}: {info['url']} => Status -> {info['status']}")
