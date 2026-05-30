import marimo

__generated_with = "0.23.6"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # ファイル構成
    <pre>
    chapter4
    ├── data
    │   ├── customer_join.csv
    │   └── use_log.csv
    └── practice_chapter4.py
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
    from dateutil.relativedelta import relativedelta
    from sklearn.tree import DecisionTreeClassifier
    import sklearn.model_selection
    from sklearn import tree
    import japanize_matplotlib

    return DecisionTreeClassifier, mo, pd, plt, relativedelta, sklearn, tree


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
    | 6   | use_log_months.csv | 第4章で作成した利用履歴を年月/顧客毎に集計したデータ |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 41 knock
    """)
    return


@app.cell
def _(pd):
    customer = pd.read_csv("data/customer_join.csv")
    customer.head()
    return (customer,)


@app.cell
def _(pd):
    uselog_months = pd.read_csv("data/use_log_months.csv")
    uselog_months.head()
    return (uselog_months,)


@app.cell
def _(pd, uselog_months):
    year_months = list(uselog_months["年月"].unique())
    uselog = pd.DataFrame()
    for i in range(1, len(year_months)):
    	_tmp = uselog_months.loc[uselog_months["年月"] == year_months[i]].copy()
    	_tmp.rename(columns={"count": "count_0"}, inplace=True)
    	_tmp_before = uselog_months.loc[uselog_months["年月"] == year_months[i-1]].copy()
    	del _tmp_before["年月"]
    	_tmp_before.rename(columns={"count": "count_1"}, inplace=True)
    	_tmp = pd.merge(_tmp, _tmp_before, on="customer_id", how="left")
    	uselog = pd.concat([uselog, _tmp], ignore_index=True)
    uselog.head()
    return (uselog,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 42 knock
    """)
    return


@app.cell
def _(customer, pd, relativedelta, uselog):
    exit_customer = customer.loc[customer["is_deleted"] == 1].copy()
    exit_customer["exit_date"] = None
    exit_customer["end_date"] = pd.to_datetime(exit_customer["end_date"])

    for _i in exit_customer.index:
    	exit_customer.loc[_i, "exit_date"] = exit_customer.loc[_i, "end_date"] - relativedelta(months=1)

    exit_customer["exit_date"] = pd.to_datetime(exit_customer["exit_date"])
    exit_customer["年月"] = exit_customer["exit_date"].dt.strftime("%Y%m")

    uselog["年月"] = uselog["年月"].astype(str)
    exit_uselog = pd.merge(uselog, exit_customer, on=["customer_id", "年月"], how="left")

    print(len(uselog))
    exit_uselog.head()
    return (exit_uselog,)


@app.cell
def _(exit_uselog):
    exit_uselog_clear = exit_uselog.dropna(subset=["name"])
    print(len(exit_uselog_clear))
    print(len(exit_uselog_clear["customer_id"].unique()))
    exit_uselog_clear.head()
    return (exit_uselog_clear,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 43 knock
    """)
    return


@app.cell
def _(customer, pd, uselog):
    conti_customer = customer.loc[customer["is_deleted"] == 0].copy()
    conti_uselog = pd.merge(uselog,conti_customer,on=["customer_id"], how="left")
    print(len(conti_uselog))
    conti_uselog = conti_uselog.dropna(subset=["name"])
    print(len(conti_uselog))
    return (conti_uselog,)


@app.cell
def _(conti_uselog):
    conti_uselog_sample = conti_uselog.sample(frac=1, random_state=0).reset_index(drop=True)
    conti_uselog_sample = conti_uselog_sample.drop_duplicates(subset=["customer_id"])
    print(len(conti_uselog_sample))
    conti_uselog_sample.head()
    return (conti_uselog_sample,)


@app.cell
def _(conti_uselog_sample, exit_uselog_clear, pd):
    predict_data = pd.concat([conti_uselog_sample,exit_uselog_clear], ignore_index=True)
    print(len(predict_data))
    predict_data.head()
    return (predict_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 44 knock
    """)
    return


@app.cell
def _(pd, predict_data, relativedelta):
    predict_data["period"] = 0
    predict_data["now_date"] = pd.to_datetime(predict_data["年月"], format="%Y%m")
    predict_data["start_date"] = pd.to_datetime(predict_data["start_date"])

    for _i in range(len(predict_data)):
    	_delta = relativedelta(predict_data.loc[_i, "now_date"], predict_data.loc[_i, "start_date"])
    	predict_data.loc[_i, "period"] = int(_delta.years * 12 + _delta.months)
    predict_data.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 45 knock
    """)
    return


@app.cell
def _(predict_data):
    predict_data.isna().sum()
    return


@app.cell
def _(predict_data):
    predict_data_drop1 = predict_data.dropna(subset=["count_1"])
    predict_data_drop1.isna().sum()
    return (predict_data_drop1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 46 knock
    """)
    return


@app.cell
def _(predict_data_drop1):
    target_col = ["campaign_name", "class_name", "gender", "count_1", "routine_flg", "period", "is_deleted"]
    predict_data_target = predict_data_drop1[target_col].copy()
    predict_data_target.head()
    return (predict_data_target,)


@app.cell
def _(pd, predict_data_target):
    predict_data_dummy = pd.get_dummies(predict_data_target, dtype=int)
    predict_data_dummy.head()
    return (predict_data_dummy,)


@app.cell
def _(predict_data_dummy):
    del predict_data_dummy["campaign_name_通常"]
    del predict_data_dummy["class_name_ナイト"]
    del predict_data_dummy["gender_M"]
    predict_data_dummy.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 47 knock
    """)
    return


@app.cell
def _(pd, predict_data_dummy, sklearn):
    exit = predict_data_dummy.loc[predict_data_dummy["is_deleted"] == 1].copy()
    conti = predict_data_dummy.loc[predict_data_dummy["is_deleted"] == 0].sample(n=len(exit), random_state=0).copy()

    X = pd.concat([exit, conti], ignore_index=True)
    y = X["is_deleted"]
    del X["is_deleted"]

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, random_state=0)
    return X, X_test, X_train, y_test, y_train


@app.cell
def _(DecisionTreeClassifier, X_test, X_train, y_train):
    model = DecisionTreeClassifier(random_state=0)
    model.fit(X_train, y_train)
    y_test_pred = model.predict(X_test)
    print(y_test_pred)
    return model, y_test_pred


@app.cell
def _(pd, y_test, y_test_pred):
    result_test = pd.DataFrame({"y_test": y_test, "y_test_pred": y_test_pred})
    result_test.head()
    return (result_test,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 48 knock
    """)
    return


@app.cell
def _(result_test):
    correct = len(result_test.loc[result_test["y_test"] == result_test["y_test_pred"]])
    data_count = len(result_test)
    score_test = correct / data_count
    print(score_test)
    return


@app.cell
def _(X_test, X_train, model, y_test, y_train):
    print(model.score(X_test, y_test))
    print(model.score(X_train, y_train))
    return


@app.cell
def _(DecisionTreeClassifier, X_test, X_train, y_train):
    model2 = DecisionTreeClassifier(random_state=0, max_depth=5)
    model2.fit(X_train, y_train)
    y_test_pred2 = model2.predict(X_test)
    print(y_test_pred2)
    return (model2,)


@app.cell
def _(X_test, X_train, model2, y_test, y_train):
    print(model2.score(X_test, y_test))
    print(model2.score(X_train, y_train))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 49 knock
    """)
    return


@app.cell
def _(X, model2, pd):
    importance = pd.DataFrame({"feature_names": X.columns, "coefficient": model2.feature_importances_})
    importance
    return


@app.cell
def _(X, model2, plt, tree):
    plt.figure(figsize=(20, 8))
    tree.plot_tree(model2, feature_names=X.columns, fontsize=8)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 50 knock
    """)
    return


@app.cell
def _():
    count_1 = 3
    routine_fig = 1
    period = 10
    campaign_name = "入会費無料"
    class_name = "オールタイム"
    gender = "M"
    return campaign_name, class_name, count_1, gender, period, routine_fig


@app.cell
def _(X, campaign_name, class_name, count_1, gender, pd, period, routine_fig):
    if campaign_name == "入会費半額":
    	campaign_name_list = [1, 0]
    elif campaign_name == "入会費無料":
    	campaign_name_list = [0, 1]
    elif campaign_name == "通常":
    	campaign_name_list = [0, 0]
    if class_name == "オールタイム":
    	class_name_list = [1, 0]
    elif class_name == "デイタイム":
    	class_name_list = [0, 1]
    elif class_name == "ナイト":
    	class_name_list = [0, 0]
    if gender == "F":
    	gender_list = [1]
    elif gender == "M":
    	gender_list = [0]

    input_data = [count_1, routine_fig, period]
    input_data.extend(campaign_name_list)
    input_data.extend(class_name_list)
    input_data.extend(gender_list)
    input_data = pd.DataFrame(data=[input_data], columns=X.columns)
    return (input_data,)


@app.cell
def _(input_data, model2):
    print(model2.predict(input_data))
    print(model2.predict_proba(input_data))
    return


if __name__ == "__main__":
    app.run()
