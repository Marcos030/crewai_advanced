# [AI Generated] Data: 19/06/2024
# Descrição: Utilitário para carregar configurações YAML de um diretório
# Gerado por: Cursor AI
# Versão: Python 3.12, PyYAML 6.0.2
# AI_GENERATED_CODE_START
import yaml

def load_configs(config_dir: str):
    files = {
        'agents': f'{config_dir}/agents.yaml',
        'tasks': f'{config_dir}/tasks.yaml'
    }
    configs = {}
    for config_type, file_path in files.items():
        with open(file_path, 'r', encoding='utf-8') as file:
            configs[config_type] = yaml.safe_load(file)
    return configs
# AI_GENERATED_CODE_END 