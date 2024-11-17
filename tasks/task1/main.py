from typing import List


class SolutionMy:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        second: int
        iteration = 0
        end = len(nums)
        while iteration < end:
            second = target - nums.pop(0)
            if second in nums:
                return [iteration, nums.index(second) + iteration + 1]
            iteration += 1


class SolutionBest:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        n = len(nums)

        for i in range(n):
            comp = target - nums[i]
            if comp in nummap:
                return [nummap[comp], i]
            nummap[nums[i]] = i

        return []


if __name__ == '__main__':
    my = SolutionMy()
    print(my.twoSum([2,7,11,15], 9))
    best = SolutionBest()
    print(best.twoSum([2,7,11,15], 9))