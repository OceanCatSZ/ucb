def epoch_based(Sn, G, T0, T):
    t = 0
    j = 0
    R_n_1_0 = []
    for t in T:
        d = 1
        for d in D:
            Set augmented set A_n_d_j = Sn ∪ Rn,d,j
            i = UCB(An,d,j , min(T − t, K0(K0 + 1)2j))
            t = t + K0(K0 + 1)2j
            Send i to neighbors
            Receive most played arms of neighbors as Rn,d,j
