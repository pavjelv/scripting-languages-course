def align_length(v1, v2):
    if type(v1) is not list or type(v2) is not list:
        raise TypeError("Type is not list!")

    if len(v1) < len(v2):
        i = 0
        for arg in v2:
            if i >= len(v1):
                v1.insert(0, 0)
            i += 1
    else:
        i = 0
        for arg in v1:
            if i >= len(v2):
                v2.insert(0, 0)
            i += 1


def trim(v):
    while v[0] == 0:
        del v[0]


class Polynomial:
    def __init__(self, args):
        supported_types = [int, list, tuple]
        self.coeffs = []
        if type(args) not in supported_types:
            raise TypeError("Incorrect type!")
        elif type(args) in [list, tuple]:
            if len(args) == 0:
                raise ValueError("Length cannot be zero!")
            for arg in args:
                if type(arg) is not int:
                    raise TypeError("Value should be int!")
                self.coeffs.append(arg)
        else:
            self.coeffs = [args]

    def __add__(self, value):
        if isinstance(value, int):
            result = self.coeffs.copy()
            result[len(self.coeffs) - 1] += value
            return Polynomial(result)
        elif isinstance(value, Polynomial):
            self_args_rev = self.coeffs.copy()
            val_args_rev = value.coeffs.copy()
            align_length(self_args_rev, val_args_rev)
            result = [x + y for (x, y) in zip(self_args_rev, val_args_rev)]
            trim(result)
            return Polynomial(result)
        else:
            raise TypeError("Incorrect type provided!")

    def __radd__(self, value):
        if value == 0:
            return self
        else:
            return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, int):
            result = self.coeffs.copy()
            result[len(self.coeffs) - 1] -= value
            return Polynomial(result)
        elif isinstance(value, Polynomial):
            self_args_rev = self.coeffs.copy()
            val_args_rev = value.coeffs.copy()
            align_length(self_args_rev, val_args_rev)
            result = [x - y for (x, y) in zip(self_args_rev, val_args_rev)]
            trim(result)
            return Polynomial(result)
        else:
            raise TypeError("Incorrect type provided!")

    def __rsub__(self, value):
        result = Polynomial([-x for x in self.coeffs])
        if value == 0:
            return result
        else:
            return result.__add__(value)

    def __mul__(self, value):
        if isinstance(value, int):
            result = []
            for arg in self.coeffs:
                result.append(arg * value)
            return Polynomial(result)
        elif isinstance(value, Polynomial):
            result = [0] * (len(self.coeffs) + len(value.coeffs) - 1)
            for i, l_coeff in enumerate(self.coeffs):
                for j, r_coeff in enumerate(value.coeffs):
                    result[i + j] += l_coeff * r_coeff
            trim(result)
            return Polynomial(result)
        else:
            raise TypeError("Incorrect type provided!")

    def __rmul__(self, value):
        if value == 0:
            return self
        else:
            return self.__mul__(value)

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
            length = len(self.coeffs) - 1
            if length == 0 and coef == 0:
                return "0"
            if coef == 1 and i != length:
                string += f" + {deg(length - i)}"
            elif coef == -1 and i != length:
                string += f" - {deg(length - i)}"
            elif coef != 0:
                string += f"{' + ' if coef > 0 else ''}{coef}{deg(length - i)}"
        return string.lstrip(" + ")

    def __eq__(self, value):
        if type(value) not in [Polynomial, int]:
            return False
        if type(value) == int:
            return len(self.coeffs) == 1 and self.coeffs[0] == value

        trim(self.coeffs)
        trim(value.coeffs)

        return self.coeffs == value.coeffs

    def __repr__(self):
        return f"Polynomial({self.coeffs})"
