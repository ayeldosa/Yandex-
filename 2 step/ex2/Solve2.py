def solve():
    import sys
    data = sys.stdin.read().strip().split('\n')
    target = "ITSWEDNESDAYMYDUDES!"
    idx = 0
    used_ids = set()
    message_num = 0
    
    for line in data:
        message_num += 1
        parts = line.split('\t')
        if len(parts) != 2:
            idx = 0
            used_ids = set()
            continue
        
        user_id, message = parts
        
        if len(message) != 1:
            idx = 0
            used_ids = set()
            if message == 'I':
                idx = 1
                used_ids = {user_id}
            continue
        
        char = message
        
        if idx < len(target) and char == target[idx]:
            if user_id in used_ids:
                idx = 0
                used_ids = set()
                if char == 'I':
                    idx = 1
                    used_ids = {user_id}
                continue
            
            used_ids.add(user_id)
            idx += 1
            
            if idx == len(target):
                print(message_num)
                return
        else:
            idx = 0
            used_ids = set()
            if char == 'I':
                idx = 1
                used_ids = {user_id}
    
    print(-1)

if __name__ == "__main__":
    solve()