# [AI Generated] Data: 19/06/2024
# Descrição: Correção do tratamento do resultado do crew para evitar erro de atributo e garantir exibição robusta
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai 0.141.0, crewai_tools 0.51.1
# AI_GENERATED_CODE_START

import warnings
warnings.filterwarnings('ignore')

from helper import load_env
load_env()

import os
from config_loader import load_configs
from agents_factory import create_agents, create_tasks
from crewai import Crew
import pandas as pd

os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o-mini'

# Carregar configurações
dataset_dir = 'config/planing_estimation_allocation'
configs = load_configs(dataset_dir)

# Dados do projeto (em português)
project = 'Website'
industry = 'Tecnologia'
project_objectives = 'Criar um website para uma pequena empresa'
team_members = """
- João Silva (Gerente de Projeto)
- Maria Santos (Engenheira de Software)
- Roberto Oliveira (Designer)
- Ana Costa (Engenheira de QA)
- Tomás Ferreira (Engenheiro de QA)
"""
project_requirements = """
- Criar um design responsivo que funcione bem em dispositivos desktop e móveis
- Implementar uma interface de usuário moderna e visualmente atraente com visual limpo
- Desenvolver um sistema de navegação amigável com estrutura de menu intuitiva
- Incluir uma página "Sobre Nós" destacando a história e valores da empresa
- Projetar uma página "Serviços" mostrando as ofertas do negócio com descrições
- Criar uma página "Contato" com formulário e mapa integrado para comunicação
- Implementar uma seção de blog para compartilhar notícias do setor e atualizações da empresa
- Garantir tempos de carregamento rápidos e otimizar para motores de busca (SEO)
- Integrar links de redes sociais e capacidades de compartilhamento
- Incluir uma seção de depoimentos para mostrar feedback dos clientes e construir confiança
"""

# Entradas do projeto
inputs = {
    'project_type': project,
    'project_objectives': project_objectives,
    'industry': industry,
    'team_members': team_members,
    'project_requirements': project_requirements
}

# Criar agentes e tarefas
agents = create_agents(configs['agents'])
tasks = create_tasks(configs['tasks'], agents)

# Criar Crew
crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    verbose=True
)

# Executar o crew
result = crew.kickoff(inputs=inputs)

costs = 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
print(f"Custos Totais: R${costs:.4f}")

# Exibir métricas de uso
df_usage_metrics = pd.DataFrame([crew.usage_metrics.dict()])
print("\nMétricas de uso:")
print(df_usage_metrics)

# Exibir resultados estruturados
if result is not None:
    # Se for objeto com .pydantic
    if hasattr(result, 'pydantic') and hasattr(result.pydantic, 'dict'):
        result_dict = result.pydantic.dict()
    # Se for dicionário
    elif isinstance(result, dict):
        result_dict = result
    # Se for string ou outro tipo, apenas exibe
    else:
        print("\nResultado bruto:")
        print(result)
        result_dict = None

    if result_dict:
        if 'tasks' in result_dict:
            print("\nTarefas estimadas:")
            df_tasks = pd.DataFrame(result_dict['tasks'])
            print(df_tasks.to_string(index=False))
        if 'milestones' in result_dict:
            print("\nMarcos do projeto:")
            df_milestones = pd.DataFrame(result_dict['milestones'])
            print(df_milestones.to_string(index=False))
else:
    print("\nNenhum resultado retornado pelo Crew.")
# AI_GENERATED_CODE_END