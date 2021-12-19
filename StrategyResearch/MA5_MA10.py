# ！/usr/bin/env python
# -*- coding:utf-8 -*-
# @Project : stock_quant
# @Date    : 2021/12/19 16:27
# @Author  : Adolf
# @File    : MA5_MA10.py
# @Function:
import pandas as pd
import pandas_ta as ta

pd.set_option("expand_frame_repr", False)
pd.set_option("display.max_rows", None)

df = pd.read_csv("data/real_data/hfq/600570.csv")

# print(df)
# df.set_index(pd.DatetimeIndex(df["date"]), inplace=True)

# df.ta.log_return(cumulative=True, append=True)
# df.ta.percent_return(cumulative=True, append=True)
df["sma5"] = ta.sma(df['close'], length=5)
df["sma10"] = ta.sma(df['close'], length=10)

# print(help(ta.macd))
macd_df = ta.macd(close=df['close'])

df['macd'], df['histogram'], df['signal'] = [macd_df['MACD_12_26_9'], macd_df['MACDh_12_26_9'],
                                             macd_df['MACDs_12_26_9']]
# pd.concat([df, ta.macd(close=df['close'])])

print(df.tail())
