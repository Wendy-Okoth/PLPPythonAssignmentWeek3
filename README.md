
# Week 3 Python Assignment

## Task Description
This program calculates the final price of an item after applying a discount.  
It uses a function named `calculate_discount(price, discount_percent)` that:
- Takes the original price and discount percentage as parameters.
- Applies the discount **only if it is 20% or higher**.
- Returns the final price if a discount is applied; otherwise, it returns the original price.

## How It Works
1. The program **prompts the user** to enter:
   - The original price of the item.
   - The discount percentage.
2. The program **calls the `calculate_discount()` function** to determine the final price.
3. The final price is **displayed with two decimal places**.
4. If the user enters non-numeric values, an error message is displayed.

## Code Structure
```python
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price
