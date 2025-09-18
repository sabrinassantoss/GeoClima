import requests

def get_address_via_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resp = requests.get(url)  
    if resp.status_code != 200:
        raise Exception('Erro ao acessar ViaCEP')
    data = resp.json()
    if "erro" in data:
        raise Exception("CEP inválido")
    return data

def get_lat_and_lon(endereco):
    query = f"{endereco['logradouro']}, {endereco['bairro']}, {endereco['localidade']}, {endereco['uf']}, Brasil"
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": query, "format": "json", "limit": 1}
    resp = requests.get(url, params=params, headers={"User-Agent": "flask-app"})
    if resp.status_code != 200 or not resp.json():
        raise Exception("Erro ao buscar coordenadas")
    data = resp.json()[0]
    return float(data["lat"]), float(data["lon"])

def get_temperature(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        raise Exception("Erro ao buscar temperatura")
    data = resp.json()
    return data["current_weather"]["temperature"]