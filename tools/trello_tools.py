# [AI Generated] Data: 19/06/2024
# Descrição: Ferramentas para integração com Trello para uso com CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai_tools 0.17.0
# AI_GENERATED_CODE_START

from crewai_tools import BaseTool
import os
import requests
import json

class BoardDataFetcherTool(BaseTool):
    name: str = "Trello Board Data Fetcher"
    description: str = "Busca dados de cartões, comentários e atividades de um board do Trello."

    api_key: str = os.environ['TRELLO_API_KEY']
    api_token: str = os.environ['TRELLO_API_TOKEN']
    board_id: str = os.environ['TRELLO_BOARD_ID']

    def _run(self) -> dict:
        url = f"{os.getenv('DLAI_TRELLO_BASE_URL', 'https://api.trello.com')}/1/boards/{self.board_id}/cards"
        query = {
            'key': self.api_key,
            'token': self.api_token,
            'fields': 'name,idList,due,dateLastActivity,labels',
            'attachments': 'true',
            'actions': 'commentCard'
        }
        response = requests.get(url, params=query)
        if response.status_code == 200:
            return response.json()
        else:
            # Fallback em caso de erro
            return json.dumps([])

class CardDataFetcherTool(BaseTool):
    name: str = "Trello Card Data Fetcher"
    description: str = "Busca dados de um cartão do Trello."

    api_key: str = os.environ['TRELLO_API_KEY']
    api_token: str = os.environ['TRELLO_API_TOKEN']

    def _run(self, card_id: str) -> dict:
        url = f"{os.getenv('DLAI_TRELLO_BASE_URL', 'https://api.trello.com')}/1/cards/{card_id}"
        query = {
            'key': self.api_key,
            'token': self.api_token
        }
        response = requests.get(url, params=query)
        if response.status_code == 200:
            return response.json()
        else:
            return json.dumps({"error": "Falha ao buscar dados do cartão"})
# AI_GENERATED_CODE_END 