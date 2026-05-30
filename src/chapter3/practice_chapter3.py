import marimo

__generated_with = "0.23.6"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # ファイル構成
    <pre>
    chapter3
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

    return mo, pd, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # データ一覧

    | No. | file name                | contents                                 |
    | --- | ------------------------ | ---------------------------------------- |
    | 1   | use_log.csv | ジムの利用履歴データ |
    | 2   | customer_master.csv | 2019年3月末時点での会員データ |
    | 3   | class_master.csv | 会員区分データ（オールタイム、デイタイム等） |
    | 4   | campaign_master.csv | キャンペーン区分データ（入会費無料等） |
    | 5   | customer_join.csv | 第3章で作成した利用履歴を含んだ顧客データ |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 31 knock
    """)
    return


@app.cell
def _(pd):
    uselog = pd.read_csv("data/use_log.csv")
    uselog.isnull().sum()
    return (uselog,)


@app.cell
def _(pd):
    customer = pd.read_csv("data/customer_join.csv")
    customer.isnull().sum()
    return (customer,)


@app.cell
def _(customer):
    customer.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 32 knock
    """)
    return


@app.cell
def _(customer):
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler

    customer_clustering = customer[["mean", "median", "max", "min", "membership_period"]]
    sc = StandardScaler()
    customer_clustering_sc = sc.fit_transform(customer_clustering)
    kmeans = KMeans(n_clusters=4, random_state=0)
    clusters = kmeans.fit(customer_clustering_sc)
    customer_clustering = customer_clustering.assign(cluster=clusters.labels_)

    print(customer_clustering["cluster"].unique())
    customer_clustering.head()
    return customer_clustering, customer_clustering_sc


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 33 knock
    """)
    return


@app.cell
def _(customer_clustering):
    customer_clustering.columns = ["月内平均値", "月内中央値", "月内最大値", "月内最小値", "会員期間", "cluster"]
    customer_clustering.groupby("cluster").count()
    return


@app.cell
def _(customer_clustering):
    customer_clustering.groupby("cluster").mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 34 knock
    """)
    return


@app.cell
def _(customer_clustering, customer_clustering_sc, pd):
    from sklearn.decomposition import PCA

    _X = customer_clustering_sc
    pca = PCA(n_components=2)
    pca.fit(_X)
    X_pca = pca.transform(_X)
    pca_df = pd.DataFrame(X_pca)
    pca_df["cluster"] = customer_clustering["cluster"]
    return (pca_df,)


@app.cell
def _(customer_clustering, pca_df, plt):
    for _i in sorted(customer_clustering["cluster"].unique()):
        _tmp = pca_df.loc[pca_df["cluster"] == _i]
        plt.scatter(_tmp[0], _tmp[1], label=_i)
    plt.legend()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 35 knock
    """)
    return


@app.cell
def _(customer, customer_clustering, pd):
    customer_clustering_join = pd.concat([customer_clustering, customer], axis=1)
    customer_clustering_join.groupby(["cluster", "is_deleted"], as_index=False).count()[["cluster", "is_deleted", "customer_id"]]
    return (customer_clustering_join,)


@app.cell
def _(customer_clustering_join):
    customer_clustering_join.groupby(["cluster", "routine_flg"], as_index=False).count()[["cluster", "routine_flg", "customer_id"]]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 36 knock
    """)
    return


@app.cell
def _(pd, uselog):
    uselog["usedate"] = pd.to_datetime(uselog["usedate"])
    uselog["年月"] = uselog["usedate"].dt.strftime("%Y%m")
    uselog_months = uselog.groupby(["年月", "customer_id"], as_index=False).count()
    uselog_months.rename(columns={"log_id": "count"}, inplace=True)
    del uselog_months["usedate"]
    uselog_months.head()
    return (uselog_months,)


@app.cell
def _(pd, uselog_months):
    year_months = list(uselog_months["年月"].unique())
    predict_data = pd.DataFrame()
    for _i in range(6, len(year_months)):
        _tmp = uselog_months.loc[uselog_months["年月"]==year_months[_i]].copy()
        _tmp.rename(columns={"count":"count_pred"}, inplace=True)
        for _j in range(1, 7):
            _tmp_before = uselog_months.loc[uselog_months["年月"]==year_months[_i-_j]].copy()
            del _tmp_before["年月"]
            _tmp_before.rename(columns={"count":"count_{}".format(_j-1)}, inplace=True)
            _tmp = pd.merge(_tmp, _tmp_before, on="customer_id", how="left")
        predict_data = pd.concat([predict_data, _tmp], ignore_index=True)
    # predict_data.head()

    predict_data = predict_data.dropna()
    predict_data = predict_data.reset_index(drop=True)
    predict_data.head()
    return (predict_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 37 knock
    """)
    return


@app.cell
def _(customer, pd, predict_data):
    predict_data_join = pd.merge(predict_data,customer[["customer_id", "start_date"]], on="customer_id", how="left")
    predict_data_join.head()
    return (predict_data_join,)


@app.cell
def _(pd, predict_data_join):
    from dateutil.relativedelta import relativedelta

    predict_data_join["now_date"] = pd.to_datetime(predict_data_join["年月"], format="%Y%m")
    predict_data_join["start_date"] = pd.to_datetime(predict_data_join["start_date"])
    predict_data_join["period"] = None
    for _i in range(len(predict_data_join)):
    	delta = relativedelta(predict_data_join.loc[_i, "now_date"], predict_data_join.loc[_i, "start_date"])
    	predict_data_join.loc[_i, "period"] = delta.years * 12 + delta.months
    predict_data_join.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 38 knock
    """)
    return


@app.cell
def _(pd, predict_data_join):
    import sklearn
    from sklearn import linear_model

    predict_data_join_newcus = predict_data_join.loc[predict_data_join["start_date"] >= pd.to_datetime("20180401")]
    model = linear_model.LinearRegression()
    _X = predict_data_join_newcus[["count_0", "count_1", "count_2", "count_3", "count_4", "count_5", "period"]]
    _y = predict_data_join_newcus["count_pred"]

    _X_train, _X_test, _y_train, _y_test = sklearn.model_selection.train_test_split(_X, _y, random_state=0)
    model.fit(_X_train, _y_train)
    print(model.score(_X_train, _y_train))
    print(model.score(_X_test, _y_test))
    coef = pd.DataFrame({
    	"feature": _X.columns,
    	"coef": model.coef_
    })
    return coef, model


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 39 knock
    """)
    return


@app.cell
def _(coef):
    coef
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 40 knock
    """)
    return


@app.cell
def _(model, pd):
    x1 = [3,4,4,6,8,7,8]
    x2 = [2,2,3,3,4,6,8]
    x_pred = pd.DataFrame(data=[x1, x2], columns=["count_0", "count_1", "count_2", "count_3", "count_4", "count_5", "period"])
    model.predict(x_pred)
    return


@app.cell
def _(uselog_months):
    uselog_months.to_csv("data/use_log_months.csv", index=False)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
