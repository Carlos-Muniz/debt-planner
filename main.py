def totalLoans(loansAndRates):
    return round(sum([x for x, _, _ in loansAndRates]), 2)


def monthlyLoanGrowth(loansAndRates):
    newLR = []
    for l, r, id in loansAndRates:
        newLR.append([round(l*(1+r/12), 2), r, id])
    return newLR

def calculatePayment(x1, y1, x2, y2):
    return round(x1 - (x2*y2)/(y1), 2)


def bestWayToPay(loansAndRates, periodicalPayment):
   
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


def bestWayToPayDownLoans(loansAndRates,paymentPerMonth):
    loansAndRates= assignIdentifiers(loansAndRates)
    months = 0
    total = totalLoans(loansAndRates)
    while (total > 0):
        print(f"Month {months}:")
        print(f"current total: {total}")
        print(loansAndRates)
        loansAndRates = bestWayToPay(loansAndRates, paymentPerMonth)
        loansAndRates = monthlyLoanGrowth(loansAndRates)
        months += 1
        total = totalLoans(loansAndRates)
        print()
    



def main():
    loansAndRates = [
        (6847.31, 3.86), 
        (7740.88, 4.66), 
        (1300.00, 4.66), 
        (4508.00, 4.29), 
        (3549.87, 4.29), 
        (8444.24, 3.76)
    ]
    
    bestWayToPayDownLoans(loansAndRates, 1500)

if __name__ == "__main__":
    main()


