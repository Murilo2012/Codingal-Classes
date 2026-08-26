# ==========================================================
# Classroom Points Calculator
# Codingal - Python Operators I
# ==========================================================

# ----------------------------------------------------------
# 1. ASSIGNMENT OPERATOR ( = )
#    The "=" operator stores a value inside a variable.
# ----------------------------------------------------------
team1 = 120
team2 = 95
team3 = 140
team4 = 110
team5 = 85

print("=== Classroom Points Calculator ===")
print("Team 1 points:", team1)
print("Team 2 points:", team2)
print("Team 3 points:", team3)
print("Team 4 points:", team4)
print("Team 5 points:", team5)
print()

# ----------------------------------------------------------
# 2. ARITHMETIC OPERATORS ( + and / )
#    "+" adds the points, "/" divides them to get the average.
# ----------------------------------------------------------
total = team1 + team2 + team3 + team4 + team5
average = total / 5

print("--- Arithmetic operators ---")
print("Total points:", total)
print("Average per team:", average)
print()

# ----------------------------------------------------------
# 3. REWARD STARS ( * )
#    Every point is worth 2 reward stars.
# ----------------------------------------------------------
stars_per_point = 2
reward_stars = total * stars_per_point

print("--- Reward stars ---")
print("Stars per point:", stars_per_point)
print("Total reward stars:", reward_stars)
print()

# ----------------------------------------------------------
# 4. FLOOR DIVISION ( // ) AND MODULUS ( % )
#    Stars are packed into boxes of 25.
#    "//" gives the number of full boxes.
#    "%"  gives the stars that are left over.
# ----------------------------------------------------------
boxes = reward_stars // 25
leftover = reward_stars % 25

print("--- Packing the stars into boxes of 25 ---")
print("Full boxes packed:", boxes)
print("Leftover stars:", leftover)
print()

# ----------------------------------------------------------
# 5. COMPARISON OPERATORS ( > , == , >= )
#    Comparisons always answer with True or False.
# ----------------------------------------------------------
last_week = 500

print("--- Comparing with last week ---")
print("Last week points:", last_week)
print("Is this week better than last week? (total > last_week):", total > last_week)
print("Is this week equal to last week? (total == last_week):", total == last_week)
print("Is this week at least as good?  (total >= last_week):", total >= last_week)
print()

# ----------------------------------------------------------
# 6. COMPOUND ASSIGNMENT OPERATORS ( += and -= )
#    "+=" adds to the variable, "-=" subtracts from it.
# ----------------------------------------------------------
print("--- Adjusting the total ---")

total += 30   # bonus points for good behaviour
print("After bonus points (+30):", total)

total -= 15   # penalty for missed tasks
print("After missed tasks (-15):", total)
print()

# ----------------------------------------------------------
#    Recalculate the rewards with the final total.
# ----------------------------------------------------------
reward_stars = total * stars_per_point
boxes = reward_stars // 25
leftover = reward_stars % 25

print("--- Final results ---")
print("Final total points:", total)
print("Final reward stars:", reward_stars)
print("Final boxes packed:", boxes)
print("Final leftover stars:", leftover)
