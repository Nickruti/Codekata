user_input_a, user_input_b, user_input_c = input().split()

try:
  P = float(user_input_a)
  T = float(user_input_b)
  R = float(user_input_c)
  S_I = (P*T*R)/100
  print("{:.2f}".format(S_I))
except ValueError:
  print("Not a number")