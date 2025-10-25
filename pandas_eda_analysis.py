import numpy as np
import pandas as pd


# pd.cut(x, bins, right=True, labels=None, include_lowest=False, duplicates='raise', retbins=False)

# Bin ages into 4 equal-width bins and incomes into 4 quantile bins, 
# then analyze average spending per bin pair.

df = pd.DataFrame({
    'Age': [20, 25, 30, 35, 40, 50, 60, 70],
    'Income': [1500, 2000, 2500, 4000, 5000, 6000, 7000, 9000],
    'Spending': [200, 250, 300, 350, 400, 500, 550, 700]
})

df["age_bin"] = pd.cut(df['Age'], bins=4)
df["income_bin"] = pd.qcut(df['Income'], q=4)
print(df)

######################################### GROUPBY #####################################################
# splitting the object, applying a function, and combining the results. 
# This can be used to group large amounts of data and compute operations on these groups.

multi_index_candidates = [
                          ["Species1","Species1", "Species2","Species2", "Species3", "Species3" , "Species4", "Species4" ],
                          ["BigBird","BigBird", "SmallBird", "SmallBird",  "Animal","Animal", "Human","Human"]
                        ]
index = pd.MultiIndex.from_arrays(multi_index_candidates, names=["Sample", "Animal"])
print(index)
columns = pd.MultiIndex.from_arrays(
    [['Attributes', 'Attributes'], ['Living Being', 'Max Speed']],
    names=['Category', 'Property']
)

dfs = pd.DataFrame(
    {
        "Living Being": ['Falcon', 'Falcon','Parrot', 'Parrot', "Lion", "Lion", "Man", "Man"],
        "Max Speed": [380., 370., 24., 26., 34., 56., 123., 45.]
    },
    index=index,
    # columns=columns
)

print(dfs)
print(dfs.columns)

# When we reset the index, the old index is added as a column, and a new sequential index is used:
new_df = dfs.reset_index(names=['Sample','Animal'])
print(new_df)
print(new_df.columns)
filtered_df = new_df.groupby(by=['Living Being'], group_keys=True )[['Max Speed']].agg(lambda x: x.values.mean())
print(filtered_df)

print(new_df)
