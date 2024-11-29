import tkinter as tk
from tkinter import messagebox
from risk_logic import calculate_positions

def calculate():
    try:
        # Get inputs
        portfolio_size = float(entry_portfolio_size.get())
        risk_percentage = float(entry_risk_percentage.get())
        entry_price = float(entry_entry_price.get())

        # Perform calculations
        positions, dollar_risk = calculate_positions(portfolio_size, risk_percentage, entry_price)

        # Display results
        result_text.set("")
        result_text.set("Results:\n")
        for key, data in positions.items():
            result_text.set(
                result_text.get()
                + f"{key} Position:\n"
                + f"  Shares: {data['shares']}, Value: ${data['value']}, Stop-Loss: ${data['stop_loss_price']}\n"
            )

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create main window
root = tk.Tk()
root.title("Risk and Position Sizing Tool (GUI)")

# Input Fields
tk.Label(root, text="Portfolio Size ($$$):").grid(row=0, column=0, padx=10, pady=5)
entry_portfolio_size = tk.Entry(root)
entry_portfolio_size.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Risk Percentage (%):").grid(row=1, column=0, padx=10, pady=5)
entry_risk_percentage = tk.Entry(root)
entry_risk_percentage.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Entry Price ($$$):").grid(row=2, column=0, padx=10, pady=5)
entry_entry_price = tk.Entry(root)
entry_entry_price.grid(row=2, column=1, padx=10, pady=5)

# Button to Calculate
tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

# Output Results
result_text = tk.StringVar(value="")
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
