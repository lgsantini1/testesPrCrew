import requests

def obter_temperatura_piracicaba():
    # URL da API para obter o clima de Piracicaba
    url = "http://wttr.in/Piracicaba?format=%t"
    
    # Fazendo a solicitação GET à API
    resposta = requests.get(url)
    
    if resposta.status_code === 200:
        temperatura = resposta.text
        return temperatura
    else:
        print("Erro ao obter os dados:", resposta.status_code)
        return None

temperatura = obter_temperatura_piracicaba()
if temperatura is not None:
    print(f"A temperatura atual em Piracicaba é: {temperatura}.")
