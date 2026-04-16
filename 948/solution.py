class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        tokens.sort()
        max_score = 0
        score = 0
        l, r = 0, n - 1

        while l <= r:
            current_power = tokens[l]
            if current_power <= power:
                power -= current_power
                l += 1
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break

        return max_score
