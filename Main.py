import yfinance as yf

a = input("Enter the stock:")
s1 = yf.Ticker(a)
print("Trailing P/E is:",s1.info.get("trailingPE"))
print("Forward P/E is:",s1.info.get("forwardPE"))
Revenue  = s1.info.get("revenueGrowth")
print("Revenue growth is:", f"{Revenue * 100:.2f}%")
print("Dividend Yield is:",s1.info.get("dividendYield"))

