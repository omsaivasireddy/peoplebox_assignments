def calculate_product_sum(first_num, second_num):
    # Calculate product of numbers and add second number.
    product = first_num * second_num
    total = product + second_num
    return total

def calculate_numbers(first_num, second_num):
    # Calculate sum and product-sum of two numbers.
    sum_result = first_num + second_num
    product_sum = calculate_product_sum(first_num, second_num)
    return sum_result, product_sum