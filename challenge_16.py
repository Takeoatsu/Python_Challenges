def consecutive_zeros(number):
    zeros = 0
    cache = 0
    for cero in number:
        if cero == "0":
            zeros += 1
            if zeros > cache:
                cache = zeros
        else:
                zeros = 0
    return cache 

print(consecutive_zeros("1001101000110"))