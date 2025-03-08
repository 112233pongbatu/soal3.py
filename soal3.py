def celsius_to_fahrenheit(c):
    return (9/5) * c + 32  

def celsius_to_reamur(c):
    return 0.8 * c 

test_cases = [100, 80, 0]

for c in test_cases:
    print(f"Input C = {c}")
    print(f"Output F = {celsius_to_fahrenheit(c)}")
    print(f"Output R = {celsius_to_reamur(c)}\n")
