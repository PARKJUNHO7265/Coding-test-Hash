import collections as col

participant = ["leo", "kiki", "eden"]
completion  = ["eden", "kiki"]
def solution(participant, completion):
    answer = col.Counter(participant) - col.Counter(completion)
    return list(answer.keys())[0]
print(solution(participant, completion))

''' collections Module
- Counter : 시퀀스 자료형의 데이터 요소 개수를 딕셔너리 형태로 반환하는 자료구조
- OrderedDict : 딕셔너리 형태의 자료를 순서에 맞게 정렬
'''
