# Fluxo para instalação das dependências

```bash
pip install -r requirements.txt
```

## Ajustar variáveis, substituir nome e versão do python em

```bash
cs_env\pyvenv.cfg
```

## Ativar ambiente

```bash
cs_env\Scripts\activate
```

## Subir aplicação

### Localhost:8080

```bash
python manage.py runserver localhost:8080
```

### 127.0.0.1:8000

```bash
python manage.py runserver
```

## Confirmar alterações do banco

```bash
python manage.py makemigrations
python manage.py migrate
```
