import turtle as t

class Maze:
    def __init__(self, mazeFilePath):
        self.mazeList = []
        mazeFile = open(mazeFilePath, 'r')
        for line in mazeFile:
            rowList = []
            for ch in line.strip():  # .strip() 去掉每行的换行符
                rowList.append(ch)
            self.mazeList.append(rowList)
    
    def drawMaze(self):
        t.speed(10)
        t.bgcolor('white')
        t.color('black')
        t.shape('turtle')
        t.pensize(2)
        
        # 绘制迷宫
        for y in range(len(self.mazeList)):
            for x in range(len(self.mazeList[y])):
                if self.mazeList[y][x] == '+':
                    self.drawCenteredBox(x, -y)
        
        t.color('red')
        t.shape('circle')
        t.fillcolor('red')
        t.penup()
        t.goto(-len(self.mazeList[0]) // 2 + 1, len(self.mazeList) // 2 - 1)
        t.speed(1)
        t.pendown()

    def drawCenteredBox(self, x, y):
        """绘制一个方格，给定坐标为中心"""
        box_size = 20  # 方格的大小
        t.penup()
        t.goto(x * box_size - len(self.mazeList[0]) * box_size // 2, y * box_size + len(self.mazeList) * box_size // 2)
        t.pendown()
        for _ in range(4):
            t.forward(box_size)
            t.left(90)
    
    def updatePosition(self, row, col, val=None):
        if val:
            self.mazeList[row][col] = val
        t.goto(col * 20 - len(self.mazeList[0]) * 20 // 2, len(self.mazeList) * 20 // 2 - row * 20)
        if val:
            t.stamp()
        else:
            t.clearstamp()

    def isExit(self, row, col):
        """检查当前位置是否为迷宫出口"""
        return row == 0 or row == len(self.mazeList) - 1 or col == 0 or col == len(self.mazeList[0]) - 1

    def searchFrom(self, startRow, startColumn):
        """递归搜索路径"""
        # 如果当前位置是墙壁，直接返回
        if self.mazeList[startRow][startColumn] != 'O':
            return False
        
        # 当前位置标记为已走过
        self.updatePosition(startRow, startColumn, '+')

        # 如果是出口，返回True
        if self.isExit(startRow, startColumn):
            return True

        # 递归搜索四个方向
        found = self.searchFrom(startRow - 1, startColumn) or \
                self.searchFrom(startRow + 1, startColumn) or \
                self.searchFrom(startRow, startColumn - 1) or \
                self.searchFrom(startRow, startColumn + 1)

        if found:
            return True
        else:
            # 如果无法找到路径，标记为回退
            self.updatePosition(startRow, startColumn, '-')
            return False

def main():
    maze = Maze("maze.txt")  # 迷宫文件路径
    
    # 绘制迷宫
    maze.drawMaze()
    
    # 设置起始位置
    startRow, startColumn = 1, 1  # 例：从 (1, 1) 开始
    maze.searchFrom(startRow, startColumn)
    
    t.done()  # 结束turtle绘图

if __name__ == "__main__":
    main()
