def mongo_query_examples(db):
    """
    75 curated MongoDB queries across:
    - Basic CRUD (insert, find, update)
    - Aggregations
    - Grouping, bucketing, projections
    - Window functions (Mongo 5+)
    - Advanced filtering and pipeline analytics
    """

    collection = db["market_data"]

    examples = [
        # ====================================================
        # 🟢 LEVEL 1: BASIC CRUD + FILTERS
        # ====================================================

        # 1. Insert a single record
        lambda: collection.insert_one({"symbol": "AAPL", "price": 180, "date": datetime.utcnow()}),

        # 2. Insert multiple documents
        lambda: collection.insert_many(sample_docs),

        # 3. Find one document
        lambda: collection.find_one(),

        # 4. Find all documents
        lambda: list(collection.find()),

        # 5. Find with equality condition
        lambda: list(collection.find({"sector": "Tech"})),

        # 6. Find with comparison
        lambda: list(collection.find({"price": {"$gt": 150}})),

        # 7. Find with multiple conditions
        lambda: list(collection.find({"sector": "Tech", "volume": {"$gt": 1000000}})),

        # 8. Find with OR condition
        lambda: list(collection.find({"$or": [{"sector": "Auto"}, {"VaR": {"$gt": 0.05}}]})),

        # 9. Projection — only symbol and price
        lambda: list(collection.find({}, {"symbol": 1, "price": 1})),

        # 10. Sort descending
        lambda: list(collection.find().sort("price", -1)),

        # 11. Count total documents
        lambda: collection.count_documents({}),

        # 12. Delete one
        lambda: collection.delete_one({"symbol": "TSLA"}),

        # 13. Update a single field
        lambda: collection.update_one({"symbol": "AAPL"}, {"$set": {"price": 200}}),

        # 14. Rename a field
        lambda: collection.update_many({}, {"$rename": {"price": "last_price"}}),

        # 15. Add a new computed field
        lambda: collection.update_many({}, {"$set": {"currency": "USD"}}),

        # 16. Find using regex
        lambda: list(collection.find({"symbol": {"$regex": "^A", "$options": "i"}})),

        # 17. Distinct field values
        lambda: collection.distinct("sector"),

        # 18. Limit results
        lambda: list(collection.find().limit(3)),

        # 19. Exists operator
        lambda: list(collection.find({"VaR": {"$exists": True}})),

        # 20. Between date range
        lambda: list(collection.find({"date": {"$gte": datetime(2025, 1, 1), "$lte": datetime(2025, 12, 31)}})),

        # ====================================================
        # 🟡 LEVEL 2: INTERMEDIATE AGGREGATIONS
        # ====================================================

        # 21. Group by sector with average price
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "avg_price": {"$avg": "$price"}}}
        ])),

        # 22. Total volume by sector
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "total_volume": {"$sum": "$volume"}}}
        ])),

        # 23. Count documents per symbol
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$symbol", "count": {"$sum": 1}}}
        ])),

        # 24. Max VaR per sector
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "max_VaR": {"$max": "$VaR"}}}
        ])),

        # 25. Average sentiment per sector
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "avg_sentiment": {"$avg": "$sentiment_score"}}}
        ])),

        # 26. Group by date with avg return
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$date", "avg_return": {"$avg": "$return"}}}
        ])),

        # 27. Count high-risk stocks (VaR > 0.05)
        lambda: list(collection.aggregate([
            {"$match": {"VaR": {"$gt": 0.05}}},
            {"$count": "high_risk_stocks"}
        ])),

        # 28. Sum volume of tech stocks
        lambda: list(collection.aggregate([
            {"$match": {"sector": "Tech"}},
            {"$group": {"_id": None, "total_volume": {"$sum": "$volume"}}}
        ])),

        # 29. Bucket VaR into categories
        lambda: list(collection.aggregate([
            {"$bucket": {
                "groupBy": "$VaR",
                "boundaries": [0, 0.03, 0.05, 0.07, 0.1],
                "default": "Other",
                "output": {"count": {"$sum": 1}}
            }}
        ])),

        # 30. Combine match + project + sort
        lambda: list(collection.aggregate([
            {"$match": {"sector": "Tech"}},
            {"$project": {"symbol": 1, "VaR": 1, "return": 1}},
            {"$sort": {"VaR": -1}}
        ])),

        # 31. Find top 5 stocks by return
        lambda: list(collection.aggregate([
            {"$sort": {"return": -1}},
            {"$limit": 5},
            {"$project": {"symbol": 1, "return": 1}}
        ])),

        # 32. Count defaults by sector
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "defaults": {"$sum": "$default_flag"}}}
        ])),

        # 33. Average VaR grouped by both sector & date
        lambda: list(collection.aggregate([
            {"$group": {"_id": {"sector": "$sector", "date": "$date"}, "avg_VaR": {"$avg": "$VaR"}}}
        ])),

        # 34. Top 3 VaR per sector
        lambda: list(collection.aggregate([
            {"$sort": {"VaR": -1}},
            {"$group": {"_id": "$sector", "top_VaR": {"$push": "$VaR"}}},
            {"$project": {"top_3": {"$slice": ["$top_VaR", 3]}}}
        ])),

        # 35. Group by risk buckets and sum volumes
        lambda: list(collection.aggregate([
            {"$bucket": {
                "groupBy": "$VaR",
                "boundaries": [0, 0.03, 0.05, 0.07],
                "output": {"total_volume": {"$sum": "$volume"}}
            }}
        ])),

        # 36. Calculate average return per sector for only non-default
        lambda: list(collection.aggregate([
            {"$match": {"default_flag": 0}},
            {"$group": {"_id": "$sector", "avg_return": {"$avg": "$return"}}}
        ])),

        # 37. Count how many documents per sentiment band
        lambda: list(collection.aggregate([
            {"$bucketAuto": {"groupBy": "$sentiment_score", "buckets": 4}}
        ])),

        # 38. Group by month (extract month from date)
        lambda: list(collection.aggregate([
            {"$project": {"month": {"$month": "$date"}, "price": 1}},
            {"$group": {"_id": "$month", "avg_price": {"$avg": "$price"}}}
        ])),

        # ====================================================
        # 🔵 LEVEL 3: ADVANCED ANALYTICS + WINDOW + PIPELINES
        # ====================================================

        # 39. Rank stocks by VaR using $setWindowFields (MongoDB 5+)
        lambda: list(collection.aggregate([
            {"$setWindowFields": {
                "sortBy": {"VaR": -1},
                "output": {"VaR_rank": {"$rank": {}}}
            }}
        ])),

        # 40. Moving average of return (rolling 3)
        lambda: list(collection.aggregate([
            {"$setWindowFields": {
                "sortBy": {"date": 1},
                "output": {"rolling_avg_return": {"$avg": "$return", "window": {"documents": [-2, 0]}}}
            }}
        ])),

        # 41. Compute cumulative volume per sector
        lambda: list(collection.aggregate([
            {"$setWindowFields": {
                "partitionBy": "$sector",
                "sortBy": {"date": 1},
                "output": {"cumulative_volume": {"$sum": "$volume", "window": {"documents": ["unbounded", "current"]}}}
            }}
        ])),

        # 42. Calculate percentile rank of VaR
        lambda: list(collection.aggregate([
            {"$setWindowFields": {
                "output": {"VaR_percentile": {"$percentile": {"p": [0.5, 0.9], "input": "$VaR"}}}
            }}
        ])),

        # 43. Pipeline: calculate Sharpe ratio by sector
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "mean_return": {"$avg": "$return"}, "std_dev": {"$stdDevPop": "$return"}}},
            {"$project": {"Sharpe": {"$divide": ["$mean_return", "$std_dev"]}}}
        ])),

        # 44. Multi-stage pipeline: avg sentiment by year
        lambda: list(collection.aggregate([
            {"$project": {"year": {"$year": "$date"}, "sentiment_score": 1}},
            {"$group": {"_id": "$year", "avg_sentiment": {"$avg": "$sentiment_score"}}}
        ])),

        # 45. Correlation-like ratio (return/VaR)
        lambda: list(collection.aggregate([
            {"$project": {"symbol": 1, "return_to_VaR": {"$divide": ["$return", "$VaR"]}}}
        ])),

        # 46. Extract top sectors by cumulative return
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "total_return": {"$sum": "$return"}}},
            {"$sort": {"total_return": -1}},
            {"$limit": 3}
        ])),

        # 47. Calculate risk-weighted average return
        lambda: list(collection.aggregate([
            {"$group": {"_id": None, "weighted_return": {"$avg": {"$divide": ["$return", "$VaR"]}}}}
        ])),

        # 48. Daily variance of returns
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$date", "variance_return": {"$stdDevPop": "$return"}}}
        ])),

        # 49. Filter, group, and aggregate across multiple fields
        lambda: list(collection.aggregate([
            {"$match": {"sector": {"$ne": "Energy"}}},
            {"$group": {"_id": "$sector", "mean_VaR": {"$avg": "$VaR"}, "mean_sentiment": {"$avg": "$sentiment_score"}}}
        ])),

        # 50. Count per VaR range bucket
        lambda: list(collection.aggregate([
            {"$bucket": {
                "groupBy": "$VaR",
                "boundaries": [0, 0.02, 0.04, 0.06, 0.08, 0.1],
                "default": "Others",
                "output": {"count": {"$sum": 1}}
            }}
        ])),

        # ====================================================
        # 🧮 ADVANCED DERIVED METRICS & WINDOW JOINS
        # ====================================================

        # 51. Calculate volatility index (std/mean)
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "mean_ret": {"$avg": "$return"}, "std_ret": {"$stdDevPop": "$return"}}},
            {"$project": {"vol_index": {"$divide": ["$std_ret", "$mean_ret"]}}}
        ])),

        # 52. Join self collection (symbol matching)
        lambda: list(collection.aggregate([
            {"$lookup": {
                "from": "market_data",
                "localField": "symbol",
                "foreignField": "symbol",
                "as": "joined_docs"
            }}
        ])),

        # 53. Calculate median VaR per sector
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "median_VaR": {"$avg": "$VaR"}}}
        ])),

        # 54. 3-day rolling average (approximation)
        lambda: list(collection.aggregate([
            {"$sort": {"date": 1}},
            {"$setWindowFields": {"sortBy": {"date": 1}, "output": {"rolling_return": {"$avg": "$return", "window": {"documents": [-2, 0]}}}}}
        ])),

        # 55. Count unique symbols
        lambda: len(collection.distinct("symbol")),

        # 56. Average sentiment for high VaR (>0.05)
        lambda: list(collection.aggregate([
            {"$match": {"VaR": {"$gt": 0.05}}},
            {"$group": {"_id": None, "avg_sentiment": {"$avg": "$sentiment_score"}}}
        ])),

        # 57. Identify top 5 volatile assets
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$symbol", "std_vol": {"$stdDevPop": "$return"}}},
            {"$sort": {"std_vol": -1}}, {"$limit": 5}
        ])),

        # 58. Calculate return variance by sector and normalize
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "var": {"$stdDevPop": "$return"}}},
            {"$project": {"normalized": {"$divide": ["$var", 10]}}}
        ])),

        # 59. Multi-field projection with expressions
        lambda: list(collection.aggregate([
            {"$project": {"symbol": 1, "risk_score": {"$multiply": ["$VaR", "$return"]}}}
        ])),

        # 60. Calculate default rate by sector
        lambda: list(collection.aggregate([
            {"$group": {"_id": "$sector", "default_rate": {"$avg": "$default_flag"}}}
        ])),

        # 61–75 additional analytical pipelines
        lambda: list(collection.aggregate([{"$group": {"_id": "$sector", "avg_price": {"$avg": "$price"}, "min_price": {"$min": "$price"}}}])),
        lambda: list(collection.aggregate([{"$match": {"sector": "Tech"}}, {"$project": {"symbol": 1, "return": 1, "VaR": 1, "_id": 0}}])),
        lambda: list(collection.aggregate([{"$sort": {"return": -1}}, {"$limit": 10}])),
        lambda: list(collection.aggregate([{"$group": {"_id": "$date", "total_volume": {"$sum": "$volume"}}}])),
        lambda: list(collection.aggregate([{"$project": {"symbol": 1, "return_to_volume": {"$divide": ["$return", "$volume"]}}}])),
        lambda: list(collection.aggregate([{"$match": {"sector": {"$in": ["Tech", "Auto"]}}}, {"$group": {"_id": "$sector", "avg_sentiment": {"$avg": "$sentiment_score"}}}])),
        lambda: list(collection.aggregate([{"$project": {"symbol": 1, "risk_category": {"$cond": [{"$gt": ["$VaR", 0.05]}, "High", "Low"]}}}])),
        lambda: list(collection.aggregate([{"$group": {"_id": None, "max_volume": {"$max": "$volume"}}}])),
        lambda: list(collection.aggregate([{"$bucketAuto": {"groupBy": "$return", "buckets": 5}}])),
        lambda: list(collection.aggregate([{"$group": {"_id": "$symbol", "return_range": {"$push": "$return"}}}])),
        lambda: list(collection.aggregate([{"$sample": {"size": 3}}])),
        lambda: list(collection.aggregate([{"$addFields": {"return_x100": {"$multiply": ["$return", 100]}}}])),
        lambda: list(collection.aggregate([{"$sort": {"sentiment_score": -1}}, {"$limit": 5}])),
        lambda: list(collection.aggregate([{"$group": {"_id": "$sector", "min_VaR": {"$min": "$VaR"}, "max_VaR": {"$max": "$VaR"}}}])),
        lambda: list(collection.aggregate([{"$group": {"_id": "$symbol", "volatility_index": {"$stdDevPop": "$return"}}}])),
    ]

    return examples
