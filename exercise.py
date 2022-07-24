#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  first_digit = num // 100
  second_digit = num // 10 % 10
  third_digit = num % 10
  return first_digit + second_digit + third_digit


print(digits_sum(123))