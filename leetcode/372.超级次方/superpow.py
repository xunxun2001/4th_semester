class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        base = 1337

        if not b:
            return 1
        last = b.pop()

        part1 = (a ** last) % base
        part2 = (self.superPow(a, b) ** 10) % base

        return (part1 * part2) % base
