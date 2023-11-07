from flask import Flask, jsonify, request

app = Flask(__name__)

# Crea la variable global `todos` con al menos una tarea
todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    # Retorna la versión en JSON de la variable `todos`
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)

    # Agregar el nuevo todo a la lista de todos
    todos.append(request_body)

    # Retorna la lista actualizada de todos en formato JSON
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)

    # Verifica si la posición es válida
    if 0 <= position < len(todos):
        # Elimina el todo en la posición especificada
        del todos[position]

        # Retorna la lista actualizada de todos en formato JSON
        return jsonify(todos)

    return 'Position out of range', 400  # Retorna un código de estado 400 si la posición está fuera de rango

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
