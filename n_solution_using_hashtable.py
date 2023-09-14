def pairSum(arr, target):
    if len(arr) < 2:
        return

    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            print(f"{num}, {complement}")
        seen.add(num)

pairSum([1, 9, 5, 0, 20, -4, 12, 16, 7, 15, 3], 12)