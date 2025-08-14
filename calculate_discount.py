# calculate_discount.py
# A program to calculate final price after discount (only if 20% or higher)

def calculate_discount(price, discount_percent):
    """
    Returns the final price after applying discount if discount is 20% or higher.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# --- Main Program ---
if __name__ == "__main__":
    print(" Welcome to the Discount Calculator!")
    try:
        # Prompt user for input
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))

        # Calculate final price
        final_price = calculate_discount(original_price, discount_percentage)

        # Display result
        if discount_percentage >= 20:
            print(f" Discount applied! The final price is: ${final_price:.2f}")
        else:
            print(f" No discount applied (less than 20%). The price remains: ${final_price:.2f}")

    except ValueError:
        print(" Invalid input! Please enter numeric values only.")