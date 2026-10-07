# 🐳 Desafio 03 — Django + Docker + Gunicorn

Aplicação Django containerizada utilizando Docker e Gunicorn, com configuração por variáveis de ambiente e preparação dos arquivos estáticos durante o processo de build.

Este projeto faz parte da minha trilha prática de estudos em **Docker e DevOps**, com foco em compreender como uma aplicação Django é construída, empacotada e executada dentro de um container.

---

## 🎯 Objetivo

Containerizar uma aplicação Django utilizando:

- Python 3.12
- Django
- Gunicorn
- Docker
- Variáveis de ambiente
- `collectstatic`

O objetivo principal foi compreender o funcionamento do container e a comunicação entre a porta do host e a porta interna do container.

---

## 🛠️ Tecnologias

- Python 3.12
- Django 6.1
- Gunicorn 23
- Docker

---

## 📁 Estrutura

```text
desafio3-django/
├── app/
├── config/
├── static/
├── manage.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 🐳 Dockerfile

A imagem utiliza `python:3.12-slim` como imagem base.

O processo de construção realiza:

1. Definição da imagem base.
2. Configuração do diretório de trabalho.
3. Cópia do `requirements.txt`.
4. Instalação das dependências.
5. Cópia do código da aplicação.
6. Execução do `collectstatic`.
7. Exposição da porta `8000`.
8. Inicialização da aplicação utilizando Gunicorn.

---

## 🚀 Build

Para construir a imagem:

```bash
docker build -t desafio3-django .
```

---

## 🔐 Variáveis de ambiente

As configurações sensíveis não são armazenadas diretamente na imagem.

Um arquivo `.env` pode ser utilizado localmente:

```env
SECRET_KEY=sua-chave
DEBUG=0
```

O arquivo `.env` não deve ser versionado.

---

## ▶️ Executando o container

As variáveis podem ser carregadas utilizando `--env-file`:

```bash
docker run -d \
  -p 8007:8000 \
  --env-file .env \
  desafio3-django
```

A aplicação fica disponível em:

```text
http://localhost:8007
```

---

## 🔌 Portas

O container utiliza a porta `8000`.

No exemplo acima, a porta `8007` do computador é mapeada para a porta `8000` do container:

```text
Mac:8007
    ↓
Docker
    ↓
Container:8000
    ↓
Gunicorn
    ↓
Django
```

O formato utilizado pelo Docker é:

```text
-p HOST:CONTAINER
```

---

## ⚙️ Gunicorn

A aplicação Django é executada através do Gunicorn utilizando a aplicação WSGI definida em:

```text
config/wsgi.py
```

A referência utilizada pelo Gunicorn é:

```text
config.wsgi:application
```

---

## 📦 Arquivos estáticos

Durante a construção da imagem é executado:

```bash
python manage.py collectstatic --noinput
```

Dessa forma, os arquivos estáticos são preparados durante o processo de build da imagem.
O WhiteNoise serve esses arquivos pelo Gunicorn, sem depender do modo de depuração
ou de um servidor web adicional.

## 🏠 Página inicial

A rota `/` apresenta uma página de boas-vindas sobre o projeto e os conceitos
praticados. Ela continua estilizada com `DEBUG=0`, inclusive quando executada
no container.

---

## 🐚 Acessando o container

Para visualizar os containers em execução:

```bash
docker ps
```

Para acessar um container:

```bash
docker exec -it <container_id> /bin/bash
```

O diretório de trabalho da aplicação é:

```text
/app
```

---

## 📋 Logs

Para acompanhar os logs:

```bash
docker logs -f <container_id>
```

---

## 🛑 Parando o container

```bash
docker stop <container_id>
```

---

## 🧠 Conceitos praticados

Neste desafio foram praticados:

- Dockerfile
- Imagens Docker
- Containers
- Docker layers e cache
- `FROM`
- `WORKDIR`
- `COPY`
- `RUN`
- `EXPOSE`
- `CMD`
- Docker build context
- `.dockerignore`
- Variáveis de ambiente
- `--env-file`
- Django dentro de container
- Gunicorn
- WSGI
- `collectstatic`
- `ALLOWED_HOSTS`
- `DEBUG`
- Mapeamento de portas
- Diferença entre porta do host e porta do container
- Execução e inspeção de containers

---

## 🚧 Próximos passos

Os próximos desafios irão evoluir a arquitetura gradualmente, adicionando novos componentes como:

- Banco de dados PostgreSQL
- Docker Compose
- Redis
- Celery
- Nginx

Esses componentes não fazem parte deste desafio.