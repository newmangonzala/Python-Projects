import random

def bound(seq, index):

    divisor = len(seq)
    infinite  = index % divisor
    return infinite
    

class Generate():
    """ index each cell in a nine by nine sudoku game
    """
    def __init__(self, column):
        self.column = column
        self.row = 0
        self.quadrant = 0
        self.numbers = set(range(1,10))
        self.value = 0
        self.chosen = {0}


    def up_column(self, integer, column):
    ### update the set of possible choices on a column

        if self.column == column:
            if {integer} <= self.numbers:
                self.numbers.remove(integer)

    def up_row(self, integer, row):
    ### update the set of possible choices on a row
        if self.row == row:
            if {integer} <= self.numbers:
                self.numbers.remove(integer)

def gen(mega, columns_index, rows_index):
    ### assign indexes to cells

    count = 0
    for i in range(0,54,9):
        for j in range(i,i+9):
            label = bound(columns_index, j)
            mega[j] = Generate(columns_index[label])
            mega[j].row = rows_index[count]
            if (label < 3) and (count < 3):
                mega[j].quadrant = 'A'
            elif (label < 6) and (count < 3):
                mega[j].quadrant = 'B'
            elif (label < 9) and (count < 3):
                mega[j].quadrant = 'C'
            elif (label < 3) and (count < 6):
                mega[j].quadrant = 'D'
            elif (label < 6) and (count < 6):
                mega[j].quadrant = 'E'
            elif (label < 9) and (count < 6):
                mega[j].quadrant = 'F'
            elif (label < 3) and (count < 9):
                mega[j].quadrant = 'G'
            elif (label < 6) and (count < 9):
                mega[j].quadrant = 'H'
            elif (label < 9) and (count < 9): # dont need that extra condition
                mega[j].quadrant = 'I'

        count += 1

def operations(mega, i):
    """ choose an integer and update row, column , and quadrant"""

    if i < 54:

        complete = {1,2,3,4,5,6,7,8,9}
        current = {0}
        row_integer = mega[i].row
        column_integer = mega[i].column
        quadrant_integer = mega[i].quadrant
            
        for k in range(54):
            if mega[k].row == row_integer or mega[k].column == column_integer or mega[k].quadrant == quadrant_integer:
                current.add(mega[k].value)
        mega[i].numbers = complete - (current | mega[i].chosen)
    
        if  mega[i].numbers != set():
    
            mega[i].value = random.choice(list(mega[i].numbers))
            value = mega[i].value
            mega[i].chosen.add(value)
            
    
            i += 1
            operations(mega,i)
    
        else:
    
            i -= 2
            for j in range(i+1,54):
                mega[j].chosen = {0}
                mega[j].value = 0
    
            operations(mega, i)
    else:
        return        
        
        

def display(mega):
    """ print the nine by nine table"""

    for i in range(0,54,9):
        for j in range(i,i+9):
#            print('{}{}{}{} '.format(mega[j].value,mega[j].quadrant,mega[j].column,mega[j].row), end="")
            print(mega[j].value, end= "     ")
        print("\n")

def main():

    mega = [0]*54
    columns_index = ['A','B','C','D','E','F','G','H','I']
    rows_index = ['a','b','c','d','e','f','g','h','i']

    gen(mega, columns_index, rows_index)
    i = 0
    operations(mega,i)
    display(mega)

main()
          
