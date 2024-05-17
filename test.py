def parse(input_string, start_symbol, parse_table):
    stack = [start_symbol, '$']  # Push Starting Symbol and end-of-file marker onto the stack
    input_string += '$'  # Append end-of-file marker to the input string
    index = 0  # Index for tracking the input string

    while stack:
        top_of_stack = stack[-1]  # Top of stack symbol
        current_token = input_string[index]  # Current input token

        if top_of_stack == current_token:  # If top of stack is a terminal symbol
            stack.pop()  # Pop the symbol from the stack
            index += 1  # Move to the next token in the input string
        else:
            # Look up the production in the parse table
            production = parse_table.get((top_of_stack, current_token))

            if production is not None:  # If Table[top_of_stack, current_token] has an entry
                stack.pop()  # Pop the symbol from the stack
                # Push the production symbols onto the stack in reverse order
                for symbol in reversed(production):
                    stack.append(symbol)
            else:
                print("Error: Invalid input at position", index)
                break

# Example usage:
# Define your parse table for the CFG
parse_table = {
    ('E', '+'): ['E', '+', 'T'],
    ('E', 'id'): ['T'],
    ('T', '*'): ['T', '*', 'F'],
    ('T', 'id'): ['F'],
    ('F', 'id'): ['id'],
    ('F', '('): ['(', 'E', ')']
}

input_string = 'id + id * id $'  # Sample input string
start_symbol = 'E'  # Starting symbol of the grammar
parse(input_string, start_symbol, parse_table)
