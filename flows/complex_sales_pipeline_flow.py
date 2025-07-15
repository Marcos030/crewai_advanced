# [AI Generated] Data: 19/06/2024
# Descrição: Ajuste do decorador @router para compatibilidade com crewai 0.141.0 (sem argumento 'paths')
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai 0.141.0
# AI_GENERATED_CODE_START
from crewai import Flow
from crewai.flow.flow import listen, start, and_, or_, router

class SalesPipeline(Flow):
    def __init__(self, lead_agents, lead_tasks, email_agents, email_tasks):
        super().__init__()
        self.lead_agents = lead_agents
        self.lead_tasks = lead_tasks
        self.email_agents = email_agents
        self.email_tasks = email_tasks

    @start()
    def fetch_leads(self):
        # Mock: puxar leads de um banco de dados
        leads = [
            {
                "lead_data": {
                    "name": "João Moura",
                    "job_title": "Director of Engineering",
                    "company": "Clearbit",
                    "email": "joao@clearbit.com",
                    "use_case": "Using AI Agent to do better data enrichment."
                },
            },
        ]
        return leads

    @listen(fetch_leads)
    def score_leads(self, leads):
        # O contexto das tasks é preenchido aqui
        self.lead_tasks['scoring_validation_task'].context = [
            self.lead_tasks['lead_data_task'],
            self.lead_tasks['cultural_fit_task']
        ]
        crew = self._make_lead_scoring_crew()
        scores = crew.kickoff_for_each(leads)
        self.state["score_crews_results"] = scores
        return scores

    @listen(score_leads)
    def store_leads_score(self, scores):
        # Aqui armazenaria os scores no banco de dados
        return scores

    @listen(score_leads)
    def filter_leads(self, scores):
        return [score for score in scores if score['lead_score'].score > 70]

    @listen(and_(filter_leads, store_leads_score))
    def log_leads(self, leads):
        print(f"Leads: {leads}")
        return leads

    @router(filter_leads)
    def count_leads(self, scores):
        if len(scores) > 10:
            return 'high'
        elif len(scores) > 5:
            return 'medium'
        else:
            return 'low'

    @listen('high')
    def store_in_salesforce(self, leads):
        # Aqui armazenaria no Salesforce
        return leads

    @listen('medium')
    def send_to_sales_team(self, leads):
        # Aqui enviaria para o time de vendas
        return leads

    @listen('low')
    def write_email(self, leads):
        scored_leads = [lead.to_dict() for lead in leads]
        crew = self._make_email_writing_crew()
        emails = crew.kickoff_for_each(scored_leads)
        return emails

    @listen(write_email)
    def send_email(self, emails):
        # Aqui enviaria os emails
        return emails

    def _make_lead_scoring_crew(self):
        from crewai import Crew
        return Crew(
            agents=[
                self.lead_agents['lead_data_agent'],
                self.lead_agents['cultural_fit_agent'],
                self.lead_agents['scoring_validation_agent']
            ],
            tasks=[
                self.lead_tasks['lead_data_task'],
                self.lead_tasks['cultural_fit_task'],
                self.lead_tasks['scoring_validation_task']
            ],
            verbose=True
        )

    def _make_email_writing_crew(self):
        from crewai import Crew
        return Crew(
            agents=[
                self.email_agents['email_content_specialist'],
                self.email_agents['engagement_strategist']
            ],
            tasks=[
                self.email_tasks['email_drafting'],
                self.email_tasks['engagement_optimization']
            ],
            verbose=True
        )
# AI_GENERATED_CODE_END