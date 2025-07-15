# [AI Generated] Data: 19/06/2024
# Descrição: Utilitário para criar agentes e tarefas a partir das configurações carregadas
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai 0.75
# AI_GENERATED_CODE_START
from crewai import Agent, Task

def create_agents(agents_config, tools=None):
    """
    Cria agentes a partir da configuração, podendo receber tools.
    """
    agents = {}
    if 'data_collection_agent' in agents_config:
        agents['data_collection_agent'] = Agent(config=agents_config['data_collection_agent'], tools=tools)
    if 'analysis_agent' in agents_config:
        agents['analysis_agent'] = Agent(config=agents_config['analysis_agent'])
    if 'project_planning_agent' in agents_config:
        agents['project_planning_agent'] = Agent(config=agents_config['project_planning_agent'])
    if 'estimation_agent' in agents_config:
        agents['estimation_agent'] = Agent(config=agents_config['estimation_agent'])
    if 'resource_allocation_agent' in agents_config:
        agents['resource_allocation_agent'] = Agent(config=agents_config['resource_allocation_agent'])
    return agents

def create_tasks(tasks_config, agents):
    """
    Cria tarefas a partir da configuração e dos agentes.
    """
    tasks = []
    if 'data_collection' in tasks_config:
        tasks.append(Task(config=tasks_config['data_collection'], agent=agents['data_collection_agent']))
    if 'data_analysis' in tasks_config:
        tasks.append(Task(config=tasks_config['data_analysis'], agent=agents['analysis_agent']))
    if 'report_generation' in tasks_config:
        tasks.append(Task(config=tasks_config['report_generation'], agent=agents['analysis_agent']))
    if 'task_breakdown' in tasks_config:
        tasks.append(Task(config=tasks_config['task_breakdown'], agent=agents['project_planning_agent']))
    if 'time_resource_estimation' in tasks_config:
        tasks.append(Task(config=tasks_config['time_resource_estimation'], agent=agents['estimation_agent']))
    if 'resource_allocation' in tasks_config:
        tasks.append(Task(config=tasks_config['resource_allocation'], agent=agents['resource_allocation_agent']))
    return tasks
# AI_GENERATED_CODE_END 