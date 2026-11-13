# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


def max_profit(prices):
    if not prices:
        return 0
    
    min_price = float('inf')
    max_prof = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_prof:
            max_prof = price - min_price
            
    return max_prof


def max_subarray(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global


def is_balanced(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return len(stack) == 0


def main():
    print("Two Sum:", two_sum([2, 7, 11, 15], 9))       # [0, 1]
    print("Max Profit:", max_profit([7, 1, 5, 3, 6, 4])) # 5
    print("Max Subarray:", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
    print("Is Balanced:", is_balanced("()[{}]"))        # True


if __name__ == "__main__":
    main()