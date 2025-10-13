
# 🧠 Mongo ↔ Pandas Syntax Mastery — 7-Day Local Revision Dashboard

> 🎯 Goal: Achieve fluent recall of MongoDB + Pandas syntax patterns across data science operations  
> 🕒 Duration: 7 days × 30 minutes/day  
> 🧩 Focus: Filter → Group → Aggregate → Feature Engineer → Window → Reshape  
> 🧾 Outcome: You can read, write, and explain both MongoDB and Pandas equivalents confidently

---

## ✅ Daily Progress Checklist
- [ ] Day 1 — CRUD, Filters, Projection
- [ ] Day 2 — Aggregation, Groupby, Pivot
- [ ] Day 3 — Sorting, Joins, Query
- [ ] Day 4 — Feature Engineering
- [ ] Day 5 — Time Series, Windows
- [ ] Day 6 — Advanced Transformations
- [ ] Day 7 — Full Revision & Quiz

---

<details>
<summary>🟢 Day 1 — CRUD + Filters + Projection</summary>

**Focus:** Basic Mongo & Pandas syntax recall

```python
# Mongo
{"price": {"$gt": 100}}, {"symbol": 1, "price": 1}

# Pandas
df[df["price"] > 100][["symbol", "price"]]
```
</details>

<details>
<summary>🟡 Day 2 — Aggregation & Groupby</summary>

**Focus:** $group, $sum, $avg ↔ .groupby().agg()

```python
# Mongo
[{"$group": {"_id": "$sector", "avg_VaR": {"$avg": "$VaR"}}}]

# Pandas
df.groupby("sector")["VaR"].mean()
```
</details>

<details>
<summary>🧩 Day 3 — Sorting, Joins, Filtering</summary>

```python
# Mongo
{"$lookup": {"from": "sector_data", "localField": "sector",
             "foreignField": "sector", "as": "info"}}

# Pandas
df.merge(sector_df, on="sector", how="left")
```
</details>

<details>
<summary>🔵 Day 4 — Feature Engineering</summary>

```python
# Mongo
{"$project": {"risk_flag": {"$cond": [{"$gt": ["$VaR", 0.05]}, "High", "Low"]}}}

# Pandas
df.assign(risk_flag=np.where(df["VaR"] > 0.05, "High", "Low"))
```
</details>

<details>
<summary>⏱ Day 5 — Time Series & Window Functions</summary>

```python
# Mongo
{"$setWindowFields": {"output": {"rolling_avg": {"$avg": "$return",
                                                "window": {"documents": [-2, 0]}}}}}

# Pandas
df["return"].rolling(3).mean()
```
</details>

<details>
<summary>🧮 Day 6 — Advanced Transformations</summary>

```python
# Mongo equivalent of pivot
[{"$group": {"_id": "$sector", "avg_VaR": {"$avg": "$VaR"}}}]

# Pandas pivot
df.pivot_table(values="VaR", index="sector", aggfunc="mean")
```
</details>

<details>
<summary>🧾 Day 7 — Full Revision & Quiz Simulation</summary>

Run your interactive quiz:
```bash
python interview_quiz.py
```
</details>

---

## Quick Reference Table

| Category | Mongo Root | Pandas Root | Concept |
|-----------|-------------|-------------|----------|
| Filter | $match | df[...] | Row filtering |
| Projection | $project | df[['col']] | Column selection |
| Aggregation | $group | .groupby().agg() | Summaries |
| Join | $lookup | .merge() | Combining tables |
| Sort | .sort() | .sort_values() | Ordering |
| Window | $setWindowFields | .rolling(), .expanding() | Moving stats |
| Feature Engg | $addFields, $cond | .assign(), np.where() | Derived features |
| Reshape | $bucket, $unwind | .pivot(), .melt() | Structure transformation |
