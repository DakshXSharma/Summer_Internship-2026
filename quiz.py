score = 0

ans = input("Capital of India: ")
if ans.lower() == "delhi":
    score += 1

ans = input("2 + 2 = ")
if ans == "4":
    score += 1

print("Score:", score)