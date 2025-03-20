import time

def main():
    print("\n🚀 Countdown to Liftoff 🚀\n")  
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    
    print("\n🚀 Liftoff! 🚀\n")

if __name__ == '__main__':
    main()
