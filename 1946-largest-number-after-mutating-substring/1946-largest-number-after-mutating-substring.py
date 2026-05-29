class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:

        num = list(num)

        started = False

        for i in range(len(num)):

            digit = int(num[i])

            # Start mutation if mapped digit is larger
            if change[digit] > digit:
                num[i] = str(change[digit])
                started = True

            # Continue mutation if already started
            elif change[digit] == digit and started:
                num[i] = str(change[digit])

            # Stop mutation if mapped digit becomes smaller
            elif change[digit] < digit and started:
                break

        return "".join(num)