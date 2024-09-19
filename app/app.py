from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    title = os.getenv('PAGE_TITLE', 'Título Padrão')
    header = os.getenv('PAGE_HEADER', 'Cabeçalho Padrão')
    message = os.getenv('PAGE_MESSAGE', 'Mensagem Padrão')
    
    # Carrega o arquivo HTML e substitui os placeholders pelos valores
    return render_template('index.html', title=title, header=header, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
