Sensor de Sites de Municípios
Este projeto é um sensor eficiente para verificar o status de vários sites.

Sobre
O projeto utiliza Python para monitorar o status HTTP de uma lista de URLs, representando portais eletrônicos municipais. Ele faz requisições HTTP usando a biblioteca requests para verificar se os sites estão online e obtém o código de status da resposta.

Funcionalidades
Verifica a disponibilidade de diversas URLs de portais municipais.

Informa o nome da cidade, URL e status da requisição HTTP.

Tratamento de exceções para capturar erros de conexão e timeout.

Resultado apresentado no console com códigos e nomes das cidades.

Como usar
Pré-requisitos
Python 3 instalado

Biblioteca requests (pode ser instalada com pip install requests)

Estrutura do projeto
sensor.py: classe principal Sensor que realiza as verificações.

municipios/municipio.py: contém a classe SensorSites com a lista de cidades e suas URLs.

Contribuições
Contribuições são bem-vindas! Fique à vontade para abrir issues, sugerir melhorias ou enviar pull requests.
