# Author: Luca Soltero
# Email: lsoltero@usc.edu
# Course: Introduction to Econometrics (ECON 318) USC

import re
import numpy as np
import pandas as pd
import statsmodels.formula.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


def dataFrame():
    contains = lambda text: bool(re.search(r'#\b(fyp|foryou|fy|foryoupage)\b', text.lower().replace('[^\w\s]', '')))
    path = "/Data/tiktok_data.xlsx"
    df = pd.read_excel(path)
    df = df.drop(df[df["videoMeta/duration"] == 0].index)
    # df = df.drop(df[df["videoMeta/duration"] > 100].index)
    df["isVerified"] = df["authorMeta/verified"]
    df["isOrigSound"] = df["musicMeta/musicOriginal"]
    df["duration"] = df["videoMeta/duration"].apply(np.log)
    df["dur"] = df["videoMeta/duration"]
    df["containsFyp"] = df["text"].apply(contains)
    df["engagement"] = (((df["commentCount"] + df["shareCount"] + df["diggCount"]) / (df["playCount"])) * 100)
    return df


def main():
    df = dataFrame()
    # -------  MODEL -----------
    # print("OLS Model")
    model = sm.ols(formula="engagement ~ duration + isVerified + isOrigSound + isPositive + containsFyp", data=df).fit()

    print(model.summary())

    # print("BRAUCSH PAGAN TEST")

    # ---------- BRAUCSH PAGAN Test ----------
    df["residuals"] = model.resid
    df["residualsSqrd"] = df["residuals"] * df["residuals"]
    BP_test = sm.ols(formula="residualsSqrd ~ duration + isVerified + isOrigSound + isPositive + containsFyp",
                     data=df).fit()

    # print(BP_test.summary())

    # -- ADJUSTED MODEL --
    adjustedModel = sm.ols(formula="engagement ~ duration + isVerified + isOrigSound + "
                                   "isPositive + containsFyp", data=df).fit(cov_type="HC0")
    print(adjustedModel.summary())

    # -- TESTING  FOR MULTICOLINEARITY---
    vif = pd.DataFrame()
    vif["variables"] = adjustedModel.model.exog_names
    vif["VIF"] = [variance_inflation_factor(adjustedModel.model.exog, i) for i in
                  range(adjustedModel.model.exog.shape[1])]
    print(vif)


if __name__ == '__main__':
    main()