def bal_bracket(brackets):
    """
        Take in string of brackets, return bool if the reversed brackets balance out
    """
    if len(brackets) % 2 != 0:
        print('Invalid string. Must be an even number of brackets')
        return None
    else:
        half_point = int(len(brackets) / 2)
        first_half = brackets[0:half_point]
        second_half = brackets[half_point:]
        bracket_pairs = [('{', '}'), ('(', ')'), ('[', ']')]
        comparison = ''
        for char in first_half:
            for pair in bracket_pairs:
                if char == pair[0]:
                    comparison +=  pair[1]
                elif char == pair[1]:
                    comparison +=   pair[0]

        print(first_half )
        print(second_half )
        print(comparison)


bal_bracket('{{(())}}')