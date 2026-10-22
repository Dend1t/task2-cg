import math

class BezierCurve:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x) - 1 

    def point(self, param):
        if self.n == 0:
            return self.x[0], self.y[0]

        res_x = 0.0
        res_y = 0.0
        
        for i in range(self.n + 1):
            basis = math.comb(self.n, i) * ((1.0 - param) ** (self.n - i)) * (param ** i)
            
            res_x += basis * self.x[i]
            res_y += basis * self.y[i]
            
        return res_x, res_y