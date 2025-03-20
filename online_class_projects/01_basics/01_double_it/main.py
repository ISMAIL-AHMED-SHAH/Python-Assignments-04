def main():
    print("\nWelcome to the Double It Program!")
    while True:
        try:
            curr_value = float(input("\nEnter a number: ")) 
            
            if curr_value >= 100:
                print("\n⚠ Warning: Please enter a number less than 100.")
                continue 

            while curr_value < 100:
                curr_value *= 2  # Double the value
                print(curr_value)  
            break  

        except ValueError:
            print("\n❌ Invalid input! Please enter a valid number.") 

if __name__ == '__main__':
    main()
