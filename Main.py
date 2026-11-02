import yfinance as yf

# Get user input for stock tickers
a = input("Enter the first stock: ")
b = input("Enter the second stock: ")

s1 = yf.Ticker(a)
s2 = yf.Ticker(b)

# Fetch metrics
t_pe1 = s1.info.get("trailingPE")
t_pe2 = s2.info.get("trailingPE")

f_pe1 = s1.info.get("forwardPE")
f_pe2 = s2.info.get("forwardPE")

rev1 = s1.info.get("revenueGrowth")
rev2 = s2.info.get("revenueGrowth")

div1 = s1.info.get("dividendYield")
div2 = s2.info.get("dividendYield")

# Print headers
print(f"{"Metric":<20}{a:>12}{b:>12}")
print("-" * 44)

# Print metrics row by row using your formatting style
print(f'{"Trailing P/E":<20}{t_pe1:>12.2f}{t_pe2:>12.2f}')
print(f'{"Forward P/E":<20}{f_pe1:>12.2f}{f_pe2:>12.2f}')
print(f'{"Revenue Growth":<20}{rev1 * 100:>11.2f}%{rev2 * 100:>11.2f}%')
print(f'{"Dividend Yield":<20}{div1:>11.2f}%{div2:>11.2f}%')
