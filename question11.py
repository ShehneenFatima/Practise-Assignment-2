#Write a program that simulates coin tossing. For each toss of the coin, the program should
#print Heads or Tails. Let the program toss the coin 100 times, and count the number of times
#each side of the coin appears and then print the results. The program should call a separate
#function flip that takes no arguments and returns 0 for tails and 1 for heads. Note: To get
#random 1 or 0 you can import a random module and then use random.randint(0,1)
import random  # Import random module

def flip():
    """Simulate a coin flip. Returns 0 (Tails) or 1 (Heads)."""
    return random.randint(0, 1)

# Initialize counters
heads_count = 0
tails_count = 0

# Toss the coin 100 times
for _ in range(100):
    result = flip()
    if result == 1:
        print("Heads")
        heads_count += 1
    else:
        print("Tails")
        tails_count += 1

# Print final results
print("\nFinal Results:")
print(f"Heads appeared {heads_count} times.")
print(f"Tails appeared {tails_count} times.")

