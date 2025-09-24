import services
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/endereco/<cep>", methods=["GET"])
def address(cep):
    try:
        address = services.get_address_via_cep(cep)
        return jsonify(address)
    except Exception as e:
        return jsonify({"erro": str(e)}), 400


@app.route("/coordenadas/<cep>", methods=["GET"])
def coordinates(cep):
    try:
        endereco = services.get_address_via_cep(cep)
        lat, lon = services.get_lat_and_lon(endereco)
        return jsonify({"latitude": lat, "longitude": lon})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400


@app.route("/temperatura/<cep>", methods=["GET"])
def temperature(cep):
    try:
        endereco = services.get_address_via_cep(cep)
        lat, lon = services.get_lat_and_lon(endereco)
        temp = services.get_temperature(lat, lon)
        return jsonify(
            {
                "cep": cep,
                "bairro": endereco["bairro"],
                "complemento": endereco["complemento"],
                "regiao": endereco["regiao"],
                "endereco": endereco["logradouro"],
                "cidade": endereco["localidade"],
                "estado": endereco["uf"],
                "latitude": lat,
                "longitude": lon,
                "temperatura": temp,
            }
        )
    except Exception as e:
        return jsonify({"erro": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
