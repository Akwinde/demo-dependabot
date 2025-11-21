"""
Currency conversion module with optimizations for performance and maintainability.
"""
from functools import lru_cache

# Constants for conversion rates (easier to update and maintain)
USD_TO_INR_RATE = 83.1


def validate_amount(amount):
    """
    Validate the input amount for currency conversion.
    
    Args:
        amount: The amount to validate
        
    Returns:
        float: The validated amount
        
    Raises:
        ValueError: If amount is invalid
        TypeError: If amount is not numeric
    """
    if amount is None:
        raise ValueError("Amount cannot be None")
    
    try:
        amount_float = float(amount)
    except (ValueError, TypeError) as e:
        raise TypeError(f"Amount must be numeric, got {type(amount).__name__}") from e
    
    if amount_float < 0:
        raise ValueError("Amount cannot be negative")
    
    return amount_float


@lru_cache(maxsize=128)
def usd_to_inr(usd):
    """
    Convert USD to INR with caching for improved performance.
    
    This function uses LRU cache to store results of frequently used conversions,
    reducing computation time for repeated calls with the same input.
    
    Args:
        usd: Amount in USD (must be numeric and non-negative)
        
    Returns:
        float: Equivalent amount in INR
        
    Raises:
        ValueError: If usd is None or negative
        TypeError: If usd is not numeric
    """
    validated_usd = validate_amount(usd)
    return validated_usd * USD_TO_INR_RATE


def main():
    """Main function to demonstrate currency conversion."""
    try:
        result = usd_to_inr(5)
        print(result)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())