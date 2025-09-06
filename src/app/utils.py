import json

def load_config(config_path):
    """Загрузка конфигурации из JSON файла"""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"default": True}
    
def save_result(result, output_path):
    """Сохранение результата в файл"""
    with open(output_path, 'w') as f:
        f.write(str(result))
