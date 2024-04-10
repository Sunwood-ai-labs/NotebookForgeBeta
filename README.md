---
title: NotebookForgeDemo
emoji: 📉
colorFrom: blue
colorTo: pink
sdk: streamlit
sdk_version: 1.33.0
app_file: app.py
pinned: false
license: mit
---

<p align="center">
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/NotebookForge/main/docs/NotebookForge_icon.png" width="100%">
<br>
<h1 align="center">NotebookForge</h1>

</p>


## Introduction
NotebookForgeは、マークダウンファイルをJupyter Notebookに変換するPythonツールです。主な特徴と利点は以下の通りです。

- マークダウンファイル内のPythonコードブロックを適切なセルタイプ（コードセルまたはマークダウンセル）に自動変換
- 通常のテキストはマークダウンセルに変換
- 生成されたNotebookは指定された出力ファイルに保存
- シンプルで使いやすいインターフェース

NotebookForgeを使用することで、マークダウンファイルで書かれたドキュメントやチュートリアルを簡単にJupyter Notebook形式に変換できます。これにより、対話的な実行環境を提供しつつ、マークダウンの読みやすさと書きやすさを維持できます。

>このリポジトリは[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage)を活用しており、リリースノートやREADME、コミットメッセージの9割は[SourceSage](https://github.com/Sunwood-ai-labs/SourceSage) ＋ [claude.ai](https://claude.ai/)で生成しています。

## Demo
NotebookForgeの使用例として、Cohere APIのClassifyエンドポイントについての解説をマークダウンで書き、Jupyter Notebookに変換しました。

- [example/example01.md](example/example01.md): 変換元のマークダウンファイル
- [example/example01.ipynb](example/example01.ipynb): 変換後のJupyter Notebookファイル

このようにNotebookForgeを使うことで、APIドキュメントやチュートリアルを対話的なNotebook形式で提供できます。

## Updates
NotebookForge v0.1.0では以下の機能が追加・改善されました。

- Cohere APIのClassifyエンドポイントについての解説をサンプルに追加
- READMEファイルを追加し、プロジェクトの概要とツールの使い方を記載
- `example`ディレクトリを新設し、サンプルファイルを整理
- サンプルコードのインデントを修正し可読性を向上

今後のリリースでは以下のような機能追加を予定しています。
- Hugging Face のウェブアプリ

## Getting Started
### インストール
NotebookForgeを使用するには、Python 3.11以上が必要です。以下のコマンドでNotebookForge用のConda環境を作成し、アクティベートします。

```bash
conda create -n notebook-forge python=3.11
conda activate notebook-forge
```

### 使用方法
1. コードブロックを含むマークダウンファイルを用意します。（例: `example/example01.md`）

2. 以下のコマンドを実行し、マークダウンファイルをJupyter Notebookに変換します。
   ```bash
   python create_jupyter_notebook.py
   ```

3. 変換後のNotebookファイルが生成されます。（例: `example/example01.ipynb`）

### カスタマイズ
`create_jupyter_notebook.py`スクリプトの以下の部分を変更することで、入出力ファイルのパスをカスタマイズできます。

```python
markdown_file = 'example/example01.md'
output_file = 'example/example01.ipynb'
create_jupyter_notebook(markdown_file, output_file)
```

## Contributing
NotebookForgeへの貢献を歓迎します。バグ報告、機能要望、プルリクエストをお待ちしております。

## License
NotebookForgeはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。

## Acknowledgements

NotebookForgeの開発にあたり、以下のオープンソースプロジェクトを参考にさせていただきました。

- [Jupyter Notebook](https://jupyter.org/)
- [nbformat](https://github.com/jupyter/nbformat)
