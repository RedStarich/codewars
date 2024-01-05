def tribonacci(signature, n):
    first = signature[0]
    second = signature[1]
    third = signature[2]
    fourth = 0
    ans = []
    
    if n<=3:
        for i in range(n):
            ans.append(signature[i])
    else:
        ans = [first, second, third]
        for i in range(n-3):
            fourth = first + second + third
            first = second
            second = third
            third = fourth
            ans.append(fourth)
    return ans