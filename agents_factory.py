# [AI Generated] Data: 19/06/2024
# Descrição: Factory para criação de agentes e tarefas do projeto (funções genéricas e específicas)
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai 0.141.0, crewai_tools 0.51.1
# AI_GENERATED_CODE_START
from crewai import Agent, Task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from models import LeadScoringResult

# --- Funções genéricas para experimentos diversos ---
def create_agents(agents_config, tools=None):
    """
    Cria agentes a partir do dicionário de configuração.
    Se tools for fornecido, injeta nas chaves que contenham 'data_collection' (compatível com uso em project_progress_report).
    """
    agents = {}
    for key, config in agents_config.items():
        if tools and 'data_collection' in key:
            agents[key] = Agent(config=config, tools=tools)
        else:
            agents[key] = Agent(config=config)
    return agents

def create_tasks(tasks_config, agents):
    """
    Cria tarefas a partir do dicionário de configuração e dos agentes.
    Associa cada task ao agente de mesmo nome (ou ao primeiro agente, se não encontrar).
    """
    tasks = []
    for key, config in tasks_config.items():
        # Busca agente correspondente
        agent_key = key.replace('task', 'agent') if key.endswith('task') else key.replace('report_generation', 'analysis_agent')
        agent = agents.get(agent_key) or list(agents.values())[0]
        tasks.append(Task(config=config, agent=agent))
    return tasks

# --- Funções específicas para pipeline de vendas ---
def create_lead_agents(configs):
    return {
        'lead_data_agent': Agent(
            config=configs['lead_qualification_agents']['lead_data_agent'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        ),
        'cultural_fit_agent': Agent(
            config=configs['lead_qualification_agents']['cultural_fit_agent'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        ),
        'scoring_validation_agent': Agent(
            config=configs['lead_qualification_agents']['scoring_validation_agent'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )
    }

def create_lead_tasks(configs, agents):
    return {
        'lead_data_task': Task(
            config=configs['lead_qualification_tasks']['lead_data_collection'],
            agent=agents['lead_data_agent']
        ),
        'cultural_fit_task': Task(
            config=configs['lead_qualification_tasks']['cultural_fit_analysis'],
            agent=agents['cultural_fit_agent']
        ),
        'scoring_validation_task': Task(
            config=configs['lead_qualification_tasks']['lead_scoring_and_validation'],
            agent=agents['scoring_validation_agent'],
            context=[],  # contexto será preenchido no pipeline_flow
            output_pydantic=LeadScoringResult
        )
    }

def create_email_agents(configs):
    return {
        'email_content_specialist': Agent(
            config=configs['email_engagement_agents']['email_content_specialist']
        ),
        'engagement_strategist': Agent(
            config=configs['email_engagement_agents']['engagement_strategist']
        )
    }

def create_email_tasks(configs, agents):
    return {
        'email_drafting': Task(
            config=configs['email_engagement_tasks']['email_drafting'],
            agent=agents['email_content_specialist']
        ),
        'engagement_optimization': Task(
            config=configs['email_engagement_tasks']['engagement_optimization'],
            agent=agents['engagement_strategist']
        )
    }
# AI_GENERATED_CODE_END 