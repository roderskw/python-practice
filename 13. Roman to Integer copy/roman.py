class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = [1, 5, 10, 50, 100, 500, 1000]
        letters = "IVXLCDM"
        lastNumber = 1001
        num = 0
        for x in s:
            next = numbers[letters.find(x)]
            if(next > lastNumber):
                next = next - lastNumber - lastNumber
            else:
                lastNumber = next
            num = num + next
        return num