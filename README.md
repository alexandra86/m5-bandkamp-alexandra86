<h1 align="center" font-family="pattaya">BandKamp</h1><br>

<h2 font-family="pattaya">Tecnologias utilizadas</h2>
<div style="display: inline_block"><br>
 <img align="center" alt="Alexandra-python" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
 <img align="center" alt="Alexandra-postgreSQL" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"> 
</div><br>

<h2 font-family="pattaya">Descrição</h2><br>
<p font-family="robotto" font-size="16px" line-height="34px" align="justify">
O projeto representa uma aplicação que simula registros de álbuns e canções de bandas autônomas, para divulgação de seus trabalhos musicais.
</p><br>

<h2 font-family="pattaya">Requisitos técnicos:</h2><br>

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```


4. Agora é só rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```

5. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:
```shell
pytest --testdox
```

## Rodando os testes por partes

Caso você tenha interesse em rodar apenas um diretório de testes específico, pode utilizar o comando:

- Rodando testes de users:
```python
pytest --testdox -vvs tests/users/
```

- Rodando testes de albums:
```python
pytest --testdox -vvs tests/albums/
```

- Rodando testes de songs:
```python
pytest --testdox -vvs tests/songs/
````

<h2 font-family="pattaya">Principais libs utilizadas</h2><br>
<ul style="display: inline_block">
<li font-family="robotto" font-size="16px">dj-database-url</li>
<li font-family="robotto" font-size="16px">Django</li>
<li font-family="robotto" font-size="16px">djangorestframework</li>
<li font-family="robotto" font-size="16px">djangorestframework-simplejwt</li>
<li font-family="robotto" font-size="16px">drf-spectacular</li>
<li font-family="robotto" font-size="16px">gunicorn</li>
<li font-family="robotto" font-size="16px">psycopg2-binary</li>
<li font-family="robotto" font-size="16px">python-dotenv</li>
<li font-family="robotto" font-size="16px">'whitenoise[brotli]'</li>
</ul><br>

<h2 font-family="pattaya">Documentação</h2><br>
<p font-family="robotto" font-size="16px" line-height="34px" align="justify">
A documentação contendo todas as rotas da aplicação pode ser conferida <a href="https://web-production-36aae.up.railway.app/api/docs/" font-family="robotto" font-size="16px">aqui</a>.
</p><br>


