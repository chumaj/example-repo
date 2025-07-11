# Capstone project 1:
# Implementing finance calculator
# allowing user to calculate investment or bond repayment,
# importing maths library to be use for calculation.
import math

# Finace Calculator UI
print("-------- Finance Calculator --------")
# Display calculation type that user can perform: Investment or Bond repayment
print(
    """Investment - to calculate the amount of
interest you'll earn on your investment.
Bond - to calculate the amount of interest
you'll have to pay on a home loan."""
)
print("-" * 30)

# Prompt the user to select the calculation type(investment or bond)
print("\nPlease indicate type of calculation to proceed: ")
calculation_type = input("Investment or Bond fromt he menu above: ").lower()
print("-" * 30)

# check if the user entered 'investment'
if calculation_type == "investment":
    print("\n--- Investment calculations ---")
    # Prompt the user to enter investment details.
    principal_amount = float(input("\nPlease enter your Principal Amount: "))
    annual_interest_rate = input("Please enter the interest rate:")
    time_period_years = float(
        input(
            """Please enter number of
    years you plan to invest: """
        )
    )
    print("-" * 30)

    # Prompt the user to enter interest rate type
    interest_rate_type = input(
        """Please select the type of interest you you 
    want: Simple or Compound: """
    ).lower()

    # removing a % sign in an input interest. e.g. 8% to 8
    # to ensure correct format for annual interest rate
    if "%" in annual_interest_rate:
        # using a replace function to replace % with empty string
        # then we cast the string to float.
        # then the interest rate is converted to
        # correct format for annual interest rate by dividing by 100
        # round of the converted interest rate to 2decimal, use round()
        interest_rate_converted = round(
            float(annual_interest_rate.replace("%", "")) / 100, 2
        )
    else:
        # if no percentage we convert diretly to annual interest rate
        # round of the converted interest rate to 2decimal, use round()

        interest_rate_converted = round(float(annual_interest_rate) / 100, 2)

    # calculating total accrued when simple interest is selected
    if interest_rate_type == "simple":
        total_accrued_amount_simple = float(
            principal_amount * (1 + 
              (interest_rate_converted * time_period_years))
        )
        print(" - " * 30)
        print(
            f"\nTotal amount when simple interest is applied:  R{
                round(total_accrued_amount_simple, 2)}"
        )
        print(
            f"Interest earned: R{total_accrued_amount_simple
                                   - principal_amount}"
        )

    # Calculating total accrued when compound interest is selected
    elif interest_rate_type == "compound":
        print(" - " * 30)
        # when calculating the compound interest we will use the math libary
        # by utiliing the math.pow() function.
        total_accrued_amount_compound = principal_amount * math.pow(
            (1 + interest_rate_converted), 
            time_period_years
        )
        print(
            f"\nTotal amount when compound interest is applied: R{round(
                total_accrued_amount_compound, 2)}"
        )
        print(
            f"Interest earned: R{round(
            (total_accrued_amount_compound-principal_amount), 2)}"
        )
    # handling exception when a user have not inputted simple/compound.
    else:
        print("\nyou have entered invalid interest type")
        print("Enter either simple or compound")

# this elif check if th user enterd bond
elif calculation_type == "bond":
    print("-" * 30)
    print("--- Bond Repayment calculations ---")

    # prompting the user to input values that will be
    # use for calculating the bond repayments
    bond_present_value = float(
        input(
            """\nPlease enter 
    the present value of the house: """
        )
    )
    bond_interest_rate = input("Please enter your bond interest rate: ")
    bond_repayment_period = int(
        input("Please enter your repayment period in years: "))

    # removing the percentage sign when the user enter a interest value with %
    # then convert the interest rate into decimals, by /100
    # the cast it to float before rounding of 2decimals
    if "%" in bond_interest_rate:
        bond_interest_rate_converted = round(
            float(bond_interest_rate.replace("%", "")) / 100, 2
        )
    else:
        # if no % present, 
        # We convert the user inputted annual interest to decimals, by dividing 100
        # Then cast the string to float.
        # Then round of into 2decimals
        bond_interest_rate_converted = round(float(
            bond_interest_rate) / 100, 2)
    # calculation of repayments,
    #dividing the montly rates by divinf annual interest rate by 12
    repayment = ((bond_interest_rate_converted / 12) * bond_present_value) / (
        1 - (1 + ((bond_interest_rate_converted) / 12)) 
        ** (-bond_repayment_period)
    )
    print("-" * 30)

    print(f"\nYour monthly repayment is: R{round(repayment, 2)}")
    # handling exception
else:
    print("\nYou have entered invalid option")
print("-" * 30)
