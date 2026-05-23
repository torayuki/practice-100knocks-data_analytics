import marimo

__generated_with = "0.23.6"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # ファイル構成
    <pre>
    chapter1
    ├── chapter1_practice.py
    └── data
        ├── customer_master.csv
        ├── item_master.csv
        ├── transaction_1.csv
        ├── transaction_2.csv
        ├── transaction_detail_1.csv
        └── transaction_detail_2.csv
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

    return mo, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # データ一覧

    | No. | file name                | contents                                 |
    | --- | ------------------------ | ---------------------------------------- |
    | 1   | customer_master.csv      | 顧客データ、名前、性別等                     |
    | 2   | item_master.csv          | 取り扱っている商品データ、商品名、価格等        |
    | 3-1 | transaction_1.csv        | 購入明細データ                             |
    | 3-2 | transaction_2.csv        | 3-1の続き。                               |
    | 4-1 | transaction_detail_1.csv | 購入明細の詳細データ                        |
    | 4-2 | transaction_detail_2.csv | 4-1の続き                                 |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 1 knock
    """)
    return


@app.cell
def _(pd):
    customer_master: pd.DataFrame = pd.read_csv('data/customer_master.csv')
    item_master: pd.DataFrame = pd.read_csv('data/item_master.csv')
    transaction_1: pd.DataFrame = pd.read_csv('data/transaction_1.csv')
    transaction_2: pd.DataFrame = pd.read_csv('data/transaction_2.csv')
    transaction_detail_1: pd.DataFrame = pd.read_csv('data/transaction_detail_1.csv')
    transaction_detail_2: pd.DataFrame = pd.read_csv('data/transaction_detail_2.csv')
    return (
        customer_master,
        item_master,
        transaction_1,
        transaction_2,
        transaction_detail_1,
        transaction_detail_2,
    )


@app.cell
def _(customer_master: "pd.DataFrame"):
    customer_master.head()
    return


@app.cell
def _(item_master: "pd.DataFrame"):
    item_master.head()
    return


@app.cell
def _(transaction_1: "pd.DataFrame"):
    transaction_1.head()
    return


@app.cell
def _(transaction_2: "pd.DataFrame"):
    transaction_2.head()
    return


@app.cell
def _(transaction_detail_1: "pd.DataFrame"):
    transaction_detail_1.head()
    return


@app.cell
def _(transaction_detail_2: "pd.DataFrame"):
    transaction_detail_2.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 2 knock
    """)
    return


@app.cell
def _(pd, transaction_1: "pd.DataFrame", transaction_2: "pd.DataFrame"):
    transaction: pd.DataFrame = pd.concat([transaction_1, transaction_2], ignore_index=True)
    assert len(transaction) == len(transaction_1) + len(transaction_2)
    transaction.head()
    return (transaction,)


@app.cell
def _(
    transaction: "pd.DataFrame",
    transaction_1: "pd.DataFrame",
    transaction_2: "pd.DataFrame",
):
    print(len(transaction_1))
    print(len(transaction_2))
    print(len(transaction))
    return


@app.cell
def _(
    pd,
    transaction_detail_1: "pd.DataFrame",
    transaction_detail_2: "pd.DataFrame",
):
    transaction_detail : pd.DataFrame = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
    assert len(transaction_detail) == len(transaction_detail_1) + len(transaction_detail_2)
    transaction_detail.head()
    return (transaction_detail,)


@app.cell
def _(
    transaction_detail: "pd.DataFrame",
    transaction_detail_1: "pd.DataFrame",
    transaction_detail_2: "pd.DataFrame",
):
    print(len(transaction_detail_1))
    print(len(transaction_detail_2))
    print(len(transaction_detail))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 3&4 knock
    """)
    return


@app.cell
def _(
    customer_master: "pd.DataFrame",
    item_master: "pd.DataFrame",
    pd,
    transaction: "pd.DataFrame",
    transaction_detail: "pd.DataFrame",
):
    joined_data: pd.DataFrame = pd.merge(transaction_detail, transaction[["transaction_id", "payment_date", "customer_id"]], on="transaction_id", how="left")
    assert len(joined_data) == len(transaction_detail)
    joined_data = pd.merge(joined_data, customer_master, on="customer_id", how="left")
    assert len(joined_data) == len(transaction_detail)
    joined_data = pd.merge(joined_data, item_master, on="item_id", how="left")
    assert len(joined_data) == len(transaction_detail)
    joined_data.head()
    return (joined_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 5 knock
    """)
    return


@app.cell
def _(joined_data: "pd.DataFrame"):
    joined_data["price"] = joined_data["quantity"] * joined_data["item_price"]
    joined_data[["quantity", "item_price", "price"]].head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 6 knock
    """)
    return


@app.cell
def _(joined_data: "pd.DataFrame", transaction: "pd.DataFrame"):
    print(joined_data["price"].sum())
    print(transaction["price"].sum())
    print(joined_data["price"].sum() == transaction["price"].sum())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 7 knock
    """)
    return


@app.cell
def _(joined_data: "pd.DataFrame"):
    joined_data.isnull().sum()
    return


@app.cell
def _(joined_data: "pd.DataFrame"):
    joined_data.describe()
    return


@app.cell
def _(joined_data: "pd.DataFrame"):
    print(joined_data["payment_date"].min())
    print(joined_data["payment_date"].max())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 8 knock
    """)
    return


@app.cell
def _(joined_data: "pd.DataFrame"):
    joined_data.dtypes
    return


@app.cell
def _(joined_data: "pd.DataFrame", pd):
    joined_data["payment_date"] = pd.to_datetime(joined_data["payment_date"])
    joined_data["payment_month"] = joined_data["payment_date"].dt.strftime("%Y%m")
    joined_data[["payment_date", "payment_month"]].head()
    return


@app.cell
def _(joined_data: "pd.DataFrame"):
    joined_data.groupby("payment_month")[["price"]].sum()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # knock 9
    """)
    return


@app.cell
def _(joined_data: "pd.DataFrame"):
    joined_data.groupby(["payment_month", "item_name"])[["price", "quantity"]].sum()
    return


@app.cell
def _(joined_data: "pd.DataFrame", pd):
    pd.pivot_table(joined_data, index="item_name", columns="payment_month", values=["price", "quantity"], aggfunc="sum")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 10 knock
    """)
    return


@app.cell
def _(joined_data: "pd.DataFrame", pd):
    graph_data:pd.DataFrame = pd.pivot_table(joined_data, index="payment_month", columns="item_name", values="price", aggfunc="sum")
    graph_data.head()
    return (graph_data,)


@app.cell
def _(graph_data: "pd.DataFrame", plt):
    # single graph
    plt.plot(graph_data.index, graph_data["PC-A"], label="PC-A")
    plt.plot(graph_data.index, graph_data["PC-B"], label="PC-B")
    plt.plot(graph_data.index, graph_data["PC-C"], label="PC-C")
    plt.plot(graph_data.index, graph_data["PC-D"], label="PC-D")
    plt.plot(graph_data.index, graph_data["PC-E"], label="PC-E")

    plt.xlabel("Payment Month")
    plt.ylabel("Total Price")
    plt.title("Sales of PC-A")
    plt.legend()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
