class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        bucket=[[] for i in range (len(nums)+1)]
        for num,count in freq.items():
            bucket[count].append(num)
        
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result


         
