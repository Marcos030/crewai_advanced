# [AI Generated] Data: 19/06/2024
# Descrição: Ajuste para compatibilidade do método plot() do Flow (sem argumento 'path') e mover arquivo gerado
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai 0.141.0
# AI_GENERATED_CODE_START
import warnings
warnings.filterwarnings('ignore')

from helper import load_env
load_env()

import os
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o-mini'

# Garantir que a pasta de outputs existe
os.makedirs('outputs/sales_pipeline', exist_ok=True)

from config_loader import load_configs
from agents_factory import (
    create_lead_agents, create_lead_tasks,
    create_email_agents, create_email_tasks
)
from flows.sales_pipeline_flow import SalesPipeline
from display_utils import print_wrapped_text
# from display_utils import display_metrics, display_html_table

# Carregar configurações dos YAMLs
configs = load_configs([
    'config/sales_pipeline/lead_qualification_agents.yaml',
    'config/sales_pipeline/lead_qualification_tasks.yaml',
    'config/sales_pipeline/email_engagement_agents.yaml',
    'config/sales_pipeline/email_engagement_tasks.yaml'
])

# Criar agentes e tarefas
lead_agents = create_lead_agents(configs)
lead_tasks = create_lead_tasks(configs, lead_agents)
email_agents = create_email_agents(configs)
email_tasks = create_email_tasks(configs, email_agents)

# Instanciar e rodar o pipeline
flow = SalesPipeline(lead_agents, lead_tasks, email_agents, email_tasks)
# Salvar o diagrama do flow (compatível com crewai 0.141.0)
flow.plot()
# Mover o arquivo gerado para a pasta correta, se existir
import shutil
if os.path.exists('crewai_flow.html'):
    shutil.move('crewai_flow.html', 'outputs/sales_pipeline/crewai_flow.html')
emails = flow.kickoff()

# --- CÓDIGO DE MÉTRICAS E TABELAS (comentado, mas já com caminho de output organizado) ---
# scores = flow.state.get("score_crews_results", [])
# if scores:
#     token_usage = getattr(scores[0], 'token_usage', None)
#     if token_usage and hasattr(token_usage, 'model_dump'):
#         display_metrics(token_usage.model_dump(), html_path='outputs/sales_pipeline/usage_metrics.html')
#     lead_scoring_result = getattr(scores[0], 'pydantic', None)
#     if lead_scoring_result:
#         display_html_table(lead_scoring_result, html_path='outputs/sales_pipeline/lead_scoring_table.html')
# if emails and hasattr(emails[0], 'token_usage'):
#     token_usage = getattr(emails[0], 'token_usage', None)
#     if token_usage and hasattr(token_usage, 'model_dump'):
#         display_metrics(token_usage.model_dump(), html_path='outputs/sales_pipeline/usage_metrics_email.html')
# -----------------------------------------------

# Exibir apenas o texto final do email
if emails and hasattr(emails[0], 'raw'):
    print_wrapped_text(emails[0].raw)
# AI_GENERATED_CODE_END