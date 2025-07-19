# [AI Generated] Data: 19/06/2024
# Descrição: Documentação principal do projeto CrewAI Advanced
# Gerado por: Cursor AI
# Versão: Python 3.12, crewai 0.141.0

# CrewAI Advanced - Projeto Organizado

Este projeto demonstra o uso avançado do CrewAI com uma estrutura organizada e modular para diferentes pipelines de IA.

## 🏗️ Estrutura do Projeto

```
crewai_advanced/
├── config/                          # Configurações YAML
│   ├── content_creator/             # Pipeline de criação de conteúdo
│   │   ├── agents.yaml
│   │   └── tasks.yaml
│   ├── sales_pipeline/              # Pipeline de vendas
│   │   ├── lead_qualification_agents.yaml
│   │   ├── lead_qualification_tasks.yaml
│   │   ├── email_engagement_agents.yaml
│   │   └── email_engagement_tasks.yaml
│   ├── test_train/                  # Pipeline de teste/treino
│   │   ├── agents.yaml
│   │   └── tasks.yaml
│   └── project_progress_report/     # Pipeline de relatórios
│       ├── agents.yaml
│       └── tasks.yaml
├── flows/                           # Implementações de flows
│   ├── sales_pipeline_flow.py
│   └── complex_sales_pipeline_flow.py
├── tools/                           # Ferramentas customizadas
│   └── trello_tools.py
├── files/                           # Arquivos de dados
│   └── support_tickets_data.csv
├── outputs/                         # Saídas dos pipelines
│   ├── sales_pipeline/
│   ├── complex_sales_pipeline/
│   └── test_train/
├── agents_factory.py                # Factory para criação de agentes
├── config_loader.py                 # Carregador de configurações
├── content_creator.py               # Pipeline de criação de conteúdo
├── test_train.py                    # Pipeline de teste/treino
├── sales_pipeline.py                # Pipeline de vendas simples
├── complex_sales_pipeline.py        # Pipeline de vendas complexo
├── project_progress_report.py       # Pipeline de relatórios
├── planing_estimation_allocation.py # Pipeline de planejamento
├── helper.py                        # Utilitários
├── models.py                        # Modelos Pydantic
├── display_utils.py                 # Utilitários de exibição
└── requirements.txt                 # Dependências
```

## 🚀 Pipelines Disponíveis

### 1. **Content Creator** (`content_creator.py`)
Criação automatizada de conteúdo financeiro com análise de mercado.

**Agentes:**
- Monitor de Notícias Financeiras
- Analista de Dados Financeiros
- Criador de Conteúdo
- Agente de Controle de Qualidade

**Como usar:**
```bash
python content_creator.py
```

### 2. **Test/Train** (`test_train.py`)
Pipeline para teste e treinamento com geração de gráficos.

**Agentes:**
- Motor de Sugestões
- Gerador de Relatórios
- Especialista em Gráficos

**Como usar:**
```bash
python test_train.py
```

### 3. **Sales Pipeline** (`sales_pipeline.py`)
Pipeline de qualificação de leads e engajamento por email.

**Agentes:**
- Agente de Dados de Lead
- Agente de Fit Cultural
- Agente de Validação de Scoring
- Especialista em Conteúdo de Email
- Estrategista de Engajamento

**Como usar:**
```bash
python sales_pipeline.py
```

### 4. **Complex Sales Pipeline** (`complex_sales_pipeline.py`)
Versão avançada do pipeline de vendas com flow complexo.

**Como usar:**
```bash
python complex_sales_pipeline.py
```

### 5. **Project Progress Report** (`project_progress_report.py`)
Geração de relatórios de progresso de projetos usando Trello.

**Como usar:**
```bash
python project_progress_report.py
```

### 6. **Planning Estimation Allocation** (`planing_estimation_allocation.py`)
Planejamento, estimativa e alocação de recursos de projetos.

**Como usar:**
```bash
python planing_estimation_allocation.py
```

## 🔧 Configuração

### 1. **Instalar Dependências**
```bash
pip install -r requirements.txt
```

### 2. **Configurar Variáveis de Ambiente**
Criar arquivo `.env` com:
```env
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
GROQ_API_KEY=your_groq_api_key
TRELLO_API_KEY=your_trello_api_key
TRELLO_TOKEN=your_trello_token
```

### 3. **Ativar Ambiente Virtual**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

## 📋 Padrões do Projeto

### 1. **Estrutura de Configuração**
- Configurações em YAML separadas por pipeline
- Agentes e tarefas em arquivos separados
- Uso do `config_loader.py` para carregamento

### 2. **Factory Pattern**
- `agents_factory.py` com funções específicas por pipeline
- Criação padronizada de agentes e tarefas
- Reutilização de código

### 3. **Modelos Pydantic**
- `models.py` com modelos de saída estruturados
- Validação de dados de saída
- Tipagem forte

### 4. **Organização de Saídas**
- Pasta `outputs/` com subpastas por pipeline
- Estrutura consistente de arquivos gerados
- Separação clara de responsabilidades

## 🛠️ Desenvolvimento

### Adicionando Novo Pipeline

1. **Criar configurações YAML:**
   ```
   config/novo_pipeline/
   ├── agents.yaml
   └── tasks.yaml
   ```

2. **Adicionar funções no agents_factory.py:**
   ```python
   def create_novo_pipeline_agents(configs, tools=None):
       # Implementação
   
   def create_novo_pipeline_tasks(configs, agents):
       # Implementação
   ```

3. **Criar script principal:**
   ```python
   # novo_pipeline.py
   from agents_factory import create_novo_pipeline_agents, create_novo_pipeline_tasks
   # Implementação
   ```

### Padrões de Código

- Usar cabeçalhos AI_GENERATED_CODE_START/END
- Documentar data, descrição e versão
- Seguir estrutura de imports padronizada
- Usar logging e tratamento de erros

## 📊 Monitoramento

### Logs
- Verbose mode ativado por padrão
- Logs estruturados por agente e tarefa
- Métricas de performance disponíveis

### Saídas
- Arquivos organizados por pipeline
- Formatação consistente
- Backup automático de resultados

## 🔒 Segurança

- Variáveis de ambiente para chaves API
- Validação de entrada com Pydantic
- Sanitização de dados de saída
- Controle de acesso a ferramentas

## 📈 Performance

- Execução paralela quando possível
- Cache de resultados intermediários
- Otimização de prompts
- Monitoramento de uso de tokens

## 🤝 Contribuição

1. Seguir padrões estabelecidos
2. Documentar mudanças
3. Testar em ambiente local
4. Usar estrutura de branches

## 📞 Suporte

Para dúvidas ou problemas:
- Verificar logs de execução
- Validar configurações YAML
- Testar com dados de exemplo
- Consultar documentação do CrewAI

---

**Versão:** 1.0.0  
**Última Atualização:** 19/06/2024  
**CrewAI Version:** 0.141.0 