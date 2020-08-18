class Solution:
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        left = 0
        right = 0
        temp = 0
        ret = ""
        for s in S:
            if s == "(":
                left += 1
            else:
                right += 1
            if left == right:
                ret += S[temp: (left + right)][1:-1]
                temp = left + right
        return ret
    # def removeOuterParentheses(self, S: str) -> str:
    #     ans = ''
    #     L = 0
    #     R = 0
    #     for i in range(0, len(S)):
    #         if L == 0:
    #             L += 1
    #             continue
    #         if S[i] == '(':
    #             L += 1
    #         else:
    #             R += 1
    #         if L != R:
    #             ans = ans+S[i]
    #         else:
    #             L = 0
    #             R = 0
    #     return ans


solution = Solution()
res = solution.removeOuterParentheses("(()())(())(()(()))")
print(res)
