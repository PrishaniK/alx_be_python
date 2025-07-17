task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        base = f"Reminder: '{task}' is a high priority task "
    case "medium":
        base = f"Reminder: '{task}' is a medium priority task "
    case "low":
        base = f"Reminder: '{task}' is a low priority task "
    case _:
        base = f"Reminder: '{task}' has an unknown priority level "

if time_bound == "yes":
    print(f"{base}that requires immediate attention today!")
else:
    print(f"{base}Consider completing it when you have free time.")
