from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date(days):
    current = datetime.now()
    future_date = current + timedelta(days = days)
    return future_date.strftime("%Y-%m-%d")


def main():
    print(f"Current date and time: {display_current_datetime()}")
    number_of_days = int(input("Enter a number of days: "))
    future_date = calculate_future_date(number_of_days)
    print(f"Future date: {future_date}")
    
    

if __name__== "__main__":
    main()