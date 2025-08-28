import tkinter as tk  # Import tkinter for GUI components
from tkinter import messagebox  # Import messagebox for displaying error dialogs

import yfinance as yf  # Import yfinance to fetch stock data
import matplotlib.pyplot as plt  # Import matplotlib for plotting charts
import matplotlib.dates as mdates  # Import date formatting for x-axis
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Embed matplotlib charts in tkinter

class CandlestickChart:
    """Class to create and manage the candlestick chart GUI."""

    def __init__(self, root):
        """Initialize the GUI, widgets, and chart area."""
        self.root = root  # Store the root window
        self.root.title("Stock Candlestick Chart")  # Set window title
        self.root.geometry("1200x800")  # Set window size
        self.root.configure(bg="#2b2b2b")  # Set background color

        plt.style.use('dark_background')  # Use dark style for matplotlib

        # Create a frame for controls (ticker, dates, button)
        control_frame = tk.Frame(self.root, bg="#2b2b2b")
        control_frame.pack(pady=10)  # Add padding above controls

        # Stock ticker label and entry
        tk.Label(control_frame, text="Stock Ticker:", font=("Arial", 12), bg="#2b2b2b", fg="white").grid(row=0, column=0, padx=5)
        self.ticker_var = tk.StringVar(value="AAPL")  # Default ticker
        ticker_entry = tk.Entry(control_frame, textvariable=self.ticker_var, width=10, font=("Arial", 12), bg="#404040", fg="white", insertbackground="white")
        ticker_entry.grid(row=0, column=1, padx=5)

        # Start date label and entry
        tk.Label(control_frame, text="Start Date:", font=("Arial", 12), bg="#2b2b2b", fg="white").grid(row=0, column=2, padx=5)
        self.start_var = tk.StringVar(value="2023-01-01")  # Default start date
        start_entry = tk.Entry(control_frame, textvariable=self.start_var, width=12, font=("Arial", 12), bg="#404040", fg="white", insertbackground="white")
        start_entry.grid(row=0, column=3, padx=5)

        # End date label and entry
        tk.Label(control_frame, text="End Date:", font=("Arial", 12), bg="#2b2b2b", fg="white").grid(row=0, column=4, padx=5)
        self.end_var = tk.StringVar(value="2024-01-01")  # Default end date
        end_entry = tk.Entry(control_frame, textvariable=self.end_var, width=12, font=("Arial", 12), bg="#404040", fg="white", insertbackground="white")
        end_entry.grid(row=0, column=5, padx=5)

        # Button to load chart
        load_btn = tk.Button(control_frame, text="Load Chart", command=self.load_chart,
                            bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=20)
        load_btn.grid(row=0, column=6, padx=10)

        # Frame for the chart itself
        chart_frame = tk.Frame(self.root, bg="#2b2b2b")
        chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create matplotlib figure and axis
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        # Embed the matplotlib figure in the tkinter window
        self.canvas = FigureCanvasTkAgg(self.fig, chart_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.load_chart()  # Load initial chart with default values

    def load_chart(self):
        """Fetch stock data and update the candlestick chart."""
        try:
            ticker = self.ticker_var.get().upper()  # Get ticker from entry
            start_date = self.start_var.get()  # Get start date from entry
            end_date = self.end_var.get()  # Get end date from entry

            stock = yf.Ticker(ticker)  # Create yfinance ticker object
            data = stock.history(start=start_date, end=end_date)  # Fetch historical data

            if data.empty:
                # Show error if no data is returned
                messagebox.showerror("Error", f"No data found for ticker {ticker}")
                return

            self.create_candlestick_chart(data, ticker)  # Draw the chart

        except Exception as e:
            # Show error if fetching or plotting fails
            messagebox.showerror("Error", f"Failed to load data: {str(e)}")

    def create_candlestick_chart(self, data, ticker):
        """Draw the candlestick chart using the fetched data."""
        self.ax.clear()  # Clear previous chart

        # Extract columns for plotting
        dates = data.index  # Dates for x-axis
        opens = data['Open']  # Opening prices
        highs = data['High']  # High prices
        lows = data['Low']  # Low prices
        closes = data['Close']  # Closing prices

        # Identify up days (close >= open) and down days (close < open)
        up_days = closes >= opens
        down_days = closes < opens

        width = 0.6  # Width of candlestick body
        width2 = 0.05  # Width of wicks

        up_color = '#26a69a'  # Color for up days (greenish)
        down_color = '#ef5350'  # Color for down days (red)

        # Plot up days candlesticks
        self.ax.bar(dates[up_days], closes[up_days] - opens[up_days], width,
                   bottom=opens[up_days], color=up_color, alpha=0.8)  # Body
        self.ax.bar(dates[up_days], highs[up_days] - closes[up_days], width2,
                   bottom=closes[up_days], color=up_color)  # Upper wick
        self.ax.bar(dates[up_days], opens[up_days] - lows[up_days], width2,
                   bottom=lows[up_days], color=up_color)  # Lower wick

        # Plot down days candlesticks
        self.ax.bar(dates[down_days], opens[down_days] - closes[down_days], width,
                   bottom=closes[down_days], color=down_color, alpha=0.8)  # Body
        self.ax.bar(dates[down_days], highs[down_days] - opens[down_days], width2,
                   bottom=opens[down_days], color=down_color)  # Upper wick
        self.ax.bar(dates[down_days], closes[down_days] - lows[down_days], width2,
                   bottom=lows[down_days], color=down_color)  # Lower wick

        # Set chart title and labels
        self.ax.set_title(f'{ticker} Stock Price', fontsize=16, fontweight='bold', pad=20)
        self.ax.set_ylabel('Price ($)', fontsize=12)
        self.ax.set_xlabel('Date', fontsize=12)

        # Format x-axis for dates
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        self.ax.xaxis.set_major_locator(mdates.MonthLocator())

        self.fig.autofmt_xdate()  # Auto-format date labels
        self.ax.grid(True, alpha=0.3)  # Add grid lines

        self.fig.tight_layout()  # Adjust layout to fit
        self.canvas.draw()  # Render the chart in the GUI

if __name__ == "__main__":
    # Entry point: create the main window and start the GUI loop
    root = tk.Tk()  # Create tkinter root window
    app = CandlestickChart(root)  # Instantiate the chart app
    root.mainloop()  # Start the event loop