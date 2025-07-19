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

# --- Funções específicas para content_creator ---
def create_content_creator_agents(configs, tools=None):
    """
    Cria agentes específicos para o pipeline content_creator.
    """
    return {
        'market_news_monitor_agent': Agent(
            config=configs['market_news_monitor_agent'],
            tools=tools or [],
            llm="groq/llama-3.3-70b-versatile"
        ),
        'data_analyst_agent': Agent(
            config=configs['data_analyst_agent'],
            tools=tools or [],
            llm="groq/llama-3.3-70b-versatile"
        ),
        'content_creator_agent': Agent(
            config=configs['content_creator_agent'],
            tools=tools or []
        ),
        'quality_assurance_agent': Agent(
            config=configs['quality_assurance_agent']
        )
    }

def create_content_creator_tasks(configs, agents):
    """
    Cria tarefas específicas para o pipeline content_creator.
    """
    monitor_financial_news = Task(
        config=configs['monitor_financial_news'],
        agent=agents['market_news_monitor_agent']
    )
    
    analyze_market_data = Task(
        config=configs['analyze_market_data'],
        agent=agents['data_analyst_agent']
    )
    
    create_content = Task(
        config=configs['create_content'],
        agent=agents['content_creator_agent'],
        context=[monitor_financial_news, analyze_market_data]
    )
    
    quality_assurance = Task(
        config=configs['quality_assurance'],
        agent=agents['quality_assurance_agent'],
        context=[monitor_financial_news, analyze_market_data, create_content]
    )
    
    return [monitor_financial_news, analyze_market_data, create_content, quality_assurance]

# --- Funções específicas para test_train ---
def create_test_train_agents(configs, tools=None):
    """
    Cria agentes específicos para o pipeline test_train.
    Inclui allow_code_execution=True para o agente de gráficos.
    """
    return {
        'suggestion_generation_agent': Agent(
            config=configs['suggestion_generation_agent'],
            tools=tools or []
        ),
        'reporting_agent': Agent(
            config=configs['reporting_agent'],
            tools=tools or []
        ),
        'chart_generation_agent': Agent(
            config=configs['chart_generation_agent'],
            allow_code_execution=True
        )
    }

def create_test_train_tasks(configs, agents):
    """
    Cria tarefas específicas para o pipeline test_train.
    Inclui context para definir dependências entre tarefas.
    """
    suggestion_generation = Task(
        config=configs['suggestion_generation'],
        agent=agents['suggestion_generation_agent']
    )
    
    table_generation = Task(
        config=configs['table_generation'],
        agent=agents['reporting_agent']
    )
    
    chart_generation = Task(
        config=configs['chart_generation'],
        agent=agents['chart_generation_agent']
    )
    
    final_report_assembly = Task(
        config=configs['final_report_assembly'],
        agent=agents['reporting_agent'],
        context=[suggestion_generation, table_generation, chart_generation]
    )
    
    return [suggestion_generation, table_generation, chart_generation, final_report_assembly]

# AI_GENERATED_CODE_END 