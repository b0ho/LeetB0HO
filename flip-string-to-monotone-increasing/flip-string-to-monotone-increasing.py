class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one = 0
        zero = s.count("0")
        res = zero

        for i in s:
            tmp = i == "1"
            one += tmp
            zero -= not tmp
            res = min(res, one + zero)

        return res