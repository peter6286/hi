
class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in dic:
                dic[num] = i
            else:
                return [dic[n], i]

    def removeDuplicates(self,nums):
        len_ = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # 因为已经sorted好跟前一个比较就行
                nums[len_] = nums[i]
                len_ += 1
        return len_

    #It doesn't matter what you leave beyond the returned length.
    #For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.

    def removeElement(self, nums, val):
        len_ = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[len_] = nums[i]
                len_ += 1
        return len_

    # It doesn't matter what you leave beyond the returned length.
    # For example if you return 2 with nums = [2,2,3,3] or nums = [2,2,0,0], your answer will be accepted.

    def maxProfit(self, prices):
        if not prices:
            return 0

        maxProfit = 0
        minPurchase = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit

    def maximumProduct(self, nums):
        nums.sort()
        candidate_1 = nums[-1] * nums[-2] * nums[-3]
        candidate_2 = nums[-1] * nums[0] * nums[1]
        max_product = max(candidate_1, candidate_2)
        return max_product


    def binsearchInsert(self, nums, target) :
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:  #当target大于mid时 只搜索比mid大的
                low = mid + 1
            else:
                high = mid         #当target小于mid时 只搜索比mid小的
        return low

    def plusOne(self, digits):
        length = len(digits) - 1
        while digits[length] == 9:
            digits[length] = 0
            length -= 1
        if (length < 0):
            digits = [1] + digits
        else:
            digits[length] += 1
        return digits


    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1
        return nums1


a=[3,2,4]
b=[7,1,5,3,6,4]
object = Solution()
print(object.maxProfit(b))
print(object.maximumProduct(b))
print(object.plusOne([9]))
print(object.plusOne([9]))
print(object.plusOne([12]))




