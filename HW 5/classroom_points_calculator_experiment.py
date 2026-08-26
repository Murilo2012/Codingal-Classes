# ==========================================================
# Classroom Points Calculator - EXPERIMENT VERSION
# Codingal - Python Operators I (step 7: try your own values)
#
# What changed compared to the original file:
#   - different points for the five teams
#   - stars_per_point is now 3 instead of 2
#   - the boxes hold 10 stars instead of 25
# ==========================================================

# ----------------------------------------------------------
# 1. ASSIGNMENT OPERATOR ( = )
# ----------------------------------------------------------
team1 = 200
team2 = 75
team3 = 160
team4 = 90
team5 = 133

print("=== Classroom Points Calculator (experiment) ===")
print("Team 1 points:", team1)
print("Team 2 points:", team2)
print("Team 3 points:", team3)
print("Team 4 points:", team4)
print("Team 5 points:", team5)
print()

# ----------------------------------------------------------
# 2. ARITHMETIC OPERATORS ( + and / )
# ----------------------------------------------------------
total = team1 + team2 + team3 + team4 + team5
average = total / 5

print("--- Arithmetic operators ---")
print("Total points:", total)
print("Average per team:", average)
print()

# ----------------------------------------------------------
# 3. REWARD STARS ( * )  -> now every point is worth 3 stars
# ----------------------------------------------------------
stars_per_point = 3
reward_stars = total * stars_per_point

print("--- Reward stars ---")
print("Stars per point:", stars_per_point)
print("Total reward stars:", reward_stars)
print()

# ----------------------------------------------------------
# 4. FLOOR DIVISION ( // ) AND MODULUS ( % )
#    Now the boxes are smaller: 10 stars per box.
# ----------------------------------------------------------
box_size = 10
boxes = reward_stars // box_size
leftover = reward_stars % box_size

print("--- Packing the stars into boxes of", box_size, "---")
print("Full boxes packed:", boxes)
print("Leftover stars:", leftover)
print()

# ----------------------------------------------------------
# 5. COMPARISON OPERATORS ( > , == , >= )
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
boxes = reward_stars // box_size
leftover = reward_stars % box_size

print("--- Final results ---")
print("Final total points:", total)
print("Final reward stars:", reward_stars)
print("Final boxes packed:", boxes)
print("Final leftover stars:", leftover)
