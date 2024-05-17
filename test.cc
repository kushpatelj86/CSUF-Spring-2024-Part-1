#include <ctype.h>
#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
#include <cstring>

#include <vector>
#include <stack>
using namespace std;

vector<string> keywords = {"auto","break","case","char", 
    "const","continue","default","do", "double",
    "else","enum","extern","float","for",
    "goto","if","int","long","register","return",
    "short","signed","sizeof","static","struct",
    "switch","typedef","union","unsigned","void",
    "volatile","while"};

vector<char> seperators = {'\'', '(', ')', '{','}', '[',']',',','.',':',';' };

vector<char> operators ={'+','-','*','/','%','&','|','>','<','='};
vector<char> delimeters = { ' ',  '+' , '-' , '*' , '/' , ',', ';','>', '<', '='
    , '(', ')', '[', ']'
    , '{','}'};

vector<char> numbers = { '0','1','2','3','4','5','6','7','8','9'};


bool isKeyword(string key)
{
  

     
        if(key == "auto" || key == "break"|| key == "case"|| key == "char"
        || key ==  "const"|| key == "continue"|| key == "default"|| key == "do"|| 
        key ==  "double"|| key == "else"|| key == "enum"|| key == "extern"|| 
        key == "float"|| key == "for"|| key == "goto"|| key == "if"|| key == "int"
        || key == "long"|| key == "register"|| key == "return"|| key == "short"
        || key == "signed"|| key == "sizeof"|| key == "static"|| key == "struct"
        || key == "switch"|| key == "typedef"|| key == "union"|| key == "unsigned"
        || key == "void"|| key == "volatile"|| key == "while" )
        {
            return true;
        }
    

    return false;
}

bool isSeperator(char sep)
{
     for(auto i : seperators)
    {
        if(sep == i)
        {
            return true;
        }
    }
    return false;
}

bool isOperator(char op)
{
    for(int i =0; i < 10;i++)
    {
        if(op == operators[i])
        {
            return true;
        }
    }
    return false;

}


bool isDelimeter(char punc)
{
    for(int i = 0; i < delimeters.size();i++)
    {
        if(delimeters[i] == punc)
        {
            return true;
        }
    }
    return false;
}


bool isIdentifier(string id)
{
    for(int i = 0; i < numbers.size(); i++)
    {
        if (id[0] == numbers[i])  
        {
            return false;
        }
    }

    if(isDelimeter(id[0]) || isSeperator(id[0]) || isOperator(id[0]))
    {
        return false;
    }
    

    return true;
}



bool isReal(string num)
{
    int count = 0;

    for(int foundDot = 0; foundDot < num.length();foundDot++)
    {
        if(num[foundDot] == '.')
        {
            count++;
        }
    }

    if(count == 1)
    {
        return true;
    }
    else 
    {
        return false;
    }


}


bool isInteger(string num)
{
    int count = 0;

    for(int foundDot = 0; foundDot < num.length();foundDot++)
    {
        if(num[foundDot] == '.')
        {
            count++;
        }
    }

    if(count == 0)
    {
        return true;
    }
    else 
    {
        return false;
    }


}

bool isInteger(char num)
{
    int count = 0;

    for(int foundDot = 0; foundDot < numbers.size();foundDot++)
    {
        if(numbers[foundDot] == num)
        {
            return true;

        }
    }

    
    
    
    return false;
    


}



string substring(string s, int left, int right)
{
    string newStr= "";
    for(int i = left; i <= right;i++)
    {
        newStr += s[i];
    }
    return newStr;
}





void readFile(string file)
{
    
    string s = file;
    
        int left = 0;
        int right = 0;
        int strlength = (int) s.length();
        while(right <= strlength && left <= right)
        {
            if(!isDelimeter(s[right]))
            {
                right++;
            }

            if(left == right && (isDelimeter(s[right])))
            { 
                if(isOperator(s[right]))   
                {
                    cout << "Operator: " << s[right] << "\n";
                    right++;
                    left = right;
                } 
                else if(isSeperator(s[right]))
                {
                    cout << "Seperator: " << s[right] << "\n";
                    right++;
                    left = right;
                }
                else if(isInteger(s[right]))
                {
                    cout << "Integer: " << s[right] << "\n";
                    right++;
                    left = right;
                }
                
                else 
                {
                    right++;
                    left = right;
                }

                
            }
            else if(((isDelimeter(s[right])) && left != right) || (left != right && right == strlength))
            {
                string sub = substring(s,  left,  right - 1);
                if(isKeyword(sub))
                {
                    cout << "Keyword: " << sub << "\n";
                    left = right;

                }

                else if(isIdentifier(sub))
                {
                    cout << "Identifier: " << sub << "\n";
                    left = right;
                }
                else if(isReal(sub))
                {
                    cout << "Real: " << sub << "\n";
                    left = right;
                }

                else if(isInteger(sub))
                {
                    cout << "Integer: " << sub << "\n";
                    left = right;
                }
                else 
                {
                    left = right;
                }
                

            }  
        }

    
}
        
        

int main()
{

    readFile("while (k < lower) s = 3.4; ");

    string s = "while (k < lower) s = 3; ";
    
    /////cout << substring("while (k < lower) s = 33.00; ", 0,s.length()) << endl;
    ///cout << substrstr((char*)"while (k < lower) s = 33.00; ", 0,  s.length()) << endl;




    return 0;



}