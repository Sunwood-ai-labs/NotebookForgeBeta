
下記のissueについてリポジトリ情報を参照して修正して

# ISSUE 7 : READMEの更新と生成物のリンクの対応

- リポジトリ全体の変更に合わせてREADMEの大幅変更
- SourceSage.py の生成物に合わせて生成物へのリンクをREADMEに記載


下記の内容を盛り込んで、必要に応じて内容を修正して

```
開発前

課題の確認とAIによる自動修正

- GitHubのオープンなissueを取得し、JSONファイルに保存する
- SourceSage.pyを使用して現在のプロジェクトのソースコードとファイル構成を1つのマークダウンファイル(SourceSageAssetsDemo\ISSUES_RESOLVE\ISSUE_7.md)に統合する
- issueデータとSourceSage.pyで生成したマークダウンをClaude AIに入力する
- AIがissueの内容を理解し、現在のソースコードを分析して自動的にissueの修正を提案する
- 提案された修正内容を確認し、必要に応じて手動で調整を行う

開発中

ステージされた変更の確認とコミットメッセージの自動生成

- StagedDiffGeneratorクラスを使用してステージされた差分を取得し、マークダウンファイルに出力する
- ステージされた変更とissueの情報をAIに入力し、適切なコミットメッセージを生成する
- get_issues.pyで取得したissueデータとStagedDiffGeneratorで生成したマークダウン（SourceSageAssetsDemo\STAGED_DIFF.md）をClaude AIに入力する
- AIが既存のissueを考慮してコミットメッセージを自動生成する


リリース後

プロジェクトの統合とドキュメント化

- SourceSage.pyを使用してプロジェクト全体のソースコードとファイル構成をAIが理解しやすい形式で統合する
- プロジェクトのディレクトリ構成とファイル内容を1つのマークダウンファイル（SourceSageAssetsDemo\SourceSage.md）にまとめる
- 不要なファイルやディレクトリを除外するための設定が可能
- 複数のプログラミング言語に対応し、シンタックスハイライト機能を提供
- Gitの変更履歴を自動生成し、ドキュメント化する
- ブランチごとに変更履歴をマークダウンファイルに出力する
- すべてのブランチの変更履歴を1つのファイルに統合する
```


## 補足事項

修正に対するコミットメッセージは日本語にして
正確にstep-by-stepで処理して
issueの番号も記載して

コミットメッセージは下記のフォーマットにして

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

種類は下記を参考にして

例：
  - feat: 新機能
  - fix: バグ修正
  - docs: ドキュメントのみの変更
  - style: コードの動作に影響しない変更（空白、フォーマット、セミコロンの欠落など） 
  - refactor: バグの修正も機能の追加も行わないコードの変更
  - perf: パフォーマンスを向上させるコードの変更
  - test: 欠けているテストの追加や既存のテストの修正
  - chore: ビルドプロセスやドキュメント生成などの補助ツールやライブラリの変更



# リポジトリ情報

# Project: NotebookForge

```plaintext
OS: posix
Directory: /home/maki/Documents/NotebookForge

├─ docs/
├─ script/
│  ├─ activate-notebook-forge.sh
│  ├─ activate-notebook-forge.bat
├─ example/
│  ├─ example01.md
│  ├─ example01.ipynb
├─ app.py
├─ create_jupyter_notebook.py
├─ README.md
```

## .

`app.py`

```python
import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
```

`create_jupyter_notebook.py`

```python
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
```

`README.md`

```markdown
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
<img src="docs/NotebookForge_icon.png" width="100%">
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
```

## docs

## script

`script/activate-notebook-forge.sh`

```bash
#!/bin/bash
conda activate notebook-forge
```

`script/activate-notebook-forge.bat`

```plaintext
conda activate notebook-forge
```

## .github

### .github/workflows

`.github/workflows/run.yaml`

```yaml
name: Sync to Hugging Face hub
on:
  push:
    branches: [main]

  # to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  sync-to-hub:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
          lfs: true
      - name: Push to hub
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: git push --force https://MakiAi:$HF_TOKEN@huggingface.co/spaces/MakiAi/NotebookForgeDemo main
```

## example

`example/example01.md`

```markdown
# Cohere APIのClassifyエンドポイントとは

Classifyエンドポイントは、テキストを事前に定義されたクラス（カテゴリ）に分類するための機能です。いくつかの例を使って、生成モデルからクラス分類器を作成します。内部的には、few-shot分類プロンプトを構築し、それを使って入力テキストを分類します。

## Classifyエンドポイントの使用例

顧客サポートチケットの分類に使えます。例えば、保険会社に届く顧客メールを以下の4つのタイプに自動分類できます。

- 保険証券の詳細を探す
- アカウント設定の変更
- 保険金請求と状況確認
- 保険の解約

これにより、サポートチームは手動で情報を分析してルーティングする手間を省けます。

## Classifyエンドポイントの使い方

### 1. Cohere SDKのインストール

まず、Cohere SDKをインストールします。

```bash
pip install cohere
```

### 2. Cohere clientの設定

次に、Cohere clientを設定します。

```python
import cohere
co = cohere.Client(api_key)
```

### 3. 学習用の例の追加

学習用の例を追加します。各例はテキストとそれに対応するラベル（クラス）で構成されます。各クラスに最低2つの例が必要です。

```python
from cohere.responses.classify import Example

examples=[
  Example("保険証券はどこで見つけられますか？", "保険証券の詳細を探す"),
  Example("保険証券のコピーをダウンロードする方法は？", "保険証券の詳細を探す"),
  ...
]
```

### 4. 分類対象テキストの追加

分類したいテキストを入力として追加します。

```python
inputs=["パスワードを変更したいのですが",
        "私の保険で処方薬はカバーされていますか？"
        ]
```

### 5. Classifyエンドポイントの呼び出し

Classifyエンドポイントを呼び出して分類します。モデルのタイプを指定します（デフォルトはlarge）。

```python
response = co.classify(
    model='large',
    inputs=inputs,
    examples=examples)

print(response.classifications)
```

## レスポンスの例

```json
{
  "results": [
    {
      "text": "パスワードを変更したいのですが",
      "prediction": "アカウント設定の変更",
      "confidence": 0.82,
      ...
    },
    {
      "text":  "私の保険で処方薬はカバーされていますか？",
      "prediction": "保険証券の詳細を探す",
      "confidence": 0.75,
      ...
    }
  ]
}
```

以上が、Cohere APIのClassifyエンドポイントの概要と基本的な使い方です。テキスト分類タスクを手軽に実装できる便利な機能といえるでしょう。
```

`example/example01.ipynb`

```plaintext
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Cohere API\u306eClassify\u30a8\u30f3\u30c9\u30dd\u30a4\u30f3\u30c8\u3068\u306f"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Classify\u30a8\u30f3\u30c9\u30dd\u30a4\u30f3\u30c8\u306f\u3001\u30c6\u30ad\u30b9\u30c8\u3092\u4e8b\u524d\u306b\u5b9a\u7fa9\u3055\u308c\u305f\u30af\u30e9\u30b9\uff08\u30ab\u30c6\u30b4\u30ea\uff09\u306b\u5206\u985e\u3059\u308b\u305f\u3081\u306e\u6a5f\u80fd\u3067\u3059\u3002\u3044\u304f\u3064\u304b\u306e\u4f8b\u3092\u4f7f\u3063\u3066\u3001\u751f\u6210\u30e2\u30c7\u30eb\u304b\u3089\u30af\u30e9\u30b9\u5206\u985e\u5668\u3092\u4f5c\u6210\u3057\u307e\u3059\u3002\u5185\u90e8\u7684\u306b\u306f\u3001few-shot\u5206\u985e\u30d7\u30ed\u30f3\u30d7\u30c8\u3092\u69cb\u7bc9\u3057\u3001\u305d\u308c\u3092\u4f7f\u3063\u3066\u5165\u529b\u30c6\u30ad\u30b9\u30c8\u3092\u5206\u985e\u3057\u307e\u3059\u3002"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Classify\u30a8\u30f3\u30c9\u30dd\u30a4\u30f3\u30c8\u306e\u4f7f\u7528\u4f8b"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\u9867\u5ba2\u30b5\u30dd\u30fc\u30c8\u30c1\u30b1\u30c3\u30c8\u306e\u5206\u985e\u306b\u4f7f\u3048\u307e\u3059\u3002\u4f8b\u3048\u3070\u3001\u4fdd\u967a\u4f1a\u793e\u306b\u5c4a\u304f\u9867\u5ba2\u30e1\u30fc\u30eb\u3092\u4ee5\u4e0b\u306e4\u3064\u306e\u30bf\u30a4\u30d7\u306b\u81ea\u52d5\u5206\u985e\u3067\u304d\u307e\u3059\u3002",
        "",
        "- \u4fdd\u967a\u8a3c\u5238\u306e\u8a73\u7d30\u3092\u63a2\u3059",
        "- \u30a2\u30ab\u30a6\u30f3\u30c8\u8a2d\u5b9a\u306e\u5909\u66f4",
        "- \u4fdd\u967a\u91d1\u8acb\u6c42\u3068\u72b6\u6cc1\u78ba\u8a8d",
        "- \u4fdd\u967a\u306e\u89e3\u7d04",
        "",
        "\u3053\u308c\u306b\u3088\u308a\u3001\u30b5\u30dd\u30fc\u30c8\u30c1\u30fc\u30e0\u306f\u624b\u52d5\u3067\u60c5\u5831\u3092\u5206\u6790\u3057\u3066\u30eb\u30fc\u30c6\u30a3\u30f3\u30b0\u3059\u308b\u624b\u9593\u3092\u7701\u3051\u307e\u3059\u3002"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Classify\u30a8\u30f3\u30c9\u30dd\u30a4\u30f3\u30c8\u306e\u4f7f\u3044\u65b9"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1. Cohere SDK\u306e\u30a4\u30f3\u30b9\u30c8\u30fc\u30eb"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\u307e\u305a\u3001Cohere SDK\u3092\u30a4\u30f3\u30b9\u30c8\u30fc\u30eb\u3057\u307e\u3059\u3002",
        "",
        "```bash",
        "pip install cohere",
        "```"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2. Cohere client\u306e\u8a2d\u5b9a"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\u6b21\u306b\u3001Cohere client\u3092\u8a2d\u5b9a\u3057\u307e\u3059\u3002"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "import cohere",
        "co = cohere.Client(api_key)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3. \u5b66\u7fd2\u7528\u306e\u4f8b\u306e\u8ffd\u52a0"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\u5b66\u7fd2\u7528\u306e\u4f8b\u3092\u8ffd\u52a0\u3057\u307e\u3059\u3002\u5404\u4f8b\u306f\u30c6\u30ad\u30b9\u30c8\u3068\u305d\u308c\u306b\u5bfe\u5fdc\u3059\u308b\u30e9\u30d9\u30eb\uff08\u30af\u30e9\u30b9\uff09\u3067\u69cb\u6210\u3055\u308c\u307e\u3059\u3002\u5404\u30af\u30e9\u30b9\u306b\u6700\u4f4e2\u3064\u306e\u4f8b\u304c\u5fc5\u8981\u3067\u3059\u3002"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "from cohere.responses.classify import Example",
        "",
        "examples=[",
        "  Example(\"\u4fdd\u967a\u8a3c\u5238\u306f\u3069\u3053\u3067\u898b\u3064\u3051\u3089\u308c\u307e\u3059\u304b\uff1f\", \"\u4fdd\u967a\u8a3c\u5238\u306e\u8a73\u7d30\u3092\u63a2\u3059\"),",
        "  Example(\"\u4fdd\u967a\u8a3c\u5238\u306e\u30b3\u30d4\u30fc\u3092\u30c0\u30a6\u30f3\u30ed\u30fc\u30c9\u3059\u308b\u65b9\u6cd5\u306f\uff1f\", \"\u4fdd\u967a\u8a3c\u5238\u306e\u8a73\u7d30\u3092\u63a2\u3059\"),",
        "  ...",
        "]"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4. \u5206\u985e\u5bfe\u8c61\u30c6\u30ad\u30b9\u30c8\u306e\u8ffd\u52a0"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\u5206\u985e\u3057\u305f\u3044\u30c6\u30ad\u30b9\u30c8\u3092\u5165\u529b\u3068\u3057\u3066\u8ffd\u52a0\u3057\u307e\u3059\u3002"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "inputs=[\"\u30d1\u30b9\u30ef\u30fc\u30c9\u3092\u5909\u66f4\u3057\u305f\u3044\u306e\u3067\u3059\u304c\",",
        "        \"\u79c1\u306e\u4fdd\u967a\u3067\u51e6\u65b9\u85ac\u306f\u30ab\u30d0\u30fc\u3055\u308c\u3066\u3044\u307e\u3059\u304b\uff1f\"",
        "        ]"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5. Classify\u30a8\u30f3\u30c9\u30dd\u30a4\u30f3\u30c8\u306e\u547c\u3073\u51fa\u3057"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Classify\u30a8\u30f3\u30c9\u30dd\u30a4\u30f3\u30c8\u3092\u547c\u3073\u51fa\u3057\u3066\u5206\u985e\u3057\u307e\u3059\u3002\u30e2\u30c7\u30eb\u306e\u30bf\u30a4\u30d7\u3092\u6307\u5b9a\u3057\u307e\u3059\uff08\u30c7\u30d5\u30a9\u30eb\u30c8\u306flarge\uff09\u3002"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "response = co.classify(",
        "    model='large',",
        "    inputs=inputs,",
        "    examples=examples)",
        "",
        "print(response.classifications)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## \u30ec\u30b9\u30dd\u30f3\u30b9\u306e\u4f8b"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "```json",
        "{",
        "  \"results\": [",
        "    {",
        "      \"text\": \"\u30d1\u30b9\u30ef\u30fc\u30c9\u3092\u5909\u66f4\u3057\u305f\u3044\u306e\u3067\u3059\u304c\",",
        "      \"prediction\": \"\u30a2\u30ab\u30a6\u30f3\u30c8\u8a2d\u5b9a\u306e\u5909\u66f4\",",
        "      \"confidence\": 0.82,",
        "      ...",
        "    },",
        "    {",
        "      \"text\":  \"\u79c1\u306e\u4fdd\u967a\u3067\u51e6\u65b9\u85ac\u306f\u30ab\u30d0\u30fc\u3055\u308c\u3066\u3044\u307e\u3059\u304b\uff1f\",",
        "      \"prediction\": \"\u4fdd\u967a\u8a3c\u5238\u306e\u8a73\u7d30\u3092\u63a2\u3059\",",
        "      \"confidence\": 0.75,",
        "      ...",
        "    }",
        "  ]",
        "}",
        "```",
        "",
        "\u4ee5\u4e0a\u304c\u3001Cohere API\u306eClassify\u30a8\u30f3\u30c9\u30dd\u30a4\u30f3\u30c8\u306e\u6982\u8981\u3068\u57fa\u672c\u7684\u306a\u4f7f\u3044\u65b9\u3067\u3059\u3002\u30c6\u30ad\u30b9\u30c8\u5206\u985e\u30bf\u30b9\u30af\u3092\u624b\u8efd\u306b\u5b9f\u88c5\u3067\u304d\u308b\u4fbf\u5229\u306a\u6a5f\u80fd\u3068\u3044\u3048\u308b\u3067\u3057\u3087\u3046\u3002"
      ]
    }
  ]
}
```





