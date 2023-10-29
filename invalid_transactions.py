
"""
A transaction is possibly invalid if:

    the amount exceeds $1000, or;
    if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.
"""

def invalid_transactions(transactions):

    # get the length of the tranactions
    l = len(transactions)

    # create an array to store invalid transactions
    invalid = []

    for i in range(l):

        # get the details of the current transaction
        tx = transactions[i].split(',')
        tx_name = tx[0]
        tx_time = int(tx[1])
        tx_amount = int(tx[2])
        tx_city = tx[3]

        # check if loop is in last element in transactions
        if i == l-1:

            # get and compare the current tx with the prev tx
            prev = i-1
            tx_prev = transactions[prev].split(',')
            ptx_name = tx_prev[0]
            ptx_time = int(tx_prev[1])
            ptx_amount = int(tx_prev[2])
            ptx_city = tx_prev[3]

            if ( (tx_amount > 1000) or ( (abs(tx_time-ptx_time) <= 60) or (tx_name == ptx_name) or (tx_city != ptx_city) ) ):
                invalid.append(transactions[i])
            break

        # get and compare the current tx with the next tx
        nxt = i+1
        tx_next = transactions[nxt].split(',')
        ntx_name = tx_next[0]
        ntx_time = int(tx_next[1])
        ntx_amount = int(tx_next[2])
        ntx_city = tx_next[3]

        if ( (tx_amount > 1000) or ( (abs(tx_time-ntx_time) <= 60) or (tx_name == ntx_name) or (tx_city != ntx_city) ) ):
            invalid.append(transactions[i])

    return invalid


t = ["alice,20,800,mtv","alice,50,1200,mtv"]

#["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]

print(invalid_transactions(t))