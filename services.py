def calculate_discount(price, discount_percentage):
    """Calculates the discount amount."""
    # Check for invalid values
    if price < 0 or discount_percentage < 0:
        raise ValueError("Price and discount_percentage must be positive values.")
    return price * (discount_percentage / 100)

def final_price(price, discount_percentage):
    """Calculates the final price after discount."""
    # Check for invalid values
    if price < 0 or discount_percentage < 0:
        raise ValueError("Price and discount_percentage must be positive values.")
    discount = calculate_discount(price, discount_percentage)
    return price - discount