# [AI Generated] Data: 19/06/2024
# Descrição: Módulo com modelos Pydantic para estruturas de dados
# Gerado por: Cursor AI
# Versão: Python 3.12, pydantic 2.11.7
# AI_GENERATED_CODE_START 

from typing import List
from pydantic import BaseModel, Field

class TaskEstimate(BaseModel):
    """Modelo para estimativa de tarefa."""
    task_name: str = Field(..., description="Name of the task")
    estimated_time_hours: float = Field(..., description="Estimated time to complete the task in hours")
    required_resources: List[str] = Field(..., description="List of resources required to complete the task")

class Milestone(BaseModel):
    """Modelo para marco do projeto."""
    milestone_name: str = Field(..., description="Name of the milestone")
    tasks: List[str] = Field(..., description="List of task IDs associated with this milestone")

class ProjectPlan(BaseModel):
    """Modelo para plano completo do projeto."""
    tasks: List[TaskEstimate] = Field(..., description="List of tasks with their estimates")
    milestones: List[Milestone] = Field(..., description="List of project milestones")

class ProjectInputs(BaseModel):
    """Modelo para entradas do projeto."""
    project_type: str = Field(..., description="Type of project")
    project_objectives: str = Field(..., description="Project objectives")
    industry: str = Field(..., description="Industry sector")
    team_members: str = Field(..., description="Team members description")
    project_requirements: str = Field(..., description="Project requirements")
# AI_GENERATED_CODE_END 