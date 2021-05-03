def solution(N, Q, B, C):
    M = len(B)
    buckets = list()
    # 0'dan M'e kadar dön, M = B ve C array'lerinin uzunluğu
    for K in range(0, M):
        if len(buckets) < (B[K] + 1):
            for x in range(len(buckets), (B[K] + 1)):
                buckets.append(list())
        buckets[B[K]].append(C[K])
        if len(buckets[B[K]]) >= Q:
            buckets[B[K]].sort()
            cur_col = buckets[B[K]][0]
            in_a_row = 0
            for elem in buckets[B[K]]:
                if cur_col == elem:
                    in_a_row = in_a_row + 1
                    if in_a_row == Q:
                        # K'ncı iterasyon
                        return K
                else:
                    cur_col = elem
                    in_a_row = 1
    return -1

print(solution(2,2,[0,1],[5,5]))

print(solution(3,2,[1,2,0,1,1,0,0,1],[0,3,0,2,0,3,0,0]))