from flask import Flask, render_template, request, redirect

app = Flask(__name__)

projetos = []

@app.route('/')
def index():
    return render_template('index.html', projetos=projetos)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    descricao = request.form['descricao']
    imagem = request.form['imagem']
    link = request.form['link']

    projetos.append({
        "nome": nome,
        "descricao": descricao,
        "imagem": imagem,
        "link": link
    })

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
