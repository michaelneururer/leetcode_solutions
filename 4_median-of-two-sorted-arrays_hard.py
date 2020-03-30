import math

def isl(x,L):
    #Returns smallest possible index of x in sorted list L.append(x)
    if len(L) == 0:
        return 0
    if len(L) == 1:
        if x > L[0]:
            return 1
        else:
            return 0
    if x > L[math.floor(len(L)/2)]:
        return math.floor(len(L)/2) + isl(x, L[math.floor(len(L)/2):])
    else:
        return isl(x,L[:math.floor(len(L)/2)])

def isl_upper(x,L):
    #Returns largest possible index of x in sorted list L.append(x)
    if len(L) == 0:
        return 0
    if len(L) == 1:
        if x >= L[0]:
            return 1
        else:
            return 0
    if x >= L[math.floor(len(L)/2)]:
        return math.floor(len(L)/2) + isl_upper(x, L[math.floor(len(L)/2):])
    else:
        return isl_upper(x,L[:math.floor(len(L)/2)])

def median_of_sorted_lists(nums1,nums2):
    L = [nums1,nums2]
    print(L)
    lengths = [len(l) for l in L]
    steps = [len(l) for l in L]
    for i in [0,1]:
        if len(L[i])==0:
            j = (i+1)%2
            if len(L[j])%2:
                return L[j][math.floor(lengths[j])//2]
            else:
                return (L[j][lengths[j]//2-1]+L[j][lengths[j]//2])/2

    indeces = [math.floor(l/2) for l in lengths]
    mus = [L[i][indeces[i]] for i in [0,1]]
    f = lambda x: lengths[0] + lengths[1] - (isl(x,L[0]) + isl(x,L[1]))
    f_upper = lambda x: lengths[0] + lengths[1] - (isl_upper(x,L[0]) - 1 + isl_upper(x,L[1]))
    rs = [f(m) for m in mus]
    rs_upper = [f_upper(m) for m in mus]
    num_right = math.floor((len(nums1)+len(nums2)+1)/2)
    flags = [1,1]
    print(steps,indeces,mus,rs,rs_upper,num_right)
    i = 0
    while not (num_right in range(rs_upper[i], rs[i]+1)):
        i = (i+1)%2
        steps[i] = max(math.floor(steps[i]/2),1) #Ensures that we dont reach an infinite loop, since there is definitely an element that satisfies the condition of the loop
        if rs[i] > num_right:
            if indeces[i]+steps[i] >= len(L[i]):
                continue
            indeces[i] += steps[i]
            mus[i] = L[i][indeces[i]]

        else:
            if indeces[i]-steps[i] < 0:
                continue
            indeces[i] -= steps[i]
            mus[i] = L[i][indeces[i]]
        rs[i] = f(mus[i])
        rs_upper[i] = f_upper(mus[i])
        print('rs', rs)
        print('rs_upper', rs_upper)
        print('mus', mus)
        print('indeces', indeces)
        print('num_right', num_right)
        print((num_right in range(rs[i], rs_upper[i]+1)))
    print('rs', rs)
    print('rs_upper', rs_upper)
    print('mus', mus)
    print('indeces', indeces)
    print('num_right', num_right)
    print((num_right in range(rs[i], rs_upper[i]+1)))
    print('i is', i)

    if sum(lengths)%2:
        return mus[i]
    else:
        j = (i+1)%2
        if num_right < rs[i]:
            print(1)
            return mus[i]
        elif isl(mus[i],L[i])==0:
            print(2)
            return (mus[i] + L[j][isl(mus[i],L[j])-1])/2
        elif isl(mus[i],L[j])==0:
            print(3)
            return (mus[i] + L[i][isl(mus[i],L[i])-1])/2
        else:
            print(4)
            return (mus[i] + max(L[i][isl(mus[i],L[i])-1], L[j][isl(mus[i],L[j])-1]))/2
