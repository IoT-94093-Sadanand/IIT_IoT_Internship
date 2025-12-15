def vowelcount(str1):
    str2=str1.replace(" ","")
    length=len(str2)
    vowelcount=0
    for i in range(length):
        if(str2[i]=='o'or str2[i]=='i'or str2[i]=='e'or str2[i]=='u'or str2[i]=='a'or str2[i] =='A'or str2[i] =='E'or str2[i] =='I'or str2[i] =='O'or str2[i] =='U'):
            vowelcount+=1
    print("vowel=",vowelcount)
    return vowelcount

def consonantcount(str1):
    str2=str1.replace(" ","")
    length=len(str2)
    consonantcount =0
    for i in range(length):
        if(str2[i] !='o'and str2[i] !='i'and str2[i] !='e'and str2[i] !='u'and str2[i] !='a' and str2[i] !='A'and str2[i] !='E'and str2[i] !='I'and str2[i] !='O'and str2[i] !='U'):
            consonantcount+=1
    print("consonant=",consonantcount)
    return consonantcount
    
def ratio():
     vol= vowelcount(str)
     con = consonantcount(str)
     ratio = vol/con
     print("ratio =",ratio)

    
    
str=input("enter your string = ")
vowelcount(str)
consonantcount(str)
ratio()