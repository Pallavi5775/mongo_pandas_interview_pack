# ============================================================
# 🧮 PANDAS DATAFRAME QUERY EXAMPLES — 75 EXERCISES
# ============================================================

def pandas_query_examples(df):
    """
    75 Pandas DataFrame manipulation examples:
    - Beginner: filtering, sorting, aggregating
    - Intermediate: groupby, pivot, merging
    - Advanced: window functions, reshaping, feature engineering
    """
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    examples = [
        # ============================================================
        # 🟢 LEVEL 1: BASIC OPERATIONS
        # ============================================================

        # 1. Show first 3 rows
        ("View first rows", df.head(3)),

        # 2. Show data types
        ("Data types", df.dtypes),

        # 3. Shape of dataframe
        ("Shape", df.shape),

        # 4. Column names
        ("Columns", df.columns.tolist()),

        # 5. Describe numeric columns
        ("Describe", df.describe()),

        # 6. Filter: Tech sector only
        ("Filter Tech sector", df[df["sector"] == "Tech"]),

        # 7. Filter VaR > 0.05
        ("High VaR", df[df["VaR"] > 0.05]),

        # 8. Select columns
        ("Select subset", df[["symbol", "price", "VaR"]]),

        # 9. Sort by return descending
        ("Sort by return", df.sort_values("return", ascending=False)),

        # 10. Count missing values
        ("Missing values", df.isna().sum()),

        # 11. Unique sectors
        ("Unique sectors", df["sector"].unique()),

        # 12. Replace missing values
        ("Fill NaN", df.fillna({"sector": "Unknown"})),

        # 13. Drop duplicates
        ("Drop duplicates", df.drop_duplicates()),

        # 14. Rename columns
        ("Rename columns", df.rename(columns={"price": "close_price"})),

        # 15. Add derived column: return %
        ("Add return_pct", df.assign(return_pct=lambda x: x["return"] * 100)),

        # 16. Boolean mask: positive returns
        ("Positive returns", df[df["return"] > 0]),

        # 17. Column statistics
        ("Mean return", df["return"].mean()),

        # 18. Count by sector
        ("Count by sector", df["sector"].value_counts()),

        # 19. Apply lambda function
        ("Squared returns", df["return"].apply(lambda x: x ** 2)),

        # 20. Create new flag
        ("High risk flag", df.assign(high_risk=df["VaR"] > 0.05)),

        # ============================================================
        # 🟡 LEVEL 2: INTERMEDIATE GROUPBY, MERGE, PIVOT
        # ============================================================

        # 21. Group by sector with mean price
        ("Group by sector (mean price)", df.groupby("sector")["price"].mean()),

        # 22. Multiple aggregations
        ("Groupby with agg", df.groupby("sector").agg({"price": "mean", "VaR": "max"})),

        # 23. Group and rename
        ("Rename groupby cols", df.groupby("sector")["return"].agg(avg_return="mean", std_return="std")),

        # 24. Pivot table: avg return by sector
        ("Pivot table", df.pivot_table(values="return", index="sector", aggfunc="mean")),

        # 25. Pivot multi-value
        ("Pivot multi", df.pivot_table(values=["return", "VaR"], index="sector", aggfunc="mean")),

        # 26. Cross-tab: sector vs default_flag
        ("Crosstab", pd.crosstab(df["sector"], df["default_flag"])),

        # 27. Reset index after groupby
        ("Reset index", df.groupby("sector")["return"].mean().reset_index()),

        # 28. Merge two DataFrames
        ("Merge example", pd.merge(df, df[["symbol", "VaR"]], on="symbol", suffixes=("", "_copy"))),

        # 29. Join on index
        ("Join example", df.set_index("symbol").join(df.set_index("symbol"), lsuffix="_1", rsuffix="_2")),

        # 30. Sort by multiple columns
        ("Multi-sort", df.sort_values(["sector", "return"], ascending=[True, False])),

        # 31. Drop column
        ("Drop column", df.drop(columns=["volume"])),

        # 32. Unique value counts
        ("Unique count", df["sector"].nunique()),

        # 33. Replace text
        ("Replace sector", df.replace({"Tech": "Technology"})),

        # 34. Filter with query()
        ("Query syntax", df.query("VaR > 0.04 and sector == 'Tech'")),

        # 35. Use np.where for flag
        ("np.where flag", df.assign(risk_flag=np.where(df["VaR"] > 0.05, "High", "Low"))),

        # 36. Conditional mean
        ("Conditional mean", df[df["sector"] == "Tech"]["return"].mean()),

        # 37. Rank by VaR
        ("Rank VaR", df.assign(VaR_rank=df["VaR"].rank(ascending=False))),

        # 38. Add daily return volatility
        ("Return volatility", df.assign(return_vol=(df["return"] - df["return"].mean()) / df["return"].std())),

        # 39. Correlation matrix
        ("Correlation matrix", df.corr(numeric_only=True)),

        # 40. Groupby and flatten columns
        ("Groupby flatten", df.groupby("sector").agg(["mean", "max"]).reset_index()),

        # ============================================================
        # 🔵 LEVEL 3: ADVANCED ANALYTICS / FEATURE ENGINEERING
        # ============================================================

        # 41. Rolling average of returns (window 2)
        ("Rolling avg returns", df.assign(rolling_avg=df["return"].rolling(2).mean())),

        # 42. Expanding cumulative sum
        ("Cumulative sum", df.assign(cum_sum=df["return"].cumsum())),

        # 43. Daily return volatility (rolling std)
        ("Rolling std", df.assign(rolling_std=df["return"].rolling(3).std())),

        # 44. Shifted lag feature
        ("Lagged returns", df.assign(prev_return=df["return"].shift(1))),

        # 45. Percentage change
        ("Pct change", df.assign(pct_change=df["price"].pct_change())),

        # 46. Normalize numeric columns
        ("Normalization", (df - df.min()) / (df.max() - df.min())),

        # 47. Z-score scaling
        ("Z-score scaling", (df - df.mean()) / df.std()),

        # 48. Apply lambda row-wise
        ("Row-wise operation", df.apply(lambda r: r["price"] * r["return"], axis=1)),

        # 49. Use np.select for multi-condition label
        ("Multi condition", df.assign(label=np.select(
            [df["VaR"] > 0.06, df["VaR"] > 0.04], ["High", "Medium"], default="Low"
        ))),

        # 50. Pivot: VaR by date and symbol
        ("Pivot VaR", df.pivot(index="date", columns="symbol", values="VaR")),

        # 51. Melt wide → long format
        ("Melt DataFrame", df.melt(id_vars=["symbol"], value_vars=["price", "VaR"])),

        # 52. Combine datasets vertically
        ("Concat DataFrames", pd.concat([df, df], axis=0)),

        # 53. MultiIndex groupby (sector, date)
        ("MultiIndex groupby", df.groupby(["sector", "date"])["VaR"].mean()),

        # 54. Resample daily average (time series)
        ("Resample daily", df.set_index("date").resample("D")["price"].mean()),

        # 55. Pivot table with multiple aggfunc
        ("Pivot multi agg", df.pivot_table(index="sector", values=["return", "VaR"], aggfunc=["mean", "std"])),

        # 56. Cumulative product (simulate returns)
        ("Cumulative product", (1 + df["return"]).cumprod()),

        # 57. Combine text columns
        ("Combine text", df.assign(symbol_sector=df["symbol"] + "_" + df["sector"])),

        # 58. Filter top 2 by VaR
        ("Top 2 VaR", df.nlargest(2, "VaR")),

        # 59. Value counts normalized
        ("Normalized counts", df["sector"].value_counts(normalize=True)),

        # 60. Rank by multiple columns
        ("Multi rank", df.assign(rank=df.rank(method="dense", ascending=False)["return"])),

        # 61. Compute Sharpe ratio (mean/std)
        ("Sharpe ratio", df["return"].mean() / df["return"].std()),

        # 62. Outlier detection (z-score > 2)
        ("Outliers", df[np.abs((df["return"] - df["return"].mean()) / df["return"].std()) > 2]),

        # 63. Custom function in apply()
        ("Apply custom func", df["return"].apply(lambda x: "Positive" if x > 0 else "Negative")),

        # 64. Merge summary stats
        ("Merge group means", df.merge(df.groupby("sector")["return"].mean(), on="sector", suffixes=("", "_sector_mean"))),

        # 65. Add percentile rank
        ("Percentile rank", df.assign(percentile=df["VaR"].rank(pct=True))),

        # 66. Quantile-based binning
        ("Quantile bins", pd.qcut(df["VaR"], 3, labels=["Low", "Med", "High"])),

        # 67. Correlation between two variables
        ("Correlation price–VaR", df["price"].corr(df["VaR"])),

        # 68. Groupby cumulative return
        ("Cumulative return per sector", df.groupby("sector")["return"].cumsum()),

        # 69. Expand each row into multiple rows
        ("Repeat rows", df.loc[df.index.repeat(2)]),

        # 70. Pivot → stack → unstack
        ("Stack/unstack", df.pivot_table(values="VaR", index="sector", columns="symbol").stack()),

        # 71. Use eval() for inline math
        ("Eval inline", df.eval("risk_ratio = VaR / return")),

        # 72. Compare columns element-wise
        ("Compare columns", df["price"].gt(df["price"].mean())),

        # 73. Groupby with lambda (custom function)
        ("Lambda groupby", df.groupby("sector")["return"].apply(lambda x: (x > 0.01).mean())),

        # 74. Assign categorical dtype
        ("Categorical dtype", df.assign(sector_cat=df["sector"].astype("category"))),

        # 75. Convert DataFrame to dict
        ("To dict", df.to_dict(orient="records")),
    ]

    return examples
# if __name__ == "__main__":
#     print("🔍 Running 10 random DataFrame queries for demo:")
#     df = pd.DataFrame(sample_docs)
#     examples = pandas_query_examples(df)
#     for i, (desc, res) in enumerate(np.random.choice(examples, 10, replace=False), 1):
#         print(f"\n{i}. {desc}\n{res}\n{'='*60}")