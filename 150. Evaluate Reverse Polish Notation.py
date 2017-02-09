#Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
#Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
#Some examples:
#  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# below is my solution that beat 96% python submissions

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = ["+","-", "*", "/"]
        stack = []
        for e in tokens:
            if e not in operators:
                stack.append(int(e))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if e == '+':
                    stack.append(op1 + op2)
                elif e == '-':
                    stack.append(op1 - op2)
                elif e == '*':
                    stack.append(op1 * op2)
                else:
                    if op1*op2 < 0 and op1 % op2 != 0:
                        stack.append(op1/op2+1)
                    else:
                        stack.append(op1/op2)
        return stack.pop()
        
