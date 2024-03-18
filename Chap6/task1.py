tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidths = [0] * len(tableData)

for row in range(len(tableData[0])):
    for col in range(len(tableData)):
        print(tableData[col][row].rjust(colWidths[col]), end=' ')
    print()
