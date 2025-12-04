## ハンズオン概要

このリポジトリは Azure OpenAI + GraphRAG ワークショップ用ハンズオン教材です。受講者は以下の 3 つのノートブックを順番に実行し、インデックス作成から検索・可視化までを体験します。

1. `1.handson.ipynb`: 演習用`handson/`ディレクトリをセットアップし、入力データの取り込み・GraphRAG インデックス作成・主要テーブルの確認を行います。
2. `2.prompt_tuning.ipynb`: 生成タスク向けのプロンプト調整や評価を段階的に試し、より良い応答を得る手順を学びます。
3. `3.visualize.ipynb`: 作成済みインデックスを使い、GraphWidget などでエンティティ/リレーションを可視化し、検索 API で質問応答を実行します。

## 事前準備（セットアップ手順）

以下の手順は、Azure Machine Learning のコンピューティングインスタンスから JupyterLab にアクセスし、**JupyterLab 内のターミナル**で実行することを想定しています。ターミナルを開いたら、次のコマンドを上から順番に実行してハンズオン用の環境を準備します。

1. **レポジトリの取得と移動**

```bash
git clone https://github.com/teshi22/graphrag-workshop.git
cd graphrag-workshop/
```

2. **handson ディレクトリの作成**  
   インデックス対象のテキストを配置するフォルダーを作ります。

```bash
mkdir -p ./handson/input
```

3. **仮想環境の作成と依存ライブラリのインストール**

```bash
python -m venv .venv   # 仮想環境を作成
conda deactivate       # conda をお使いの場合はいったん無効化
conda deactivate       # 二重で有効になっている場合に備えて再度無効化
source .venv/bin/activate
pip install -r requirements.txt
```

4. **サンプルデータの準備**  
   Azure の利用が難しい場合は、リポジトリ同梱の`sample.md`をコピーして使っても構いません。

```bash
cp data/sample.md handson/input/sample.txt
```

5. **GraphRAG プロジェクトの初期化**  
   `handson/`配下に GraphRAG の設定ファイルや出力ディレクトリが作成されます。

```bash
graphrag init --root ./handson
```

5-1. **settings.yaml のコピーとエンドポイントの設定**  
ルートディレクトリにある`settings.yaml`を`handson/`配下にコピーし、自分の Azure OpenAI エンドポイントに書き換えます。

```bash
cp ./settings.yaml ./handson/settings.yaml
```

コピー後、`handson/settings.yaml`を開き、`llm:` → `api_base:` の値を **自分のエンドポイント URL**（例: `https://<your-resource-name>.openai.azure.com/`）に変更してください。

5-2. **.env に自分の API キーを設定**  
同じく`handson/`配下の`.env`ファイルに、自分の Azure OpenAI API キーを設定します。

```env
AZURE_OPENAI_API_KEY=あなたのAPIキー
```

6. **Jupyter から使うカーネルの登録**  
   ノートブックで`.venv`の Python を選べるようにします。

```bash
ipython kernel install --user --name=graphrag-env
```

## 参考ドキュメント

- GraphRAG 公式サイト: https://microsoft.github.io/graphrag/
- GraphRAG GitHub リポジトリ: https://github.com/microsoft/graphrag
