# [AI Generated] Data: 19/06/2024
# Descrição: Refatoração das ferramentas Trello para o padrão BaseTool moderno (crewai 0.141.0, crewai_tools 0.51.1)
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai 0.141.0, crewai_tools 0.51.1
# AI_GENERATED_CODE_START

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import os
import requests
import json

class BoardDataFetcherInput(BaseModel):
    pass  # Sem argumentos obrigatórios

class BoardDataFetcherTool(BaseTool):
    name: str = "Trello Board Data Fetcher"
    description: str = "Busca dados de cartões, comentários e atividades de um board do Trello."
    args_schema: type = BoardDataFetcherInput

    def _run(self):
        api_key = os.environ['TRELLO_API_KEY']
        api_token = os.environ['TRELLO_API_TOKEN']
        board_id = os.environ['TRELLO_BOARD_ID']
        url = f"{os.getenv('DLAI_TRELLO_BASE_URL', 'https://api.trello.com')}/1/boards/{board_id}/cards"
        query = {
            'key': api_key,
            'token': api_token,
            'fields': 'name,idList,due,dateLastActivity,labels',
            'attachments': 'true',
            'actions': 'commentCard'
        }
        response = requests.get(url, params=query)
        if response.status_code == 200:
            return response.json()
        else:
            return []

class CardDataFetcherInput(BaseModel):
    card_id: str = Field(..., description="ID do cartão do Trello.")

class CardDataFetcherTool(BaseTool):
    name: str = "Trello Card Data Fetcher"
    description: str = "Busca dados de um cartão do Trello."
    args_schema: type = CardDataFetcherInput

    def _run(self, card_id: str):
        api_key = os.environ['TRELLO_API_KEY']
        api_token = os.environ['TRELLO_API_TOKEN']
        url = f"{os.getenv('DLAI_TRELLO_BASE_URL', 'https://api.trello.com')}/1/cards/{card_id}"
        query = {
            'key': api_key,
            'token': api_token
        }
        response = requests.get(url, params=query)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Falha ao buscar dados do cartão"}
# AI_GENERATED_CODE_END 