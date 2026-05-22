# 100 Knocks Data Analytics

データ分析 100 本ノックを `uv` と `marimo` で進めるための作業用リポジトリです。  
各章の演習を `src/` 配下に置き、`marimo` notebook として VS Code から編集・実行する前提で構成しています。

## 目的

- `uv` で Python 環境と依存関係を管理する
- `marimo` でコードと Markdown を 1 つの `.py` にまとめる
- VS Code の `marimo` 拡張で notebook 形式のまま編集する

## ディレクトリ構成

```text
src/
├── chapter1/
│   ├── chapter1_practice.py
│   └── data/
│       ├── customer_master.csv
│       ├── item_master.csv
│       ├── transaction_1.csv
│       ├── transaction_2.csv
│       ├── transaction_detail_1.csv
│       └── transaction_detail_2.csv
├── chapter2/
├── chapter3/
├── chapter4/
├── chapter5/
├── chapter6/
├── chapter7/
├── chapter8/
├── chapter9/
└── chapter10/
```

## セットアップ

`uv` が未導入なら先にインストールします。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

このリポジトリで仮想環境を作成し、必要なパッケージを入れます。

```bash
uv venv
uv add marimo pandas matplotlib
```

Python のバージョンは [pyproject.toml](/home/toyuki/Documents/practice/100knocks-data_analytics/pyproject.toml:1) の設定に従います。  
別バージョンを明示したい場合は、先に `uv python install <version>` を実行してください。

## 実行方法

`chapter1` の notebook を起動する例です。

```bash
cd src/chapter1
uv run marimo edit chapter1_practice.py
```

このファイルは `data/` を相対パスで読むため、`src/chapter1` で起動するのが安全です。

## VS Code での使い方

必要な拡張機能:

- `Python`
- `marimo`

手順:

1. VS Code でこのリポジトリを開く
2. `Python: Select Interpreter` で `.venv` を選ぶ
3. [src/chapter1/chapter1_practice.py](/home/toyuki/Documents/practice/100knocks-data_analytics/src/chapter1/chapter1_practice.py:1) を開く
4. `marimo` 拡張で notebook 表示に切り替える

`.vscode/settings.json` を使う場合は、次の設定が実用的です。

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "marimo.uv.path": "uv"
}
```

Windows の場合は `python.defaultInterpreterPath` を `.venv\\Scripts\\python.exe` に変更してください。

## 補足

- `marimo` では、セルをまたいで同じ変数名を再定義できません
- 前のセルの値を使うときは、次のセルの引数で受け取ります
- notebook は `.py` として保存されるため、通常のコードレビューや差分確認がしやすいです

## 今後の進め方

- 章ごとに `chapterN_practice.py` を追加する
- 必要なライブラリは `uv add` で都度管理する
- 実行確認は各章ディレクトリで `uv run marimo edit ...` を使う
