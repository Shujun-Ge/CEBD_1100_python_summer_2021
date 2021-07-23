#  “Tip Calculator” program that calculates the price per person for a meal.

# Input: 1. The number of diners
#        2. The price of the meal before tax
#        3. The tip percentage

# Output: 1. The number of diners
#         2. The price of the meal before tax
#         3. The Quebec tax added (Federal)
#         4. The Quebec tax added (Provincial)
#         5. The total including tax
#         6. The tip amount (Based on the price before tax)
#         7. The grand total including tax
#         8. The amount owed per person


# Product Description
print("Hi, this is Tip Calculator. We will help you calculate the price per person for a meal.")

# Set Delimiter
num_stars = 65  # The length of the Delimiter
bar_of_stars = "*" * num_stars
print(bar_of_stars)  # Delimiter

print("Please enter the following information.")

loop_init_1 = 1  # Loop Controller of Input of The number of diners Input
loop_init_2 = 1  # Loop Controller of Input of The price of the meal before tax
loop_init_3 = 1  # Loop Controller of Input of The tip percentage

while loop_init_1:
    # Input Begin:
    try:
        num_din = int(input("The number of diners : "))  # Input the number of diners
        assert num_din > 0
    except AssertionError as p_error:
        print("Sorry, please enter a positive number.")
    except ValueError as v_error:
        print("Sorry, invalid input! Please re-enter The Number Of Diners.")
        print(bar_of_stars)  # Delimiter

    else:
        loop_init_1 = 0  # Stop Loop of Input of The number of diners Input
        while loop_init_2:
            try:
                price_o = float(input("The price of the meal before tax : "))  # Input The price of the meal before tax
                assert price_o >= 0
            except AssertionError as p_error:
                print("Sorry, please enter a positive number.")
            except ValueError as v_error:
                print("Sorry, invalid input! Please re-enter The Price Of The Meal Before Tax.")
                print(bar_of_stars)  # Delimiter

            else:
                loop_init_2 = 0  # Stop Loop of Input of The price of the meal before tax
                while loop_init_3:
                    try:
                        tip_level = input("The tip percentage : ")  # Input The tip percentage
                        assert tip_level.upper() == "A" or tip_level.upper() == "B" or tip_level.upper() == "C" or tip_level.upper() == "D"
                    except AssertionError as a_error:
                        print("Sorry, invalid input! Please re-enter The Tip Percentage.")
                        print("Please use A(Exceptional Service), B(Good service), C(Basic service), D(Horrible) "
                              "as the tip percentage input.")
                        print(bar_of_stars)  # Delimiter

                    # Input End

                    else:
                        loop_init_3 = 0  # Stop Loop of Input of The tip percentage
                        print(bar_of_stars)  # Delimiter

                        # Calculate Begin:
                        gst = 0.05  # The Quebec tax (Federal)
                        pst = 0.09975  # The Quebec tax (Provincial)
                        price_gst = price_o * gst  # Calculate the Quebec tax added (Federal)
                        price_pst = price_o * pst  # Calculate the Quebec tax added (Provincial)
                        price_notip = price_o + price_gst + price_pst  # Calculate the total including tax

                        # Tip amount calculation
                        if tip_level.upper() == "A":
                            amount_tip = price_o * 0.2
                        elif tip_level.upper() == "B":
                            amount_tip = price_o * 0.15
                        elif tip_level.upper() == "C":
                            amount_tip = price_o * 0.1
                        elif tip_level.upper() == "D":
                            amount_tip = price_o * 0
                        else:
                            print("Wrong Input")

                        price_all = price_notip + amount_tip  # Calculate the grand total including tax
                        price_person = price_all / num_din  # Calculate the amount owed per person

                        print(bar_of_stars)  # Delimiter
                        # All Calculation End

                        # Display Results:
                        print("Calculation Results:")
                        print(bar_of_stars)  # Delimiter

                        print("The number of dinners is : \t\t\t\t\t\t\t\t {:d}".format(num_din))
                        print("The price of the meal before tax is : \t\t\t\t\t ${:.2f}".format(price_o))
                        print("The Quebec tax added (Federal) is : \t\t\t\t\t ${:.2f}".format(price_gst))
                        print("The Quebec tax added (Provincial) is : \t\t\t\t\t ${:.2f}".format(price_pst))
                        print("The total including tax is : \t\t\t\t\t\t\t ${:.2f}".format(price_notip))
                        print("The tip amount (Based on the price before tax) is : \t ${:.2f}".format(amount_tip))
                        print("The grand total including tax is : \t\t\t\t\t\t ${:.2f}".format(price_all))
                        print("The amount owed per person is : \t\t\t\t\t\t ${:.2f}".format(price_person))

                        print(bar_of_stars)  # Delimiter
                        # Display End

print(bar_of_stars)  # Delimiter
print("Thank you for using our application！Have a good day!")