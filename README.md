## ハンズオン概要

このリポジトリは Azure OpenAI + GraphRAG ワークショップ用ハンズオン教材です。受講者は以下の 3 つのノートブックを順番に実行し、インデックス作成から検索・可視化までを体験します。

1. `1.handson.ipynb`: 演習用`handson/`ディレクトリをセットアップし、入力データの取り込み・GraphRAG インデックス作成・主要テーブルの確認を行います。
2. `2.prompt_tuning.ipynb`: 生成タスク向けのプロンプト調整や評価を段階的に試し、より良い応答を得る手順を学びます。
3. `3.visualize.ipynb`: 作成済みインデックスを使い、GraphWidget などでエンティティ/リレーションを可視化し、検索 API で質問応答を実行します。

## 実行コマンド

```
$ git clone https://github.com/teshi22/graphrag-workshop.git
$ cd graphrag-workshop/
$ mkdir -p ./handson/input
$ python -m venv .venv
$ conda deactivate
$ conda deactivate
$ pip install -r requirements.txt
$ source .venv/bin/activate
($ python scripts/pdf2txt.py -i data/sample.pdf -o handson/input/sample.md)
$ cp data/sample.md handson/input/sample.txt
$ graphrag init --root ./handson
$ ipython kernel install --user --name=graphrag-env
```
