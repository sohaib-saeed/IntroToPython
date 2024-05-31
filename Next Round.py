def NextRound(n,k):
    count = 0
    scores = input().split()
    for score in scores:
        if (int(score) >= int(scores[k - 1])) and int(score) > 0:
            count += 1
    print(count)
n,k = input().split()
n = int(n)
k = int(k)
NextRound(n,k)

    