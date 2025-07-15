# [AI Generated] Data: 19/06/2024
# Descrição: Utilitário compatível para carregamento de configs por diretório ou lista de arquivos YAML
# Gerado por: Cursor AI
# Versão: Python 3.12, PyYAML 6.0.0
# AI_GENERATED_CODE_START
import os
import yaml

def load_configs(config_input):
    """
    Carrega múltiplos arquivos YAML e retorna um dicionário de configurações.
    Aceita:
      - lista de caminhos de arquivos YAML
      - string de diretório (busca agents.yaml e tasks.yaml)
    """
    configs = {}
    if isinstance(config_input, str):
        # Compatibilidade retroativa: busca padrão agents.yaml e tasks.yaml
        files = {
            'agents': os.path.join(config_input, 'agents.yaml'),
            'tasks': os.path.join(config_input, 'tasks.yaml')
        }
        for key, path in files.items():
            with open(path, 'r', encoding='utf-8') as f:
                configs[key] = yaml.safe_load(f)
    else:
        # Lista de arquivos YAML
        for path in config_input:
            key = os.path.splitext(os.path.basename(path))[0]
            with open(path, 'r', encoding='utf-8') as f:
                configs[key] = yaml.safe_load(f)
    return configs
# AI_GENERATED_CODE_END 