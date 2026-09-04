class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        if zeros >= 2:
            return [0]*len(nums)
        product = 1
        products = []
        for i in nums:
            product *= i
        for i in range(len(nums)):
            if nums[i] == 0:
                zproduct = 1
                ncopy = nums.copy()
                ncopy[i] = 1
                for k in range(len(ncopy)):
                    zproduct *= ncopy[k]
                products.append(int(zproduct))
                continue
            products.append(int(product/nums[i]))
        return products
        