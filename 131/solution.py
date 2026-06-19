class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]

        def is_palindrome(word):
            return word == word[::-1]

        res = []
        n = len(s)
        def dfs(i, curr):
            if i == n:
                res.append(curr[::])
                return
            
            for j in range(i + 1, n + 1):
                curr_word = s[i:j]
                if is_palindrome(curr_word):
                    curr.append(curr_word)
                    dfs(j, curr)
                    curr.pop()
        dfs(0, [])

        return res