from collections import deque
import copy

# N개의 강의
n = int(input())

# 모든 강의에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)

# 각 강의에 연결된 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(n + 1)]

# 각 강의 시간을 0으로 초기화
time = [0] * (n + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]: #두번째 수부터 마지막값 전까지는 선행강의들의 번호
        indegree[i] += 1
        graph[x].append(i)
        
# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    # time은 강의 별 시간이라면 result는 해당 강의까지 수강하기 위해 걸리는 최소 시간
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    #큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            # 선수 강의로 인해 더 커지는 값이 업데이트되는 것이 맞으므로  max함수를 이용한다.
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1 #해당 노드에서 나가는 간선을 그래프에서 제거한는 과정
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        
    # 위상 정렬을 수행한 결과 출력
    for i in range(1, n + 1):
        print(result[i])

topology_sort()
            