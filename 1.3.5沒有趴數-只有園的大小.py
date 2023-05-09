import os  

os.chdir(r'C:\Users\peggydbc1217\Desktop\python')


txt = open('16.txt' , 'r')


global maxnum       #找最大值

maxnum = 0.00

for each_line in txt:     
    
    if each_line.find(' ') !=-1:

        
        (v1 , v2 , a1 , a3 , a5  ) = each_line.split(' ',4)

        
        each_line_max =  float(max(int(a1),int(a3),int(a5) ))  

        if  each_line_max > (maxnum) :

            maxnum =  each_line_max


        

import os

os.chdir(r'C:\Users\peggydbc1217\Desktop\python')

txt = open('16.txt' , 'r')

svg = open('L1.svg' ,'w')


for each_line in txt:
    
    if each_line.find(' ') !=-1:
        
        (v1 , v2 , a1 , a3 , a5 ) = each_line.split(' ',4)     

        num1 = int(v1)

        num2 = int(v2)

        svg.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
'<svg width="400px" height="400px"\n'
'viewBox="0 0 0 0"\n'
'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"  version="1.2" baseProfile="tiny">\n'
'<title>ZZ Aromaticity Export</title>\n'
'<desc>Generated with Qt</desc>\n'
'<defs>\n'
'</defs>\n')

            
        svg.write('<path d="M {} {} L {} {} L {} {} L {} {} L {} {} L {} {} z" fill="none" fill-opacity="0.5" \
stroke="#000000" stroke-width="5" stroke-linecap="round" stroke-linejoin="miter" stroke-miterlimit="2"\n \
'.format(num1*26*2+num2*-26+104  ,  num2*45+120  ,  num1*26*2+num2*-26+130 ,  num2*45+105,\
num1*26*2+num2*-26+156  , num2*45+120   , num1*26*2+num2*-26+156 , num2*45+150 , \
num1*26*2+num2*-26+130  , num2*45+165   , num1*26*2+num2*-26+104  , num2*45+150 ))

        svg.write('<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n\
<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n\
<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n'\
.format(num1*26*2+num2*-26+104  , num2*45+120   ,  float(a1)/maxnum*15    ,  \
num1*26*2+num2*-26+156  , num2*45+120   ,          float(a3)/maxnum*15 ,  \
num1*26*2+num2*-26+130  , num2*45+165   ,          float(a5)/maxnum*15    ))


        
svg.close()

txt.close()
