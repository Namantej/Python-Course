#Weather Program
temperature = int(input("Enter Temperature: "))
forecast = input("Enter forecast: ")
if temperature > 80:
    print("Stay Inside!!")
    print("It's too hot")
elif forecast == "foggy" or forecast == "snowy":
    print("Its too cold!")
    print("Stay Inside!!")
else:
    print("Enjoy the outdoors")
