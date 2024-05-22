def Team(n):
    team = []
    count = 0
    sum = 0
    for i in range(n):
        surety = str(input()).split() # 0 or 1
        team.append(surety)
    for i in range(n):
        for j in range(3):
             sum += int(team[i][j])
        if sum >= 2:
            count += 1
            sum = 0
        sum = 0
    print(count)
        
n = int(input())
Team(n)
