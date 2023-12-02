import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

PROJECT_NAME = 'mlops-project-with-mlflow'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{PROJECT_NAME}/__init__.py',
    f'src/{PROJECT_NAME}/components/__init__.py',
    f'src/{PROJECT_NAME}/utils/__init__.py',
    f'src/{PROJECT_NAME}/utils/common.py',
    f'src/{PROJECT_NAME}/config/__init__.py',
    f'src/{PROJECT_NAME}/config/configuration.py',
    f'src/{PROJECT_NAME}/pipeline/__init__.py',
    f'src/{PROJECT_NAME}/entity/__init__.py',
    f'src/{PROJECT_NAME}/entity/config_entity.py',
    f'src/{PROJECT_NAME}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html',
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Created directory: {file_dir} for the file {file_name}')

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path, 'w') as f:
                f.write('')
                logging.info(f'Created file: {file_path}')
            
    else:
        logging.info(f'File already exists: {file_name}')