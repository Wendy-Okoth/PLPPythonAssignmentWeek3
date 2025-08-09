# Week 3 Python Assignment
# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, it applies the discount.
    Otherwise, it returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function
    final_price = calculate_discount(price, discount_percent)

    # Display the result
    print(f"Final price: {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
