class Parser:
    def __init__(self):
        self.stack = []
        self.table = {
            (0, 'id'): 's5',
            (0, '('): 's4',
            (0, 'E'): 1,
            (0, 'T'): 2,
            (0, 'F'): 3,
            (1, '+'): 's6',
            (1, '$'): 'acc',
            (2, '+'): 'r2',
            (2, '*'): 's7',
            (2, ')'): 'r2',
            (2, '$'): 'r2',
            (3, '+'): 'r4',
            (3, '*'): 'r4',
            (3, ')'): 'r4',
            (3, '$'): 'r4',
            (4, 'id'): 's5',
            (4, '('): 's4',
            (4, 'E'): 8,
            (4, 'T'): 2,
            (4, 'F'): 3,
            (5, '+'): 'r6',
            (5, '*'): 'r6',
            (5, ')'): 'r6',
            (5, '$'): 'r6',
            (6, 'id'): 's5',
            (6, '('): 's4',
            (6, 'T'): 9,
            (6, 'F'): 3,
            (7, 'id'): 's5',
            (7, '('): 's4',
            (7, 'F'): 10,
            (8, '+'): 's6',
            (8, ')'): 's11',
            (9, '+'): 'r1',
            (9, '*'): 's7',
            (9, ')'): 'r1',
            (9, '$'): 'r1',
            (10, '+'): 'r3',
            (10, '*'): 'r3',
            (10, ')'): 'r3',
            (10, '$'): 'r3',
            (11, '+'): 'r5',
            (11, '*'): 'r5',
            (11, ')'): 'r5',
            (11, '$'): 'r5',
        }

    def parse(self, input_str):
        self.stack.append(0)  # Initial state
        input_str += '$'  # Add end marker
        idx = 0  # Input string index
        while True:
            state = self.stack[-1]
            symbol = input_str[idx:idx + 2] if input_str[idx:idx + 2] in ['id', 'E', 'T', 'F'] else input_str[idx]

            if (state, symbol) in self.table:
                action = self.table[(state, symbol)]
                print("Stack before action:", self.stack)  # Print stack before taking action
                print("State:", state)
                print("Symbol:", symbol)
                print("Action:", action)

                if isinstance(action, int):  # GOTO
                    self.stack.append(symbol)
                    self.stack.append(action)
                    idx += len(symbol) if len(symbol) > 1 else 1
                elif action[0] == 's':  # Shift
                    self.stack.append(symbol)
                    self.stack.append(int(action[1:]))
                    idx += len(symbol) if len(symbol) > 1 else 1
                elif action[0] == 'r':  # Reduce
                    print("Action while reduction: %s" % action)
                        


                    rule_num = int(action[1:])
                    if rule_num == 6:  # Reduction rule for F -> id
                        self.reduce_rule_6(rule_num)
                    elif rule_num == 4:
                        self.reduce_rule_4(rule_num)

                    elif rule_num == 3:
                        self.reduce_rule_3(rule_num)

                    elif rule_num == 2:

                        self.reduce_rule_2(rule_num)


                    elif rule_num == 1:

                        self.reduce_rule_1(rule_num)

                    else:
                        # Handle other reduction rules
                        pass

                elif action == 'acc':  # Accept
                    return "String is accepted."
                
            else:
                print("Stack before action:", self.stack)  # Print stack before error
                return "String is not accepted."

    def reduce_rule_6(self, num):
        # F -> id
        print("num ", num)
        print("Stack before reduction:", self.stack)  # Print stack before reduction
        index = self.stack.index("id") + 1
        print("index ", index)
        print("num ", self.stack[index])
        a = self.stack[index]
        self.stack.remove("id")
        self.stack.remove(a)
        self.stack.append("F")  

        print((num, "F") in self.table)
        j = self.table[(num, "F")]
        print(j)
        self.stack.append(j)  
        print("Stack after reduction:", self.stack)  # Print stack after reduction


    def reduce_rule_4(self, num):
        #T→ F

        print("num ", num)
        print("Stack before reduction:", self.stack)  # Print stack before reduction
        index = len(self.stack) - 1
        while self.stack[index] != "F":
            index -= 1  # Find the index of 'F'
        self.stack = self.stack[:index]  # Remove elements after 'F' (including 'F')
        self.stack.append("T")
        print((num, "T") in self.table)
        j = self.table[(num, "T")]



        
        print(j)
        self.stack.append(j)  
        print("Stack after reduction:", self.stack)  # Print stack after reduction


    def reduce_rule_2(self, num):
    # E -> T
        print("num ", num)
        print("Stack before reduction:", self.stack)  # Print stack before reduction
        index = len(self.stack) - 1
        while self.stack[index] != "T":
            index -= 1  # Find the index of 'T'
        self.stack = self.stack[:index]  # Remove elements after 'T' (including 'T')
        print((num, "E") in self.table)
        key = (num, "E")  
        print("key in " ,key in self.table)      
        if key in self.table == True:
            
            j = self.table[key]
            self.stack.append("E")
            self.stack.append(j)

    def reduce_rule_3(self, num):
        # T -> T * F
        print("num ", num)
        print("Stack before reduction:", self.stack)  # Print stack before reduction
        index1 = self.stack.index("T") + 1
        print("Index1:", index1)
        index2 = self.stack.index("*") + 1
        print("Index2:", index2)

        index3 = self.stack.index("F") + 1
        print("Index3:", index3)
        num1 =   self.stack[index1]
        print("Num1:", num1)
        num2 =   self.stack[index2]
        print("Num2:", num2)
        num3 =   self.stack[index3]
        print("Num3:", num3)
        self.stack.remove("T")
        self.stack.remove(num1)
        self.stack.remove("*")
        self.stack.remove(num2)
        self.stack.remove("F")
        self.stack.remove(num3)
        self.stack.append("T")
        self.stack.append(self.table[(num,"T")])

    def reduce_rule_1(self, num):
        # E -> E + T
        print("num ", num)
        print("Stack before reduction:", self.stack)  # Print stack before reduction
        index1 = self.stack.index("E") + 1
        print("Index1:", index1)
        index2 = self.stack.index("+") + 1
        print("Index2:", index2)

        index3 = self.stack.index("T") + 1
        print("Index3:", index3)
        num1 =   self.stack[index1]
        print("Num1:", num1)
        num2 =   self.stack[index2]
        print("Num2:", num2)
        num3 =   self.stack[index3]
        print("Num3:", num3)
        self.stack.remove("E")
        self.stack.remove(num1)
        self.stack.remove("+")
        self.stack.remove(num2)
        self.stack.remove("T")
        self.stack.remove(num3)
        self.stack.append("E")
        self.stack.append(self.table[(num,"E")])

        





   
            








          






# Test the LR parser with sample input strings
parser = Parser()
print("Output:", parser.parse("id+id"))
print()
