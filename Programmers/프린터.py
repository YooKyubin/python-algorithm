from collections import deque
def solution(priorities, location):
    answer = 0
    j = deque(priorities)
    # 중요도가 큰 것부터 하나씩 뽑을 수 있도록 정렬
    sorted_priorities = deque(sorted(priorities, reverse = True))
    pri = sorted_priorities.popleft()
    while j:
        temp = j.popleft()
        # 출력
        if temp == pri:
            answer += 1
            # 목표 문서가 출력 될 차례
            if location == 0:
                return answer
            else:
                location -= 1
                # 다음 우선 순위 중요도 설정
                pri = sorted_priorities.popleft()
        # 우선순위가 맞지 않아 출력 없음
        # 맨앞의 문서를 맨 뒤로 옮기고 location 만 변경
        else:
            j.append(temp)
            if location == 0:
                # 목표하는 문서의 위치가 0인데 우선순위가 부족하여 j의 가장 뒤로 위치 설정
                location = len(j) - 1
            else:
                location -= 1
