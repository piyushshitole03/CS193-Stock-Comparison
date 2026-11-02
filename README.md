# Stock Comparison and Recommendation Tool

A Python-based stock comparison tool designed to help investors evaluate two publicly traded companies using financial metrics and make more informed investment decisions.

## The Problem

Whenever I research stocks to invest in, I often end up choosing between two promising companies with similar financial metrics but different valuations. This creates a dilemma when deciding which stock offers better investment value.

This project aims to simplify that decision by providing a structured comparison of important financial indicators.

## How It Works

The Stock Comparison and Recommendation Tool will retrieve financial data for two user-selected stocks using Yahoo Finance through the Python `yfinance` library.

My Minimum Viable Product (MVP) will include:

1. **Stock Input:** Allow users to enter two stock ticker symbols through a Python command-line interface.
2. **Financial Data Retrieval:** Use `yfinance` to retrieve trailing P/E ratios, forward P/E ratios, revenue growth, and dividend yields.
3. **Stock Comparison:** Display the financial metrics of both companies side by side to evaluate their relative valuations and growth.
4. **Dividend Preference:** Allow users to choose whether dividend yield should influence the recommendation.
5. **Stock Recommendation:** Implement a rules-based scoring system to recommend a stock based on financial metrics and explain the reasoning behind the result.
6. **Error Handling:** Handle invalid ticker symbols and missing financial information.

### System Architecture

![Stock Comparison System Diagram](docs/System%20Diagram.jpg)

The system will accept two stock ticker symbols, retrieve their financial information from Yahoo Finance, compare the available metrics, and provide an investment recommendation based on predefined criteria.

## Tech Stack

1. **Programming Language:** Python 3.12
2. **Python Libraries:** `yfinance`
3. **External Data Source:** Yahoo Finance, accessed through `yfinance`
4. **User Interface:** Command-Line Interface (CLI)
5. **Development Environment:** VS Code / PyCharm
6. **Data Storage:** No persistent storage required for Version 1.0.
7. **Version Control:** Git and GitHub

## Setup

**Status: Under Development**

The following instructions cover the initial Python environment setup. Instructions for running the completed application will be added during development.

**Prerequisites:**

- Python 3.12
- Git
- pip (Python package manager)

**Clone the repository:**

```bash
git clone https://github.com/piyushshitole03/CS193-Stock-Comparison.git
cd CS193-Stock-Comparison
```

**Install the required Python library (Windows):**

```powershell
py -3.12 -m pip install yfinance
```

The financial data source has already been tested by retrieving financial metrics for Microsoft and dividend information for Amazon.

Additional instructions for running the completed application will be provided as development progresses.

## Usage

**Status: Not Yet Implemented**

Once developed, users will be able to:

1. Start the application through their terminal.
2. Enter the ticker symbols of two stocks they wish to compare.
3. Choose whether dividend income should influence the recommendation.
4. View a comparison of trailing P/E, forward P/E, and revenue growth.
5. Receive a stock recommendation with an explanation of the factors behind the decision.

Detailed execution instructions and sample outputs will be added once the MVP is functional.

## Roadmap

### Version 1.0 — MVP

- [x] Set up the GitHub repository and initial project documentation.
- [x] Test financial data retrieval using `yfinance`.
- [ ] Implement financial data retrieval in the application.
- [ ] Accept and validate two stock ticker symbols.
- [ ] Display financial metrics in a readable comparison.
- [ ] Handle invalid ticker symbols and missing financial data.
- [ ] Implement a rules-based stock recommendation system.
- [ ] Include an optional dividend preference.
- [ ] Test the complete application and update documentation.

### Version 2.0 — Future Improvements

- [ ] Develop an interactive website using Streamlit.
- [ ] Add financial charts and stock performance visualizations.
- [ ] Implement Monte Carlo simulations for portfolio risk analysis.

## Project Documentation

The `docs/` directory contains the planning documents for this project, including:

- Eisenhower Matrix
- System Flowchart
- Editable draw.io System Diagram

## Current Development Status

The project is currently in its planning and initial development stage. Financial data retrieval has been successfully tested using `yfinance`, but the complete stock comparison and recommendation system has not yet been implemented.

## Limitations

- Financial information depends on the availability and accuracy of Yahoo Finance data.
- Certain companies may not have all financial indicators available.
- Recommendations will be based on predefined rules rather than predictions of future stock performance.
- Financial metrics alone cannot guarantee investment returns.

## Disclaimer

This application is being developed for educational purposes as part of CS 193 at Purdue University. Its recommendations are informational and should not be considered professional financial advice.

## Author

**Piyush Dhananjay Shitole**

GitHub: [https://github.com/piyushshitole03](https://github.com/piyushshitole03)
