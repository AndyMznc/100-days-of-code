def is_prime(num):
    for index in range(1, num + 1):
        if not index == 1 and not index == num:
            if num % index == 0:
                return False

    return True


is_prime(73)
