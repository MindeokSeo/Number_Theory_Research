def generate_P9_values(limit):
    """
    limit 이하의 모든 일반화된 9각수 P_9(x)를 생성하여 정렬된 리스트로 반환합니다.
    P_9(x) = (7x^2 - 5x) / 2  (단, x는 정수)
    """
    p9_set = set()
    x = 0
    while True:
        # 양수와 음수 방향 모두 계산 (일반화된 다각수)
        p_pos = (7 * (x**2) - 5 * x) // 2
        p_neg = (7 * ((-x)**2) - 5 * (-x)) // 2
        
        if p_pos <= limit:
            p9_set.add(p_pos)

        if p_neg <= limit:
            p9_set.add(p_neg)
            
        if p_pos > limit and p_neg > limit:
            break
        x += 1
        
    return sorted(list(p9_set))

def get_representable_numbers(tuple_a, p9_vals, limit):
    """
    주어진 계수 튜플(tuple_a)의 선형 결합으로 limit까지 만들 수 있는 모든 수의 집합을 구합니다.
    tuple_a=(a1,a2,...,ak)와 P9 값들을 사용하여 만들 수 있는 수의 집합을 계산합니다."""
    dp = {0}
    for a in tuple_a:
        next_dp = set()
        for val in dp:
            for p in p9_vals:
                new_val = val + a * p
                if new_val <= limit:
                    next_dp.add(new_val)
                else:
                    break # p9_vals는 오름차순 정렬되어 있으므로 조기 종료
        dp = next_dp #한 턴이 끝나면 계수 a로 만들 수 있는 모든 수들은 dp에 저장됩니다.
    return dp

def find_truant(representable_set, limit):
    """
    만들 수 없는 가장 작은 양의 정수(truant)를 찾습니다.
    """
    for i in range(1, limit + 1): #1부터 limit까지 순회하며 representable_set에 없는 가장 작은 수를 찾습니다.
        if i not in representable_set:
            return i
    return None

def build_complete_escalator_tree(limit=450, max_depth=8):
    """
    에스컬레이터 트리를 구축하여 모든 보편 형식(Universal Form) 후보를 반환합니다.
    """
    p9_vals = generate_P9_values(limit)
    candidates = []
    pruned_branches = []

    def escalate(current_tuple):
        representable = get_representable_numbers(current_tuple, p9_vals, limit)
        truant = find_truant(representable, limit)
        
        # 1. Truant가 없으면 보편 형식 후보로 확정 (트리 가지 성장 종료)
        if truant is None:
            candidates.append(current_tuple)
            return
        
        # 2. Truant가 존재하면 가지 뻗기 (Escalation)
        depth = len(current_tuple)
        if depth < max_depth:
            # 중복 방지를 위해 a_{k} <= a_{k+1} <= truant 조건으로 탐색
            start_a = current_tuple[-1] #current_tuple[-1]은 현재 튜플의 마지막 요소로, 다음 계수는 이 값 이상이어야 합니다.
            for next_a in range(start_a, truant + 1):
                escalate(current_tuple + (next_a,))
        else:
            # max_depth에 도달했는데도 truant가 남아있다면 기록 (여기서는 0개여야 함)
            pruned_branches.append((current_tuple, truant))

    # 계수의 시작은 무조건 1이어야 하므로 (1,)에서 출발
    escalate((1,))
    
    return candidates, pruned_branches

def verify_candidates(candidates, check_limit):
    """
    발견된 후보 튜플들이 실제로 check_limit까지 모든 자연수를 생성하는지 검증합니다.
    """
    p9_vals = generate_P9_values(check_limit)
    verified = []
    failed = []

    for cand in candidates:
        # check_limit 범위까지 생성 가능한 숫자 목록 추출
        representable = get_representable_numbers(cand, p9_vals, check_limit)
        truant = find_truant(representable, check_limit)
        
        if truant is None:
            verified.append(cand)
        else:
            failed.append((cand, truant))
            
    return verified, failed

if __name__ == "__main__":
    print("==========================================================")
    print(" [Generalized 9-gonal Numbers Universal Forms Escalator] ")
    print("==========================================================\n")
    
    LIMIT = 1000
    MAX_DEPTH = 9
    
    print(f"탐색을 시작합니다... (Limit: {LIMIT}, Max Depth: {MAX_DEPTH})")
    candidates, pruned = build_complete_escalator_tree(limit=LIMIT, max_depth=MAX_DEPTH)
    
    # 튜플의 길이(차원)에 따라 그룹화하여 출력하기 위한 딕셔너리
    candidates_by_depth = {}
    for cand in candidates:
        d = len(cand)
        if d not in candidates_by_depth:
            candidates_by_depth[d] = []
        candidates_by_depth[d].append(cand)

    print("\n탐색 완료! 결과를 출력합니다.\n")
    
    total_count = 0
    # 길이(차원) 순으로 정렬하여 출력
    for depth in sorted(candidates_by_depth.keys()):
        tups = candidates_by_depth[depth]
        print(f"--- {depth}변수 (n={depth}) 보편 형식 후보: {len(tups)}개 ---")
        for t in tups:
            print(t)
        print()
        total_count += len(tups)
        
    print("==========================================================")
    print(f"총 발견된 후보 개수: {total_count}개")
    print(f"강제 종료된 미완성 가지(Pruned branches) 개수: {len(pruned)}개")
    if len(pruned) == 0:
        print("-> 트리가 완벽하게 닫혔습니다(Closed). 더 이상의 변수는 필요 없습니다!")
    print("==========================================================")

    VERIFY_LIMIT = 5
    print(f"\n발견된 {len(candidates)}개의 후보에 대해 대규모 검증을 시작합니다... (Verify Limit: {VERIFY_LIMIT})")
    
    # 여기서 verify_candidates 함수를 실행하여 결과를 변수에 저장합니다.
    verified_candidates, failed_candidates = verify_candidates(candidates, VERIFY_LIMIT)
    
    print("검증이 완료되었습니다!\n")

    # 변수 개수(Depth)별로 묶어서 출력
    candidates_by_depth = {}
    for cand in verified_candidates:
        d = len(cand)
        candidates_by_depth.setdefault(d, []).append(cand)

    for depth in sorted(candidates_by_depth.keys()):
        tups = candidates_by_depth[depth]
        print(f"--- {depth}변수 (n={depth}) 보편 형식 확정: {len(tups)}개 ---")
        for t in tups:
            print(t)
        print()

    if failed_candidates:
        print("--- 검증 실패 목록 (후보, 발견된 Truant) ---")
        for fail_cand, trt in failed_candidates[:10]: # 너무 많을 수 있으니 상위 10개만 출력
            print(f"튜플: {fail_cand} -> Truant: {trt}")
        if len(failed_candidates) > 10:
            print(f"... 외 {len(failed_candidates)-10}개")
