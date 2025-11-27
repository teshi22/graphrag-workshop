実行コマンド

```
$ git clone https://github.com/teshi22/graphrag-workshop.git
$ mkdir -p ./handson/input
$ python -m venv .venv
$ source ..venv/bin/activate
($ python scripts/pdf2txt.py -i data/sample.pdf -o handson/input/sample.md)
$ cp data/sample.md handson/input/sample.txt
$ graphrag init --root ./handson
```
