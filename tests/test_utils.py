import os
import tempfile
from app.utils import load_config, save_result

def test_load_config_existing_file():
    # Создаем временный файл конфигурации
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write('{"test": true, "value": 42}')
        temp_path = f.name
    
    try:
        config = load_config(temp_path)
        assert config["test"] is True
        assert config["value"] == 42
    finally:
        os.unlink(temp_path)

def test_load_config_missing_file():
    config = load_config("non_existent_file.json")
    assert config["default"] is True

def test_save_result():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_path = f.name
    
    try:
        save_result("test result", temp_path)
        with open(temp_path, 'r') as f:
            content = f.read()
        assert content == "test result"
    finally:
        os.unlink(temp_path)
