'''
Usage:
python consumer.py -u usuario -p senha
'''
from pprint import pprint
from typing import Dict

import click
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = 'http://127.0.0.1:8000/api'


def fetch_token(session, endpoint,
                username, password):
    '''
    Funçao responsavel pela autenticação do usuário.
    '''
    # headers = {'Content-type': 'application/json'}
    data = {
        'username': username,
        'password': password,
    }
    with session.post(
        endpoint,
        auth=HTTPBasicAuth(username, password),
        # headers=headers,  # Não precisou
        data=data
    ) as response:
        return response.json()


def get_token(username: str, password: str) -> Dict[str, str]:
    '''
    Funçao responsavel para coletar o access_token do usuário logado.
    '''
    with requests.Session() as session:
        endpoint = f'{BASE_URL}auth/jwt/create/'
        response = fetch_token(session, endpoint, username, password)
        data = {
            'access_token': response['access'],
        }
        return data


def fetch(session, endpoint, access_token):
    '''
    Autenticação via JWT.
    '''
    headers = {'Authorization': f'Bearer {access_token}'}
    with session.get(endpoint, headers=headers) as response:
        return response.json()


def post_data(session, endpoint, access_token, id, title):
    '''
    Funçao responsavel para salvar o produto.
    '''
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        'id': id,
        'title': title,
        # 'title': title,
        # 'completed': completed,
    }
    with session.post(endpoint, headers=headers, data=data) as response:
        print(response)
        pprint(response.json())


@click.command()
@click.option('--username', '-u', prompt='username', help='Type the username.')
@click.option('--password', '-p', prompt='password', help='Type the password.')
#@click.option('--userId', '-t', help='Type the userId.')
@click.option('--id', '-pr', help='Type the id.')
@click.option('--title', '-pr', help='Type the title data.')
# @click.option('--completed', '-pr', help='Type the completed data.')
def main(username, password, id=None, title=None):
    '''
    Consumindo os dados.
    '''
    token = get_token(username, password)
    access_token = token['access_token']
    with requests.Session() as session:
        endpoint = 'http://127.0.0.1:8000/api'
        response = fetch(session, endpoint, access_token)
        pprint(response)

        if id and title:
            print(f'Dados {id}, {title} inseridos')
            post_data(session, endpoint, access_token, id, title)


if __name__ == '__main__':
    print('Dados')
    main()