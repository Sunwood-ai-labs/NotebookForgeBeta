import streamlit as st
from create_jupyter_notebook import create_jupyter_notebook
import base64
import re
import jupytext

def load_markdown(file_path):
    with open(file_path, encoding="utf8") as f:
        return f.read()

def display_front_page():
    html_front = load_markdown('docs/page_front.md')
    st.markdown(f"{html_front}", unsafe_allow_html=True)

def download_file(file_path, file_name):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    b64 = base64.b64encode(file_data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">{file_name}をダウンロード</a>'
    return href

def get_first_heading(markdown_content):
    match = re.search(r'^#\s*(.*)', markdown_content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    else:
        return 'output'

def main():
    display_front_page()

    markdown_content = st.text_area('Markdownファイルの内容を貼り付けてください', height=400)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button('Jupyter Notebookに変換'):
            if markdown_content.strip():
                with open('temp_markdown.md', 'w', encoding='utf-8') as file:
                    file.write(markdown_content)
                            
                output_file = f"{get_first_heading(markdown_content)}.ipynb"
                create_jupyter_notebook('temp_markdown.md', output_file)
                
                st.success('Jupyter Notebookが生成されました。')
                st.markdown(download_file(output_file, output_file), unsafe_allow_html=True)
            else:
                st.warning('Markdownファイルの内容を入力してください。')

    with col2:
        if st.button('Jupytext形式に変換'):
            if markdown_content.strip():
                notebook = jupytext.reads(markdown_content, fmt='md')
                output_file = f"{get_first_heading(markdown_content)}.py"
                
                with open(output_file, 'w', encoding='utf-8') as file:
                    jupytext.write(notebook, file, fmt='py:percent')
                
                st.success('Jupytext形式のファイルが生成されました。')
                st.markdown(download_file(output_file, output_file), unsafe_allow_html=True)
            else:
                st.warning('Markdownファイルの内容を入力してください。')

if __name__ == '__main__':
    main()
