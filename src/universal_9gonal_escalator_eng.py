def generate_P9_values(limit):
    """
    Generates all generalized 9-gonal numbers P_9(x) up to the limit and returns a sorted list.
    P_9(x) = (7x^2 - 5x) / 2  (where x is an integer)
    """
    p9_set = set()
    x = 0
    while True:
        # Calculate for both positive and negative directions (generalized polygonal numbers)
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
    Finds the set of all representable numbers up to the limit using a linear combination of the given coefficient tuple (tuple_a).
    Calculates the set of numbers that can be formed using tuple_a=(a1,a2,...,ak) and the P9 values.
    """
    dp = {0}
    for a in tuple_a:
        next_dp = set()
        for val in dp:
            for p in p9_vals:
                new_val = val + a * p
                if new_val <= limit:
                    next_dp.add(new_val)
                else:
                    break # Early termination since p9_vals is sorted in ascending order
        dp = next_dp # After one turn, all numbers representable with coefficient 'a' are stored in dp.
    return dp

def find_truant(representable_set, limit):
    """
    Finds the smallest positive integer that cannot be represented (the truant).
    """
    for i in range(1, limit + 1): # Iterate from 1 to the limit to find the smallest number missing from the representable_set.
        if i not in representable_set:
            return i
    return None

def build_complete_escalator_tree(limit=450, max_depth=8):
    """
    Builds an escalator tree and returns all universal form candidates.
    """
    p9_vals = generate_P9_values(limit)
    candidates = []
    pruned_branches = []

    def escalate(current_tuple):
        representable = get_representable_numbers(current_tuple, p9_vals, limit)
        truant = find_truant(representable, limit)
        
        # 1. If there is no truant, confirm as a universal form candidate (stop branch growth)
        if truant is None:
            candidates.append(current_tuple)
            return
        
        # 2. If a truant exists, grow branches (Escalation)
        depth = len(current_tuple)
        if depth < max_depth:
            # Search with the condition a_{k} <= a_{k+1} <= truant to prevent duplicates
            start_a = current_tuple[-1] # current_tuple[-1] is the last element; the next coefficient must be greater than or equal to this value.
            for next_a in range(start_a, truant + 1):
                escalate(current_tuple + (next_a,))
        else:
            # Record if max_depth is reached but a truant still remains (should be 0 here)
            pruned_branches.append((current_tuple, truant))

    # Start with (1,) since the first coefficient must always be 1
    escalate((1,))
    
    return candidates, pruned_branches

def verify_candidates(candidates, check_limit):
    """
    Verifies if the discovered candidate tuples actually generate all natural numbers up to the check_limit.
    """
    p9_vals = generate_P9_values(check_limit)
    verified = []
    failed = []

    for cand in candidates:
        # Extract the list of representable numbers up to the check_limit
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
    
    print(f"Starting the search... (Limit: {LIMIT}, Max Depth: {MAX_DEPTH})")
    candidates, pruned = build_complete_escalator_tree(limit=LIMIT, max_depth=MAX_DEPTH)
    
    # Dictionary to group and print by the length (dimension) of the tuples
    candidates_by_depth = {}
    for cand in candidates:
        d = len(cand)
        if d not in candidates_by_depth:
            candidates_by_depth[d] = []
        candidates_by_depth[d].append(cand)

    print("\nSearch complete! Printing the results.\n")
    
    total_count = 0
    # Sort and print by length (dimension)
    for depth in sorted(candidates_by_depth.keys()):
        tups = candidates_by_depth[depth]
        print(f"--- {depth}-variable (n={depth}) Universal Form Candidates: {len(tups)} ---")
        for t in tups:
            print(t)
        print()
        total_count += len(tups)
        
    print("==========================================================")
    print(f"Total candidates found: {total_count}")
    print(f"Number of pruned branches: {len(pruned)}")
    if len(pruned) == 0:
        print("-> The tree is completely closed. No further variables are needed!")
    print("==========================================================")

    VERIFY_LIMIT = 5
    print(f"\nStarting massive verification for the {len(candidates)} found candidates... (Verify Limit: {VERIFY_LIMIT})")
    
    # Execute verify_candidates function and store the results
    verified_candidates, failed_candidates = verify_candidates(candidates, VERIFY_LIMIT)
    
    print("Verification complete!\n")

    # Group by depth for printing
    candidates_by_depth = {}
    for cand in verified_candidates:
        d = len(cand)
        candidates_by_depth.setdefault(d, []).append(cand)

    for depth in sorted(candidates_by_depth.keys()):
        tups = candidates_by_depth[depth]
        print(f"--- {depth}-variable (n={depth}) Confirmed Universal Forms: {len(tups)} ---")
        for t in tups:
            print(t)
        print()

    if failed_candidates:
        print("--- Verification Failed List (Candidate, Found Truant) ---")
        for fail_cand, trt in failed_candidates[:10]: # Print only the top 10 as there might be too many
            print(f"Tuple: {fail_cand} -> Truant: {trt}")
        if len(failed_candidates) > 10:
            print(f"... and {len(failed_candidates)-10} more")
