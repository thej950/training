s = input("Enter a string: ")
rev = s[::-1] 
if s == rev:
    print(f"{s} = {rev} → Palindrome")
else:
    print(f"{s} ≠ {rev} → Not a Palindrome")
