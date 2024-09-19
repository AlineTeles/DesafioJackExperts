FROM python:3.9-slim

# usuário não root
RUN adduser --disabled-password appuser

# Defina o diretório de trabalho no contêiner
WORKDIR /app

COPY app/app.py .
COPY app/templates ./templates/
COPY app/requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Defina o usuário não root
USER appuser

# Exponha a porta da aplicação
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
