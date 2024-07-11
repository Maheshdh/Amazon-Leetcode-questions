# approach
# use bfs to explore all states 1 move away for each position
# if the target is found, return the number of moves
# else explore the other states in fifo manner
# Time complexity -> O(10*4)
# Space complexity -> O(10*4)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # deadends represent non reachable nodes
        visit = set(deadends)
        # cannot proceed if start is itself a deadend
        if "0000" in visit:
            return -1
        # maintain a queue for bfs
        q = deque([["0000",0]])
        # helper function to find next moves
        def children(lock):
            res = []
            for i in range(4):
                next_child = lock[:i] + str((int(lock[i])+1)%10) + lock[i+1:]
                prev_child = lock[:i] + str((int(lock[i])-1 + 10)%10) + lock[i+1:]
                res.append(next_child)
                res.append(prev_child)
            return res
        # performing bfs
        while q:
            state, turns = q.popleft()
            if state == target:
                return turns
            next_moves = children(state)
            for child in next_moves:
                if child in visit:
                    continue
                visit.add(child)
                q.append([child,turns+1])
        return -1
        
