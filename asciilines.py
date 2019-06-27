import sys

def make_matrix(row, col):
    matrix={}

    for index in range(0, row):
        matrix[index]={}

    for i in range(0, row):
        for j in range(0, col):
            matrix[i][j]='.'

    return matrix

def print_matrix(matrix, row, col):
   for i in range(0, row):
       for j in range(0, col):
           print(matrix[i][j], end='')
       print('')

# ............................................................
#                             main
# ............................................................

matrix={}
lineCount=0

fin = open(sys.argv[1], 'rt')
for line in fin:

    if line[-1] == '\n':
        line=line[:-1:]

    if lineCount == 0:
        print('matrix dimensions: ', line)
        rowCol= line.split(' ', 2)
        row=int(rowCol[0])
        col=int(rowCol[1])
        matrix= make_matrix(row, col)
        print_matrix(matrix, row, col)
    else:
        print('parse line: ', line)

    lineCount= lineCount + 1

fin.close()
