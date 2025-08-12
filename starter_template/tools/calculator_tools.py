from langchain.tools import tool 
class CalculatorTools():
    @tool ("Make a calculator ")
    def calculate(operation):
        """Useful to calculate any mathmetical operations 
        like multipulication ,division, sum,
        minus,etc.
        The input to this tool should be a mathematical expression like  '60* 800'
        or 4000/4* 2



        """
        try:
            return eval(operation)
        except SyntaxError:
            return"Error : invalid syntax in math operation"