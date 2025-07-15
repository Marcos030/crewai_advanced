# [AI Generated] Data: 19/06/2024
# Descrição: display_html_table e display_metrics agora apenas salvam HTML, sem exibir no terminal
# Gerado por: Cursor AI
# Versão: Python 3.12, pandas 2.x
# AI_GENERATED_CODE_START
import pandas as pd
import sys

def display_metrics(token_usage, html_path='usage_metrics.html'):
    df_usage_metrics = pd.DataFrame([token_usage])
    costs = 0.150 * df_usage_metrics['total_tokens'].sum() / 1_000_000
    df_usage_metrics['Custos_totais_R$'] = costs
    html_table = df_usage_metrics.to_html(index=False)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_table)
    print(f'Métricas salvas em: {html_path}')
    return df_usage_metrics

def display_html_table(lead_scoring_result, html_path='lead_scoring_table.html'):
    data = {
        'Nome': lead_scoring_result.personal_info.name,
        'Cargo': lead_scoring_result.personal_info.job_title,
        'Relevância do Cargo': lead_scoring_result.personal_info.role_relevance,
        'Histórico Profissional': lead_scoring_result.personal_info.professional_background,
        'Empresa': lead_scoring_result.company_info.company_name,
        'Setor': lead_scoring_result.company_info.industry,
        'Tamanho da Empresa': lead_scoring_result.company_info.company_size,
        'Receita': lead_scoring_result.company_info.revenue,
        'Presença de Mercado': lead_scoring_result.company_info.market_presence,
        'Score do Lead': lead_scoring_result.lead_score.score,
        'Critérios de Score': ', '.join(lead_scoring_result.lead_score.scoring_criteria),
        'Notas de Validação': lead_scoring_result.lead_score.validation_notes
    }
    df = pd.DataFrame.from_dict(data, orient='index', columns=['Valor'])
    df = df.reset_index().rename(columns={'index': 'Atributo'})
    html_table = df.style.set_properties(**{'text-align': 'left'}) \
                         .format({'Atributo': lambda x: f'<b>{x}</b>'}) \
                         .hide(axis='index') \
                         .to_html()
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_table)
    print(f'Tabela HTML salva em: {html_path}')
    return df

def print_wrapped_text(text, width=80):
    import textwrap
    wrapped_text = textwrap.fill(text, width=width)
    print(wrapped_text)
# AI_GENERATED_CODE_END 