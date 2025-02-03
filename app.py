from flask import Flask, request, render_template, jsonify
import subprocess
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    try:
        # Récupérer le code Python du client
        data = request.get_json()
        code = data.get("code", "")

        # Exécuter le code en isolant le processus
        result = subprocess.run(
            ["python", "-c", code],
            text=True,
            capture_output=True,
            timeout=5  # Limite de temps pour éviter les boucles infinies
        )

        # Retourner la sortie au client
        output = result.stdout if result.stdout else result.stderr
        return jsonify({"output": output})

    except subprocess.TimeoutExpired:
        return jsonify({"output": "Erreur : Temps d'exécution dépassé."})
    except Exception as e:
        return jsonify({"output": f"Erreur : {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
