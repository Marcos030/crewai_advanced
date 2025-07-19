# [AI Generated] Data: 19/06/2024
# Descrição: Script para criação de conteúdo financeiro usando CrewAI
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai 0.141.0
# AI_GENERATED_CODE_START

import warnings
warnings.filterwarnings('ignore')

from helper import load_env
load_env()

import os
from config_loader import load_configs
from agents_factory import create_content_creator_agents, create_content_creator_tasks
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool
from crewai import Crew
from pydantic import BaseModel, Field
from typing import List

# Configurar modelo LLM via variável de ambiente
# O CrewAI usará automaticamente o modelo configurado
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o-mini'

# Definir modelo Pydantic para saída
class SocialMediaPost(BaseModel):
    platform: str = Field(..., description="The social media platform where the post will be published (e.g., Twitter, LinkedIn).")
    content: str = Field(..., description="The content of the social media post, including any hashtags or mentions.")

class ContentOutput(BaseModel):
    article: str = Field(..., description="The article, formatted in markdown.")
    social_media_posts: List[SocialMediaPost] = Field(..., description="A list of social media posts related to the article.")

# Carregar configurações
configs = load_configs([
    'config/content_creator/agents.yaml',
    'config/content_creator/tasks.yaml'
])

# Criar ferramentas
tools = [SerperDevTool(), ScrapeWebsiteTool(), WebsiteSearchTool()]

# Criar agentes usando a factory específica
agents = create_content_creator_agents(configs['agents'], tools=tools)

# Criar tarefas usando a factory específica
tasks = create_content_creator_tasks(configs['tasks'], agents)

# Configurar output_pydantic para a tarefa de qualidade
tasks[-1].output_pydantic = ContentOutput  # Última tarefa é quality_assurance

# Criar Crew
content_creation_crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    verbose=True
)

# Executar o pipeline
if __name__ == "__main__":
    print("🚀 Iniciando criação de conteúdo financeiro...")
    print("📊 Modelo: GPT-4o-mini (configurado via variável de ambiente)")
    print("-" * 50)
    
    result = content_creation_crew.kickoff(inputs={
        'subject': 'Inflation in the US and the impact on the stock market in 2024'
    })
    
    print("-" * 50)
    print("✅ Conteúdo criado com sucesso!")
    
    # Exibir posts de redes sociais
    if hasattr(result, 'pydantic') and result.pydantic:
        posts = result.pydantic.dict()['social_media_posts']
        print("\n📱 Posts para Redes Sociais:")
        print("=" * 50)
        
        for post in posts:
            platform = post['platform']
            content = post['content']
            print(f"\n🔗 {platform.upper()}")
            print("-" * 30)
            print(content)
            print("-" * 50)
        
        # Exibir artigo
        print("\n📄 Artigo Completo:")
        print("=" * 50)
        print(result.pydantic.dict()['article'])
    else:
        print("\n📄 Resultado:")
        print(result)

# AI_GENERATED_CODE_END