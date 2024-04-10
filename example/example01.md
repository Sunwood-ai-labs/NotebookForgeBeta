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