#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#Example 1:
#
#11110
#11010
#11000
#00000
#Answer: 1
#
#Example 2:
#
#11000
#11000
#00100
#00011
#Answer: 3


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # define union find class using weighted quick union with path compression 
        class UF(object):
            def __init__(self, grid):
                """
                :type grid: List[List[str]]
                :rtype: int
                """
                self.row = len(grid)
                self.col = len(grid[0]) 
                self.uf = range(self.row*self.col)
                self.sz = [1 for i in range(self.row * self.col)]
    
            def convertIndex(self, i, j):
                # input row, col index(starting from zero) in the matrix 
                # return index of corresponding 1D list 
                return i * self.col + j
                
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
                
            def connected(self, i,j):
                return self.root(i) == self.root(j)

        # union connected "1"   
        if grid == []:
            return 0
        ufgrid = UF(grid)
        row = ufgrid.row
        col = ufgrid.col
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == '1':
                    for (x,y) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if (x >= 0 and x < row) and (y >= 0 and y < col):
                            if grid[x][y] == '1':
                                ufgrid.union(ufgrid.convertIndex(i, j), ufgrid.convertIndex(x, y))
        # return the number of distinct root of "1" (the number of island)
        root = set()
        for i in xrange(row*col):
            if grid[i//col][i%col] == '1':
                root.add(ufgrid.root(i))
        return len(root)
        


        
