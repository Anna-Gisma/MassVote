def MassVote(N, Votes):

    summ = 0
    perc = 0
    p_Votes = []
    for el in Votes:
        summ += el
    if N == 1 and Votes[0] == 0:
        res = 'no winner'
    elif N == 1 and Votes[0] > 0:
        res = 'majority winner 1'
    else:
        for el in Votes:
            perc = round((el*100 / summ), 2)
            p_Votes.append(perc)
        mxx = max(p_Votes[0], p_Votes[1])
        sec_max = min(p_Votes[0], p_Votes[1])
        for el in range(2, N):
            if p_Votes[el] > mxx:
                sec_max = mxx
                mxx = p_Votes[el]
            else:
                if p_Votes[el] > sec_max:
                    sec_max = p_Votes[el]
    
        ind_mxx = p_Votes.index(mxx) + 1
        if mxx > 50:
            res = 'majority winner ' + str(ind_mxx)
        else:
            if mxx > sec_max:
                res = 'minority winner ' + str(ind_mxx)
            else:
                res = 'no winner'


    return res  
    

N = 3
Votes = [10, 15, 10]
print(MassVote(N, Votes))
