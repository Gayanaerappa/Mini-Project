# Online Voting System Mini Project

voters = {}        # voter_id : has_voted
candidates = {
    "A": 0,
    "B": 0,
    "C": 0
}

# -------------------------
# Voter Registration
# -------------------------
def register_voter():
    voter_id = input("Enter Voter ID: ")

    if voter_id in voters:
        print("Voter already registered!")
    else:
        voters[voter_id] = False
        print("Voter registered successfully!")

# -------------------------
# Cast Vote
# -------------------------
def cast_vote():
    voter_id = input("Enter your Voter ID: ")

    if voter_id not in voters:
        print("Voter not registered!")
        return

    if voters[voter_id] == True:
        print("You have already voted!")
        return

    print("\nCandidates:")
    for c in candidates:
        print(c)

    choice = input("Enter candidate name: ").upper()

    if choice in candidates:
        candidates[choice] += 1
        voters[voter_id] = True
        print("Vote cast successfully!")
    else:
        print("Invalid candidate!")

# -------------------------
# View Results
# -------------------------
def view_results():
    print("\n--- Voting Results ---")
    for c, votes in candidates.items():
        print(c, ":", votes)

# -------------------------
# Main Menu
# -------------------------
while True:
    print("\n===== ONLINE VOTING SYSTEM =====")
    print("1. Register Voter")
    print("2. Cast Vote")
    print("3. View Results")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register_voter()

    elif choice == "2":
        cast_vote()

    elif choice == "3":
        view_results()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")