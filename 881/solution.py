class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        print(people)
        l, r = 0, n - 1

        boat_count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                boat_count += 1
            else:
                r -= 1
                boat_count += 1
        return boat_count