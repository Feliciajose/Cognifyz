class PatternGenerator:
    @staticmethod
    def generate_pyramid(rows):
        pattern = ""
        for i in range(1, rows + 1):
            pattern += " " * (rows - i) + str(i) * (2 * i - 1) + "\n"
        return pattern

    @staticmethod
    def generate_square(rows):
        pattern = ""
        for i in range(1, rows + 1):
            pattern += str(i) * rows + "\n"
        return pattern

    @staticmethod
    def generate_alternating(rows):
        pattern = ""
        for i in range(1, rows + 1):
            pattern += " " * (rows - i) + str(i) * i + "\n"
        return pattern
