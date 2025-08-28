# Stock Candlestick Chart GUI (Tkinter + Matplotlib + yfinance)

This project is a Python desktop application that displays interactive candlestick charts for stock prices. It uses **Tkinter** for the GUI, **Matplotlib** for charting, and **yfinance** to fetch historical stock data.

---

## Features

- Enter any stock ticker (e.g., `AAPL`, `MSFT`, `GOOG`)
- Select start and end dates for the chart
- View candlestick charts with color-coded up/down days
- Responsive, dark-themed interface

---

## Installation

1. **Clone or Download the Repository**

   Download the code to your local machine.

2. **Install Required Python Packages**

   Open a terminal in the project directory and run:

   ```sh
   pip install yfinance matplotlib
   ```

   > **Note:** Tkinter comes pre-installed with most Python distributions.

---

## How to Run

1. Open a terminal and navigate to the project folder (where `main.py` is located):

   ```sh
   cd path/to/project/TKinter
   ```

2. Run the application:

   ```sh
   python main.py
   ```

   The GUI window will open. Enter a stock ticker and date range, then click **Load Chart** to view the candlestick chart.

---

## Code Overview

### Main Components

- **Tkinter GUI:** Provides input fields for ticker, start date, end date, and a button to load the chart.
- **Matplotlib Chart:** Embedded inside the Tkinter window to display candlestick charts.
- **yfinance:** Fetches historical stock data for the selected ticker and date range.

### File Structure

- `main.py` — Main application file containing all logic and GUI code.

### Key Classes & Functions

#### `CandlestickChart`

- **Purpose:** Manages the GUI and chart rendering.
- **Constructor (`__init__`):**
  - Sets up the main window, input fields, and chart area.
  - Initializes the chart with default values (`AAPL`, `2023-01-01` to `2024-01-01`).

- **`load_chart` Method:**
  - Reads user input for ticker and dates.
  - Fetches stock data using yfinance.
  - Handles errors (e.g., invalid ticker, no data).
  - Calls `create_candlestick_chart` to draw the chart.

- **`create_candlestick_chart` Method:**
  - Clears previous chart.
  - Plots candlestick bars for each day:
    - **Up days:** Close >= Open (greenish color)
    - **Down days:** Close < Open (red color)
  - Adds wicks for high/low prices.
  - Sets chart title, axis labels, and formats date axis.
  - Renders the chart in the GUI.

#### Main Entry Point

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = CandlestickChart(root)
    root.mainloop()
```
- Starts the Tkinter event loop and launches the application.

---

## Example Usage

1. Enter a stock ticker (e.g., `TSLA`)
2. Set a start date (e.g., `2024-01-01`)
3. Set an end date (e.g., `2024-08-01`)
4. Click **Load Chart** to view the candlestick chart for Tesla in 2024.

---

## Troubleshooting

- **Missing Dependencies:**  
  If you see `ModuleNotFoundError`, make sure you installed all required packages:

  ```sh
  pip install yfinance matplotlib
  ```

- **Permission Errors:**  
  Try installing with the `--user` flag:

  ```sh
  pip install --user yfinance matplotlib
  ```

- **Tkinter Not Found:**  
  On some Linux systems, you may need to install Tkinter separately:

  ```sh
  sudo apt-get install python3-tk
  ```

---

## License

This project is provided for educational purposes.

---

## Author

Created by Anil Raut.  
Feel free to modify
