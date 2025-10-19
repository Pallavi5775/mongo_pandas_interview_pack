import numpy as np
import pandas as pd

######################### SERIES #################################

ser = pd.Series(data=[89, 67])
print(ser)

ser2 = pd.Series(data=[89, 67], index=["index1",'index2'])
print(ser2)

data_1d_array = np.array([2,5,4])
# Operations between Series (+, -, /, *, **) align values based on their associated index values
# -- they need not be the same length. 
# The result index will be the sorted union of the two indexes.

# For indexes - Values must be hashable and have the same length as data
# for indexes - If data is dict-like and index is None, 
# then the keys in the data are used as the index. 
# If the index is not None, 
# the resulting Series is reindexed with the index values.
ser3 = pd.Series(data_1d_array,index=['coum1', 'coum2', 'coum3'])
print(ser3)
dicti ={
    "name":"pallavi",
    "age":25
}
ser4 = pd.Series(dicti) # dict so creating keys as columns
print(ser4)

####################### Pandas Creation ##############################

dictionary_list =[{
  "_id": {
    "$oid": "68f0885270d366928ebaa3ed"
  },
  "name": "Laptop",
  "category": "Electronics",
  "price": 1200,
  "inStock": True
},{
  "_id": {
    "$oid": "68f0885270d366928ebaa3ee"
  },
  "name": "Shoes",
  "category": "Fashion",
  "price": 80,
  "inStock": False
},{
  "_id": {
    "$oid": "68f0885270d366928ebaa3ef"
  },
  "name": "Phone",
  "category": "Electronics",
  "price": 850,
  "inStock": True
},{
  "_id": {
    "$oid": "68f0885270d366928ebaa3f0"
  },
  "name": "T-Shirt",
  "category": "Fashion",
  "price": 20,
  "inStock": True
},{
  "_id": {
    "$oid": "68f0885270d366928ebaa3f1"
  },
  "name": "Watch",
  "category": "Accessories",
  "price": 150,
  "inStock": False
}]

# Dict can contain Series, arrays, constants, dataclass or list-like objects. 
# If data is a dict, column order follows insertion-order. 
# If a dict contains Series which have an index defined, 
# it is aligned by its index. 
# This alignment also occurs if data is a Series or a DataFrame itself.
# Alignment is done on Series/DataFrame inputs.
# If data is a list of dicts, column order follows insertion-order.
df = pd.DataFrame(data=dictionary_list)
print(df)


####################### Pandas Reading ##############################
print(df.iloc[0], type(df.iloc[0])) # gives the 0the row in form of series
print(df.iloc[0].to_dict())  # extractin the row in form of dict
print(df.iloc[0].to_numpy()) # extractin the row in form of numpy
print(df.iloc[0].to_list())  # extractin the row in form of list
# getting all the indexs currently and converting to list

print(df.index.to_list()) 
print(df['name'].to_dict()) # df['name'] gives series of index and list and i converted into mapper

# index : dict-like or function
# Alternative to specifying axis (mapper, axis=0 is equivalent to index=mapper).

# columns : dict-like or function
# Alternative to specifying axis (mapper, axis=1 is equivalent to columns=mapper).
df.rename(df['name'].to_dict(), axis=0, inplace=True)

print("New Indexed DF", df)


############################################## EXPLORING THE DATAFRAME ##########################################################
#seeing all the properties on the dataframe object
# print(dir(df))
#see properties which are callable
callable_props = [prop for prop in dir(df) if not prop.startswith('_') and callable(getattr(df, prop))]
# print(callable_props)

non_callable_props = [prop for prop in dir(df) if not prop.startswith('_') and not callable(getattr(df, prop))]
# print(non_callable_props)
# print(df.loc['Laptop'])

####################################################################################################################
# item : label
# Label of column to be popped.
print(df.pop(item='_id'))

print("**********************")
print(df.values) #Return a Numpy representation of the DataFrame.
print("**********************")
# subset : label or list of labels, optional
# Columns to use when counting unique combinations.
print(df.value_counts()) #Return a Series containing counts of unique rows in the DataFrame.
print("**********************")
print(df.value_counts(subset=["category",'price'])) #subset means columns
print("**********************")
# Modify in place using non-NA values from another DataFrame.
# Aligns on indices. There is no return value.

# Should have at least one matching index/column label with the original DataFrame. 
# If a Series is passed, its name attribute must be set, 
# and that will be used as the column name to align with the original DataFrame.
# print(df.update)


print("**********************")
print("**********************")
print(df.transpose())

print("**********************")
print("**********************")
# print(df.unstack)

print("**********************")
print("**********************")
# Convert DataFrame to a NumPy record array.
# Index will be included as the first field of the record array if requested.
print(df.to_records())

print("**********************")
print("**********************")
# print(df.agg)



print("**********************")
print("**********************")
# Objects passed to the function are Series objects 
# whose index is either the DataFrame's index (axis=0) '
# 'or the DataFrame's columns (axis=1). By default (result_type=None),
# the final return type is inferred from the return type of the applied function. 
# Otherwise, it depends on the result_type argument.



# func : function
# Function to apply to each column or row.

# axis : {0 or 'index', 1 or 'columns'}, default 0
# Axis along which the function is applied:

# 0 or 'index': apply function to each column.
# 1 or 'columns': apply function to each row.
# raw : bool, default False
# Determines if row or column is passed as a Series or ndarray object:
# False ⁠:⁠ passes each row or column as a Series to the function.
# True ⁠:⁠ the passed function will receive ndarray objects instead. If you are just applying a NumPy reduction function this will achieve much better performance.
# result_type : {'expand', 'reduce', 'broadcast', None}, default None
# These only act when axis=1 (columns):
# 'expand' ⁠:⁠ list-like results will be turned into columns.
# 'reduce' ⁠:⁠ returns a Series if possible rather than expanding list-like results. 
# This is the opposite of 'expand'.
# 'broadcast' ⁠:⁠ results will be broadcast to the original shape of the DataFrame, 
# the original index and columns will be retained.
# The default behaviour (None) depends on the return value of the applied function: 
# list-like results will be returned as a Series of those. 
# However if the apply function returns a Series these are expanded to columns.
print(df["price"].apply(lambda x: x-10))

print("**********************")
print("**********************")
# Assign new columns to a DataFrame.
# Returns a new object with all original columns in addition to new ones.
# Existing columns that are re-assigned will be overwritten.
new_df = df.assign(discountd_price=lambda x : x['price'] - (0.5 * x['price']))
print(df.assign(discountd_price=lambda x : x['price'] - (0.5 * x['price'])))

print("**********************")
print("**********************")
# To select all numeric types, use np.number or 'number'
# To select strings you must use the object dtype, but note that this will return all object dtype columns
# See the numpy dtype hierarchy
# To select datetimes, use np.datetime64, 'datetime' or 'datetime64'
# To select timedeltas, use np.timedelta64, 'timedelta' or 'timedelta64'
# To select Pandas categorical dtypes, use 'category'
# To select Pandas datetimetz dtypes, use 'datetimetz' (new in 0.20.0) or 'datetime64[ns, tz]'
numeric_df = new_df.select_dtypes(include="number")
print(numeric_df)


print("**********************")
print("**********************")

for row in df.itertuples():
    print(row.category)


print("**********************")
print("**********************")
# DataFrame.max : Return the maximum over DataFrame axis.

# DataFrame.cummax : Return cumulative maximum over DataFrame axis.

# DataFrame.cummin : Return cumulative minimum over DataFrame axis.

# DataFrame.cumsum : Return cumulative sum over DataFrame axis.

# DataFrame.cumprod : Return cumulative product over DataFrame axis.
print(df['price'].cummax())





print("**********************")
print("**********************")















##############################################BroadCasting##################################################################

# other : scalar, sequence, Series, dict or DataFrame
# Any single or multiple element data structure, or list-like object.

# axis : {0 or 'index', 1 or 'columns'}
# Whether to compare by the index (0 or 'index') or columns. (1 or 'columns'). 
# For Series input, axis to match Series index on.

# level : int or label
# Broadcast across a level, matching Index values on the passed MultiIndex level.

# fill_value : float or None, default None
# Fill existing missing (NaN) values, and any new element needed for successful DataFrame alignment, 
# with this value before computation. 
# If data in both corresponding DataFrame locations is missing the result will be missing.
# print(df.add)


