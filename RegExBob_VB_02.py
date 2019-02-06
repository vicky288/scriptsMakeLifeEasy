"""
This script can be used to convert a VBScript for which a regex cann't be written based on unique patterns.
This script randomizes variables and takes care of white space evasion to generate a regex which matches different variations of the script.
"""
regex_string = ""
alphaNumerics = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
metaChars = {'^':'\\x5e', '$':'\\x24', '[':'\\x5b', ']':'\\x5d', '(':'\\x28', ')':'\\x29', '{':'\\x7b', '}':'\\x7d', '.':'\\x2e', '*':'\\x2a', '+':'\\x2b', '?':'\\x3f', '<':'\\x3c', '>':'\\x3e', '|':'\\x7c','\\':'\\\\' }
arithmeticOperatorsMeta = ['+','*','<','>','^']
arithmeticOperatorsNonMeta = ['=','%','&','-','/']
nonArithmeticNonMeta = [',']
whiteSpace = ['\x20','\x09']
otherWhiteSpace = ['\x0a','\x0b','\x0c','\x0d']


otherWhiteSpaceCtr = 0;     #To avoid consecutive other white space regex expression
whiteSpaceCtr = 0           #To avoid consecutive white space regex expression
stringLiteralCounter = 0    #To Mark start and end of string
commentCounter = 0          #To Mark start of a comment

def get_reg_char(charVal):
    global otherWhiteSpaceCtr
    global whiteSpaceCtr
    global regex_string
    global stringLiteralCounter
    global commentCounter 
    if charVal == "\'":
        regex_string = regex_string + charVal
        commentCounter = 1
        whiteSpaceCtr = 0
        otherWhiteSpaceCtr = 0
    elif charVal == "\"":
        if whiteSpaceCtr == 1:
            regex_string = regex_string + charVal
        else:
            regex_string = regex_string + "[\\x09\\x20]*" + charVal
        if commentCounter == 1:
            stringLiteralCounter = 0
        else:
            if stringLiteralCounter == 1:
                stringLiteralCounter = 0
            else:
                stringLiteralCounter = 1
        whiteSpaceCtr = 0
        otherWhiteSpaceCtr = 0
    elif charVal in alphaNumerics:
        regex_string = regex_string + charVal
        whiteSpaceCtr = 0
        otherWhiteSpaceCtr = 0 
    elif charVal in nonArithmeticNonMeta:
        if stringLiteralCounter == 0:
            if whiteSpaceCtr == 1:
                regex_string = regex_string + charVal + "[\\x09\\x20]*"
            if whiteSpaceCtr == 0:
                regex_string = regex_string + "[\\x09\\x20]*" + charVal + "[\\x09\\x20]*"
                whiteSpaceCtr = 1
                otherWhiteSpaceCtr = 0
        else:
            regex_string = regex_string + charVal
            whiteSpaceCtr = 0
            otherWhiteSpaceCtr = 0        
    elif charVal in metaChars.keys() and charVal in arithmeticOperatorsMeta:
        if stringLiteralCounter == 0:
            if whiteSpaceCtr == 1:
                regex_string = regex_string + metaChars[charVal] + "[\\x09\\x20]*"
            if whiteSpaceCtr == 0:
                regex_string = regex_string + "[\\x09\\x20]*"+ metaChars[charVal] + "[\\x09\\x20]*"
            whiteSpaceCtr = 1
            otherWhiteSpaceCtr = 0 
        else:
            regex_string = regex_string + metaChars[charVal]
            whiteSpaceCtr = 0
            otherWhiteSpaceCtr = 0
    elif charVal not in metaChars.keys() and charVal in arithmeticOperatorsNonMeta:
        if stringLiteralCounter == 0:
            if whiteSpaceCtr == 1:
                regex_string = regex_string + charVal + "[\\x09\\x20]*"
            if whiteSpaceCtr == 0:
                regex_string = regex_string + "[\\x09\\x20]*"+ charVal + "[\\x09\\x20]*"
            whiteSpaceCtr = 1
            otherWhiteSpaceCtr = 0 
        else:
            regex_string = regex_string + charVal
            whiteSpaceCtr = 0
            otherWhiteSpaceCtr = 0 
    elif charVal in metaChars.keys() and charVal not in arithmeticOperatorsMeta:
        if stringLiteralCounter == 0:
            if whiteSpaceCtr == 1:
                regex_string = regex_string + metaChars[charVal] + "[\\x09\\x20]*"
            if whiteSpaceCtr == 0:
                regex_string = regex_string + "[\\x09\\x20]*"+ metaChars[charVal] + "[\\x09\\x20]*"
            whiteSpaceCtr = 1
            otherWhiteSpaceCtr = 0 
        else:
            regex_string = regex_string + metaChars[charVal]
            whiteSpaceCtr = 0
            otherWhiteSpaceCtr = 0
    elif charVal in whiteSpace and whiteSpaceCtr == 0:
        if stringLiteralCounter == 0:
            regex_string = regex_string + "[\\x09\\x20]*"
            whiteSpaceCtr = 1
            otherWhiteSpaceCtr = 0
        else:
            regex_string = regex_string + charVal
            whiteSpaceCtr = 0
            otherWhiteSpaceCtr = 0     
    elif charVal in otherWhiteSpace and otherWhiteSpaceCtr == 0:
        if stringLiteralCounter == 0:
            regex_string = regex_string + "[\\x09-\\x0d\\x20]*"
            whiteSpaceCtr = 1
            otherWhiteSpaceCtr = 1
        else:
            regex_string = regex_string + charVal
            whiteSpaceCtr = 0
            otherWhiteSpaceCtr = 1
        commentCounter = 0
    else:
        if charVal in whiteSpace:
            whiteSpaceCtr = 1
        elif charVal in otherWhiteSpace:
            otherWhiteSpaceCtr = 1
        else:
            regex_string = regex_string + charVal
            whiteSpaceCtr = 0
            otherWhiteSpaceCtr = 0    


if __name__ == "__main__":
    fileName = raw_input('Enter file Name:')
    file_handle = open(fileName,"rb")
    try:
        byte = file_handle.read(1)
        while byte != "":
            byte = file_handle.read(1)
            #print byte
            get_reg_char(byte)
    finally:
        file_handle.close()
    print regex_string 

"""
#testString = "If Len(ioniiichstic222)<Length Then  ' a8urJSPhfF = \"For Each T2TTMp In I8rQbmO End Function\x0a\x0dioniiichstic222=String(Length-Len(ioniiichstic222),\"0\") &ioniiichstic222    'pad allign with zeros"
testString = "x = a +b\x0a\x0dprint{ \"This is a comment,jui\" \'is my @gmail.com\"test $123\x0a\x0df8TbspmhLQ = \"While Not Z0Jqto.b8VDvBhh Set p0Ntgxy = Nothing Function b6rtM(R7RFSM, X6ZuF \"}"
for eachChar in testString:
    get_reg_char(eachChar)
    
print testString
print "============"
print regex_string   """ 
# http://rextester.com/l/vb
