from flask import Flask

# Criando a instância da aplicação Flask
app = Flask(__name__)

# Definindo uma rota
@app.route('/')
def hello_world():
	return 'Fala fiote'

# Rodando a aplicação
if __name__ == '__main__':
	app.run(debug=True)
	