def user_input(input1):
    while True:
        try:
            value = float(input(input1))
            if value > 0:
                return value
            else:
                print(" enter a positive value.")
        except ValueError:
            print("Invalid input.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    while True:
       print("BMI Calculator")
       weight = user_input("Enter your weight in kilograms: ")
       height = user_input("Enter your height in meters: ")
    
       bmi = calculate_bmi(weight, height)
       category = bmi_category(bmi)
    
       print(f"Your BMI is: {bmi:.2f}")
       print(f"Category: {category}")

if __name__ == "__main__":
    main()

