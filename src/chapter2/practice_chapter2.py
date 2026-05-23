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

    return mo, pd


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
    # 11 knock
    """)
    return


@app.cell
def _(pd):
    uriage_data:pd.DataFrame = pd.read_csv("data/uriage.csv")
    uriage_data.head()
    return (uriage_data,)


@app.cell
def _(pd):
    kokyaku_data:pd.DataFrame = pd.read_excel("data/kokyaku_daicho.xlsx")
    kokyaku_data.head()
    return (kokyaku_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 12 knock
    """)
    return


@app.cell
def _(uriage_data: "pd.DataFrame"):
    uriage_data["item_name"].head()
    return


@app.cell
def _(uriage_data: "pd.DataFrame"):
    uriage_data["item_price"].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 13 knock
    """)
    return


@app.cell
def _(pd, uriage_data: "pd.DataFrame"):
    uriage_data["purchase_date"] = pd.to_datetime(uriage_data["purchase_date"])
    uriage_data["purchase_month"] = uriage_data["purchase_date"].dt.strftime("%Y%m")
    result = uriage_data.pivot_table(index="purchase_month", columns="item_name", aggfunc="size", fill_value=0)
    result
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 14 knock
    """)
    return


@app.cell
def _(pd, uriage_data: "pd.DataFrame"):
    print(len(pd.unique(uriage_data["item_name"])))
    return


@app.cell
def _(uriage_data: "pd.DataFrame"):
    uriage_data["item_name"] = uriage_data["item_name"].str.upper()
    uriage_data["item_name"] = uriage_data["item_name"].str.replace(" ", "")
    uriage_data["item_name"] = uriage_data["item_name"].str.replace("　", "")
    uriage_data.sort_values(by="item_name", ascending=True)
    return


@app.cell
def _(pd, uriage_data: "pd.DataFrame"):
    print(pd.unique(uriage_data["item_name"]))
    print(len(pd.unique(uriage_data["item_name"])))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 15 knock
    """)
    return


@app.cell
def _(uriage_data: "pd.DataFrame"):
    uriage_data.isnull().any(axis=0)
    return


@app.cell
def _(uriage_data: "pd.DataFrame"):
    fig_is_null = uriage_data["item_price"].isnull()
    for _trg in list(uriage_data.loc[fig_is_null, "item_name"].unique()):
        price = uriage_data.loc[(~fig_is_null) & (uriage_data["item_name"] == _trg), "item_price"].max()
        uriage_data.loc[(fig_is_null) & (uriage_data["item_name"] == _trg), "item_price"] = price
    uriage_data.head()
    return


@app.cell
def _(uriage_data: "pd.DataFrame"):
    uriage_data.isnull().any(axis=0)
    return


@app.cell
def _(uriage_data: "pd.DataFrame"):
    # check price
    for _trg in list(uriage_data["item_name"].unique()):
        print(_trg + "の最大値：" + str(uriage_data.loc[uriage_data["item_name"] == _trg, "item_price"].max()) \
              + "、最小値：" + str(uriage_data.loc[uriage_data["item_name"] == _trg, "item_price"].min(skipna=True)))
        assert uriage_data.loc[uriage_data["item_name"] == _trg, "item_price"].max() \
              == uriage_data.loc[uriage_data["item_name"] == _trg, "item_price"].min(skipna=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 16 knock
    """)
    return


@app.cell
def _(kokyaku_data: "pd.DataFrame"):
    kokyaku_data["顧客名"].head()
    return


@app.cell
def _(uriage_data: "pd.DataFrame"):
    uriage_data["customer_name"].head()
    return


@app.cell
def _(kokyaku_data: "pd.DataFrame"):
    kokyaku_data["顧客名"] = kokyaku_data["顧客名"].str.replace(" ", "")
    kokyaku_data["顧客名"] = kokyaku_data["顧客名"].str.replace("　", "")
    kokyaku_data["顧客名"].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 17 knock
    """)
    return


@app.cell
def _(kokyaku_data: "pd.DataFrame"):
    fig_is_serial = kokyaku_data["登録日"].astype(str).str.isdigit()
    print(fig_is_serial.sum())
    return (fig_is_serial,)


@app.cell
def _(fig_is_serial, kokyaku_data: "pd.DataFrame", pd):
    fromSerial = pd.to_timedelta(kokyaku_data.loc[fig_is_serial, "登録日"].astype(float) - 2, unit="D") + pd.to_datetime("1900/1/1")
    fromSerial
    return (fromSerial,)


@app.cell
def _(fig_is_serial, kokyaku_data: "pd.DataFrame", pd):
    fromString = pd.to_datetime(kokyaku_data.loc[~fig_is_serial, "登録日"])
    fromString
    return (fromString,)


@app.cell
def _(fromSerial, fromString, kokyaku_data: "pd.DataFrame", pd):
    kokyaku_data["登録日"] = pd.concat([fromSerial, fromString])
    kokyaku_data.head()
    return


@app.cell
def _(kokyaku_data: "pd.DataFrame"):
    kokyaku_data["登録年月"] = kokyaku_data["登録日"].dt.strftime("%Y%m")
    rslt = kokyaku_data.groupby("登録年月").count()["顧客名"]
    print(rslt)
    print(len(kokyaku_data))
    return


@app.cell
def _(kokyaku_data: "pd.DataFrame"):
    _fig_is_serial = kokyaku_data["登録日"].astype(str).str.isdigit()
    print(_fig_is_serial.sum())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 18 knock
    """)
    return


@app.cell
def _(kokyaku_data: "pd.DataFrame", pd, uriage_data: "pd.DataFrame"):
    joined_data = pd.merge(uriage_data, kokyaku_data, left_on="customer_name", right_on="顧客名", how="left")
    joined_data = joined_data.drop("customer_name", axis=1)
    joined_data
    return (joined_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 19 knock
    """)
    return


@app.cell
def _(joined_data):
    print(joined_data.columns)
    return


@app.cell
def _(joined_data):
    dump_data = joined_data[["purchase_date", "purchase_month", "item_name", "item_price", \
                                                                "顧客名", "かな", "地域", "メールアドレス", "登録日"]]
    dump_data
    return (dump_data,)


@app.cell
def _(dump_data):
    dump_data.to_csv("data/dump_data.csv", index=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 20 knock
    """)
    return


@app.cell
def _(pd):
    import_data = pd.read_csv("data/dump_data.csv")
    import_data.head()
    return (import_data,)


@app.cell
def _(import_data):
    byItem = import_data.pivot_table(index="purchase_month", columns="item_name", aggfunc="size", fill_value=0)
    byItem
    return


@app.cell
def _(import_data):
    byPrice = import_data.pivot_table(index="purchase_month", columns="item_name", values="item_price", aggfunc="sum", fill_value=0)
    byPrice
    return


@app.cell
def _(import_data):
    byCustomer = import_data.pivot_table(index="purchase_month", columns="顧客名", aggfunc="size", fill_value=0)
    byCustomer
    return


@app.cell
def _(import_data):
    byRegion = import_data.pivot_table(index="purchase_month", columns="地域", aggfunc="size", fill_value=0)
    byRegion
    return


@app.cell
def _(kokyaku_data: "pd.DataFrame", pd, uriage_data: "pd.DataFrame"):
    away_data = pd.merge(uriage_data, kokyaku_data, left_on="customer_name", right_on="顧客名", how="right")
    away_data[away_data["purchase_date"].isnull()][["顧客名", "メールアドレス", "登録日"]]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
