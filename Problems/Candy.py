def candy(ratings):
    #[3,5,4,2,4,8]
    #[1,3,2,1
    candies=[]
    candies.append(1)
    for i in range(1,len(ratings)):
        if ratings[i]>ratings[i-1]:
            candies.append(candies[i-1]+1)
        elif ratings[i]<ratings[i-1]:
            award = 1
            candies.append(award)
            prev = i-1
            while (prev>=0 and award==candies[prev]):
                candies[prev]+=1
                award = candies[prev]
                prev = prev-1
        else:
            candies.append(candies[i-1])
    return sum(candies)
print candy([3,5,4,2,4,8])

