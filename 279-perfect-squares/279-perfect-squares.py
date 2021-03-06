class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(num):
            # num의 제곱수 여부를 리턴
            return (int(num**0.5))**2 == num
        
        if is_square(n):
            # 자기 자신이 완전 제곱수인 경우는 1이 최소
            return 1
        
        for i in range(n + 1):
            # 제곱수 확인은 양의 정수만 필요
            # 이를 초과하는 경우는 이미 i가 초과 된 경우로
            # for문 시간 낭비임
            if (n -  i*i) < 0:
                break
            # (자기 자신 - 제곱수*제곱수)가 제곱수인 경우
            # 이 경우 자기 자신 + 제곱수 = 2가 최소
            # 필요한 정답은 정수를 이루는 최소 제곱수의 개수
            if is_square(n - i*i):
                return 2
            
        for i in range(n + 1):
            # 제곱수 확인은 양의 정수만 필요
            # 이를 초과하는 경우는 이미 i가 초과 된 경우로
            # for문 시간 낭비임
            if (n -  i*i) < 0:
                break
            for j in range(n + 1):
                # 제곱수 확인은 양의 정수만 필요
                # 이를 초과하는 경우는 이미 j가 초과 된 경우로
                # for문 시간 낭비임
                if (n - i*i - j*j) < 0:
                    break
                # 제곱수 3개가 가능한 경우 탐색
                elif is_square(n - i*i - j*j):
                    return 3
                
        # [그랑주 네 제곱수 정리]
        # 임의의 양수 n은 최대 4개의 제곱수만을 가질 수 있음
        # 따라서 1,2,3 이 아닌 경우는 4일 수 밖에 없음
        return 4
    