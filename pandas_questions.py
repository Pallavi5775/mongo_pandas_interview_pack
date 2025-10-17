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
print(dir(df))
#see properties which are callable
callable_props = [prop for prop in dir(df) if not prop.startswith('_') and callable(getattr(df, prop))]
print(callable_props)

non_callable_props = [prop for prop in dir(df) if not prop.startswith('_') and not callable(getattr(df, prop))]
print(non_callable_props)
# print(df.loc['Laptop'])

