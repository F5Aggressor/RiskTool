import tkinter as tk
from tkinter import ttk, messagebox

# Global variables to track intermediate data
portfolio_size = 0
risk_percentage = 0
stock_entry_price = 0
manual_position_size = 0
risk_type = "Portfolio Risk"

def step1_calculate_risk_levels():
    try:
        global portfolio_size, risk_type
        portfolio_size = float(entry_portfolio_size.get())
        risk_type = risk_type_var.get()

        # Display risk levels based on the selected risk type
        result_text.set(f"Risk Levels for Portfolio Size: ${portfolio_size:,}\n")
        if risk_type == "Portfolio Risk":
            result_text.set(result_text.get() + f"Conservative (1%): ${portfolio_size * 0.01:.2f}\n")
            result_text.set(result_text.get() + f"Moderate (2%): ${portfolio_size * 0.02:.2f}\n")
            result_text.set(result_text.get() + f"Aggressive (5%): ${portfolio_size * 0.05:.2f}\n")
        elif risk_type == "Trade Risk":
            trade_size = portfolio_size * 0.1  # Assuming 10% of portfolio size as max trade size
            result_text.set(result_text.get() + f"Conservative (0.5%-1%): ${trade_size * 0.005:.2f} - ${trade_size * 0.01:.2f}\n")
            result_text.set(result_text.get() + f"Moderate (1%-2%): ${trade_size * 0.01:.2f} - ${trade_size * 0.02:.2f}\n")
            result_text.set(result_text.get() + f"Aggressive (3%-5%): ${trade_size * 0.03:.2f} - ${trade_size * 0.05:.2f}\n")
        
        result_text.set(result_text.get() + "\nEnter Risk Percentage and Stock Entry Price, then click 'Calculate Position Sizes'.")
        
        # Enable the next input
        entry_risk_percentage.config(state="normal")
        entry_stock_price.config(state="normal")
        btn_step2.config(state="normal")
        btn_step1.config(state="disabled")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid portfolio size.")

def step2_calculate_position_sizes():
    try:
        global risk_percentage, stock_entry_price
        risk_percentage = float(entry_risk_percentage.get())
        stock_entry_price = float(entry_stock_price.get())

        # Perform calculations for position sizes
        result_text.set(f"Position Sizes for {risk_type} and Entry Price: ${stock_entry_price:.2f}\n")
        position_sizes = [0.02, 0.05, 0.10, 0.20]  # 2%, 5%, 10%, 20%

        for size in position_sizes:
            if risk_type == "Portfolio Risk":
                shares = (portfolio_size * size) // stock_entry_price
                value = shares * stock_entry_price
            elif risk_type == "Trade Risk":
                trade_size = portfolio_size * 0.1  # Assuming 10% of portfolio size as max trade size
                shares = (trade_size * size) // stock_entry_price
                value = shares * stock_entry_price

            result_text.set(
                result_text.get()
                + f"{int(size * 100)}% Position: {int(shares)} shares, Value: ${value:.2f}\n"
            )
        
        # Enable manual position size entry
        entry_manual_position_size.config(state="normal")
        btn_step3.config(state="normal")
        btn_step2.config(state="disabled")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid risk percentage and ticker price.")

def step3_display_loss_summary():
    try:
        global manual_position_size
        manual_position_size = float(entry_manual_position_size.get())

        # Generate loss summary at different price drops (e.g., 1%, 5%, 10%, 20%)
        price_drops = [0.01, 0.05, 0.10, 0.20]  # Representing 1%, 5%, 10%, 20% drops
        result_text.set("Loss Summary for Various Price Points:\n\n")
        result_text.set(
            result_text.get()
            + f"Trade Size: {manual_position_size} shares, Entry Price: ${stock_entry_price:.2f}\n\n"
        )
        
        for drop in price_drops:
            dropped_price = stock_entry_price * (1 - drop)
            loss_amount = manual_position_size * (stock_entry_price - dropped_price)
            result_text.set(
                result_text.get()
                + f"Price Drop: {int(drop * 100)}% -> Dropped Price: ${dropped_price:.2f}, "
                + f"Loss: ${loss_amount:.2f}\n"
            )
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid manual position size.")

def reset_app():
    """Reset all fields and results to initial state."""
    global portfolio_size, risk_percentage, stock_entry_price, manual_position_size, risk_type
    portfolio_size = 0
    risk_percentage = 0
    stock_entry_price = 0
    manual_position_size = 0
    risk_type = "Portfolio Risk"

    # Reset all input fields
    entry_portfolio_size.delete(0, tk.END)
    entry_risk_percentage.delete(0, tk.END)
    entry_stock_price.delete(0, tk.END)
    entry_manual_position_size.delete(0, tk.END)

    # Disable input fields and buttons except for the first step
    entry_risk_percentage.config(state="disabled")
    entry_stock_price.config(state="disabled")
    entry_manual_position_size.config(state="disabled")
    btn_step1.config(state="normal")
    btn_step2.config(state="disabled")
    btn_step3.config(state="disabled")

    # Clear result text
    result_text.set("")

# Create main window
root = tk.Tk()
root.title("Risk and Position Sizing Tool (GUI)")

# Step 1: Portfolio Size and Risk Type
tk.Label(root, text="Portfolio Size ($$$):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_portfolio_size = tk.Entry(root)
entry_portfolio_size.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Risk Type:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
risk_type_var = tk.StringVar(value="Portfolio Risk")
risk_type_dropdown = ttk.Combobox(root, textvariable=risk_type_var, values=["Portfolio Risk", "Trade Risk"], state="readonly")
risk_type_dropdown.grid(row=1, column=1, padx=10, pady=5)

btn_step1 = tk.Button(root, text="Calculate Risk Levels", command=step1_calculate_risk_levels)
btn_step1.grid(row=1, column=2, padx=10, pady=5)

# Step 2: Risk Percentage and Ticker Price
tk.Label(root, text="Risk Percentage (%):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_risk_percentage = tk.Entry(root, state="disabled")
entry_risk_percentage.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Stock Entry Price (Ticker Price):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_stock_price = tk.Entry(root, state="disabled")
entry_stock_price.grid(row=3, column=1, padx=10, pady=5)

btn_step2 = tk.Button(root, text="Calculate Position Sizes", command=step2_calculate_position_sizes, state="disabled")
btn_step2.grid(row=3, column=2, padx=10, pady=5)

# Step 3: Manual Position Size and Loss Summary
tk.Label(root, text="Manual Position Size (Shares):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_manual_position_size = tk.Entry(root, state="disabled")
entry_manual_position_size.grid(row=4, column=1, padx=10, pady=5)

btn_step3 = tk.Button(root, text="Display Loss Summary", command=step3_display_loss_summary, state="disabled")
btn_step3.grid(row=4, column=2, padx=10, pady=5)

# Reset Button
btn_reset = tk.Button(root, text="Reset", command=reset_app)
btn_reset.grid(row=5, column=0, columnspan=3, pady=10)

# Output Results
result_text = tk.StringVar(value="")
result_label = tk.Label(root, textvariable=result_text, justify="left", anchor="w")
result_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10, sticky="w")

# Start the main loop
root.mainloop()

