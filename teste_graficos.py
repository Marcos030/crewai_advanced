import os
from crewai import Agent, Task, Crew, Process

# Criação da pasta de saída
os.makedirs("output", exist_ok=True)

# Agente que pode executar código
analyst_agent = Agent(
    role="Analista de Dados",
    goal="Analisar dados simples e gerar um gráfico de exemplo",
    backstory=(
        "Você é um analista experiente que sabe visualizar dados. "
        "Sua tarefa é gerar e salvar um gráfico com base em uma série de dados estáticos."
    ),
    allow_code_execution=True,  # Permite execução de código Python
    verbose=True,
    memory=True
)

# Task que pede para gerar o gráfico
generate_plot_task = Task(
    description=(
        "Crie um gráfico simples com matplotlib. "
        "Use os dados [1, 2, 3] para o eixo X e [4, 5, 6] para o eixo Y. "
        "Adicione um título 'Exemplo de gráfico'. "
        "Salve esse gráfico como 'output/meu_grafico.png'. "
        "Garanta que a pasta 'output' exista antes de salvar. "
        "Seu resultado final deve confirmar que o gráfico foi salvo com sucesso."
    ),
    expected_output="Confirmação de que o gráfico foi salvo corretamente em 'output/meu_grafico.png'",
    agent=analyst_agent
)

# Crew com processo sequencial
crew = Crew(
    agents=[analyst_agent],
    tasks=[generate_plot_task],
    process=Process.sequential
)

# Executa o processo
if __name__ == "__main__":
    result = crew.kickoff()
    print("\n✅ Resultado final:\n", result)
