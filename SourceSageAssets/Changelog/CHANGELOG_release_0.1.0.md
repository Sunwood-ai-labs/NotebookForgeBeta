# Changelog

## release/0.1.0

- [ff78e67] - [docs] ドキュメントを追加

READMEファイルを追加し、以下の内容を記載しました。

- プロジェクトの概要
- ツールの使い方
  - コードブロックがあるマークダウンファイルの用意
  - 変換コマンドの実行
  - 出力されたJupyter Notebookファイル

[feat] 入出力ファイルのパスを変更

`create_jupyter_notebook.py`の入出力ファイルのパスを以下のように変更しました。

- 入力ファイル: `example.md` → `example/example01.md`
- 出力ファイル: `example.ipynb` → `example/example01.ipynb`

これにより、サンプルファイルを`example`ディレクトリ内で管理できるようになります。

[chore] 不要なファイルを削除

サンプルとして作成していた以下のファイルを削除しました。

- `example.md`: Cohereに関する説明が書かれたマークダウンファイル
- `example.ipynb`: 上記のマークダウンファイルから変換されたJupyter Notebookファイル

これらのファイルは`example`ディレクトリ内の新しいサンプルファイルに置き換えられるため、不要になりました。 (Maki, 2024-04-10)
- [7263e21] - [feat] Cohereの分類APIのClassifyエンドポイントについて説明

Cohereの分類APIのClassifyエンドポイントの概要と使用例、使い方を説明しました。

具体的には以下の内容を含みます：

- Classifyエンドポイントの概要
 - テキストを事前定義されたクラスに分類する機能
 - 例を使ってfew-shot分類器を作成

- 使用例
 - 顧客サポートチケットを4つのタイプに自動分類
   1. 保険証券の詳細を探す
   2. 請求関連の質問
   3. 保険金請求と状況確認
   4. 保険の解約

- 使い方
 1. Cohere SDKのインストール
 2. Cohere clientの設定
 3. 学習用の例の追加
 4. 分類対象テキストの追加
 5. Classifyエンドポイントの呼び出し

- レスポンスの例（JSONフォーマット） (Maki, 2024-04-10)
- [7cbace3] - [docs] Cohere APIのClassifyエンドポイントについての解説を追加

example.ipynbとexample.mdにCohere APIのClassifyエンドポイントについて以下の内容を追加しました。

- Classifyエンドポイントの概要説明
- 顧客サポートチケットの分類への適用例
- Cohere SDKのインストール方法
- Cohere clientの設定方法
- 学習用の例の追加方法
- 分類対象テキストの追加方法
- Classifyエンドポイントの呼び出し方法
- レスポンスのJSON例

これにより、Classifyエンドポイントを使ったテキスト分類タスクの実装方法が理解しやすくなります。

[style] コードブロックのインデントを修正

example.ipynbのPythonコードブロックのインデントが不揃いだったため、適切にインデントを調整しました。これによりコードの可読性が向上します。 (Maki, 2024-04-10)
- [08727e5] - [feat] Markdownファイルから対話型Jupyter Notebookを生成するPythonスクリプトを作成

- MarkdownファイルからJupyter Notebookを生成するPythonスクリプト`create_jupyter_notebook.py`を作成しました。
- このスクリプトは、Markdownファイル内のPythonコードブロックを認識し、それらを適切なセルタイプ（コードセルまたはマークダウンセル）に変換します。
- Markdownファイル内の通常のテキストはマークダウンセルに変換されます。
- 生成されたJupyter Notebookは、指定された出力ファイルに保存されます。

[docs] サンプルのMarkdownファイルとJupyter Notebookを追加

- `example.md`ファイルを追加しました。このファイルは、Pythonコードブロックを含むサンプルのMarkdownファイルです。
- `example.ipynb`ファイルを追加しました。このファイルは、`create_jupyter_notebook.py`スクリプトを使用して`example.md`から生成されたJupyter Notebookです。

[chore] .gitignoreファイルにSourceSageAssetsディレクトリを追加

- `.gitignore`ファイルに`SourceSageAssets/`ディレクトリを追加しました。このディレクトリは、バージョン管理の対象外となります。

[chore] activate-notebook-forge.batファイルを追加

- `activate-notebook-forge.bat`ファイルを追加しました。このバッチファイルは、`notebook-forge`という名前のConda環境をアクティベートするために使用されます。 (Maki, 2024-04-07)
- [f145003] - Initial commit (Maki, 2024-04-06)
