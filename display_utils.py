# [AI Generated] Data: 19/06/2024
# Descrição: Módulo para exibição de resultados e formatação
# Gerado por: Cursor AI
# Versão: Python 3.12, pandas 2.3.1
# AI_GENERATED_CODE_START 

import pandas as pd
from typing import Dict, Any
from crewai import Crew
from models import ProjectInputs

def show_project_summary(inputs: Dict[str, Any]) -> None:
    """
    Exibe um resumo do projeto.
    
    Args:
        inputs: Dicionário com as entradas do projeto
    """
    print("=" * 80)
    print("RESUMO DO PROJETO")
    print("=" * 80)
    print(f"Tipo de Projeto: {inputs.get('project_type', 'N/A')}")
    print(f"Objetivos: {inputs.get('project_objectives', 'N/A')}")
    print(f"Indústria: {inputs.get('industry', 'N/A')}")
    print(f"Membros da Equipe: {inputs.get('team_members', 'N/A')}")
    print("=" * 80)

def show_results(result: Any, crew: Crew) -> None:
    """
    Exibe os resultados do crew e métricas de uso.
    
    Args:
        result: Resultado do crew
        crew: Instância do crew
    """
    print("\n" + "=" * 80)
    print("RESULTADOS DO PLANEJAMENTO")
    print("=" * 80)
    
    # Exibe custos
    if hasattr(crew, 'usage_metrics'):
        costs = 0.150 * (crew.usage_metrics.prompt_tokens + crew.usage_metrics.completion_tokens) / 1_000_000
        print(f"Custos Totais: ${costs:.4f}")
        print(f"Tokens de Prompt: {crew.usage_metrics.prompt_tokens:,}")
        print(f"Tokens de Completão: {crew.usage_metrics.completion_tokens:,}")
    
    # Exibe resultados estruturados
    if hasattr(result, 'pydantic'):
        result_dict = result.pydantic.dict()
        
        # Exibe tarefas
        if 'tasks' in result_dict:
            print("\nTAREFAS ESTIMADAS:")
            print("-" * 40)
            task_list = result_dict['tasks']
            df_tasks = pd.DataFrame(task_list)
            print(df_tasks.to_string(index=False))
        
        # Exibe marcos
        if 'milestones' in result_dict:
            print("\nMARCOS DO PROJETO:")
            print("-" * 40)
            milestone_list = result_dict['milestones']
            df_milestones = pd.DataFrame(milestone_list)
            print(df_milestones.to_string(index=False))

def show_usage_metrics(crew: Crew) -> pd.DataFrame:
    """
    Retorna métricas de uso como DataFrame.
    
    Args:
        crew: Instância do crew
        
    Returns:
        pd.DataFrame: DataFrame com métricas de uso
    """
    if hasattr(crew, 'usage_metrics'):
        return pd.DataFrame([crew.usage_metrics.dict()])
    return pd.DataFrame()

def format_project_requirements(requirements: str) -> str:
    """
    Formata os requisitos do projeto para exibição.
    
    Args:
        requirements: String com os requisitos
        
    Returns:
        str: Requisitos formatados
    """
    return requirements.strip()

def create_project_inputs(
    project_type: str,
    project_objectives: str,
    industry: str,
    team_members: str,
    project_requirements: str
) -> Dict[str, Any]:
    """
    Cria dicionário de entradas do projeto.
    
    Args:
        project_type: Tipo do projeto
        project_objectives: Objetivos do projeto
        industry: Indústria
        team_members: Membros da equipe
        project_requirements: Requisitos do projeto
        
    Returns:
        Dict[str, Any]: Dicionário com as entradas
    """
    return {
        'project_type': project_type,
        'project_objectives': project_objectives,
        'industry': industry,
        'team_members': team_members,
        'project_requirements': project_requirements
    }
# AI_GENERATED_CODE_END 