
import random
import time

# Simulated INTERVIEW_MAP subset for demo
INTERVIEW_MAP = [
    # ====================================================
    # 🟢 LEVEL 1 — FOUNDATIONS
    # ====================================================
    {"Category": "Filter / Select",
     "Mongo": '{"price": {"$gt": 100}}',
     "Pandas": 'df[df["price"] > 100]',
     "Concept": "Row filtering based on condition"},

    {"Category": "Projection",
     "Mongo": 'find({}, {"symbol": 1, "price": 1})',
     "Pandas": 'df[["symbol", "price"]]',
     "Concept": "Select specific columns"},

    {"Category": "Sorting",
     "Mongo": 'find().sort("price", -1)',
     "Pandas": 'df.sort_values("price", ascending=False)',
     "Concept": "Sort rows by value"},

    {"Category": "Distinct / Unique",
     "Mongo": 'distinct("sector")',
     "Pandas": 'df["sector"].unique()',
     "Concept": "Extract unique categorical values"},

    {"Category": "Count / Size",
     "Mongo": 'count_documents({})',
     "Pandas": 'len(df)',
     "Concept": "Get total record count"},

    {"Category": "Rename Fields",
     "Mongo": 'update_many({}, {"$rename": {"price": "close_price"}})',
     "Pandas": 'df.rename(columns={"price": "close_price"})',
     "Concept": "Rename columns"},

    {"Category": "Missing Handling",
     "Mongo": '{"$exists": True}',
     "Pandas": 'df.fillna(df.mean())',
     "Concept": "Handle missing values"},

    {"Category": "Insert / Append",
     "Mongo": 'insert_many(docs)',
     "Pandas": 'pd.concat([df, new_df])',
     "Concept": "Add new records"},

    # ====================================================
    # 🟡 LEVEL 2 — AGGREGATIONS & GROUPBY
    # ====================================================

    {"Category": "Groupby Mean",
     "Mongo": '[{"$group": {"_id": "$sector", "avg_price": {"$avg": "$price"}}}]',
     "Pandas": 'df.groupby("sector")["price"].mean()',
     "Concept": "Aggregate average by category"},

    {"Category": "Multiple Aggregations",
     "Mongo": '[{"$group": {"_id": "$sector", "avg": {"$avg": "$price"}, "max": {"$max": "$price"}}}]',
     "Pandas": 'df.groupby("sector").agg({"price": ["mean", "max"]})',
     "Concept": "Perform multiple aggregations"},

    {"Category": "Sum by Group",
     "Mongo": '[{"$group": {"_id": "$sector", "total_volume": {"$sum": "$volume"}}}]',
     "Pandas": 'df.groupby("sector")["volume"].sum()',
     "Concept": "Sum values per group"},

    {"Category": "Count per Category",
     "Mongo": '[{"$group": {"_id": "$sector", "count": {"$sum": 1}}}]',
     "Pandas": 'df["sector"].value_counts()',
     "Concept": "Category frequency count"},

    {"Category": "Pivoting",
     "Mongo": "N/A (achieved via $group + $project)",
     "Pandas": 'df.pivot_table(values="VaR", index="sector", aggfunc="mean")',
     "Concept": "Reshape and aggregate data"},

    {"Category": "Distinct Count",
     "Mongo": '[{"$group": {"_id": "$sector", "unique_symbols": {"$addToSet": "$symbol"}}}]',
     "Pandas": 'df.groupby("sector")["symbol"].nunique()',
     "Concept": "Count distinct items per category"},

    {"Category": "Aggregation Pipeline",
     "Mongo": '[{"$match": {...}}, {"$group": {...}}, {"$sort": {...}}]',
     "Pandas": 'df.query(...).groupby(...).agg(...).sort_values(...)',
     "Concept": "Chained operations equivalent to Mongo pipelines"},

    # ====================================================
    # 🔵 LEVEL 3 — ADVANCED ANALYTICS / WINDOW FUNCTIONS
    # ====================================================

    {"Category": "Rolling Average",
     "Mongo": '{"$setWindowFields": {"output": {"rolling_avg": {"$avg": "$return", "window": {"documents": [-2, 0]}}}}}',
     "Pandas": 'df["return"].rolling(3).mean()',
     "Concept": "Moving average (window function)"},

    {"Category": "Cumulative Sum",
     "Mongo": '{"$setWindowFields": {"output": {"cum_sum": {"$sum": "$volume", "window": {"documents": ["unbounded", "current"]}}}}}',
     "Pandas": 'df["volume"].cumsum()',
     "Concept": "Cumulative aggregation over time"},

    {"Category": "Rank",
     "Mongo": '{"$setWindowFields": {"sortBy": {"VaR": -1}, "output": {"rank": {"$rank": {}}}}}',
     "Pandas": 'df["VaR"].rank(ascending=False)',
     "Concept": "Ranking rows"},

    {"Category": "Percentile / Quantile",
     "Mongo": '{"$setWindowFields": {"output": {"VaR_percentile": {"$percentile": {"p": [0.25, 0.5, 0.75], "input": "$VaR"}}}}}',
     "Pandas": 'df["VaR"].quantile([0.25, 0.5, 0.75])',
     "Concept": "Percentile thresholds"},

    {"Category": "Bucket / Binning",
     "Mongo": '{"$bucket": {"groupBy": "$VaR", "boundaries": [0,0.03,0.05,0.07]}}',
     "Pandas": 'pd.cut(df["VaR"], bins=[0,0.03,0.05,0.07], labels=["Low","Med","High"])',
     "Concept": "Discretizing continuous values"},

    {"Category": "Join / Lookup",
     "Mongo": '{"$lookup": {"from": "sector_data", "localField": "sector", "foreignField": "sector", "as": "info"}}',
     "Pandas": 'df.merge(sector_df, on="sector", how="left")',
     "Concept": "Join tables across datasets"},

    {"Category": "Aggregation by Date",
     "Mongo": '[{"$group": {"_id": "$date", "avg_return": {"$avg": "$return"}}}]',
     "Pandas": 'df.groupby("date")["return"].mean()',
     "Concept": "Time-based grouping"},

    {"Category": "Correlation",
     "Mongo": "N/A (computed client-side)",
     "Pandas": 'df.corr()',
     "Concept": "Relationship strength between variables"},

    {"Category": "Volatility (std dev)",
     "Mongo": '[{"$group": {"_id": "$symbol", "std_ret": {"$stdDevPop": "$return"}}}]',
     "Pandas": 'df.groupby("symbol")["return"].std()',
     "Concept": "Standard deviation by group"},

    {"Category": "Sharpe Ratio",
     "Mongo": 'Aggregation of mean/std (custom)',
     "Pandas": 'df["return"].mean() / df["return"].std()',
     "Concept": "Risk-adjusted performance metric"},

    # ====================================================
    # 🧠 LEVEL 4 — FEATURE ENGINEERING & DATA TRANSFORMATION
    # ====================================================

    {"Category": "Derived Columns",
     "Mongo": '{"$project": {"return_to_VaR": {"$divide": ["$return", "$VaR"]}}}',
     "Pandas": 'df.assign(return_to_VaR=df["return"]/df["VaR"])',
     "Concept": "Feature creation with expressions"},

    {"Category": "Conditional Feature",
     "Mongo": '{"$project": {"risk_category": {"$cond": [{"$gt": ["$VaR", 0.05]}, "High", "Low"]}}}',
     "Pandas": 'df.assign(risk=np.where(df["VaR"]>0.05,"High","Low"))',
     "Concept": "Conditional label creation"},

    {"Category": "Combine Columns",
     "Mongo": "N/A",
     "Pandas": 'df["symbol_sector"] = df["symbol"] + "_" + df["sector"]',
     "Concept": "Text feature concatenation"},

    {"Category": "Outlier Detection",
     "Mongo": "Client-side computation",
     "Pandas": 'df[np.abs((df["return"]-df["return"].mean())/df["return"].std())>2]',
     "Concept": "Identify extreme values"},

    {"Category": "Normalize / Scale",
     "Mongo": "Client-side only",
     "Pandas": '(df - df.mean()) / df.std()',
     "Concept": "Standardization (Z-score)"},

    {"Category": "Reshape Wide→Long",
     "Mongo": "N/A",
     "Pandas": 'df.melt(id_vars=["symbol"])',
     "Concept": "Reshape long format"},

    {"Category": "Cumulative Return",
     "Mongo": "Simulated metric",
     "Pandas": '(1 + df["return"]).cumprod()',
     "Concept": "Portfolio growth over time"},

    {"Category": "Quantile Labeling",
     "Mongo": "Manual buckets",
     "Pandas": 'pd.qcut(df["VaR"], 3, labels=["Low","Med","High"])',
     "Concept": "Quantile binning"},

    {"Category": "Evaluate Inline Expression",
     "Mongo": "N/A",
     "Pandas": 'df.eval("risk_ratio = VaR / return")',
     "Concept": "Inline feature creation with eval()"},

    {"Category": "Categorical Encoding",
     "Mongo": "N/A",
     "Pandas": 'df["sector"].astype("category").cat.codes',
     "Concept": "Encode categorical values numerically"},
]

def run_quiz(num_questions=5):
    print("\n🧠 Data Science Recall Quiz")
    print("="*60)
    score = 0

    for i in range(num_questions):
        q = random.choice(INTERVIEW_MAP)
        q_type = random.choice(["mongo", "pandas", "concept"])
        print(f"\nQ{i+1}. Category: {q['Category']}")

        if q_type == "mongo":
            print(f"💬 Given Pandas: {q['Pandas']}")
            input("👉 Write the Mongo equivalent (press Enter to reveal)...")
            print(f"✅ Correct: {q['Mongo']}\n💡 Concept: {q['Concept']}")
        elif q_type == "pandas":
            print(f"💬 Given Mongo: {q['Mongo']}")
            input("👉 Write the Pandas equivalent (press Enter to reveal)...")
            print(f"✅ Correct: {q['Pandas']}\n💡 Concept: {q['Concept']}")
        else:
            print(f"💬 Question: What does {q['Category']} mean conceptually?")
            input("👉 Think aloud, then press Enter...")
            print(f"💡 Answer: {q['Concept']}\n🧩 Example Pandas: {q['Pandas']}")

        score += 1
        print("-"*60)
        time.sleep(0.4)

    print(f"\n🎯 Quiz complete! You practiced {num_questions} items.")

if __name__ == "__main__":
    run_quiz()
