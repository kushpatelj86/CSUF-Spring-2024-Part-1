#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cctype>
#include <vector>
#include <map>
using namespace std;

vector<string> keywords = {"auto","break","case","char", 
    "const","continue","default","do", "double",
    "else","enum","extern","float","for",
    "goto","if","int","long","register","return",
    "short","signed","sizeof","static","struct",
    "switch","typedef","union","unsigned","void",
    "volatile","while"};

vector<char> seperators = {'\'', '(', ')', '{','}', '[',']',',','.',':',';' };

vector<char> operators ={'+','-','*','/','%','&','|','>','<','=', '!'};
vector<char> delimeters = { ' ',  '+' , '-' , '*' , '/' , ',', ';','>', '<', '='
    , '(', ')', '[', ']'
    , '{','}'};

vector<char> numbers = { '0','1','2','3','4','5','6','7','8','9'};

bool isKeyword(string key)
{
  

    for(int i = 0; i < keywords.size();i++)
    {
        if(keywords[i] == key)
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




bool isSeperator(char sep)
{
     for(int i = 0; i < 11;i++)
    {
        if(seperators[i] == sep)
        {
            return true;
        }
    }
    return false;
}

bool isOperator(char op)
{
    for(int i =0; i < 11;i++)
    {
        if(operators[i] == op)
        {
            return true;
        }
    }
    return false;

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

bool isIdentifier(string id)
{
     if (id.empty() || !isalpha(id[0]) && id[0] != '_') {
        return false;  // Identifier must start with a letter or underscore
    }

    for (size_t i = 1; i < id.size(); i++) {
        if (!isalnum(id[i]) && id[i] != '_') {
            return false;  // Subsequent characters can be alphanumeric or underscore
        }
    }

    return true;
}



bool isReal(string num)
{
    int count = 0;
    int nonNumCount = 0;
    for(int foundDot = 0; foundDot < num.length();foundDot++)
    {
        if(num[foundDot] == '.')
        {
            count++;
        }
    }

    /*for(int i = 0; i < num.length();i++)
    {
        if(num[i]  !=  '0' && num[i]  !=  '1' && num[i]  !=  '2' && num[i]  !=  '3' &&
        num[i]  !=  '4'&& num[i]  !=  '5'&& num[i]  !=  '6'&& num[i]  !=  '7'&& num[i]  !=  '8'
        && num[i]  !=  '9')
        {
            nonNumCount++;
        }
    }*/ 
    if(count == 1 && nonNumCount == 0)
    {
        return true;
    }
    else 
    {
        return false;
    }
    





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





bool isInteger(string num)
{
    for(int i = 0; i < num.size(); i++) 
    {
        if(!isInteger(num[i]))
        {
            return false;
        }
    }
    return true;

}

bool isOperator(string num)
{
    for(int i = 0; i < num.size(); i++) 
    {
        if(!isOperator(num[i]))
        {
            return false;
        }
    }
    return true;

}


multimap<string,string> lexer(string file)
{
    ifstream myFile;
    myFile.open(file);
    ofstream outFile;
    outFile.open("output.txt");
    string s;
    outFile << " Lexeme       " <<"|"<< "       Token"  << "   \n";
    outFile << "___________________________________________________\n";
    multimap<string,string> tokens;
    while (getline(myFile, s)) 
    {
         
        int left = 0;
        int right = 0;
        int strlength = (int) s.length();

        while(right <= strlength && left <= right)  // if the left and right are
        // equal we are comparing only one character but if the left and right are different
        //we are comparing an entire string 
        {
            if(!isDelimeter(s[right]))
            {
                right++;
            }

            if(left == right && (isDelimeter(s[right])))
            { 
                if(isOperator(s[right]))   
                {
                    outFile << " Operator     " <<"|" <<"       " << s[right] << "   \n";
                    outFile << "_____________________________________________________\n";
                    tokens.insert({"Operator", to_string(s[right])});
                    right++;
                    left = right;
                } 
                else if(isSeperator(s[right]))
                {
                    outFile << " Seperator    " <<"|" <<"       " << s[right] << "       \n";
                    outFile << "_____________________________________________________\n";
                    tokens.insert({"Seperator", to_string(s[right])});
                    right++;
                    left = right;
                }
                else if(isInteger(s[right]))
                {
                    outFile << " Integer       " << "|" <<"       " << s[right] << "      \n";
                    outFile << "_____________________________________________________\n";
                    tokens.insert({"Integer", to_string(s[right])});
                    right++;
                    left = right;
                }
                
                else 
                {
                    right++;
                    left = right;
                }


                
            }
            else if(((isDelimeter(s[right])) && left != right) || 
            (left != right && right == strlength))
            {
                string sub = substring(s,  left,  right - 1);
                if(isKeyword(sub))
                {
                    outFile << " Keyword      " << "|" <<"       " << sub << "   \n";
                    outFile << "_____________________________________________________\n";
                    tokens.insert({"Keyword", sub});
                    left = right;

                }

                else if(isIdentifier(sub))
                {
                    outFile << " Identifier   " << "|" <<"       " << sub << "          \n";
                    outFile << "_____________________________________________________\n";
                    tokens.insert({"Identifier", sub});
                    left = right;
                }
                else if(isReal(sub))
                {
                    outFile << " Real         " << "|" <<"       " << sub << "   \n";
                    outFile << "_____________________________________________________\n";
                    tokens.insert({"Real", sub});
                    left = right;
                }

                else if(isInteger(sub))
                {
                    outFile << " Integer      " << "|" <<"      " << sub << "   \n";
                    outFile << "___________________________________________________\n";
                    tokens.insert({"Integer", sub});
                    left = right;
                }

                else if(isOperator(sub))
                {
                    outFile << " Operator     " << "|" <<"     " << sub << "   \n";
                    outFile << "___________________________________________________\n";
                    tokens.insert({"Operator", sub});
                    left = right;
                }


                else 
                {
                    left = right;
                }

            }  
        }
    }
    return tokens;
}       
        

int main()
{
        multimap<string,string> lex = lexer("input.txt");

        for (multimap<string, string>::iterator it = lex.begin(); it != lex.end();++it)
        {
            cout << it->first << ": " << it->second << endl;
        }
}