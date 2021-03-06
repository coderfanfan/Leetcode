#Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
#A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#For example,
#X X X X
#X O O X
#X X O X
#X O X X
#After running your function, the board should be:
#X X X X
#X X X X
#X X X X
#X O X X



class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # define union find class using weighted quick union with path compression 
        class UF(object):
            def __init__(self, matrix):
                """
                :type grid: List[List[str]]
                :rtype: int
                """
                self.row = len(matrix)
                self.col = len(matrix[0]) 
                self.uf = range(self.row*self.col + 4)  #reserve the last 4 positions for the boarder 
                self.sz = [1 for i in range(self.row * self.col + 4)] #reserve the last 4 positions for the boarder 
                
            def root(self, i):
                while self.uf[i] != i:
                    self.uf[i] = self.uf[self.uf[i]]
                    i = self.uf[i]
                return i
                
            def union(self, i, j):
                p = self.root(i)
                q = self.root(j)
                if p == q:
                    return
                if self.sz[p] < self.sz[q]:
                    self.uf[p] = q
                    self.sz[q] += self.sz[p]
                else:
                    self.uf[q] = p
                    self.sz[p] += self.sz[q]
            def connected(self, i, j):
                return self.root(i) == self.root(j)
        
        if board == []:
            return 
        s = UF(board)
        row = len(board)
        col = len(board[0])
        # union 'O' with neighbor 'O' and boarders
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == 'O':
                    # Union 'O' with neighbor 'O'
                    for (x,y) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if (x >= 0 and x < row) and (y >= 0 and y < col):
                            if board[x][y] == 'O':
                                s.union(i * col + j, x * col + y)
                    # Union 'O' with each boarder (each 'O' can be connected with multiple boarders)
                    if i == 0:
                        s.union(i*col+j, row*col)
                    if i == row - 1:
                        s.union(i*col + j, row*col+1)
                    if j == 0:
                        s.union(i*col+j, row*col+2)
                    if j == col - 1:
                        s.union(i*col+j, row*col+3)
        # flip an 'O' if it is not connected with any boarder
        for i in xrange(row):
            for j in xrange(col):
                connectedToBoarder = s.connected(i*col+j, row*col) or s.connected(i*col+j, row*col+1) or s.connected(i*col+j, row*col+2) or s.connected(i*col+j, row*col+3)
                if board[i][j] == 'O' and not connectedToBoarder:
                    board[i][j] = 'X'
                    
        
