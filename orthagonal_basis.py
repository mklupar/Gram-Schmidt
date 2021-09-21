# uses the Gram-Schmidt Orthogonality Process to take a basis that is not orthogonal, and make it orthogonal.

def dot(x, y):  # does the dot product between the x and y (x and y are vectors)

    x_list = list(x)
    y_list = list(y)
    product_list = []

    for i in range(len(x_list)):
        product_list.append(x_list[i] * y_list[i])
    return sum(product_list)


def vec_sub(x, y):  # add two vectors together

    x_list = list(x)
    y_list = list(y)
    product_list = []

    for i in range(len(x_list)):
        product_list.append(x_list[i] - y_list[i])
    return product_list


def scalar_multi(x, y_list):  # x is scalar , y is list

    return [x * i for i in y_list]


def make_orthogonal(*args):  # input basis vectors

    x_list = args  # list of the basis

    v_list = []

    for xterm in x_list:
        newterm = xterm
        for vterm in v_list:
            scalar = dot(xterm, vterm) / dot(vterm, vterm)
            newterm = vec_sub(newterm,
                              scalar_multi(scalar, vterm))
        v_list.append(newterm)

    return v_list

if __name__ == '__main__':
    print(make_orthogonal([1, 0], [0,1]))
