from risk_logic import calculate_positions

def calculate_risk_position():
    print("Welcome to the Enhanced Risk and Position Sizing Tool (CLI)\n")

    # Input Portfolio Size
    portfolio_size = float(input("Enter your portfolio size ($$$): "))
    risk_percentage = float(input("Enter your portfolio risk percentage (e.g., 2 for 2%): "))
    entry_price = float(input("Enter the entry price of the trade ($$$): "))

    # Perform calculations
    positions, dollar_risk = calculate_positions(portfolio_size, risk_percentage, entry_price)

    # Display Results
    print("\n--- Results ---")
    print(f"Portfolio Size: ${portfolio_size:,}")
    print(f"Risk Percentage: {risk_percentage}%")
    print(f"Entry Price: ${entry_price}\n")
    print("Position Sizes, USD Values, and Stop-Loss Prices:")
    print(f"{'Position Size':<15} {'Position Value':<20} {'Stop-Loss Price':<20} {'Dollar Risk':<15}")
    for key, data in positions.items():
        print(
            f"{data['shares']:<15} ${data['value']:<20} ${data['stop_loss_price']:<20} ${dollar_risk:<15}"
        )
    print("\n")

if __name__ == "__main__":
    calculate_risk_position()
