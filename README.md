# Estágios API

Projeto Django e Django REST Framework para gerenciamento de estágios supervisionados.

## Estrutura

- `estagios/` projeto Django
- `core/` app principal com modelos e APIs
- `media/` arquivos enviados
- `static/` arquivos estáticos
- `venv/` ambiente virtual opcional

## Requisitos

- Docker e Docker Compose instalados.

## Configuração

1. Construa os containers:

```bash
docker-compose build
```

2. Inicie os serviços:

```bash
docker-compose up
```

A aplicação estará disponível em `http://localhost:8000/` e o pgAdmin em `http://localhost:5050/`.

3. Acesse o Django Admin em `/admin/` após criar um superusuário:

```bash
docker-compose run web python manage.py createsuperuser
```

## Endpoints

Todas as rotas da API estão sob `/api/`.
Consulte o arquivo `core/urls.py` para ver todas as rotas disponíveis.

## Migrações

As migrações já estão versionadas no diretório `core/migrations/`. Caso precise recriar o banco:

```bash
docker-compose run web python manage.py migrate
```
