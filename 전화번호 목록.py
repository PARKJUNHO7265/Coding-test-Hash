def solution(phone_book):
    ph_bk = sorted(phone_book)
    answer = True
    for a, b in zip(ph_bk,ph_bk[1:]):
        if b.startswith(a):
            answer = False
    return answer
phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

''' startswith : 대상 문자열이 특정 문자 또는 문자열로 시작하는지 검사
   endswith : 대상 문자열이 특정 문자 또는 문자열로 끝나는지 검사'''
