# [AI Generated] Data: 19/06/2024
# Descrição: Modelos Pydantic centralizados e incrementais para todo o projeto
# Gerado por: Cursor AI
# Versão: Python 3.12, pydantic 2.x
# AI_GENERATED_CODE_START
"""
Este módulo centraliza todos os modelos Pydantic do projeto.
Sempre adicione novas classes aqui, sem sobrescrever as existentes.
"""
from pydantic import BaseModel, Field
from typing import Optional, List

# --- Modelos para planejamento, estimativa e alocação (exemplo) ---
class TaskEstimate(BaseModel):
    """Modelo para estimativa de tarefa."""
    task_name: str = Field(..., description="Nome da tarefa")
    estimated_time_hours: float = Field(..., description="Tempo estimado em horas")
    required_resources: List[str] = Field(..., description="Recursos necessários")

class Milestone(BaseModel):
    """Modelo para marco do projeto."""
    milestone_name: str = Field(..., description="Nome do marco")
    tasks: List[str] = Field(..., description="IDs das tarefas associadas")

class ProjectPlan(BaseModel):
    """Modelo para plano completo do projeto."""
    tasks: List[TaskEstimate] = Field(..., description="Lista de tarefas")
    milestones: List[Milestone] = Field(..., description="Lista de marcos")

class ProjectInputs(BaseModel):
    """Modelo para entradas do projeto."""
    project_type: str = Field(..., description="Tipo de projeto")
    project_objectives: str = Field(..., description="Objetivos do projeto")
    industry: str = Field(..., description="Setor")
    team_members: str = Field(..., description="Membros da equipe")
    project_requirements: str = Field(..., description="Requisitos do projeto")

# --- Modelos para pipeline de vendas (Lead Scoring) ---
class LeadPersonalInfo(BaseModel):
    name: str = Field(..., description="Nome completo do lead.")
    job_title: str = Field(..., description="Cargo do lead.")
    role_relevance: int = Field(..., ge=0, le=10, description="Relevância do cargo para decisão (0-10).")
    professional_background: Optional[str] = Field(..., description="Resumo do histórico profissional do lead.")

class CompanyInfo(BaseModel):
    company_name: str = Field(..., description="Nome da empresa do lead.")
    industry: str = Field(..., description="Setor de atuação da empresa.")
    company_size: int = Field(..., description="Tamanho da empresa (nº de funcionários).")
    revenue: Optional[float] = Field(None, description="Receita anual da empresa, se disponível.")
    market_presence: int = Field(..., ge=0, le=10, description="Presença de mercado da empresa (0-10).")

class LeadScore(BaseModel):
    score: int = Field(..., ge=0, le=100, description="Score final do lead (0-100).")
    scoring_criteria: List[str] = Field(..., description="Critérios usados para o score.")
    validation_notes: Optional[str] = Field(None, description="Notas sobre a validação do score.")

class LeadScoringResult(BaseModel):
    personal_info: LeadPersonalInfo = Field(..., description="Informações pessoais do lead.")
    company_info: CompanyInfo = Field(..., description="Informações da empresa do lead.")
    lead_score: LeadScore = Field(..., description="Score calculado e informações relacionadas ao lead.")

# Adicione novos modelos abaixo desta linha, mantendo compatibilidade incremental
# AI_GENERATED_CODE_END 