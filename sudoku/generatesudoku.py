import random
import functions

class Generate():
    """ index each cell in a nine by nine sudoku game
    """
    def __init__(self, column):
        self.column = column
        self.row = 0
        self.quadrant = 0    
        self.numbers = set(range(1,10))
        self.value = 0

    def integer(self):
    ### set an integer to each cell and update the remaining options to zero 
     

        if self.numbers == set():
            return 81
        self.value = random.choice(list(self.numbers))
        self.numbers = {0}
        return self.value

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

    def up_quadrant(self, integer, quadrant):
    ### update the set of possible choices on a quadrant
        if self.quadrant == quadrant: 
            if {integer} <= self.numbers:
                self.numbers.remove(integer)
         
    def reset(self):
    ### reset the set of possible choices
        self.value = 0
        self.numbers = set(range(1,10))
            

def gen(mega, columns_index, rows_index):
    ### assign indexes to cells

    count = 0
    for i in range(0,81,9):
        for j in range(i,i+9):
            label = functions.bound(columns_index, j)
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

def operations(mega):
    """ choose an integer and update row, column , and quadrant"""

    count = 0
    i = 0
    while i < 81:
    
        value = mega[i].integer() 
        if value == 81:
#            print(count)
            count += 1
            for j in range(81):
                mega[j].reset()
            i = 0
            continue
 
        row_integer = mega[i].row 
        column_integer = mega[i].column 
        quadrant_integer = mega[i].quadrant 
        
        for j in range(81):
            mega[j].up_row(value, row_integer)
        for j in range(81):
            mega[j].up_column(value, column_integer)
#        for j in range(81):
#            mega[j].up_quadrant(value, column_integer)

        i += 1
    
def display(mega):
    """ print the nine by nine table"""
                
    for i in range(0,81,9):
        for j in range(i,i+9):
            print('{}{}{}{}{} '.format(mega[j].value,mega[j].quadrant,mega[j].column,mega[j].row, mega[i].numbers), end="")
        print("\n") 

def main():
    
    mega = [0]*81
    columns_index = ['A','B','C','D','E','F','G','H','I']
    rows_index = ['a','b','c','d','e','f','g','h','i']

    gen(mega, columns_index, rows_index)
    operations(mega)
    display(mega)

main()
