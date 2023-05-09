import os  

os.chdir(r'C:\Users\peggydbc1217\Desktop\python')


txt = open('16.txt' , 'r')


global maxnum_v2,maxnum_zz, maxnum_nics, maxnum_homa, maxnum_pdi, maxnum_sci, maxnum_plr, maxnum_bird, maxnum_flu  #找最大值

maxnum = 0.00
maxnum_v2 = 0.0
maxnum_zz =0.0
maxnum_homa =0.0
maxnum_nics = 0.0
maxnum_pdi =0.0
maxnum_sci = 0.0
maxnum_plr =0.0
maxnum_bird =0.0
maxnum_flu =0.0

for each_line in txt:     
    
    if each_line.find('\t') !=-1:

        
        (v1 , v2 , a1 , a2 , a3 ,a4 , a5 , a6 , a7 , a8 ) = each_line.split('\t',9)

        
        

        each_line_max_v2 =  float(v2)

        if  each_line_max_v2 > (maxnum_v2) :

            maxnum_v2 =  each_line_max_v2
        
        each_line_max_zz =  float(a1)

        if  each_line_max_zz > (maxnum_zz) :

            maxnum_zz =  each_line_max_zz
            
        each_line_max_homa =  float(a2)

        if  each_line_max_homa > (maxnum_homa) :

            maxnum_homa =  each_line_max_homa
            
        each_line_max_nics =  float(a3)

        if  each_line_max_nics > (maxnum_nics) :

            maxnum_nics =  each_line_max_nics

        each_line_max_pdi =  float(a4)

        if  each_line_max_pdi > (maxnum_pdi) :

            maxnum_pdi =  each_line_max_pdi

        each_line_max_sci =  float(a5)

        if  each_line_max_sci > (maxnum_sci) :

            maxnum_sci =  each_line_max_sci
            
        each_line_max_plr =  float(a6)

        if  each_line_max_plr > (maxnum_plr) :

            maxnum_plr =  each_line_max_plr

        each_line_max_bird =  float(a7)

        if  each_line_max_bird > (maxnum_bird) :

            maxnum_bird =  each_line_max_bird

        each_line_max_flu =  float(a8)

        if  each_line_max_flu > (maxnum_flu) :

            maxnum_flu =  each_line_max_flu
        

import os

os.chdir(r'C:\Users\peggydbc1217\Desktop\python')

txt = open('16.txt' , 'r')

svg = open('L1.svg' ,'w')


for each_line in txt:
    
    if each_line.find('\t') !=-1:
        
        (v1 , v2 , a1 , a2 , a3 ,a4 , a5 , a6 , a7 , a8  ) = each_line.split('\t',9)     

        num1 = int(v1)

        num2 = int(v2)

        svg.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
'<svg width="0px" height="0px"\n'
'viewBox="0 0 0 0"\n'
'xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"  version="1.2" baseProfile="tiny">\n'
'<title>ZZ Aromaticity Export</title>\n'
'<desc>Generated with Qt</desc>\n'
'<defs>\n'
'</defs>\n')

        



 #8個結構
        #ZZ
        svg.write('<path d="M {} {} L {} {} L {} {} L {} {} L {} {} L {} {} z" fill="none" fill-opacity="0.5" \
stroke="#000000" stroke-width="5" stroke-linecap="round" stroke-linejoin="miter" stroke-miterlimit="2"\n \
'.format(num1*26*2+num2*-26+104  ,  num2*45+120  ,  num1*26*2+num2*-26+130 ,  num2*45+105,\
num1*26*2+num2*-26+156  , num2*45+120   , num1*26*2+num2*-26+156 , num2*45+150 , \
num1*26*2+num2*-26+130  , num2*45+165   , num1*26*2+num2*-26+104  , num2*45+150 ))

        svg.write('<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n'\
.format(num1*26*2+num2*-26+104+26  , num2*45+135   ,  float(a1)/maxnum_zz*22) )

        svg.write('<text fill="#000000" fill-opacity="1" stroke="none" xml:space="preserve" x="{}" y="{}" \
textLength="100px" lengthAdjust="spacing" font-family="Arial Rounded MT Bold" font-size="30px" font-style="Bold" line-height="10">ZZ\n</text>\n' \
.format(104  , maxnum_v2*45+195    ) )

 #HOMA
        svg.write('<path d="M {} {} L {} {} L {} {} L {} {} L {} {} L {} {} z" fill="none" fill-opacity="0.5" \
stroke="#000000" stroke-width="5" stroke-linecap="round" stroke-linejoin="miter" stroke-miterlimit="2"\n \
'.format(num1*26*2+num2*-26+104  ,  num2*45+120+(maxnum_v2*45+195)  ,  num1*26*2+num2*-26+130 ,  num2*45+105+(maxnum_v2*45+195) ,\
num1*26*2+num2*-26+156  , num2*45+120+(maxnum_v2*45+195)    , num1*26*2+num2*-26+156 , num2*45+150+(maxnum_v2*45+195)  , \
num1*26*2+num2*-26+130  , num2*45+165+(maxnum_v2*45+195)    , num1*26*2+num2*-26+104  , num2*45+150+(maxnum_v2*45+195)  ))

        svg.write('<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n'\
.format(num1*26*2+num2*-26+104+26  , num2*45+135+(maxnum_v2*45+195)    ,  float(a2)/maxnum_homa*22) )

        svg.write('<text fill="#000000" fill-opacity="1" stroke="none" xml:space="preserve" x="{}" y="{}" \
textLength="100px" lengthAdjust="spacing" font-family="Arial Rounded MT Bold" font-size="30px" font-style="Bold" line-height="10">HOMA\n</text>\n' \
.format(104  , 2*(maxnum_v2*45+195)    ) )
        
#NICS
        svg.write('<path d="M {} {} L {} {} L {} {} L {} {} L {} {} L {} {} z" fill="none" fill-opacity="0.5" \
stroke="#000000" stroke-width="5" stroke-linecap="round" stroke-linejoin="miter" stroke-miterlimit="2"\n \
'.format(num1*26*2+num2*-26+104  ,  num2*45+120+2*(maxnum_v2*45+195)  ,  num1*26*2+num2*-26+130 ,  num2*45+105+2*(maxnum_v2*45+195),\
num1*26*2+num2*-26+156  , num2*45+120+2*(maxnum_v2*45+195)   , num1*26*2+num2*-26+156 , num2*45+150+2*(maxnum_v2*45+195) , \
num1*26*2+num2*-26+130  , num2*45+165+2*(maxnum_v2*45+195)   , num1*26*2+num2*-26+104  , num2*45+150+2*(maxnum_v2*45+195) ))

        svg.write('<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n'\
.format(num1*26*2+num2*-26+104+26  , num2*45+135+2*(maxnum_v2*45+195)   ,  float(a3)/maxnum_nics*22) )

        svg.write('<text fill="#000000" fill-opacity="1" stroke="none" xml:space="preserve" x="{}" y="{}" \
textLength="100px" lengthAdjust="spacing" font-family="Arial Rounded MT Bold" font-size="30px" font-style="Bold" line-height="10">NICS\n</text>\n' \
.format(104  , 3*(maxnum_v2*45+195)    ) )
        
#PDI

        svg.write('<path d="M {} {} L {} {} L {} {} L {} {} L {} {} L {} {} z" fill="none" fill-opacity="0.5" \
stroke="#000000" stroke-width="5" stroke-linecap="round" stroke-linejoin="miter" stroke-miterlimit="2"\n \
'.format(num1*26*2+num2*-26+104  ,  num2*45+120+3*(maxnum_v2*45+195)  ,  num1*26*2+num2*-26+130 ,  num2*45+105+3*(maxnum_v2*45+195),\
num1*26*2+num2*-26+156  , num2*45+120+3*(maxnum_v2*45+195)   , num1*26*2+num2*-26+156 , num2*45+150+3*(maxnum_v2*45+195) , \
num1*26*2+num2*-26+130  , num2*45+165+3*(maxnum_v2*45+195)   , num1*26*2+num2*-26+104  , num2*45+150+3*(maxnum_v2*45+195) ))

        svg.write('<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n'\
.format(num1*26*2+num2*-26+104+26  , num2*45+135+3*(maxnum_v2*45+195)   ,  float(a4)/maxnum_pdi*22) )       
        svg.write('<text fill="#000000" fill-opacity="1" stroke="none" xml:space="preserve" x="{}" y="{}" \
textLength="100px" lengthAdjust="spacing" font-family="Arial Rounded MT Bold" font-size="30px" font-style="Bold" line-height="10">PDI\n</text>\n' \
.format(104  , 4*(maxnum_v2*45+195)   ) )

#SCI
        svg.write('<path d="M {} {} L {} {} L {} {} L {} {} L {} {} L {} {} z" fill="none" fill-opacity="0.5" \
stroke="#000000" stroke-width="5" stroke-linecap="round" stroke-linejoin="miter" stroke-miterlimit="2"\n \
'.format(num1*26*2+num2*-26+104  ,  num2*45+120+4*(maxnum_v2*45+195)  ,  num1*26*2+num2*-26+130 ,  num2*45+105+4*(maxnum_v2*45+195),\
num1*26*2+num2*-26+156  , num2*45+120+4*(maxnum_v2*45+195)   , num1*26*2+num2*-26+156 , num2*45+150+4*(maxnum_v2*45+195) , \
num1*26*2+num2*-26+130  , num2*45+165+4*(maxnum_v2*45+195)   , num1*26*2+num2*-26+104  , num2*45+150+4*(maxnum_v2*45+195) ))

        svg.write('<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n'\
.format(num1*26*2+num2*-26+104+26  , num2*45+135+4*(maxnum_v2*45+195)   ,  float(a5)/maxnum_sci*22) )


        svg.write('<text fill="#000000" fill-opacity="1" stroke="none" xml:space="preserve" x="{}" y="{}" \
textLength="100px" lengthAdjust="spacing" font-family="Arial Rounded MT Bold" font-size="30px" font-style="Bold" line-height="10">SCI\n</text>\n' \
.format(104  , 5*(maxnum_v2*45+195)    ) )

#PLR
        svg.write('<path d="M {} {} L {} {} L {} {} L {} {} L {} {} L {} {} z" fill="none" fill-opacity="0.5" \
stroke="#000000" stroke-width="5" stroke-linecap="round" stroke-linejoin="miter" stroke-miterlimit="2"\n \
'.format(num1*26*2+num2*-26+104  ,  num2*45+120+5*(maxnum_v2*45+195)  ,  num1*26*2+num2*-26+130 ,  num2*45+105+5*(maxnum_v2*45+195),\
num1*26*2+num2*-26+156  , num2*45+120+5*(maxnum_v2*45+195)   , num1*26*2+num2*-26+156 , num2*45+150+5*(maxnum_v2*45+195) , \
num1*26*2+num2*-26+130  , num2*45+165+5*(maxnum_v2*45+195)   , num1*26*2+num2*-26+104  , num2*45+150+5*(maxnum_v2*45+195) ))

        svg.write('<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n'\
.format(num1*26*2+num2*-26+104+26  , num2*45+135+5*(maxnum_v2*45+195)   ,  float(a6)/maxnum_plr*22) )
        svg.write('<text fill="#000000" fill-opacity="1" stroke="none" xml:space="preserve" x="{}" y="{}" \
textLength="100px" lengthAdjust="spacing" font-family="Arial Rounded MT Bold" font-size="30px" font-style="Bold" line-height="10">PLR\n</text>\n' \
.format(104  , 6*(maxnum_v2*45+195)   ) )        
#Bird

        svg.write('<path d="M {} {} L {} {} L {} {} L {} {} L {} {} L {} {} z" fill="none" fill-opacity="0.5" \
stroke="#000000" stroke-width="5" stroke-linecap="round" stroke-linejoin="miter" stroke-miterlimit="2"\n \
'.format(num1*26*2+num2*-26+104  ,  num2*45+120+6*(maxnum_v2*45+195)  ,  num1*26*2+num2*-26+130 ,  num2*45+105+6*(maxnum_v2*45+195),\
num1*26*2+num2*-26+156  , num2*45+120+6*(maxnum_v2*45+195)   , num1*26*2+num2*-26+156 , num2*45+150+6*(maxnum_v2*45+195) , \
num1*26*2+num2*-26+130  , num2*45+165+6*(maxnum_v2*45+195)   , num1*26*2+num2*-26+104  , num2*45+150+6*(maxnum_v2*45+195) ))

        svg.write('<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n'\
.format(num1*26*2+num2*-26+104+26  , num2*45+135+6*(maxnum_v2*45+195)   ,  float(a7)/maxnum_bird*22) )
        svg.write('<text fill="#000000" fill-opacity="1" stroke="none" xml:space="preserve" x="{}" y="{}" \
textLength="100px" lengthAdjust="spacing" font-family="Arial Rounded MT Bold" font-size="30px" font-style="Bold" line-height="10">Bird\n</text>\n' \
.format(104  , 7*(maxnum_v2*45+195)  ) )

#FLU

        svg.write('<path d="M {} {} L {} {} L {} {} L {} {} L {} {} L {} {} z" fill="none" fill-opacity="0.5" \
stroke="#000000" stroke-width="5" stroke-linecap="round" stroke-linejoin="miter" stroke-miterlimit="2"\n \
'.format(num1*26*2+num2*-26+104  ,  num2*45+120+7*(maxnum_v2*45+195)  ,  num1*26*2+num2*-26+130 ,  num2*45+105+7*(maxnum_v2*45+195),\
num1*26*2+num2*-26+156  , num2*45+120+7*(maxnum_v2*45+195)   , num1*26*2+num2*-26+156 , num2*45+150+7*(maxnum_v2*45+195) , \
num1*26*2+num2*-26+130  , num2*45+165+7*(maxnum_v2*45+195)   , num1*26*2+num2*-26+104  , num2*45+150+7*(maxnum_v2*45+195) ))

        svg.write('<circle cx="{}" cy="{}" r="{}" style="fill:hsl(0,100%,50%)" />\n'\
.format(num1*26*2+num2*-26+104+26  , num2*45+135+7*(maxnum_v2*45+195)   ,  float(a8)/maxnum_flu*22) )  

        svg.write('<text fill="#000000" fill-opacity="1" stroke="none" xml:space="preserve" x="{}" y="{}" \
textLength="100px" lengthAdjust="spacing" font-family="Arial Rounded MT Bold" font-size="30px" font-style="Bold" line-height="10">FLU\n</text>\n' \
.format(104  , 8*(maxnum_v2*45+195)   ) )



        
svg.close()

txt.close()
