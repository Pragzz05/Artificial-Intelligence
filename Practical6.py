import math

def alpha_beta(depth, index, is_max, values, a, b):
    if depth == 0:
        return values[index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth - 1, index * 2 + i, False, values, a, b)
            best = max(best, val)
            a = max(a, best)
            if b <= a:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth - 1, index * 2 + i, True, values, a, b)
            best = min(best, val)
            b = min(b, best)
            if b <= a:
                break
        return best


# --- Simple Input ---
d = int(input("Depth: "))
vals = list(map(int, input(f"Enter {2**d} values: ").split()))

result = alpha_beta(d, 0, True, vals, -math.inf, math.inf)
print("Result:", result)