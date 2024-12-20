from getCreditApprove import get_approval

data = [
        1,
        1,
        1,
        3,
        500,
        1,
        1,
        1,
        1,
        -4000,
        -300,
        1,
        1,
        1,
        1,
        3,
        3
    ]

print(data)
status_data=(get_approval(data))
print(status_data)