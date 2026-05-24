import marimo

__generated_with = "0.23.6"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # ファイル構成
    <pre>
    chapter2
    ├── data
    │   ├── dump_data.csv
    │   ├── kokyaku_daicho.xlsx
    │   └── uriage.csv
    └── practice_chapter2.py
    </pre>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # import
    """)
    return


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # データ一覧

    | No. | file name                | contents                                 |
    | --- | ------------------------ | ---------------------------------------- |
    | 1   | uriage.csv               | 売上履歴                                   |
    | 2   | kokyaku_daicho.xlsx      | 手入力で店舗が管理している顧客台帳           　 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 31 knock
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 32 knock
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 33 knock
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 34 knock
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 35 knock
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 36 knock
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 37 knock
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 38 knock
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 39 knock
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 40 knock
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
