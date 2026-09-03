class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        freq = sorted(freq.items(), key=lambda x: x[1])
        results = []
        for i in range(len(freq)-1, len(freq)-1-k, -1):
            results.append(freq[i][0])
        return results