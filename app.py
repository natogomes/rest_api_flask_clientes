from flask import Flask, jsonify, request
import json

# pip install Flask

app = Flask(__name__)


# simula um banco de dados podendo ser adicionado, alterado e excluído enquanto estiver executando
clientes = [
    {
        'nome': 'pedro augusto',
        'endereco': 'rua das flores',
        'bairro': 'torre',
        'cidade': 'recife',
        'email': 'pedroaugusto@gmail.com'
    },
    {
        'nome': 'julia de oliveira',
        'endereco': 'rua da paz',
        'bairro': 'iputinga',
        'cidade': 'recife',
        'email': 'juliaoliveira@gmail.com'
    }
]


# pagina de entrada
@app.route('/')
def inicial():
    return jsonify(
        {
            'nome': 'REST API com FLASK - Clientes'
        }
    )


# lista todos os clientes cadastrados(GET) e faz novos registros(POST)
@app.route('/clientes/', methods=['GET', 'POST'])
def lista_clientes():
    if request.method == 'GET':
        return jsonify(clientes)

    elif request.method == 'POST':
        dados = json.loads(request.data)
        clientes.append(dados)
        return jsonify(
            {
                'status': 'sucesso',
                'mensagem': 'cliente cadastrado com sucesso!'
            },
            dados
        )


# acessa, altera e exclui o cadastro do cliente pelo email
@app.route('/cliente/<email>', methods=['GET', 'PUT', 'DELETE'])
def cliente(email):
    if request.method == 'GET':
        for i in clientes:
            if len(i) == 0:
                continue
            elif i['email'] == email:
                return jsonify(i)

        return jsonify(
            {
                'status': 'erro',
                'mensagem': 'registro não encontrado!'
            }
        )

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        for i in clientes:
            if len(i) == 0:
                continue
            if i['email'] == email:
                i['nome'] = dados['nome']
                i['endereco'] = dados['endereco']
                i['bairro'] = dados['bairro']
                i['cidade'] = dados['cidade']
                i['email'] = dados['email']
                return jsonify(
                    {
                        'status': 'sucesso',
                        'mensagem': 'registro alterado com sucesso'
                    },
                    i
                )
        return jsonify(
            {
                'status': 'erro',
                'mensagem': 'registro não encontrado!'
            }
        )

    elif request.method == 'DELETE':
        for i in clientes:
            if len(i) == 0:
                continue
            elif i['email'] == email:
                i.clear()
                return jsonify(
                    {
                        'status': 'sucesso',
                        'mensagem': 'registro excluído com sucesso'
                    }
                )
        return jsonify(
            {
                'status': 'erro',
                'mensagem': 'registro não encontrado!'
            }
        )


if __name__ == '__main__':
    app.run(debug=True)
