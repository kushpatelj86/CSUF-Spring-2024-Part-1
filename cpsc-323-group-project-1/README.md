CPSC 323 Project 1

Team Members: Kush Patel, Guillermo Montoya, and Alvaro Contreras


The program acts as a lexical analyzer for the compiler, it reads through a file line at a time, similiar to how a compiler does it, there are so many different vectors all pertaining to different types of tokens, there is one vector that stores all the keywords,
there is one vector that stores all the seperators, there is one vector that stores all the operators,there is one vector that stores all the delimeters,and there is one vector that stores all the numbers. Delimeters are characters that seperate pieces of data from each other
and prevents mix ups in token types. There is a "isKeyword" function in which it takes a string as a parameter and loops through the keyword vector to check to see if it s in there, if it is in there it returns true, otherwise it returns false, there is a "isDelimeter" function in which 
it takes a character as a parameter and loops through the delimeter vector  to check to see if it s in there, if it is in there it returns true, otherwise it returns false, there is a "isSeperator" function in which  it takes a character as a parameter and loops through the seperator vector 
to check to see if it s in there, if it is in there it returns true, otherwise it returns false,  there is a "isOperator" function in which it takes a character as a parameter and loops through the operator vector  to check to see if it s in there, if it is in there it returns true, 
otherwise it returns false, there is an "isIdentifier" function, which takes a string as a parameter, it first checks the first character or any character to see if it is a delimeter,seperator,operator or integer, if it is then it returns false other it returns true, there is an "isReal"
function, which counts the number of "." in the function, if there is only one ".", then it returns true or else it returns false, there is an substring function which has a left index which is the starting index and a right index which is the ending index of the substring and it loops from 
the start to the end and appends each character at the string paramater index and appends it to a new string and returns the new string,the substring function will be used to check if it is a keyword, identifier, or any string lexeme, when we read through the file and loop through each line of the file
there is a "isInteger" function which loops through the number vector, if there are any characters that are not integers it return false, otherwise it returns true, there is a "isOperator" function which loops through the operator vector, if there are any characters that are not operatoes it return false,
otherwise it returns true. There is a lexer function which then takes an string file as a paramter and reads through string file and loops through each line of the string file using two int values as indexes which are left and right, and left tells its the beggining of the loop and right tells its 
the end of the loop the string loops when left is less than or equal to right or right is less than or equal to the string length, if the left and right numbers are the same then its only looking at one character and if the left and right are different its looking for or comparing a string, when the left
and right are different it gets a substring from the left index to the right index minus 1, and it compares the string and checks if it is a keyword, identifier, operator, real or integer when the character at the right index of the string is a delimeter and if it is a delimeter, then it gets a substring from left to right -1 because they don't want the delimeter in the string and it makes sure the delimeter isn't appended to the substring, if it is a keyword, identifier, integer, or operator then it would output the token and lexeme into a new output file and set the left index equal to the right index, if there is no delimeter at the right index of the string it increments the right and if the left and right are equal to each other and if it is a delimeter it then checks to see if that character is an operator, seperator, integer, and under call conditions it increments the right and sets the left equal
to the right, if a character or string mrrts a condition through the function calls then it gets outputted to the output file and when the loop stops, the output file is generated through a main function in the program.


Token classes

Keywords,
Identifiers,
Integers(String/Multi-Dight),
Reals,
Operators(String/Multi-Operator),
Seperators,
Operators(Character/Single-Operator),
Integers(Character/Single-Dight)




