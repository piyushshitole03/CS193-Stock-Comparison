import yfinance as yf

a = input("Enter the first stock  :")
b = input("Enter the second stock :")

s1 = yf.Ticker(a)
s2 = yf.Ticker(b)

print("========== "+ a + " ==========")
print("Trailing P/E is:",s1.info.get("trailingPE"))
print("Forward P/E is:",s1.info.get("forwardPE"))
Revenue  = s1.info.get("revenueGrowth")
print("Revenue growth is:", f"{Revenue * 100:.2f}%")
print("Dividend Yield is:",s1.info.get("dividendYield"))

print("========== "+ b + " ==========")
print("Trailing P/E is:",s2.info.get("trailingPE"))
print("Forward P/E is:",s2.info.get("forwardPE"))
Revenue2  = s2.info.get("revenueGrowth")
print("Revenue growth is:", f"{Revenue2 * 100:.2f}%")
print("Dividend Yield is:",s2.info.get("dividendYield"))

