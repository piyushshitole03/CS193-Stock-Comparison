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
