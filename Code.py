class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = list(bin(x))[2:]
        y = list(bin(y))[2:]
        if len(x) < len(y):
            x = list((len(y)-len(x))*'0') + x
        if len(x) > len(y):
            y = list((len(x)-len(y))*'0') + y
        c = 0
        for i in range(len(y)):
            if x[i] != y[i]:
                c += 1
        return c
