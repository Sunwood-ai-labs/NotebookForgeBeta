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

