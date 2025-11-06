# Exchange rate constant
USD_TO_INR_RATE = 83.1

def usd_to_inr(usd):
    """
    Convert USD to INR (Indian Rupees).
    
    Args:
        usd: The amount in USD (must be a number)
        
    Returns:
        The equivalent amount in INR
        
    Raises:
        ValueError: If the input is not a valid number or is negative
    """
    # Check if input is None
    if usd is None:
        raise ValueError("Error: USD amount cannot be None. Please provide a valid number.")
    
    # Check if input is a number (int or float)
    if not isinstance(usd, (int, float)):
        raise ValueError(f"Error: Invalid input type. Please provide a valid number for USD amount, not '{type(usd).__name__}'.")
    
    # Check if input is negative
    if usd < 0:
        raise ValueError("Error: USD amount cannot be negative. Please provide a positive number.")
    
    # Perform the conversion
    return usd * USD_TO_INR_RATE

if __name__ == "__main__":
    try:
        result = usd_to_inr(5)
        print(result)
    except ValueError as e:
        print(e)