#Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
#For example,
#Given the following matrix:
#
#[
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
#]
#You should return [1,2,3,6,9,8,7,4,5].



class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        elif len(matrix) == 1:
            return matrix[0]
        elif len(matrix[0]) == 1:
            result = []
            for list in matrix:
                result.append(list[0])
            return result
        else:
            result = []
            rowstep = len(matrix[0])
            colstep = len(matrix) -1 
            turn = 1
            r, c = 0, -1 
            while rowstep>= 0 and colstep>= 0:
                if turn%4 == 1:
                    for i in xrange(1, rowstep+1):
                        result.append(matrix[r][c+i])
                    c += rowstep
                    rowstep -= 1
                elif turn%4 == 3:
                    for i in xrange(1, rowstep+1):
                        result.append(matrix[r][c-i])
                    c -= rowstep
                    rowstep -= 1
                elif turn%4 == 2:
                    for j in xrange(1, colstep+1):
                        result.append(matrix[r+j][c])
                    r += colstep 
                    colstep -= 1
                elif turn%4 == 0:
                    for j in xrange(1, colstep+1):
                        result.append(matrix[r-j][c])
                    r -= colstep
                    colstep -= 1
                turn += 1
                print rowstep, colstep
                
            return result
                
            
                
                
                
