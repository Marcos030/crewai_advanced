# [AI Generated] Data: 19/06/2024
# Descrição: Script principal para relatório de progresso do projeto, usando módulos utilitários
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai 0.75
# AI_GENERATED_CODE_START

import warnings
warnings.filterwarnings('ignore')

from helper import load_env
load_env()

import os
from config_loader import load_configs
from agents_factory import create_agents, create_tasks
from tools.trello_tools import BoardDataFetcherTool, CardDataFetcherTool
from crewai import Crew
import pandas as pd

os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o-mini'

# Carregar configurações
configs = load_configs('config/project_progress_report')

# Criar ferramentas externas
tools = [BoardDataFetcherTool(), CardDataFetcherTool()]

# Criar agentes e tarefas
agents = create_agents(configs['agents'], tools=tools)
tasks = create_tasks(configs['tasks'], agents)

# Criar Crew
crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    verbose=True
)

# Executar o crew
result = crew.kickoff()

costs = 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
print(f"Custos Totais: R${costs:.4f}")

# Exibir métricas de uso
df_usage_metrics = pd.DataFrame([crew.usage_metrics.dict()])
print("\nMétricas de uso:")
print(df_usage_metrics)

from IPython.display import Markdown
markdown = result.raw
Markdown(markdown)
# AI_GENERATED_CODE_END