from collections import Counter

def solve(n, a):
    """
    Solves a competitive programming problem.
    """
    # Example: Find the most frequent element in an array
    freq = Counter(a)
    return freq.most_common(1)[0][0]

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    result = solve(n, a)
    print(result)
