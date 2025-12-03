実行コマンド

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
