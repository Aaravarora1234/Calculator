from tkinter import *

Root = Tk()
Root.geometry('288x330')
Root.config(bg = 'black')
Root.title('Calculator')
Root.resizable(False, False)
Root.iconbitmap('G:\Programs\Python\Python Projects\Calculator\Calculator.ico')

Number_Sensor = ''
Expression = ''
Equation = StringVar()

Textbox = Entry(Root, width = 20, textvariable = Equation, font = ('Helvetica 17'), fg = 'white', bg = 'black', borderwidth = 0)
Textbox.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 10)

def Number_Click(Number, Limit_Reached = False, Bracket_Types = [')','}',']']):
    try :
        global Expression 
        global Number_Sensor      
        Expression = str(Expression) + Number
        Number_Sensor = Number_Sensor + Number
        if (len(Expression) >= 21):
            raise IndexError ('Limit Exceeded')
        else :
            Equation.set(Expression)
    except :
        Equation.set('Limit Exceeded')
        Expression = ''
        Number_Sensor = ''

def Symbol_Click(Symbol, Limit_Reached = False):
    try :
        global Expression 
        global Number_Sensor
        if (Expression == ''):
            raise ValueError("Error")
        elif (Expression[len(Expression) - 1] in ['+','−','×','/','%']):
            raise ValueError("Error")
        Expression = str(Expression) + Symbol
        Number_Sensor = ''
        if (len(Expression) >= 21):
            Limit_Reached = True
            raise IndexError ('Limit Exceeded')
        else :
            Equation.set(Expression)
    except :
        if (Limit_Reached == True):
            Equation.set('Limit Exceeded')
        else :
            Equation.set('Error')
        Expression = ''
        Number_Sensor = ''

def Integer_Switch(Term_Division = [], Digits = 0, Limit_Reached = False):
    try :
        global Expression
        global Number_Sensor
        if (Expression == ''):
            raise ValueError("Error")
        elif (Expression[len(Expression) - 1] in ['+','−','×','/','%']):
            raise ValueError("Error")
        elif ('(' in Expression or '{' in Expression or '[' in Expression and ')' in Expression or ')' in Expression or ']' in Expression):
            Term_Division = [Index for Index in range(len(Expression)) if Expression[Index] in ['+','−','×','/','%'] and Expression[Index + 1] in ['(','{','['] and Expression[Index - 1] in [')','}',']']]
            if (Term_Division == []):
                if (Expression[len(Expression) - 1] not in [')','}',']']):
                    for Character in Number_Sensor :
                        Digits = Digits + 1
                    Expression = Expression[ : Digits * -1] + '(−' + Expression[-1 * Digits : ] + ')'
                elif (Expression[len(Expression) - 1] == ')'):
                    Expression = '{−' + Expression + '}'
                elif (Expression[len(Expression) - 1] == '}'):
                    Expression = '[−' + Expression + ']'
                elif (Expression[len(Expression) - 1] == ']'):
                    Expression = '(−' + Expression + ')'
            elif (Expression[max(Term_Division) + 1] == '('):
                Expression = Expression[ : max(Term_Division) + 1] + '{−' + Expression[max(Term_Division) + 1 : ] + '}'
            elif (Expression[max(Term_Division) + 1] == '{'): 
                Expression = Expression[ : max(Term_Division) + 1] + '[−' + Expression[max(Term_Division) + 1 : ] + ']'
            elif (Expression[max(Term_Division) + 1] == '['):
                Expression = Expression[ : max(Term_Division) + 1] + '(−' + Expression[max(Term_Division) + 1 : ] + ')'
        else :
            for Character in Number_Sensor :
                Digits = Digits + 1
            Expression = Expression[ : Digits * -1] + '(−' + Expression[-1 * Digits : ] + ')'
        if (len(Expression) >= 28):
            Limit_Reached = True
            raise IndexError ('Limit Exceeded')
        else :
            Equation.set(Expression)
    except :
        if (Limit_Reached == True):
            Equation.set('Limit Exceeded')
        else :
            Equation.set('Error')
        Expression = ''
        Number_Sensor = ''

def Bracket (Term_Division = [], Digits = 0, Limit_Reached = False):
    try :
        global Expression
        if (Expression == '' ):
            raise ValueError("Error")
        elif (Expression[len(Expression) - 1] in ['+','-','×','/','%']):
            raise ValueError("Error")
        Term_Division = [Index for Index in range(len(Expression)) if Expression[Index] in ['+','−','×','/','%'] and Expression[Index + 1] in ['(','{','['] and Expression[Index - 1] in [')','}',']']]
        if (Term_Division == []):
            if (Expression[len(Expression) - 1] not in [')','}',']']):
                Term_Division = [Index for Index in range(len(Expression)) if Expression[Index] in ['+','−','×','/','%'] and Expression[Index - 1] in [')','}',']']]
                if (Term_Division == []):
                    Expression = '(' + Expression + ')'
                else :
                    Expression = Expression[ : max(Term_Division) + 1] + '(' + Expression[max(Term_Division) + 1 : ] + ')'
            else :
                if (Expression[len(Expression) - 1] == ')'):
                    Expression = '{' + Expression + '}'
                elif (Expression[len(Expression) - 1] == '}'):
                    Expression = '[' + Expression + ']'
                elif (Expression[len(Expression) - 1] == ']'):
                    Expression = '(' + Expression + ')'
        elif (Expression[max(Term_Division) + 1] == '('):
            Expression = Expression[ : max(Term_Division) + 1] + '{' + Expression[max(Term_Division) + 1 : ] + '}'
        elif (Expression[max(Term_Division) + 1] == '{'): 
            Expression = Expression[ : max(Term_Division) + 1] + '[' + Expression[max(Term_Division) + 1 : ] + ']'
        elif (Expression[max(Term_Division) + 1] == '['):
            Expression = Expression[ : max(Term_Division) + 1] + '(' + Expression[max(Term_Division) + 1 : ] + ')'
        if (len(Expression) > 28):
            Limit_Reached = True
            raise IndexError ('Limit Exceeded')
        else :
            Equation.set(Expression)
    except :
        if (Limit_Reached == True):
            Equation.set('Limit Exceeded')
        else :
            Equation.set('Error')
        Expression = ''
        Number_Sensor = ''

def Equal(Limit_Reached = False): 
    try : 
        global Expression
        global Number_Sensor
        if (Expression == ''):
            raise ValueError("Error")
        elif ('%' in Expression or '×' in Expression or '−' in Expression): 
            for Special_Character in Expression :
                if (Special_Character == '×'):
                    Expression = Expression.replace(Special_Character, '*')
                elif (Special_Character == '%'):
                    Expression = Expression.replace(Special_Character, '*1/100')
                elif (Special_Character == '−'):
                    Expression = Expression.replace(Special_Character,'-')
        if ('{' in Expression and '}' in Expression):
            Expression = Expression.replace('{', '(')
            Expression = Expression.replace('}', ')')
        if ('[' in Expression and ']' in Expression):
            Expression = Expression.replace('[', '(')
            Expression = Expression.replace(']', ')')
        Expression = str(eval(Expression))
        if ('-' in Expression):
            Expression = Expression.replace('-', '−')
        Expression = Expression.replace(')','')
        Expression = Expression.replace('(','')
        if (len(Expression) >= 21):
            Limit_Reached = True
            raise IndexError ('Limit Exceeded')
        else :
            Equation.set(Expression)
    except :
        if (Limit_Reached == True):
            Equation.set('Limit Exceeded')
        else :
            Equation.set('Error')
        Expression = ''
        Number_Sensor = ''


def Clear():
    global Expression
    global Number_Sensor 
    Expression = ''
    Number_Sensor = ''
    Equation.set(Expression)

Clear_Button = Button(Root, text = 'C', font = ('Helvetica 14'), padx = 19, pady = 10, fg = 'black', bg = '#d4d4d2', command = Clear)
Clear_Button.grid(row = 1, column = 0)

Integer = Button(Root, text = '+/-', font = ('Helvetica 14'), padx = 20, pady = 10, fg = 'black', bg = '#d4d4d2', command = Integer_Switch)
Integer.grid(row = 1, column = 1)

Percentage = Button(Root, text = '%', font = ('Helvetica 14'), padx = 25, pady = 10, fg = 'black', bg = '#d4d4d2', command = lambda : Symbol_Click('%'))
Percentage.grid(row = 1, column = 2)

Divide = Button(Root, text = '/', font = ('Helvetica 14'), padx = 23, pady = 10, fg = 'white', bg = '#ff9500', command = lambda : Symbol_Click('/'))
Divide.grid(row = 1, column = 3)

Button_7 = Button(Root, text = '7', font = ('Helvetica 14'), padx = 20, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('7'))
Button_7.grid(row = 2, column = 0)

Button_8 = Button(Root, text = '8', font = ('Helvetica 14'), padx = 25, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('8'))
Button_8.grid(row = 2, column = 1)

Button_9 = Button(Root, text = '9', font = ('Helvetica 14'), padx = 28, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('9'))
Button_9.grid(row = 2, column = 2)

Multiply = Button(Root, text = '×', font = ('Helvetica 15'), padx = 19, pady = 10, fg = 'white', bg = '#ff9500', command = lambda : Symbol_Click('×'))
Multiply.grid(row = 2, column = 3)

Button_4 = Button(Root, text = '4', font = ('Helvetica 14'), padx = 20, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('4'))
Button_4.grid(row = 3, column = 0)

Button_5 = Button(Root, text = '5', font = ('Helvetica 14'), padx = 25, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('5'))
Button_5.grid(row = 3, column = 1)

Button_6 = Button(Root, text = '6', font = ('Helvetica 14'), padx = 28, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('6'))
Button_6.grid(row = 3, column = 2)

Subtract = Button(Root, text = '−', font = ('Helvetica 14'), padx = 20, pady = 10, fg = 'white', bg = '#ff9500', command = lambda : Symbol_Click('−'))
Subtract.grid(row = 3, column = 3)

Button_1 = Button(Root, text = '1', font = ('Helvetica 14'), padx = 20, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('1'))
Button_1.grid(row = 4, column = 0)

Button_2 = Button(Root, text = '2', font = ('Helvetica 14'), padx = 25, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('2'))
Button_2.grid(row = 4, column = 1)

Button_3 = Button(Root, text = '3', font = ('Helvetica 14'), padx = 28, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('3'))
Button_3.grid(row = 4, column = 2)

Add = Button(Root, text = '+', font = ('Helvetica 14'), padx = 20, pady = 10, fg = 'white', bg = '#ff9500', command = lambda : Symbol_Click('+'))
Add.grid(row = 4, column = 3)

Decimal = Button(Root, text = '.', font = ('Helvetica 14'),padx = 23, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('.'))
Decimal.grid(row = 5, column = 0)

Button_0 = Button(Root, text = '0', font = ('Helvetica 14'), padx= 25, pady = 10, fg = 'white', bg = '#505050', command = lambda : Number_Click('0'))
Button_0.grid(row = 5, column = 1)

Brackets = Button(Root, text = '( )', font = ('Helvetica 14'), padx = 25, pady = 10, fg = 'white', bg = '#505050', command = Bracket)
Brackets.grid(row = 5, column = 2)

Equal_Button = Button(Root, text = '=', font = ('Helvetica 14'),padx = 20, pady = 10, fg = 'white', bg = '#ff9500', command = Equal)
Equal_Button.grid(row = 5, column = 3)

Root.mainloop()