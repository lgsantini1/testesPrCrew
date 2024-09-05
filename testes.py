import requests

def obter_temperatura_piracicaba():
    # URL da API para obter o clima de Piracicaba
    url = "http://wttr.in/Piracicaba?format=%t"
    
    try:
        # Fazendo a solicitação GET à API com tempo limite de 10 segundos
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()  # Verifica se houve algum erro HTTP
        
        # Obtém a temperatura se a resposta for bem-sucedida
        temperatura = resposta.text.strip()  # Remove espaços em branco extras
        return temperatura
    except requests.exceptions.Timeout:
        print("A conexão demorou muito para responder.")
        return None
    except requests.exceptions.HTTPError as err:
        print(f"Erro ao obter os dados: {err}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao se conectar à API: {e}")
        return None

temperatura = obter_temperatura_piracicaba()
if temperatura is not None:
    print(f"A temperatura atual em Piracicaba é: {temperatura}")
