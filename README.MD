# Fluxo para instalação das dependências

```bash
pip install -r requirements.txt
```

## Ajustar variáveis, substituir nome e versão do python em

cs_env\pyvenv.cfg

## Ativar Docker

```bash
cs_env\Scripts\activate
```

## Subir aplicação

```bash
python manage.py runserver
```

## Confirmar alterações do banco

```bash
python manage.py makemigrations
python manage.py migrate
```
