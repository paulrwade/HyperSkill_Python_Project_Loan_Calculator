import argparse, math

parser = argparse.ArgumentParser(description="This program...")
parser.add_argument("--type", default="annuity")
parser.add_argument("--principal", default=0)
parser.add_argument("--payment", default=0)
parser.add_argument("--periods", default=0)
parser.add_argument("--interest", default=0)

args = parser.parse_args()

loan_type = str(args.type)
principal = float(args.principal)
payment = float(args.payment)
periods = int(args.periods)
interest = round(float(args.interest) / 100, 3)
monthly_interest = interest / 12

if interest is not None and interest > 0:

    if loan_type == "annuity":

        if principal > 0 and periods > 0 and payment == 0.0:

            # Calculate monthly payment

            payment = math.ceil(principal * (monthly_interest * ((1 + monthly_interest) ** periods)) \
                                / (((1 + monthly_interest) ** periods) - 1))

            print("\nYour annuity payment =", payment, "!")

            overpayment = (payment * periods) - principal

            print("Overpayment  =", overpayment)

        elif principal > 0 and payment > 0 and periods == 0:

            # # DEBUG CODE
            # print("INPUT VALUES:")
            # print("  principal =", str(principal))
            # print("  payment =", str(payment))
            # print("  period =", str(period))
            # print("  interest =", str(interest))
            # print("  monthly_interest =", str(monthly_interest))

            # Calculate loan period (in months)

            # # numerator = math.log(1 - (principal / (monthly_interest_rate * payment)))
            # numerator = 1 - (principal / (monthly_interest * payment))
            # print("numerator =", numerator)
            #
            # # denominator = math.log(1 + monthly_interest_rate)
            # denominator = 1 + monthly_interest
            # print("denominator =", denominator)

            # period = (-1 * numerator) / denominator

            # print("")

            numerator = payment
            # print("numerator = ", numerator)

            denominator = payment - monthly_interest * principal
            # print("denominator =", denominator)

            division_result = numerator / denominator
            # print("division result =", division_result)

            log_base = (1 + monthly_interest)
            # print("log_base =", log_base)

            periods = math.ceil(math.log((numerator / denominator), log_base))
            # print("Number of months now is: ", periods)

            number_of_years = math.floor(periods / 12)
            number_of_months = periods - (number_of_years * 12)

            print("\nIt will take", number_of_years, "years and", number_of_months, "months to repay this loan!")

            overpayment = (periods * payment) - principal

            print("Overpayment =", overpayment)

        elif payment > 0 and periods > 0 and principal == 0.00:

            principal = round(payment / ((monthly_interest * ((1 + monthly_interest) ** periods)) \
                                         / (((1 + monthly_interest) ** periods) - 1)))

            print("Your loan principal =", principal)

        else:

            print("Incorrect parameters")

    elif loan_type == "diff":

        # print("principal =", principal)

        if payment > 0 or principal <= 0 or periods <= 0 or interest <= 0:

            print("Incorrect parameters")

        else:

            total_of_payments = 0.0
            # month_range = periods + 1

            # print("")
            # print("******* DEBUG ********")
            # print("principal =", principal)
            # print("interest =", interest)
            # print("monthly_interest =", monthly_interest)
            # print("periods =", periods)
            # print("**********************")
            # print("")

            for current_month in range(periods):
                this_months_payment = math.ceil((principal / periods) + \
                                                (monthly_interest * (principal - (
                                                            (principal * (current_month + 1 - 1)) / periods))))

                total_of_payments += this_months_payment

                # print("")
                # print("******* DEBUG ********")
                # print("current_month =", current_month)
                # print("this_months_payment =", this_months_payment)
                # print("total_of_payments =", total_of_payments)
                # print("**********************")
                # print("")

                print("Month", current_month, ": payment is", this_months_payment)

            overpayment = total_of_payments - principal

            print("")
            print("Overpayment =", overpayment)

    else:

        print("Incorrect parameters")

else:

    print("Incorrect parameters")
