import sys

def fill_canvas(row, col):
    if row < 1 or col < 1:
        return None 
    else:
        canvas={}

        for index in range(0, row):
            canvas[index]={}

        for i in range(0, row):
            for j in range(0, col):
                canvas[i][j]='.'

        return canvas

def print_canvas(canvas, row, col):
   for i in range(0, row):
       for j in range(0, col):
           print(canvas[i][j], end='')
       print('')

def render_char(line, canvas):
    lineList= line.split(' ', 5)
    #print('lineList: ', lineList)

    char=lineList[0]
    rowStart=int(lineList[1])
    colStart=int(lineList[2])
    lineDir=lineList[3]
    length=int(lineList[4])

    if lineDir == 'h':
        if rowStart in canvas:
            for i in range(colStart, length+1):
                if i in canvas[rowStart]:
                    canvas[rowStart][i]= char

    elif lineDir == 'v':
        for i in range(rowStart, length+1):
            if i in canvas and colStart in canvas[i]:
                canvas[i][colStart]= char
    else:
        return False

# ............................................................
#                             main
# ............................................................

canvas={}
lineCount=0

fin = open(sys.argv[1], 'rt')

for line in fin:
    if line[-1] == '\n':
        line=line[:-1:]

    if lineCount == 0:
        #print('canvas dimensions: ', line)
        rowCol= line.split(' ', 2)
        row=int(rowCol[0])
        col=int(rowCol[1])
        canvas= fill_canvas(row, col)
        #print_canvas(canvas, row, col)
    else:
        render_char(line, canvas)

    lineCount= lineCount + 1

print_canvas(canvas, row, col)
fin.close()