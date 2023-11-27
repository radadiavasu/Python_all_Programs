import time

SCRIPT = '''we want to make a multiply function that takes any number of arguments and is able to multiply them all together.

Type the exact paragraph: '''

def calculate_typing_speed(text, duration):
    words = len(text.split())
    minutes = duration / 60
    speed = words / minutes
    return speed

def main():   
    start_time = time.time()
    input(SCRIPT)
    end_time = time.time()
    calculated_time = end_time - start_time
    
    typing_speed = calculate_typing_speed(SCRIPT, calculated_time)
    print(f"Your typing speed is approximately {round(typing_speed)} words per minute.")
    
if __name__ == '__main__':
    main()