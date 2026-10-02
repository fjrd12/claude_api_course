"""
Module to calculate pi to various decimal places.
"""

from decimal import Decimal, getcontext


def calculate_pi(decimal_places=5):
    """
    Calculate pi to the specified number of decimal places.
    
    Uses the Machin formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        decimal_places (int): Number of decimal places to calculate (default: 5)
    
    Returns:
        Decimal: Pi calculated to the specified decimal places
    """
    # Set precision higher than needed to avoid rounding errors
    getcontext().prec = decimal_places + 10
    
    # Machin formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(Decimal(1) / Decimal(5)) - arctan(Decimal(1) / Decimal(239)))
    
    # Round to the specified number of decimal places
    return round(pi, decimal_places)


def arctan(x, num_terms=500):
    """
    Calculate arctan(x) using the Taylor series.
    
    arctan(x) = x - x^3/3 + x^5/5 - x^7/7 + ...
    
    Args:
        x (Decimal): The input value
        num_terms (int): Number of terms to use in the series (default: 500)
    
    Returns:
        Decimal: The arctan of x
    """
    power = x
    result = power
    
    for n in range(1, num_terms):
        power *= -x * x
        result += power / (2 * n + 1)
    
    return result


if __name__ == "__main__":
    # Example usage
    pi_value = calculate_pi(5)
    print(f"Pi to 5 decimal places: {pi_value}")
