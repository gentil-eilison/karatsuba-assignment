from timeit import default_timer as timer
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def karatsuba(x: int, y: int):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    x_high, x_low = divmod(x, 10**m)
    y_high, y_low = divmod(y, 10**m)

    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)

    return z2 * 10**(2 * m)+ ((z1 - z2 - z0) * 10**m) + z0


def run_test_python(test_name: str, num_a: int, num_b: int):
    test_start = timer()
    result = num_a * num_b
    test_end = timer()
    runtime_in_ms = (test_end - test_start) * 1000
    print(f"Test {test_name} with Python: {result:n} in {runtime_in_ms}")


def run_test_karatsuba(test_name: str, num_a: int, num_b: int):
    test_start = timer()
    result = karatsuba(num_a, num_b)
    test_end = timer()
    runtime_in_ms = (test_end - test_start) * 1000
    print(f"Test {test_name} with Karatsuba: {result:n} in {runtime_in_ms}")

# Teste 1 - Números com 10 dígitos
run_test_python("10 digit", 1234567890, 1234567890)
run_test_karatsuba("10 digit", 1234567890, 1234567890)

# Teste 2 - Números com 50 dígitos
run_test_python(
    "50 digit", 
    12345678901234567890123456789012345678901234567890, 
    12345678901234567890123456789012345678901234567890
)
run_test_karatsuba(
    "50 digit", 
    12345678901234567890123456789012345678901234567890, 
    12345678901234567890123456789012345678901234567890
)

# Teste 3 - Números com 100 dígitos
run_test_python(
    "100 digit", 
    1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890, 
    1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
)
run_test_karatsuba(
    "100 digit", 
    1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890,
    1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
)