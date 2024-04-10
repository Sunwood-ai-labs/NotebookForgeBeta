

下記はgitはStageの情報です

issueは掲載しないで

見やすくコミットメッセージにして
章やパラグラフ、箇条書きを多用して見やすくして

コミットメッセージは日本語にして
正確にstep-by-stepで処理して

下記のマークダウンフォーマットで出力して

## フォーマット

```markdown

[種類] 概要

詳細な説明（必要に応じて）

```

## 種類

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


## Stageの情報

```markdown
# Staged Files Diff

## .github/workflows/run.yaml

### 差分:

```diff
@@ -0,0 +1,20 @@
+name: Sync to Hugging Face hub
+on:
+  push:
+    branches: [main]
+
+  # to run this workflow manually from the Actions tab
+  workflow_dispatch:
+
+jobs:
+  sync-to-hub:
+    runs-on: ubuntu-latest
+    steps:
+      - uses: actions/checkout@v3
+        with:
+          fetch-depth: 0
+          lfs: true
+      - name: Push to hub
+        env:
+          HF_TOKEN: ${{ secrets.HF_TOKEN }}
+        run: git push --force https://MakiAi:$HF_TOKEN@huggingface.co/spaces/MakiAi/NotebookForgeDemo main
\ No newline at end of file

```

## README.md

### 差分:

```diff
@@ -1,4 +1,14 @@
-
+---
+title: NotebookForgeDemo
+emoji: 📉
+colorFrom: blue
+colorTo: pink
+sdk: streamlit
+sdk_version: 1.33.0
+app_file: app.py
+pinned: false
+license: mit
+---
 
 <p align="center">
 <img src="docs/NotebookForge_icon.png" width="100%">

```

## app.py

### 差分:

```diff
@@ -0,0 +1,4 @@
+import streamlit as st
+
+x = st.slider('Select a value')
+st.write(x, 'squared is', x * x)
\ No newline at end of file

```



```