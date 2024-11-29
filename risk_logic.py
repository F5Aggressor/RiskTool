def calculate_positions(portfolio_size, risk_percentage, entry_price):
    """
    Calculate position sizes, USD values, and stop-loss prices for given portfolio size, risk, and entry price.
    """
    # Calculate dollar risk
    dollar_risk = portfolio_size * (risk_percentage / 100)

    # Calculate positions and stop-loss
    positions = {
        "5%": {
            "shares": round(portfolio_size * 0.05 / entry_price),
            "value": round(portfolio_size * 0.05),
        },
        "10%": {
            "shares": round(portfolio_size * 0.10 / entry_price),
            "value": round(portfolio_size * 0.10),
        },
        "20%": {
            "shares": round(portfolio_size * 0.20 / entry_price),
            "value": round(portfolio_size * 0.20),
        },
    }

    # Calculate stop-loss prices
    for key, data in positions.items():
        stop_loss_distance = dollar_risk / data["shares"]
        data["stop_loss_price"] = round(entry_price - stop_loss_distance, 2)

    return positions, dollar_risk
