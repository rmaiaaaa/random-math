import re
from RandomMath.RandomMathOperations import RandomMath

class TestJustSomeMath:

    def test1(self):
        
        #Arrange
        randomMath = RandomMath()
        number = 1

        #Act
        result = randomMath.random_sum(number)
        
        #Assert
        assert result < number

        pass