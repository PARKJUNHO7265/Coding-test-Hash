def solution(clothes):
    from collections import Counter
    cnt = Counter([kind for name, kind in clothes])
    print(cnt)
    cnt = list(cnt.values())
    print(cnt)
    answer = 1
    for i in cnt:
        answer = (answer * (i+1))
    answer  = answer - 1
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))


'''Counter를 이용하여 name과 clothes 두개의 개수를 세고 그 value를 list형태로 다시 cnt에 저장하였다.'''
