import pytz
from datetime import timedelta, datetime
import pandas as pd
import numpy as np

np.random.seed(42)

# -----------------------------------
# 1️⃣ Generate base date range
# -----------------------------------
dates = pd.date_range(start="2025-01-01", end="2025-06-30", freq="D")

# number of records
n = len(dates) * 10  # 10 records per day

# -----------------------------------
# 2️⃣ Create random dataset
# -----------------------------------
df_time = pd.DataFrame({
    "Date": np.random.choice(dates, size=n),
    "Region": np.random.choice(["North", "South", "East", "West"], size=n),
    "Salesperson": np.random.choice(
        ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"], size=n
    ),
    "Product": np.random.choice(
        ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"], size=n
    ),
    "Units_Sold": np.random.randint(1, 50, size=n),
    "Unit_Price": np.random.randint(200, 2000, size=n),
    "Discount": np.random.choice([0, 5, 10, 15, 20], size=n),
    "Customer_Rating": np.random.choice([1, 2, 3, 4, 5], size=n)
})

# -----------------------------------
# 3️⃣ Derived columns
# -----------------------------------
df_time["Revenue"] = df_time["Units_Sold"] * \
    df_time["Unit_Price"] * (1 - df_time["Discount"] / 100)
df_time["Profit"] = df_time["Revenue"] * np.random.uniform(0.1, 0.3, size=n)

# Date-based features
df_time["Month"] = df_time["Date"].dt.month_name()
df_time["Weekday"] = df_time["Date"].dt.day_name()
df_time["Week_Number"] = df_time["Date"].dt.isocalendar().week
df_time["Quarter"] = df_time["Date"].dt.quarter

# Sort by date
df_time = df_time.sort_values("Date").reset_index(drop=True)

print(df_time.head(10))

# Total daily revenue

daily_df = df_time.groupby(by=['Date'], group_keys=True)[
    ["Revenue"]].agg(lambda x: x.sum())
print(daily_df)

# dates and timeseries execrises 


sample_time_series = pd.date_range(start=datetime.date(
    datetime.now()) - timedelta(days=5), end=datetime.date(datetime.now()))
print(sample_time_series)


# get the UTC timezone
utc_now = datetime.now(pytz.UTC)
print()

# getting all the timezone information and convert the utc time zone to local time zone
all_time_zone_informations = [
    (pytz.timezone(tzn).zone, utc_now.astimezone(pytz.timezone(tzn)))
    for tzn in pytz.all_timezones
]

# extracting the tuple to dict for simplicity
local_time = list(map(lambda x: {"tz_info": x[0], "date": datetime.date(x[1])},all_time_zone_informations ))

# mapping through the list of local time and timezones and creating a pd range out of that
tz_dates = list(map(lambda x: pd.date_range(
    start=x['date'] - timedelta(days=5),
    end=x['date'],
    tz=x['tz_info'],
    freq='D'
), local_time))

import asyncio
columns = ['Region', 'Salesperson','Product','Units_Sold','Unit_Price','Discount','Customer_Rating']
async def get_dates(tz_date):
    print(".......>")
    print(tz_date)
    df = pd.DataFrame(data={
                "Region": np.random.choice(["North", "South", "East", "West"], size=len(tz_date)),
                "Salesperson": np.random.choice(["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona"], size=len(tz_date)),
                "Product": np.random.choice(["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"], size=len(tz_date)),
                "Units_Sold": np.random.randint(1, 50, size=len(tz_date)),
                "Unit_Price": np.random.randint(200, 2000, size=len(tz_date)),
                "Discount": np.random.choice([0, 5, 10, 15, 20], size=len(tz_date)),
                "Customer_Rating": np.random.choice([1, 2, 3, 4, 5], size=len(tz_date))
            }, columns=columns,
                index=tz_date)
    print(df)
    return df

#passing the tz_dates to the function to create the dataframe
async def main():
    tasks = [get_dates(item) for item in tz_dates]
    result = asyncio.gather(*tasks)
    print(result)

asyncio.run(main())











# resampling exercise
# Weekly sales trend

# df_weekly =  df_time.res


# https://chatgpt.com/c/68fbed56-35cc-8324-b4f3-d5e414b1c37b
