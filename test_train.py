# AI_GENERATED_CODE_START
# [AI Generated] Data: 19/03/2024
# Descrição: Script para teste e treinamento usando módulos utilitários
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai 0.28.0
# AI_GENERATED_CODE_END

import warnings
warnings.filterwarnings('ignore')

from helper import load_env
load_env()

import os
from config_loader import load_configs
from agents_factory import create_test_train_agents, create_test_train_tasks
from crewai_tools import FileReadTool
from crewai import Crew

os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'

# Configurar diretório de saída
output_dir = 'outputs/test_train'
os.makedirs(output_dir, exist_ok=True)

# Carregar configurações
configs = load_configs('config/test_train')

# Criar ferramentas
csv_tool = FileReadTool(file_path='./files/support_tickets_data.csv')
tools = [csv_tool]

# Criar agentes e tarefas específicos para test_train
agents = create_test_train_agents(configs['agents'], tools=tools)
tasks = create_test_train_tasks(configs['tasks'], agents)

# Preparar inputs para as tarefas
inputs = {
    'output_dir': output_dir,
    'language': 'pt-BR'
}

# Criar Crew
crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    verbose=True
)

# Executar teste
print("🚀 Iniciando teste do pipeline de suporte...")
print(f"📁 Diretório de saída: {output_dir}")
print("🇧🇷 Todas as saídas serão em português brasileiro")
print("-" * 50)

##crew.test(n_iterations=1, eval_llm='gpt-4o', inputs=inputs)
##results = crew.kickoff(inputs=inputs)
# Usar kickoff() em vez de test() para permitir execução real de código
results = crew.kickoff(inputs=inputs)

print("-" * 50)
print("✅ Teste concluído!")
print(f"📊 Gráficos salvos em: {output_dir}")
print(f"📄 Resultado: {results}")