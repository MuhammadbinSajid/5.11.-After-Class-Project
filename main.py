def shutdown():
    # Get user input
    user_input = input("Do you want to shut down the system? (yes/no): ").lower()
    
    # Check conditions
    if user_input == "yes":
        print("Shutting down...")
    elif user_input == "no":
        print("Abort shut down.")
    else:
        print("Sorry, invalid input.")

# Call the function to test it
shutdown()