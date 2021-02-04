from numpy import random

def totalLoans(loansAndRates):
    return round(sum([x for x, _, _ in loansAndRates]), 2)


def monthlyLoanGrowth(loansAndRates):
    newLR = []
    for l, r, id in loansAndRates:
        newLR.append([round(l*(1+r/12), 2), r, id])
    return newLR

def calculatePayment(x1, y1, x2, y2):
    return round(x1 - (x2*y2)/(y1), 2)


# Loans are payed by how much interest they are accruing
def interestOwed(loansAndRates, periodicalPayment):
    lri = sorted([[l*r, l, r, id] for l, r, id in loansAndRates], reverse=True)
    lri.append([0, 0, 1, -1])
    totalPayments = {}
    for i in range(len(lri) - 1):
        for j in range(i+1, 0, -1):
            _, x1, y1, id1 = lri[j-1]
            _, x2, y2, _ = lri[j]
            partialPayment = calculatePayment(x1, y1, x2, y2)
            lri[j-1][1] -= min(partialPayment, periodicalPayment)
            if id1 not in totalPayments:
                totalPayments[id1] = 0
            totalPayments[id1] += min(partialPayment, periodicalPayment)
            periodicalPayment -= min(partialPayment, periodicalPayment)

    sortedKeys = sorted(list(totalPayments.keys()))
    print("Payments on loans:")
    print([[x, totalPayments[x]] for x in sortedKeys])
    print("total:", round(sum(list(totalPayments.values())), 2))
    return [[round(l, 2), r, id] for _, l, r, id in lri[:-1]]


def assignIdentifiers(loansAndRates):
    p = 10**-2
    return [[s[0], s[1] * p, i] for i, s in enumerate(loansAndRates)]


# def bestWayToPayDownLoans(loansAndRates,paymentPerMonth):
#     loansAndRates= assignIdentifiers(loansAndRates)
#     months = 0
#     total = totalLoans(loansAndRates)
#     while (total > 0):
#         print(f"Month {months}:")
#         print(f"current total: {total}")
#         print(loansAndRates)
#         loansAndRates = bestWayToPay(loansAndRates, paymentPerMonth)
#         loansAndRates = monthlyLoanGrowth(loansAndRates)
#         months += 1
#         total = totalLoans(loansAndRates)
#         print()


def randomLoansAndRates(n=5):
    loansAndRates = []
    for i in range(n):
        loan = round(random.randint(1000,10000) + random.rand(), 2)
        rate = round(random.randint(3,20) + random.rand(), 2)
        loansAndRates.append((loan, rate))
    return loansAndRates


"""
Ways to pay loans:
    1) Pay 100% of monthly payment to a randomly picked loan each month, if
        more payment than loan, randomly choose another loan.
    2) Pay random amounts that add up to monthly payment, to a random loans
    3) Sort loans by rates and loan amounts, and pay off highest first
    4) Sort loans by rates and loan amounts, and pay off lowest first
    4) Sort loans by interest owed, and pay off loans with most interest owed first.
"""


# A way to simulate loan changes each month
def monthlySimulator(loansAndRates, paymentPerMonth, method):
    loansAndRates= assignIdentifiers(loansAndRates)
    months = [0]
    totals = [totalLoans(loansAndRates)]
    
    while (totals[-1] > 0):
        print(f"Month {months[-1]}:")
        print(f"current total: {totals[-1]}")
        loansAndRates = method(loansAndRates, paymentPerMonth)
        loansAndRates = monthlyLoanGrowth(loansAndRates)
        months.append(months[-1] + 1)
        totals.append(totalLoans(loansAndRates))
        print()
    
    return months, totals


# Random Loan Each Month
def randomMonthlyLoan(loansAndRates, periodicalPayment):
    return []


# Random amounts to each random loan each month
def randomAmountRandomLoan(loansAndRates, periodicalPayment):
    return []


# Pay off loans by highest interests first
def highestInterest(loansAndRates, periodicalPayment):
    return []


# Pay off loans by lowest interests first
def lowestInterest(loansAndRates, periodicalPayment):
    return []


def main():
    loansAndRates = [
        (6847.31, 3.86), 
        (7740.88, 4.66), 
        (1300.00, 4.66), 
        (4508.00, 4.29), 
        (3549.87, 4.29), 
        (8444.24, 3.76)
    ]
    
    # monthlySimulator(loansAndRates, 1500, interestOwed)
    monthlySimulator(loansAndRates, 1500, )

if __name__ == "__main__":
    main()


