

def setOP(set1, set2):
    union_set = set1 | set2
    iset = set1 & set2
    diffset1 = set1 - set2
    diffset2 = set2 - set1
    SymmDiff = set1 ^ set2
    return union_set, iset, diffset1, diffset2, SymmDiff

set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))

union_set, iset, diffset1, diffset2, SymmDiff = setOP(set1, set2)

print(f"\nUnion: {union_set}")
print(f"Intersection: {iset}")
print(f"Difference (Set1 - Set2): {diffset1}")
print(f"Difference (Set2 - Set1): {diffset2}")
print(f"Symmetric Difference: {SymmDiff}")
