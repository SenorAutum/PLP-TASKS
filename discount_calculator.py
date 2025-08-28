# 1. Create a function named calculate_discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after the discount is applied, or the original price
               if the discount is less than 20%.
    """
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# 2. Prompt the user for input and use the function
try:
    # Get the original price from the user
    original_price = float(input("Enter the original price of the item: $"))

    # Get the discount percentage from the user
    discount_percentage = float(input("Enter the discount percentage (%): "))

    # Call the function with the user's input
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the final price, formatted to two decimal places
    if final_price != original_price:
        print(f"🎉 The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount was applied. The original price is: ${final_price:.2f}")

except ValueError:
    # Handle cases where the user enters non-numeric input
    print("Invalid input. Please enter valid numbers for the price and discount.")

