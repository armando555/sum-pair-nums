def sum_pairs(arr,target):
    for i in arr:
        for j in arr:
            if i + j ==  target:
                print(f"{i}, {j}")

sum_pairs([1,9,5,0,20,-4,12,16,7,15,3],12)