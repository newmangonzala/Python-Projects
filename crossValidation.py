a = [-5,9]
b = [-4,7]
c = [-3,4]
d = [-2,2]
e = [-1,1]
f = [0,0]
g = [1,1]
h = [2,2]
i = [3,4]
j = [4,7]
k = [5,9]
l = [6,12]
A = [a,b,c,d,e,f,g,h,i,j,k,l]

def Transpose(A):
    l1=[]
    for i in range(len(A[0])):
        l2=[]
        for j in range(len(A)):
            value = A[j][i]
            l2.append(value)
        l1.append(l2)
    return l1

first = [l,i,e,b]
second = [d,j,f,a]
third = [h,c,g,k]

c1 = first + second 
c2 =  first + third 
c3 = second + third

train = [c1,c2,c3]
test = [third,second,first]

def poly(A,degree):
    if degree > 0:
        degree -= 1
        return A*poly(A,degree)
    else:
        return 1

def function(A,degree):
    l2 = []
    for i in range(len(A)):
        l1 = []
        l1.append(1)
        for j in range(1,degree + 1):
            l1.append(poly(A[i][0],j))
        l2.append(l1)
    return l2

def squared_error(test_y, output):
    error = 0
    for i in range(len(output)):
        error += (test_y[i][1]-output[i])**2

#    print("{}\n".format(error))
    return error

def test_y(test_y,coef,order):
    l1 = []
    for i in test_y:
        y = 0
        for j in range(order+1):
            y += coef[j][0]*poly(i[0],j)
        l1.append(y)
    return l1

def Matrix_multip(A, B):
    try:
        A_column_lengh = len(A[0])
    except:
        A_column_lengh = 1
    try:
        B_column_lengh = len(B[0])
    except:
        B_column_lengh = 1

    if (A_column_lengh) == (len(B)):
        l2 = []
        for i in range(len(A)):
            l2.append(Single_row_multip(A[i],B,B_column_lengh))
        return l2
    else:
        print('No valid multiplication')
        return

def Single_row_multip(row, B, Bl):
    l1 = []
    if Bl == 1:
        sum = 0
        for i in range(len(B)):
            b = B[i][0]
            a = row[i]
            sum += a * b
        l1.append(sum)
    else: 
        for j in range(Bl):
            sum = 0
            for i in range(len(B)):
                sum += row[i] * B[i][j]
            l1.append(sum)
    return l1

def Vector_b(A):
    l2 = []
    for i in range(len(A)):
        l1 = []
        l1.append(float(A[i][1]))
        l2.append(l1)

    return l2


def Adjoin(A,order):
    pivot = len(A)
    for i in range(order+1):
        for j in range(order+1):
            A[i].append(0)
    for i in range(order+1):
        A[i][i+pivot] = 1
    return A

def Inverse(A,order):
    for pivot in range(order+1):
        for i in range(order+1):
            temp = A[i][pivot]
            for j in range((order+1)*2):
                A[i][j] /= temp
        for i in range(order+1):
            if i != pivot:
                for j in range((order+1)*2):
                    A[i][j] -= A[pivot][j]
    for pivot in range(order+1):
        temp = A[pivot][pivot]
        for i in range(len(A[0])):
            A[pivot][i] /= temp 
    l1=[]
    for i in range(order+1):
        l2=[]
        for j in range(order+1):
            value = A[i][j+order+1]
            l2.append(value)
        l1.append(l2)
    return l1


def show(A):
    for i in range(len(A)):
        print(A[i])
    print("\n")

def main(train,test):

    first_assignment = True
    for order in range(1,8):
        error = 0
        count = 0
        for j in train:
            c = j
            b = Vector_b(c)
    #        show(b)
            c1 = function(c,order)
    #        show(c1)
            c1t = Transpose(c1)
    #        show(c1t)
            c1m = Matrix_multip(c1t,c1)
    #        show(c1m)
            c1a = Adjoin(c1m,order)
    #        show(c1a)
            ci = Inverse(c1m,order)
    #        show(ci)
            cs = Matrix_multip(c1t,b)
    #        show(cs)
            x = Matrix_multip(ci,cs)
    #        show(x)
            i = test[count]
            output_y = test_y(i,x,order)    
    #        show(output_y)
            error += squared_error(i,output_y)
            count += 1

        mean_error = error/len(test)
        if first_assignment:
            smallest = mean_error
            best_order = order
        first_assignment = False
        if smallest > mean_error:
            smallest = mean_error
            best_order = order
    print("the best order to fit the data is {}\n".format(best_order))

main(train,test)

