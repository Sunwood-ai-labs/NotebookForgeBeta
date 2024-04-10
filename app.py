import streamlit as st
from create_jupyter_notebook import create_jupyter_notebook
import base64

def download_notebook(notebook_file):
    with open(notebook_file, 'rb') as file:
        notebook_data = file.read()
    b64 = base64.b64encode(notebook_data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{notebook_file}">ノートブックをダウンロード</a>'
    return href

def main():

    st.markdown('''
    
<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/NotebookForgeBeta/main/docs/NotebookForge_icon.jpg" width="50%">
<br>
<h1 align="center">NotebookForge</h1>
<h3 align="center">～Markdown to Jupyter Notebook Converter～</h3>

</p>

    ''', unsafe_allow_html=True)
    markdown_content = st.text_area('Markdownファイルの内容を貼り付けてください', height=400)
    
    if st.button('変換'):
        if markdown_content.strip():
            with open('temp_markdown.md', 'w', encoding='utf-8') as file:
                file.write(markdown_content)
            
            output_file = 'output_notebook.ipynb'
            create_jupyter_notebook('temp_markdown.md', output_file)
            
            st.success('ノートブックが生成されました。')
            st.markdown(download_notebook(output_file), unsafe_allow_html=True)
        else:
            st.warning('Markdownファイルの内容を入力してください。')

if __name__ == '__main__':
    main()