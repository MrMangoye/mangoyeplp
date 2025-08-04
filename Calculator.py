print("🔢 Welcome to the Super Simple Calculator!")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    sum_result = round(num1 + num2, 2)
    difference_result = round(num1 - num2, 2)
    product_result = round(num1 * num2, 2)
    
    # Safe division with check
    if num2 != 0:
        quotient_result = round(num1 / num2, 2)
    else:
        quotient_result = "Undefined (division by zero)"
    
    print("\n📊 Results of your two numbers:")
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")
    print(f"Product: {product_result}")
    print(f"Quotient: {quotient_result}")

except ValueError:
    print("❌ Oops! Please enter valid numbers.")
