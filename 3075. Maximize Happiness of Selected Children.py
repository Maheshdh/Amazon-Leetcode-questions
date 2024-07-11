# approach
# generate top k happiest using a min heap to ensure we use only O(k) space for the heap
# Now, convert the list to max heap
# keep adding the happiest value to the total
# since the happiness decereases by 1 each time, and cannot get below 0, keep a count of reductions and add maximum of 0 or the value after deductions
# Time complexity -> O(nlog(k) for creating min heap , O(k) for heapify function, O(k log(k) for finding total -> O(nlog(k)) overall
# Space complexity -> O(k)
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        top_k_happy = []
        for i in happiness:
            heapq.heappush(top_k_happy, i)
            if len(top_k_happy) > k:
                heapq.heappop(top_k_happy)
        # converting min to max heap
        top_happy = [-h for h in top_k_happy]
        heapq.heapify(top_happy)
        turns = 0
        total = 0
        for i in range(k):
            total += max((-heapq.heappop(top_happy) - turns),0)
            turns += 1
        return total
