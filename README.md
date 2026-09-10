# COMPT-TASK-3mmmmmbbbb
print("hello world")
def game_over(score):
    print("\n" + "=" * 30)
    print("       GAME OVER")
    print("=" * 30)
    print(f"Your final score is: {score}")
    print("Thank you for playing!\n")
    
    choice = input("Do you want to play again? (y/n): ").strip().lower()
    
    if choice == 'y':
        print("\nRestarting the game...\n")
        # Add your game restart code or function here
    else:
        print("\nGoodbye! Have a great day.")

# Example usage:
final_score = 1250
game_over(final_score)
