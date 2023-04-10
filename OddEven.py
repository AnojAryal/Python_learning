def odd_or_even():
  user_number = int(input("Let's check if a number is odd or even! Please enter one: "))
  if (user_number % 4 == 0):
    print('{} is even and a multiple of 4'.format(user_number))
  elif (user_number % 2 == 0):
    print('{} is even!'.format(user_number))
  else:
    print('{} is odd'.format(user_number))
  num = int(input("Let's divide numbers and check if they are odd or even. Enter a dividend: "))
  check = int(input("Please enter a divisor: "))
  if num % 2 == 0:
    print('{} and {} divide evenly'.format(num, check))
  else:
    print("{} and {} don't divide evenly".format(num, check))


odd_or_even()