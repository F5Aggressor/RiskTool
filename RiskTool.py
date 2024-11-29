def calculate_risk_position():
    print("Welcome to the Enhanced Risk and Position Sizing Tool\n")
    
    # Step 1: Get Portfolio Size and Trade Parameters
    portfolio_size = float(input("Enter your portfolio size (e.g., 217000): "))
    max_trade_size = float(input("Enter your max trade size (e.g., 20000): "))
    
    # Step 2: Choose Risk Level
    print("\nChoose your portfolio risk level:")
    print("1. Conservative (Green): 0.5% - 1%")
    print("2. Moderate (Yellow): 1% - 2%")
    print("3. Aggressive (Red/Orange): 2% - 5%")
    
    risk_level = int(input("Enter the number corresponding to your choice: "))
    if risk_level == 1:
        risk_percentage = float(input("Enter risk percentage (0.5 - 1): "))
        risk_color = "\033[92m"  # Green
    elif risk_level == 2:
        risk_percentage = float(input("Enter risk percentage (1 - 2): "))
        risk_color = "\033[93m"  # Yellow
    elif risk_level == 3:
        risk_percentage = float(input("Enter risk percentage (2 - 5): "))
        risk_color = "\033[91m"  # Red/Orange
    else:
        print("Invalid choice. Defaulting to Conservative (1%).")
        risk_percentage = 1
        risk_color = "\033[92m"  # Green
    
    print(f"\nYou selected: {risk_color}{risk_percentage}% Risk Level\033[0m\n")
    
    # Step 3: Get Entry Price
    entry_price = float(input("Enter the entry price of the trade: "))
    
    # Step 4: Calculate Risk Metrics
    risk_decimal = risk_percentage / 100
    dollar_risk = portfolio_size * risk_decimal
    stop_loss_distance = dollar_risk / max_trade_size
    stop_loss_percentage = (stop_loss_distance / entry_price) * 100

    # Step 5: Display Results
    print("\n--- Results ---")
    print(f"Dollar Risk: ${round(dollar_risk, 2)}")
    print(f"Recommended Stop-Loss Distance ($): ${round(stop_loss_distance, 2)}")
    print(f"Recommended Stop-Loss Percentage (%): {round(stop_loss_percentage, 2)}%")

# Run the tool
calculate_risk_position()

