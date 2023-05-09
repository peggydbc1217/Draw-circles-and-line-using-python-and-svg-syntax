import os  

os.chdir(r'C:\Users\peggydbc1217\Desktop\python')


txt = open('15.txt' , 'r')


global maxnum       #找最大值

maxnum = 0.00

for each_line in txt:     
    
    if each_line.find(' ') !=-1:

        
        (v1 , v2 , a1 , a2 , a3 , a4 , a5 , a6 ) = each_line.split(' ',7)

        
        each_line_max =  float(max(a1,a2,a3,a4,a5,a6 ))  

        if  each_line_max > (maxnum) :

            maxnum =  each_line_max

                    

import os   #輸入svg開頭代碼

os.chdir(r'C:\Users\peggydbc1217\Desktop\python')


txt = open('15.txt' , 'r')

svg = open('L1.svg' ,'w')


svg.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
'<svg width="400px" height="400px"\n'
'viewBox="0 0 0 0"\n'
'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"  version="1.2" baseProfile="tiny">\n'
'<title>ZZ Aromaticity Export</title>\n'
'<desc>Generated with Qt</desc>\n'
'<defs>\n'
'</defs>\n')



for each_line in txt:  #上benzene線段

    
    if each_line.find(' ') !=-1:
        
        (v1 , v2 , d1 , d2 , d3 , d4 , d5 , d6 ) = each_line.split(' ',7)

        num1 = int(v1)

        num2 = int(v2)    
       
        
        svg.write('<path d="M {} {} L {} {} L {} {} L {} {} L {} {} L {} {} z" fill="none" fill-opacity="0.5" \
stroke="#000000" stroke-width="5" stroke-linecap="round" stroke-linejoin="miter" stroke-miterlimit="2"\n'
.format(num1*26*2+num2*-26+104  ,  num2*45+120  ,  num1*26*2+num2*-26+130 ,  num2*45+105,\
num1*26*2+num2*-26+156  , num2*45+120   , num1*26*2+num2*-26+156 , num2*45+150 , \
num1*26*2+num2*-26+130  , num2*45+165   , num1*26*2+num2*-26+104  , num2*45+150  ))




import os  #上圓

os.chdir(r'C:\Users\peggydbc1217\Desktop\python')


txt = open('15.txt' , 'r')

svg = open('L1.svg' ,'a')


txt2 = open('17.txt' , 'r')

for each_line in txt:
    
            
    if each_line.find(' ') !=-1:
        
        
        (v1 , v2 , a1 , a2 , a3 , a4 , a5 , a6 ) = each_line.split(' ',7)

    for each_line in txt2:
        
    
        if each_line.find(' ') !=-1:
            
            

            (b1,c2) = each_line.split(' C :    ',1)


        for each_line in txt2:
            
            
        
            if c2.find('    ') !=-1:
                
                
            
                (c3,b2) = c2.split('    ',1)



            if float(a1) == float(b1):
                   
                   a1 = b2

            elif float(a2) == float(b1):
                       
                   a2 = b2
                       
            elif float(a3) == float(b1):
                             
                   a3 = b2

            elif float(a4) == float(b1):
                   
                   a4 = b2

            elif float(a5) == float(b1):
                   
                   a5 = b2

            elif float(a6) == float(b1):
                   
                   a6 = b2
                       
            svg.write('<circle cx="{}" cy="{}" r="{}" style="fill:hsl(100,100%,50%)" />\n\
<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n\
<circle cx="{}" cy="{}" r="{}" style="fill:hsl(100,100%,50%)" />\n\
<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n\
<circle cx="{}" cy="{}" r="{}" style="fill:hsl(100,100%,50%)" />\n\
<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n'
.format(num1*26*2+num2*-26+104  , num2*45+120   ,  (float(a1)/maxnum*150)    ,\
num1*26*2+num2*-26+130  , num2*45+105   ,          (float(a2)/maxnum*150)    ,\
num1*26*2+num2*-26+156  , num2*45+120   ,          (float(a3)/maxnum*150)    ,\
num1*26*2+num2*-26+156  , num2*45+150   ,          (float(a4)/maxnum*150)    ,\
num1*26*2+num2*-26+130  , num2*45+165   ,          (float(a5)/maxnum*150)    ,\
num1*26*2+num2*-26+104  , num2*45+150   ,          (float(a6)/maxnum*150)     ))




        
svg.close()

txt.close()