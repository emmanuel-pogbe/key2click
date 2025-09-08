def get_first_opp(text,index):
    opp1 = ""
    end_char = -1
    for i in range(index-1,-1,-1):
        if text[i].isnumeric() or text[i] == ".":
            opp1 = text[i] + opp1
            end_char = i
        else:
            break
    return [opp1,end_char]
def get_second_opp(text,index):
    opp2 = ""
    end_char = -1
    for i in range(index+1,len(text)):
        if text[i].isnumeric() or text[i] == ".":
            opp2 += text[i]
            end_char = i
        else:
            break
    return [opp2,end_char]
def eval_operator(operator,text):
        index = text.find(operator)
        op1 = get_first_opp(text,index)
        op2 = get_second_opp(text,index)
        operator1 = op1[0]
        operator2 = op2[0]
        if operator1 and operator2:
            if operator == "+":
                result = float(operator1)+float(operator2)
            elif operator == "-":
                result = float(operator1)-float(operator2)
            elif operator == "*":
                result = float(operator1)*float(operator2)
            elif operator == "/":
                if float(operator2) == 0:
                    return None
                result = float(operator1)/float(operator2)
            final = text[:op1[1]] + str(result) + text[op2[1]+1:]
            return final
def evaluate(text):
    while True:
        if "/" in text:
            text = eval_operator("/",text)
            if text == None:
                break
            continue
        if "*" in text:
            text = eval_operator("*",text)
            if text==None:
                break
            continue
        if "+" in text:
            text = eval_operator("+",text)
            if text==None:
                break
            continue
        if "-" in text:
            text = eval_operator("-",text)
            if text==None:
                break
            continue
        break
    return text