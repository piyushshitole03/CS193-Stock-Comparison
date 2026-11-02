Stock Comparison and Recommendation Tool

A Python-based stock comparison tool designed to help investors evaluate two stocks using financial metrics and make more informed investment decisions.

The Problem

Whenever I try to research a stock to invest in, I end up with 2 really good companies which have similar financial metrics, but different valuation. I want to address the difficulty of comparing these investments objectively and determining which stock might offer better value. 

Project Goal

The goal is to develop a simple command-line application that compares two publicly traded stocks using financial indicators. The program will provide an explainable, rules-based recommendation rather than relying on predictions of future stock prices.

MVP Features (Version 1.0)

Accept two stock ticker symbols from the user.

Retrieve financial information using Yahoo Finance.

Compare trailing P/E ratios, forward P/E ratios, and revenue growth.

Allow users to optionally prioritize dividend yield.

Generate a recommendation based on predefined financial criteria.

Explain the reasoning behind the recommendation.

Handle invalid stock symbols and unavailable financial data.

How It Works

The application will retrieve financial data for two user-selected stocks through the yfinance library and display their financial metrics side by side.

I plan to build a Python-based tool that takes two stock ticker symbols and retrieves their financial data using Yahoo finance. The program will compare key metrics such as trailing and forward P/E ratios and revenue growth to provide an explainable stock recommendation, with an optional preference for dividend income.

System Diagram

System Diagram.jpg

Tech Stack

Programming Language: Python 3.12

Financial Data Source: Yahoo Finance

External Library: yfinance

User Interface: Command-Line Interface (CLI)

Development Tools: VS Code / PyCharm

Version Control: Git and GitHub

Data Storage: No persistent storage required for the MVP.

Setup

The application is currently under development.

Python 3.12 is required. The financial data library can be installed using:

python -m pip install yfinance

Additional installation and execution instructions will be added as the application is developed and tested.

Usage

The planned application workflow is:

Start the Python application.

Enter two stock ticker symbols.

Select whether dividend income should influence the recommendation.

View a comparison of financial metrics.

Receive a stock recommendation with an explanation.

The complete application and verified usage instructions will be added during development.

Roadmap

Version 1.0 — MVP

Set up the project structure and Git repository.

Retrieve financial data for individual stocks.

Accept and validate two stock ticker symbols.

Display financial metrics in a comparison table.

Handle missing or invalid financial data.

Implement rules-based stock recommendations.

Include an optional dividend preference.

Test the application and improve documentation.

Version 2.0 — Future Improvements

Build an interactive website using Streamlit.

Add financial charts and visualizations.

Implement Monte Carlo simulations for portfolio risk analysis.

Project Documentation

The docs/ directory contains project planning materials:

Eisenhower Matrix

System Flowchart (PNG)

Editable System Diagram (draw.io)

Current Status

Project planning and initial data-source testing have been completed. Financial information retrieval has been tested using Python and yfinance. The full application has not yet been implemented.

Limitations

Financial data depends on Yahoo Finance availability.

Some companies may not have all required financial metrics.

Financial indicators do not guarantee future stock performance.

Recommendations will depend on predefined comparison rules.

Author

Piyush Dhananjay Shitole
GITHUB: https://github.com/piyushshitole03
