import yfinance as yf

# STEP 1: Ask for two stocks and get their data
while True:
    a = input("Enter the first stock: ").strip().upper()
    b = input("Enter the second stock: ").strip().upper()

    if a == "" or b == "" or a == b:
        print("Please enter two different stock tickers.")
        continue

    try:
        s1 = yf.Ticker(a)
        s2 = yf.Ticker(b)
        info1 = s1.info
        info2 = s2.info
    except Exception:
        print("Could not get stock data. Please try again.")
        continue

    t_pe1 = info1.get("trailingPE")
    t_pe2 = info2.get("trailingPE")
    f_pe1 = info1.get("forwardPE")
    f_pe2 = info2.get("forwardPE")
    rev1 = info1.get("revenueGrowth")
    rev2 = info2.get("revenueGrowth")

    if (t_pe1 is None or t_pe2 is None or
        f_pe1 is None or f_pe2 is None or
        rev1 is None or rev2 is None):
        print("Invalid ticker or missing financial data. Try again.")
        continue

    if t_pe1 <= 0 or t_pe2 <= 0 or f_pe1 <= 0 or f_pe2 <= 0:
        print("This version only compares stocks with positive P/E ratios.")
        continue

    break

print("Stock data loaded successfully!")


# STEP 2: Show a comparison table

div1 = info1.get("dividendYield")
div2 = info2.get("dividendYield")


# Ignore suspicious or missing values
if div1 is not None and (div1 < 0 or div1 > 20):
    div1 = None

if div2 is not None and (div2 < 0 or div2 > 20):
    div2 = None

# Format dividend yields
if div1 is None:
    div_text1 = "N/A"
else:
    div_text1 = f"{div1:.2f}%"

if div2 is None:
    div_text2 = "N/A"
else:
    div_text2 = f"{div2:.2f}%"

print(f"\n{'Metric':<20}{a:>12}{b:>12}")
print("-" * 44)

print(f"{'Trailing P/E':<20}{t_pe1:>12.2f}{t_pe2:>12.2f}")
print(f"{'Forward P/E':<20}{f_pe1:>12.2f}{f_pe2:>12.2f}")
print(f"{'Revenue Growth':<20}{rev1 * 100:>11.2f}%{rev2 * 100:>11.2f}%")
print(f"{'Dividend Yield':<20}{div_text1:>12}{div_text2:>12}")
