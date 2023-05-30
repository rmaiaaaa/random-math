from RandomMath.RandomMathOperations import RandomMath


class TestJustSomeMath:

    def test_random_sum(self):

        # Arrange
        randomMath = RandomMath()
        number = 1

        # Act
        result = randomMath.random_sum(number)

        # Assert
        assert result > number

        pass

    def test_random_sub(self):

        # Arrange
        randomMath = RandomMath()
        number = 1

        # Act
        result = randomMath.random_sub(number)

        # Assert
        assert result < number

        pass

    def test_random_mul(self):

        # Arrange
        randomMath = RandomMath()
        number = 1

        # Act
        result = randomMath.random_mul(number)

        # Assert
        assert result >= number

        pass
