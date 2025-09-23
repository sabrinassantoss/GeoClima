# Arquitetura da GeoClima API

## Objetivo
Este documento descreve a arquitetura da aplicação **GeoClima API**, detalhando os módulos internos, suas responsabilidades e a forma como se conectam às APIs externas.  

---

## Estrutura de Pastas
A API segue a seguinte organização de diretórios:

´´´text
GECLIMAAPI
┣ docs/
┃ ┗ architecture.md # Documentação da arquitetura
┣ postman/
┃ ┗ GeoClima.postman_collection.json # Coleção Postman exportada
┣ src/
┃ ┣ app.py # Endpoints da API em Flask
┃ ┗ services.py # Funções de integração com APIs externas
┣ tests/
┃ ┣ init.py # Inicializador de pacotes de testes
┃ ┗ test_app.py # Testes unitários com unittest
┣ .gitignore # Ignora arquivos temporários
┗ README.md # Documentação principal do projeto
´´´
---

## Componentes e Responsabilidades

- **app.py**  
  - Implementa a API utilizando Flask.  
  - Define os endpoints:  
    - `/endereco/<cep>`  
    - `/coordenadas/<cep>`  
    - `/temperatura/<cep>`  

- **services.py**  
  - Contém funções responsáveis pela integração com serviços externos:  
    - **ViaCEP** → busca dados de endereço pelo CEP.  
    - **Nominatim (OpenStreetMap)** → converte endereço em latitude/longitude.  
    - **Open-Meteo** → retorna a temperatura atual.  

- **test_app.py**  
  - Implementa testes automatizados com unittest.  
  - Cada endpoint é validado quanto ao status da resposta e ao conteúdo retornado.  

- **postman/GeoClima.postman_collection.json**  
  - Coleção exportada para facilitar testes manuais dos endpoints.  

---

## Fluxo de Funcionamento
1. O cliente (usuário, Postman ou outra aplicação) faz uma requisição HTTP para a API.  
2. O Flask (`app.py`) recebe a requisição.  
3. O `app.py` chama funções de `services.py`.  
4. O `services.py` consulta as APIs externas:  
   - ViaCEP → retorna endereço.  
   - Nominatim → retorna coordenadas.  
   - Open-Meteo → retorna temperatura.  
5. A resposta é estruturada em JSON e devolvida ao cliente.  

---

## Diagrama de Arquitetura

O diagrama abaixo ilustra os principais componentes da API e sua interação com os serviços externos:

![Diagrama da Arquitetura](GeoClima_Arquitetura.png)
