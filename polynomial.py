def align_length(v1, v2):
    if type(v1) is not list:
        raise TypeError("")

    if type(v2) is not list:
        raise TypeError("")

    if len(v1) < len(v2):
        i = 0
        for arg in v2:
            if i >= len(v1):
                v1.append(0)
            i += 1
    else:
        i = 0
        for arg in v1:
            if i >= len(v2):
                v2.append(0)
            i += 1


def trim(v):
    while v[0] == 0:
        del v[0]


class Polynomial:
    def __init__(self, args):
        supported_types = [int, list, tuple]
        self.coeffs = []
        if type(args) not in supported_types:
            raise TypeError("")
        elif type(args) in [list, tuple]:
            for arg in args:
                self.coeffs.append(arg)
        else:
            self.args = [args]

    def __add__(self, value):
        if isinstance(value, int):
            self.coeffs[len(self.coeffs) - 1] += value
            return Polynomial(self.coeffs)
        elif isinstance(value, Polynomial):
            self_args_rev = self.coeffs[::-1]
            val_args_rev = value.coeffs[::-1]
            align_length(self_args_rev, val_args_rev)
            result = [x + y for (x, y) in zip(self_args_rev, val_args_rev)]
            return Polynomial(result[::-1])

    def __radd__(self, value):
        if value == 0:
            return self
        else:
            return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, int):
            self.coeffs[len(self.coeffs) - 1] -= value
            return Polynomial(self.coeffs)
        elif isinstance(value, Polynomial):
            self_args_rev = self.coeffs[::-1]
            val_args_rev = value.coeffs[::-1]
            align_length(self_args_rev, val_args_rev)
            result = [x - y for (x, y) in zip(self_args_rev, val_args_rev)]
            return Polynomial(result[::-1])

    def __rsub__(self, value):
        if value == 0:
            return self
        else:
            return self.__sub__(value)

    def __mul__(self, value):
        if isinstance(value, int):
            result = []
            for arg in self.coeffs:
                result.append(arg * value)
            return Polynomial(result)
        elif isinstance(value, Polynomial):
            align_length(self.coeffs, value.coeffs)
            result = []
            for i, l_coeff in enumerate(self.coeffs):
                for j, r_coeff in enumerate(value.coeffs):
                    result[i + j] += l_coeff * r_coeff
            trim(result)
            return Polynomial(result)

    def __rmul__(self, value):
        if value == 0:
            return self
        else:
            return self.__rmul__(value)

    def __str__(self):
        string = ""

        def deg(degree):
            if degree == 0:
                r = ""
            elif degree == 1:
                r = "x"
            else:
                r = f"x^{degree}"
            return r

        for i, coef in enumerate(self.coeffs):
            if self.max_degree == 0 and coef == 0:
                return "0"
            if coef == 1 and i != self.max_degree:
                string += f"+{x_exp(self.max_degree - i)}"
            elif coef == -1 and i != self.max_degree:
                string += f"-{x_exp(self.max_degree - i)}"
            elif coef != 0:
                string += f"{'+' if coef > 0 else ''}{coef}{x_exp(self.max_degree - i)}"
        return string.lstrip("+")

    def __eq__(self, value):
        if type(value) not in [Polynomial, int]:
            return False
        arg_ = Polynomial(value)
        self_ = Polynomial(self)

        trim(self_.coeffs)
        trim(arg_.coeffs)

        return True if self_.coeffs == arg_.coeffs else False
