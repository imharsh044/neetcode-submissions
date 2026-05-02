class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # to keep only 32 bits
        max_int = 0x7FFFFFFF # the largest 32-bit signed integer

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)