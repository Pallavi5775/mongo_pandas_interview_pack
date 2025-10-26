import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta

index = pd.date_range('1/1/2025', periods=24, freq='H')

df = pd.DataFrame({'Sales': np.random.randint(
    100, 500, size=len(index))}, index=index)
print(df.head())

print(df.resample(rule='D').sum())

index = pd.date_range('1/1/2025', periods=24, freq='D')

df_d = pd.DataFrame({'Sales': np.random.randint(
    100, 500, size=len(index))}, index=index)
print(df_d.head())
# hourly rows with NaN values (because there’s no hourly data).
print(df_d.resample(rule='h').sum())

print(df_d.resample(rule='h').ffill())

# Downsampling	Reduce frequency (hourly → daily)	“Group by bigger time intervals”
# Upsampling	Increase frequency (daily → hourly)	“Fill missing finer intervals”


dates = pd.date_range(datetime.date(datetime.now()), periods=12, freq='ME')
print(dates)

df_ = pd.DataFrame({
    'open': ((np.random.randn(10, 12)).ravel()[:12]),
    'high': (np.random.randn(10, 12)).ravel()[:12],
    'close': (np.random.randn(10, 12)).ravel()[:12],
    'volume': (np.random.randn(10, 12)).ravel()[:12]
}, index=dates)

print(df_)
# df_.shape == (12, 5) a tuple --> * unpacks ---> 12,5
unmask = np.random.rand(*df_.shape) < 0.2

new_df = df_.mask(unmask)

print(new_df)

n_df = new_df.apply(lambda col: col.ffill() if col.isna().mean(
) > 0.2 else (col.bfill() if col.isna().mean() > 0 else col))
print(n_df)

df_down = n_df.resample('YE').sum()
print(n_df.resample('D').ffill())
df_up = n_df.resample('D').ffill()
import plotly.graph_objects as go

fig = go.Figure()

# 🔹 Real data
fig.add_trace(go.Scatter(
    x=n_df.index,
    y=n_df['close'],
    mode='lines+markers',
    name='Original (Daily)',
    line=dict(width=2)
))

# 🔹 Downsampled data
fig.add_trace(go.Scatter(
    x=df_down.index,
    y=df_down['close'],
    mode='lines+markers',
    name='Downsampled (YE sum)',
    line=dict(width=3, dash='dot')
))

# 🔹 Upsampled data
fig.add_trace(go.Scatter(
    x=df_up.index,
    y=df_up['close'],
    mode='lines',
    name='Upsampled (D interpolated)',
    line=dict(width=2, dash='dash')
))

# Layout
fig.update_layout(
    title="Original vs Downsampled vs Upsampled Data",
    xaxis_title="Date",
    yaxis_title="Close Price",
    template="plotly_dark",
    width=950,
    height=500,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

fig.add_trace(go.Bar(
    x=n_df.index,
    y=n_df['volume'],
    name='Volume (original)',
    opacity=0.3,
    yaxis='y2'
))

fig.update_layout(
    yaxis2=dict(title="Volume", overlaying='y', side='right')
)

fig.show()


# https://chatgpt.com/c/68fd5476-4bf0-8320-900d-5af5167c8c82