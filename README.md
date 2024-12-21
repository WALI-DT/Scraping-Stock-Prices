# STOCK DATA
**Project Title: Automated Stock Data Scraping from Yahoo Finance**

**Overview:**
This project utilizes Python to scrape key stock information from **Yahoo Finance**, providing essential data to inform a dollar-cost averaging investment strategy. The code has been automated to run from Monday to Friday, ensuring up-to-date insights on selected stocks. By leveraging Python libraries such as `requests`, `BeautifulSoup`, and `pandas`, the project efficiently collects, processes, and saves stock data for analysis and decision-making.

The Python code used for the scraping process is contained in the **`stock_data.py`** file, and the resulting structured data is provided in the **`result_data.csv`** file.

---

**Data Extracted:**
1. **Stock Name:** The name or ticker symbol of the stock.
2. **Previous Day Closing Price:** The price at which the stock closed the previous trading day.
3. **24-Hour Movement:** The absolute change in stock price over the last 24 hours.
4. **Percentage Movement:** The percentage change in stock price over the last 24 hours.

---

**Libraries Used and Their Roles:**
1. **`requests`:** Sends HTTP requests to fetch web content from Yahoo Finance.
2. **`bs4` with `BeautifulSoup`:** Parses and extracts relevant data from the HTML content retrieved by `requests`.
3. **`pandas`:** Converts the extracted data into a structured DataFrame and saves it as a CSV file for easy access and analysis.

---

**Project Files:**
- **`stock_data.py`**: Contains the Python code used for scraping and processing stock data.
- **`result_data.csv`**: Stores the cleaned and structured data extracted during the web scraping process.

---

**Purpose:**
The project aims to support a dollar-cost averaging strategy by providing timely and accurate stock data. By automating the data collection process, it ensures consistent updates on stock performance, enabling informed investment decisions. Whether you're a technical professional exploring Python web scraping or a non-technical investor seeking actionable insights, this project showcases the seamless integration of automation and data analysis.

**Explore the files to see how Python can streamline stock market analysis and investment strategies!**


