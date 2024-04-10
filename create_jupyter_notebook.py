import json
import re

def create_jupyter_notebook(markdown_file, output_file):
    with open(markdown_file, 'r', encoding="utf-8") as file:
        markdown_content = file.read()

    cells = []
    chunks = re.split(r'(#+\s.*)', markdown_content)

    for i in range(len(chunks)):
        chunk = chunks[i].strip()
        if chunk:
            if chunk.startswith('#'):
                cells.append({
                    'cell_type': 'markdown',
                    'source': [chunk]
                })
            else:
                code_chunks = re.split(r'```python\n(.*?)```', chunk, flags=re.DOTALL)
                for j in range(len(code_chunks)):
                    if j % 2 == 0 and code_chunks[j].strip():
                        cells.append({
                            'cell_type': 'markdown',
                            'source': code_chunks[j].strip().split('\n')
                        })
                    elif j % 2 == 1:
                        code_lines = code_chunks[j].strip().split('\n')
                        cells.append({
                            'cell_type': 'code',
                            'execution_count': None,
                            'metadata': {},
                            'outputs': [],
                            'source': code_lines
                        })

    notebook = {
        'nbformat': 4,
        'nbformat_minor': 0,
        'metadata': {
            'colab': {
                'provenance': []
            },
            'kernelspec': {
                'name': 'python3',
                'display_name': 'Python 3'
            },
            'language_info': {
                'name': 'python'
            }
        },
        'cells': cells
    }

    with open(output_file, 'w') as file:
        json.dump(notebook, file, indent=2)

# 使用例
markdown_file = 'example/example01.md'
output_file = 'example/example01.ipynb'
create_jupyter_notebook(markdown_file, output_file)