from numpy import sort, loadtxt, isin

A, B = sort(loadtxt('day1/input.txt', int).T)

print(sum(abs(A-B)), sum(isin(B, A) * B))