import re
import sys
import codecs
import xml.etree.ElementTree as ET
import os
import shutil
import random
from re import sub
import os
import shutil
import glob, os
import PIL
from PIL import Image
  # -*- coding: UTF-8 -*-

#This script converts Markdown Format into Webwork Question format
#Inputs: File location
#Outputs:.pg file,.def file question images are moved to the same folder as the questions
#Notes: Sometimes code may need to be adjusted to address different problems 

 
 
#input file location below
filelocation=r''
#input intial problem set number- need to be updated between modules
setcount=10 


#moving and renaming images
imglinelist=[]
newimglinelist=[]
imgerrormovinglist=[]
imgscaleerrors=[]
def imgmove(imgline,imgcount,filename,filetowrite,qtype):
  if imgline in imglinelist:
    imgindex=imglinelist.index(imgline)
    linetowrite=newimglinelist[imgindex]
    if qtype=='n':
      filetowrite.write('\n')
    else:
      filetowrite.write('\n$BR\n')    
    filetowrite.write(linetowrite)
    if qtype=='n':
      filetowrite.write('\n')
    else:
      filetowrite.write('\n$BR\n')    
  else:
    imglinelist.append(imgline)
    m = re.search("\/(.*?)\]", imgline)
    filename=filename.replace('.md','')
    imgname=m.group(1)
    if '%' in imgname:
      #m = re.search("%/(.*?)\.", imgname)
      #imgname=imgname.rstrip(m.group(1))
      if imgcount==0:
        imgname=imgname.split('%',1)[0]+'.png'
      else:
        imgname=imgname.split('%',1)[0]+' '+str(imgcount)+'.png'
    newname=filelocation+'\\'+filename+str(imgcount)+'.png'
    newimgname=filename+str(imgcount)+'.png'
    originpath=filelocation+"\\"+filename+"\\"+imgname
    subfolders = [ f.path for f in os.scandir(filelocation) if f.is_dir() ]
    width,height=100,100
    #print(subfolders)
    for i in range(len(subfolders)):
      if  filename in subfolders[i]:
        originpath=subfolders[i]+"\\"+imgname
    try:
      with Image.open(originpath) as img:
        width, height = img.size;
        imgScale = 0.35; 
        imgscale=0.35
        width=width*imgscale
        height=height*imgscale
    except:
      try:
        originpath=filelocation+"\\"+newimgname
        with Image.open(originpath) as img:
          width, height = img.size;
          imgscale=0.35
          width=width*imgscale
          height=height*imgscale
      except:
        try:
          newimgname=newimgname.replace(' ','-')
          originpath=filelocation+"\\"+newimgname
          with Image.open(originpath) as img:
            width, height = img.size;
            imgscale=0.35
            width=width*imgscale
            height=height*imgscale          
          
        except:
          imgscaleerrors.append(originpath)
          pass
    
    try:
      os.rename(originpath,newname)
    except:
      imgerrormovinglist.append(originpath)
      pass
    imgcount=imgcount+1
    if qtype=='n':
      newimgname=newimgname.replace(' ','-')
      newimgline='\n[@ image( "'+newimgname+'", width=>'+str(width)+', height=>'+str(height)+') @]*\n'
      newimglinelist.append(newimgline)
      filetowrite.write(newimgline)
      filetowrite.write('END_PGML\nBEGIN_PGML\n')
    else:
      newimgname=newimgname.replace(' ','-')
      filetowrite.write('\n$BR\n$BR\n')
      newimgline='\{ image("'+ newimgname +'" , width=>'+str(width)+', height=>'+str(height)+') \}'
      newimglinelist.append(newimgline)
      filetowrite.write(newimgline) 

  return imgcount
  
  
  
#Translating the formula from markdown to webwork in numerical format questions
#Inputs: l->line of code, continuation-> 1 if formulas have values in multiple equations and 0 if otherwise, anglesint-> 1 if angles are intialized and 0 otherwise
#output: Translated line for formulas
def formulatranslate(l,continuation,anglesint):
  l=re.sub('mathrm{.*?}','',l)
  l=l.replace(r'\times','*').replace(',','')
  l=l.replace('**','').replace('ft','').replace('in.','').replace('m','').replace(r'\underline\bold{','')
  l=re.sub('sqrt{(.*?)}',r'sqrt(\1)',l)
  l=re.sub('frac{(.*?)}{(.*?)}',r'(\1)/(\2)',l)
  l=re.sub('text{(.*?)}','',l)
  l=l.replace('~','')
  if continuation==0:
    l=l.replace('$','')
    l=re.sub('overrightarrow{(.*?)}',r'\$\1',l)
  l=l.replace('\\','')
  l=l.replace('text','')
  l=l.replace('cdot','*')
  l=l.replace('{cos}^{-1}','arccos')
  l=l.replace('{sin}^{-1}','arcsin')
  l=l.replace('{tan}^{-1}','arctan')
  
                                    
  l=l.replace('[','$')#could use re.sub
  l=l.replace('arccos','arcc')
  l=l.replace('arcsin','arcs')
  l=l.replace('arctan','arct')
  l=re.sub('sec\((.*?)\)',r'sec((\1))',l)
  l=re.sub('cos\({(.*?)}\)',r'cos((\1))',l)
  l=re.sub('sin\({(.*?)}\)',r'sin((\1))',l)
  l=re.sub('tan\({(.*?)}\)',r'tan((\1))',l)
  l=re.sub('cot\({(.*?)}\)',r'cot((\1))',l)
  l=re.sub('csc\({(.*?)}\)',r'csc((\1))',l)
  l=re.sub('sec\({(.*?)}\)',r'sec((\1))',l)
  l=re.sub('cos(.*?)\]',r'cos((pi/180)*\1)',l)
  l=re.sub('sin(.*?)\]',r'sin((pi/180)*\1)',l)
  l=re.sub('tan(.*?)\]',r'tan((pi/180)*\1)',l)
  l=re.sub('sec(.*?)\]',r'sec((pi/180)*\1)',l)
  l=re.sub('csc(.*?)\]',r'csc((pi/180)*\1)',l)
  l=re.sub('cot(.*?)\]',r'cot((pi/180)*\1)',l)  
  l=re.sub('(w*?)cos',r'\1*cos',l)
  l=re.sub('(w*?)sin',r'\1*sin',l)
  l=re.sub('(w*?)tan',r'\1*tan',l) 
  l=re.sub(r'arc\*(.*?)',r'arc\1',l)
  l=l.replace('arcc','arccos')
  l=l.replace('arcs','arcsin')
  l=l.replace('arct','arctan') 
  #l=l.replace('arc','(180/pi)*arc)
  l=l.replace(')(',')*(')
 
  
  
  l=l.replace(']$','*$')
  l=l.replace(']','')
  l=l.replace('^','**')
  l=l.replace('{','')
  l=l.replace('}','')
  l=l.replace('[','$')
  l=l.replace(']','')
  l=l.replace('|','')
  l=l.replace('\\','')
  l=l.replace('right','')
  l=l.replace('left','')
  
  if anglesint==1:
    l=l.replace('alpha','$alpha')
    l=l.replace('beta','$beta')
    l=l.replace('gamma','$gamma')
    l=l.replace('cos($alpha','cos((pi/180)*$alpha').replace('cos($beta','cos((pi/180)*$beta').replace('cos($gamma','cos((pi/180)*$gamma')
    l=l.replace('sin($alpha','sin((pi/180)*$alpha').replace('sin($beta','sin((pi/180)*$beta').replace('sin($gamma','sin((pi/180)*$gamma')
    l=l.replace('tan($alpha','tan((pi/180)*$alpha').replace('tan($beta','tan((pi/180)*$beta').replace('tan($gamma','tan((pi/180)*$gamma')
    
  #else:
    ##l=l.replace('arccos','(180/pi)*arccos').replace('arcsin','(180/pi)*arcsin').replace('arctan','(180/pi)*arctan') #use this get for degrees
  
  return l


#function to write the beginning of file
#Input: f2-> file to write to, f-> original file
#output: writing the beginning of the new file
def beginfile(f2,f):

    searchquery = 'Key'
    count=0
    for i, line in enumerate(lines):
        done=0
        if line.startswith(searchquery) or line.startswith('Automatic') and done==0:
                done=1
                f2.write('#')
                f2.write('DESCRIPTION')
                f2.write('\n')
                while count< 5: #while '#Q' not in lines [i+count} and line.strip
                    f2.write('#')
                    f2.write(lines[i+count])#might need to make it a little more efficient
                    count=count+1
                f2.write('#')
                f2.write(lines[i+7])
                f2.write('#')
                f2.write(lines[i+13])
                f2.write('#')
                f2.write(' END DESCRIPTION')
                f2.write('\n\n########################################################\n')
                f2.write('DOCUMENT();\n')
                f2.write('loadMacros(\n')
                f2.write('"PGstandard.pl",	# Standard macros for PG language\n')
                f2.write('"MathObjects.pl",\n')
                f2.write('"PGML.pl",\n')
                f2.write('"parserPopUp.pl",\n')
                f2.write('"parserMultiAnswer.pl",\n')
                f2.write('"parserRadioButtons.pl",')
                f2.write('\n"weightedGrader.pl",\n')
                f2.write('"PGchoicemacros.pl",\n')
                f2.write('\n')
                f2.write('\n"source.pl",\n')
                f2.write('\n')
                f2.write('\n"PGcourse.pl",\n);\n')
                f2.write('TEXT(beginproblem());\n\n')
                f2.write('\n')
                f2.write('\n')
                f2.write('########################################################\n\n')
                f2.write('#Setup\n\n')
                f2.write('Context("Numeric");\n\n')
                f2.write('#---------------Tolerance------------------#\n\n')
                f2.write('Context()->flags->set(\n')
                f2.write('tolerance=>.03,\n')
                f2.write("tolType=>'relative');  #relative or absolute\n")
                f2.write('\n#---- Random variables for this problem --------#\n\n')
                return


                           
#finds the legnth of the original file  
def file_len(file):
  with open(file, 'r', encoding='utf-8') as f:
    for i, l in enumerate(f):
      pass
  return i + 1  

#Translates lines for Numerical response format questions from markdown to webwork
#Input: line to translate
#Output: Translated Line
def translateline(line):
  encoding='utf-8'
  if '_' in line:
    line=re.sub(' ((\S*)_(\w*)) ',r'[`\1`]',line)  
  #line=line.replace('__','[__]')
  line=line.replace('Find the three coordinate direction angles','Find the three coordinate direction angles (in radians) ')#degrees?
  line=line.replace('Find the magnitude and each direction angle','Find the magnitude and each direction angle (in radians)')
  if 'Calculate' in line and 'the' in line and 'angle' in line:
    line=line.replace('angle','angle (in radians)')
  line=re.sub('text{(.)}',r'[`\1`]',line)
  line=line.replace(r'}\,\mathrm','}\ \mathrm')
  line=line.replace('left(','')
  line=line.replace('right)','')
  line=line.replace('$\\','')
  line=line.replace('$','')
  line=line.replace('\\','')
  line=re.sub('\[(.)\]',r'[`[$\1]`]',line)
  line=line.replace('\\times',r'*')
  line=re.sub('overrightarrow{(.*?)}',r'[`\\overrightarrow{\1}`]',line)
  line=re.sub('mathrm{(.*?)}',r' \1',line)
  line=re.sub('cdot',r'[`\\cdot`]',line)
  line=re.sub('~~','',line)
  line=line.replace('**','')
  line=line.replace('}$','')
  line=re.sub('hat{(.)}',r'[`\\hat{\1}`]',line)
  line=line.replace('\cos','[`cos`]')
  line=line.replace('\sin','[`sin`]')
  line=line.replace('\tan','[`tan`]') 
  line=line.replace('quad',' ').replace(r'{y}=,','y =').replace(r'{x}=,','x =').replace(r'{z}=,','z =')
  line=line.replace('theta','[`\\theta`]')
  line=line.replace('phi','[`\\phi`]')
  line=re.sub('mathrm{(.)}',r'[`\1`]',line)
  line=re.sub('\$(.)\$',r'$\1*$',line)
  line=re.sub('ans(\d)',r'$ans\1',line)#re.sub
  line=line.replace('$answer','answer')
  line=re.sub('vec{(.*?)}',r'[`\\vec{\1}`]',line)
  line=line.replace('|','')
  line=re.sub('bold{(.*?)}',r'[`\1`]',line)
  line=re.sub('`]_(.w*)',r'_\1`]',line)
  line=line.replace('circ','[`^{\circ}`]')
  line=line.replace('\xb0','[`^{\circ}`]')
  line=line.replace('degree',' [`^{\circ}`]')
  line=re.sub('\^\((.*?)\)',r'[`^{\1}`]',line)
  line=line.replace('}^[`^','}[`^').replace(']}  m[`\overr',']} m  [`\overr')
  line=re.sub('\(hat\{\[`\[(.*?)\]`\]i\}\)',r'[`[\1]`][`\\hat{i}`]',line) 
  while '_[' in line or ']_' in line:
          line=line.replace('_[','[')
          line=line.replace(']_',']')  
  while '$ans0"}_' in line:
    line=line.replace('ans0"}_','ans0"}')
    line=line.replace('ans0"},','ans0"}')
  line=line.replace('ans0"}[`\hat{k}`]),','ans0"}[`\hat{k}`])')
  line=re.sub('text{~(.*?)}',r'\1',line)
  line=re.sub('text{(.*?)}',r'\1',line)
  line=line.replace('[`[`\overrightarrow{F_2}`]=[____]{"$ans0"}`]','[`\overrightarrow{F_2}`]=[____]{"$ans0"}')
  line=line.replace('Enter your answer:[`d=[____]{"$ans0"}`]','Enter your answer: d=[____]{"$ans0"}')
  line=line.replace('Resultant force at point O: {[____]{"$ans0"}[`\hat{i}`]+[____]{"$ans1"}[`\hat{j}`]}','Resultant force at point O: [____]{"$ans0"}[`\hat{i}`]+[____]{"$ans1"}[`\hat{j}`]').replace('~','')
  line=line.replace('{[____]{"$ans0"}  N [`\cdot`] m}','[____]{"$ans0"}  N [`\cdot`] m').replace('[`[____]{"$ans1"}_`]','[____]{"$ans1"}').replace('[`[____]{"$ans2"}_`]','[____]{"$ans2"} ')
  line=line.replace(r'[`[____]{"$ans0"}`]','[____]{"$ans0"}').replace('w_1','[`w_1`]').replace('w_2','[`w_2`]').replace(r'[`^{\circ}`]ular',r'circular').replace(r'x_{COG}',r'[`x_{COG}`]').replace(r'y_{COG}',r'[`y_{COG}`]').replace(r'z_{COG}',r'[`z_{COG}`]')
  line=line.replace('=,','=')
  line=line.replace('__,','__') 
  line=line.replace(r'{"$ans0"}, lb','{"$ans0"} lb').replace(r'10^3','[`10^3`]').replace(r'times',r'[`\times`]').replace(r'{"$ans0"}, N',r'{"$ans0"} N').replace(r'slugs/ft^2','[`slugs/ft^2`]').replace(r'[`10^3`], N','[`10^3`] N')
  line=line.replace(r'kg/m^2','[`kg/m^2`]').replace(r', [`kg/m^2`]',r' [`kg/m^2`]').replace(r', [`slugs/ft^2`]',r' [`slugs/ft^2`]')
  
  return line

#Translates lines for multiple choice format questions from markdown to webwork
#Input: data->line to translate
#Output: Translated Line
def mctranslate(data):
  #data=re.search
  data=data.replace(r'\,\mathr',' mathr')
  data=data.replace('overrightarrow{}','arrow1')
  data=re.sub('bold{(.*?)}_(w*?)',r'mathbf-/-\1_\2',data)
  mat3=re.findall(r"begin{matrix}(.*?)end{matrix}",data)
  data=data.replace('begin{matrix}','beginmatrix')
  data=data.replace(r'hat{k}\\$$',r'hat{k}').replace(r'hat{j}\\$$',r'hat{j}').replace(r'hat{i}\\$$',r'hat{i}')
  if 'begin{vmatrix}' in data:
    mat1=re.findall(r"begin{vmatrix}(.*?)end{vmatrix}", data)
    m=re.search(r"begin{vmatrix}(.*?)end{vmatrix}", data)
    data=sub('((\w*)_(\w*))',r'\\(\1'+'\\)', data,1)
    p=re.search(r"begin{vmatrix}(.*?)end{vmatrix}", data)
    data=data.replace(p.group(0),m.group(0))  
  if 'overrightarrow ' in data:
      data=re.sub('overrightarrow (w*?)\$',r'(\\overrightarrow{\1}\\)',data)  
  elif 'overrightarrow' in data:
        data=re.sub('overrightarrow{(.*?)}',r'(\\overrightarrow{\1}\)',data)
        m=re.findall(r"overrightarrow{(.*?)}", data)
        data=re.sub('((\w*)_(\w*))',r'\\(\1'+'\\)', data)
        p=re.findall(r"overrightarrow{(.*?)}", data)
        for i in range(len(m)):
            data=data.replace(p[i],m[i])   




        
  elif '_{' in data:
    #m=re.search(r"_{(.*?)}", data)
    data=sub('((\w*)_(\w*))',r'\\(\1', data)
    data=sub('_{(.*?)}',r'_{\1}'+'\\)',data)
    data=sub('_(\w*)',r'_\1'+'\\)',data)
    data=data.replace('\){','{')
    #data=sub('_{(\w*)}',r'_{\1\}'+'\\)', data,1)
    #data=sub('{(.*?)}',r'{\1}\\)',data)
  else:
    data=re.sub('_{2,}_','111',data)
    data=data.replace('_ ','_')
    data=re.sub('111','____',data)
    data=sub('((\w*)_(\w*))',r'\\(\1', data)
    data=sub('_(\w*)',r'_\1'+'\\)',data)
  data=data.replace(',]', ']')
  if 'random' not in data:
    data=data.replace('$', '')
  data=data.replace('\\left(','')
  data=data.replace('\\right)','')
  data=data.replace('\cos','\(\cos\)')
  data=data.replace('\sin','\(\sin\)')
  data=data.replace('\tan','\(\tan\)')
  data=data.replace('\\theta','\(\\theta\)')
  data=data.replace('\\alpha','\(\\alpha\)')
  data=data.replace('\\beta','\(\\beta\)')
  data=data.replace('\\gamma','\(\\gamma\)')
  data=data.replace(r'\delta','\(\\delta\)')  
  #data=sub(r'N','(*)',data)
  #specifcally search within line for string
  data=re.sub('vec{(.*?)}',r'(\\vec{(\1)}\\)',data)
  #data=data.replace('vec','hbc')
  #data=data.replace('\hbc{', '\( '+'\hbc{')
  #data=data.replace('hbc','vec')
  #data=data.replace('}=', '} \)='
  data=re.sub('hat{(.)}',r'(\\hat{\1}\\)',data)
  data=data.replace('mc', '$mc')
  data=data.replace(r'times','( \\times\)')
  data=data.replace(')\\)',')')
  data=data.replace('BR', '$BR')
  data=data.replace('**','')
  data=data.replace('\cdot','\(\cdot\)')
  data=data.replace('\\\\\\','')
  data=data.replace('\\\\','\\')
  data=data.replace('text{sin}','\sin')
  data=data.replace('text{tan}','\tan')
  data=data.replace('text{cos}','\cos')
  data=data.replace('mathrm','text')
  data=data.replace('\\sum',r'\(\sum\)')
  data=data.replace('\;\;','')
  data=data.replace('}!\($','}')
  data=data.replace('force vectors in red', 'force vectors') #MODULE 2 
  
  
  x='alpha\\'

  #data=data.replace( x , '(alpha\)' )
  #data=sub('overrightarrow{(.)}_', r'11111111111111{\1}',data)
  #data=sub('\\\overrightarrow{(.*?)}', r'\(\\overrightarrow{\1}\\)',data,1)
  data=data.replace('\\(\\(\\', r'\(\\')
  data=data.replace('\(\\','\(\\')
  #data=sub('11111111111111{(.)}', r'overrightarrow{\1}_',data)
  #data=sub('\\((.*?)\\)',r'\1',data)
  #data=data.replace('\\)\\)',r'\\)')
  data=data.replace('\)\(\(_','_')
  data=sub('\\)_(.)',r'_\1 \\)',data)
  data=data.replace('\\_','_')
  #data=data.replace('overright','123')
  #data=data.replace('\\\\','\\')
  data=data.replace('\(BEGIN_TEXT\)','BEGIN_TEXT')
  data=data.replace('\(END_TEXT\)','END_TEXT')
  data=data.replace('}\(_','}_rep')
  data=re.sub('{(.*?)}_rep',r'\\(\1_', data)
  #data=data.replace('){','(repl){')
  data=re.sub('\){(.*?)}',r')\\(\1\\)', data)
  #replacecos,sin,tan,theta
  data=data.replace('~','')
  data=data.replace('\)\(_','_')
  data=data.replace('\(\\','\(\\')
  
  if '\\text' in data:
    try:
      m=re.search(r"\\text{(.*?)}", data)
      data=data.replace(m.group(0), m.group(1),1) 
    except:
      pass

  leftbracket=0
  if 'RadioButtons' not in data and '[' in data:
    data=data.replace('[','\\($')
    leftbracket=1
  if leftbracket==1:
    data=data.replace(']','\\)')
    data=data.replace("\),","],")
  data=data.replace(r')\)\(',')\(')
  data=data.replace('\;','')
  data=data.replace('\\\\',r'\\')
  data=data.replace('---','')
  data=data.replace('theta','\\theta')
  data=data.replace('\\text','deletee')
  data=re.sub('deletee{(.*?)}',r' \1',data)
  data=data.replace('\degree',' \(^\circ\)')
  data=data.replace('deletee','')
  data=data.replace('\)\)','\)')
  data=data.replace('\)_','_')
  data=data.replace('\\\\','\\')
  data=re.sub('\)\^{(.*?)}',r'^{\1}\)',data)
  data=data.replace('\^','^')
  
  #sqrt replacement
  line=re.findall('sqrt{(.*?)}',data,flags=0)
  newline = [w.replace('\\', '') for w in line]
  num=len(line)
  for i in range(num):
          data=data.replace('sqrt{'+line[i]+'}','(\\sqrt{'+newline[i]+'}\\)')  
  line=re.findall('frac{(.*?)}\)',data,flags=0)
  other=0
  if not line:
    other=1
    line=re.findall('frac{(.*?)}"',data,flags=0)   
  newline = [w.replace('\\', '/') for w in line]
  newline= [w.replace('/)', '') for w in newline]
  newline= [w.replace('/(', '') for w in newline]
  newline= [w.replace('/', '\\') for w in newline]
  num=len(line)
  for i in range(num):
    if other==0:
          data=data.replace('frac{'+line[i]+'})','frac{'+newline[i]+'}\\)')
          data=data.replace('(\\frac','\(\\frac')
          data=data.replace('\\\\\\\\','\\')          
    elif other==1:
      data=data.replace('frac{'+line[i]+'}"','(\\frac{'+newline[i]+'}\\)"')
    data=data.replace('\\\\\\',"\\")
  data=data.replace('Sigma','(\Sigma\)')
  data=data.replace('arrow1','(\overrightarrow{}\)')
  data=re.sub('mathbf-/-(.*?)\)',r'(\\mathbf{\1}\)',data)
  data=data.replace('mathbf{\(','mathbf{')
  data=data.replace('^\circ','\(^\circ\)')  
  data=data.replace('\\','///21q')
  data=data.replace('///21q(///21q(','///21q(')
  data=data.replace('///21q)///21q)','///21q)')
  data=re.sub('rrightarrow{(.*?)}\]',r'rrightarrow{\1}///21q)',data)
  data=re.sub('mathbf{(.*?)///21q}',r'mathbf{\1}',data)
  data=data.replace('///21q','\\')
  data=data.replace('\(phi','\(\phi')
  data=data.replace('\\\\','\\')
  data=data.replace('\\','//i/')
    
  data=re.sub('overrightarrow{(.*?)}_//i/\)//i/\((.*?)//i/\)',r'overrightarrow{\1}_{\2}//i/)',data)
  data=re.sub(r'overrightarrow//i/\((.*?)//i/\)',r'(\\overrightarrow{\1}\\)',data)
  data=data.replace('//i/','\\')
  data=data.replace('\xb0',r'\(^\circ\)').replace(r'k}\)(\overrightarrow',r'k}\) \(\overrightarrow')
  data=re.sub(r"begin{vmatrix}(.*?)\\(.*?)end{vmatrix}",r"(\\begin{vmatrix}(\1)\\\\(\2)\\end{vmatrix}\)", data)
  data=data.replace(r'\(\overrightarrow{M_O}\)=\(\begin{vmatrix}()\\((\hat{i}\)&\(\hat{j}\)\r_x&r_y\F_x&F_y)\end{vmatrix}\)\(\hat{k}\)',r'\(\overrightarrow{M}_O=\begin{vmatrix}\hat{i}&\hat{j}\\r_x&r_y\\F_x&F_y\\\end{vmatrix}\hat{k}\)')
  #data=data.replace(r'\(\overrightarrow{M_O}\)=\(\begin{vmatrix}()\\((\hat{i}\)&\(\hat{j}\)&\(\hat{k}\)\F_x&F_y&F_z\r_x&r_y&r_z)\end{vmatrix}\)',r'\(\overrightarrow{M}_O=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\F_x&F_y&F_z\\r_x&r_y&r_z\\\end{vmatrix}\)')  
  #data=data.replace('9.81m/s^2','9.81 \(m/s^2\)')
  #data=re.sub(r'overrightarrow{M_O}\)=\(\begin{vmatrix}()\\((\\hat{i}\)&\(\\hat{j}\)&\(\\hat{k}\)\(.*?)\(.*?)\\end{vmatrix}',r'overrightarrow{M_O}\)=\(\begin{vmatrix}\\hat{i}\)&\\hat{j}&\\hat{k}\\\1\\\2\\\\\\end{vmatrix}',data)
  mat2=re.findall(r"begin{vmatrix}(.*?)end{vmatrix}", data)
  #data=data.replace('\xb7','\(\cdot\)')
  data=data.replace(r'end\(matrix',r'end{matrix')
  mat4=re.findall(r"beginmatrix(.*?)end{matrix}",data)
  try:
    for i in range(len(mat1)):
      data=data.replace(mat2[i],mat1[i])
  except:
    pass
  try:
    for i in range(len(mat3)):
        data=data.replace(r'beginmatrix',r'(\begin{matrix}')
        data=data.replace(mat4[i],mat3[i])
        data=data.replace(r'end{matrix}',r'end{matrix}\)')
  except:
    pass  
  data=data.replace(r'alpha\)(\h',r'alpha\)\(\h').replace('~','').replace('{[____]{"$ans0"}  N [`\cdot`] m}','[____]{"$ans0"}  N [`\cdot`] m')
  data=data.replace(r',\,\,|','   |')
  data=re.sub('text{(.*?)}',r'\1',data)
  data=re.sub(r'\\{(.*?)\\}\\\(\\hat{(.*?)}\\\)',r'\1 \\(\\hat{\2}\\)',data)
  data=data.replace(r'\)\)','\)')
  data=data.replace(r'\(\hat\(i\)',r'\(\hat{i}\)').replace(r'(\hat\(j\)',r'(\hat{j}\)').replace(r'(\hat\(k\)',r'(\hat{k}\)').replace(r'\(\hat{k\)',r'\(\hat{k}\)')
  data=data.replace('fuelDimensions', 'fuel dimensions').replace(r'shown\(',r'shown \(')
  data=re.sub('kN\\\(.*?)arrow',r' \\(kN\\\1arrow\\)',data)
  data=re.sub('\\(kN}\\\(.*?)arrow',r' \\(kN\\\1arrow\\)',data)
  data= data.replace(' \\ ',' ')
  data=data.replace(r'A_\)\(x',r'\(A_x\)').replace(r'A_\)\(y',r'\(A_y\)').replace(r'F_\){CD',r'\(F_{CD}\)')
  data=data.replace('form the list below','from the list below')
  data=data.replace(r'hat{j}\)\   ',r'hat{j}\)').replace(r'hat{k}\)\   ',r'hat{k}\)')
  data=data.replace(r'hat{j}\)(\overrightarrow', r'hat{j}\) \(\overrightarrow').replace(r'hat{k}\)(\overrightarrow',r'hat{k}\) \(\overrightarrow').replace(r'hat{i}\)(\overrightarrow',r'hat{i}\) \(\overrightarrow')
  data=data.replace(r'AB\tan\(\theta\)',r'AB\(\tan\)\(\theta\)')
  data=data.replace(r'\($(\(A_yB_z',r'\(A_yB_z')
  bld=re.findall('bold{(.*?)}',data)
  nbld=re.findall('bold{(.*?)}',data)
  data=data.replace(r'\curvearrowleft',r'\(\curvearrowleft\)')
  data=data.replace(r'overrightarrow{F_\) CD',r'overrightarrow{F}_{CD}\)').replace(r'\(F_\) DC',r'\(F_{DC}\)').replace(r'overrightarrow{F}_\) DC',r'overrightarrow{F_DC}\)')
  data=data.replace('lbCoordinate axes','lb Coordinate axes')
  data=data.replace(r'\(A_z\)\(k\)(\overrightarrow{B}\)',r'\(A_z\)\(\hat{k}\) \(\overrightarrow{B}\)')
  for i in range(len(bld)):
    nbld[i]=bld[i].replace(r'\(','').replace(r'\)','')
    data=data.replace('bold{'+bld[i]+'}','(\\bold{'+nbld[i]+'}\)')
  if data.startswith('(\overrightarrow'):
    data=data.replace(r'(\overright',r'\(\overright',1)

  data=data.replace(r'mu_',r'\mu_').replace(r'P\le\(\mu','P\(\le\)\(\mu').replace(r'mu_kN\)\le',r'mu_kN\)\(\le\)')
  data=data.replace(r'\rightarrow',r'\(\rightarrow\)').replace(r'\(\rightarrow\){}',r'\(\rightarrow\)')
  data=data.replace('"ZFMs"','ZFMs')
  #data=data.replace(r'\\(\begin',r'\(\'begin
  #data=re.sub(r'{(.*?)\\,N\\\(\\cdot\\\) m\\},',r'\1\\(\\cdot\\) m',data)
  #data=data.replace('\)}','\)'
  return data
 
 
#Function to convert Numerical questions from Markdown to webwork
#Inputs: None
#Outputs: New file-.pg file for webwork
def Numerical():
      imgcount=0#find out how many images there are
      anglesint=0 #variable to check if angles have been initialized for question
      with open(file, 'r', encoding='utf-8') as f: #opening original file
          f_len=file_len(file)#find length of file
          with open(newfile, 'w') as f2: #opening new file
            #Starting the document
              beginfile(f2,file) # write beggining part of question file using information from first file

      #finding variables
              searchquery='Variable' 
              varinit=0
              for i, line in enumerate(lines):
                if 'Range' in line and varinit==0:
                    if 'alpha'in line or 'beta' in line or 'gamma' in line: # check if angle names have been initialized
                      anglesint=1
                    l=line.split('(', 1 )[0]
                    l=l.replace('$','')
                    l=l.replace('[','$')
                    l=l.replace(']','')
                    l=l.replace(':','=')
                    l=l.replace('Range','random(')
                    f2.write(l)
                    m = re.search("\((.*?)\)", line)
                    f2.write(m.group(1))#writing the variables in new file
                    m = re.search("\((.*?)\)", line)

                    f2.write(',1);')
                    f2.write('\n')   
                    
                if searchquery in line:
                  n=1
                  while 'Answer' not in lines[i+n]:
                    #f2.write('substitueavoid3')
                    lines[i+n]=re.sub('frac{(.*?)}{(.*?)}',r'(\1)/(\2)',lines[i+n])
                    if 'Range' in lines[i+n]:
                      varinit=1
                      line=lines[i+n]
                      if 'alpha'in line or 'beta' in line or 'gamma' in line:
                          anglesint=1
                          
                      l=line.split('(', 1 )[0]
                      l=l.replace('$','')
                      l=l.replace('[','$')
                      l=l.replace(']','')
                      l=l.replace(':','=')
                      l=l.replace('Range','random(')
                      l=re.sub('frac{(.*?)}{(.*?)}',r'(\1)/(\2)',l)
                      f2.write(l)
                      m = re.search("\((.*?)\)", lines[i+n])
                      f2.write(m.group(1))
                      m = re.search("\((.*?)\)", lines[i+n])
    
                      f2.write(',1);')
                      f2.write('\n')                      
                    if lines[i+n].strip() and 'Range' not in lines[i+n]:
                      m = lines[i+n]
                      m=m.split(':',1)[0]
                      m=m.replace('[','')
                      m=m.replace(']','')
                      f2.write(m+'=')
              
                      line=lines[i+n]
                      if ':' in line and '=' in line:
                        line=line.split('=',1)[1]
                      elif ':' in line:   
                        line=line.split(':',1)[1]
                      line=line.replace('\\times',r'*')
                      line=line.replace('^\\circ',r'*3.141592654/180')
                      line=line.replace('\\','')
              
                      line=line.replace('$','')
                      line=line.replace('[','$')
                      line=line.replace(']','')
                      f2.write(line.rstrip('\n')+';')
                      f2.write('\n')
              
                    f2.write('\n')
                    n=n+1           
                    
                               
                
                          
                          
      #Computing Answers
              f2.write('#---- Formulas to compute answers --------------#')
              f2.write('\n')
              #check if the question askes for magnitude of vector, and if so, write the specific equation. Equation may need to be adjusted
              for n, line in enumerate(lines):
                if 'find the magnitude' in line:
                  for i, line in enumerate(lines): 
                    if 'Answer' in line:
                      count=0
                      written=1
                      while 'Feedback' not in lines[i+count] and i+count<len(file) and written==1:
                        if '|\overrightarrow' in lines[i+count]:
                          f2.write('$v=sqrt($A**2+$B**2+$C**2);\n')
                          written=0
                        count=count+1#need to adjust later
                      
              for i, line in enumerate(lines):
                    if 'Answer' in line:
                      count=0
                      written=0
                      while 'Feedback' not in lines[i+count] and i+count<len(file) and written==0:
                        if '=' in lines[i+count]:
                          line=lines[i+count]
                          line=line.split('=',1)[1]
                          if 'alpha' in line or 'beta'in line or 'gamma' in line and written==0:# Check if question asks for angles( alpha, beta, gamma)
                            written=1
                            writtena,writtenb,writtenc=0,0,0
                            for n, line in enumerate(lines):
                              if 'alpha=' in line and writtena==0:
                                m=re.search('alpha=(.*?)\$',line)
                                m=formulatranslate(m.group(1),0,anglesint)
                                f2.write('$alpha='+m+';\n')
                                writtena==0
                                anglesint=1
                              if'beta=' in line and writtenb==0:
                                m=re.search('beta=(.*?)\$',line)
                                m=formulatranslate(m.group(1),0,anglesint)
                                f2.write('$beta='+m+';\n')  
                                writtenb==1
                              
                              if'gamma=' in line and writtenc==0:
                                m=re.search('gamma=(.*?)\$',line)
                                m=formulatranslate(m.group(1),0,anglesint)
                                f2.write('$gamma='+m+';\n') 
                                writtenc==1
                        count=count+1                 
              f2.write('\n')
              #find answers
              searchquery='Answer'
              continued=0
              #check if the answers carry over through different equations
              for i, line in enumerate(lines):
                if searchquery in line :
                  count=1
                  ansnum=0
                  left=''
                  while 'eedback' not in lines[i+count] and continued==0:
                    if '=' in lines[i+count] and not left and '$$' in lines[i+count]:# check if left side of one equation is in the right side of the next equations
                      
                      m=re.search('\$\$(.*?)=',lines[i+count])
                      try:
                        left=m.group(1) #initialize the left side of the equation
                      except:
                        pass
                    elif '=' in lines[i+count] and left in lines[i+count] and left != '' and continued==0:
                      continued=1 #if the left side(one variable) is in multiple equations, then the equations are continue off each other

                      left=''
                    count=count+1

              ansnum=0 
              anseq=''
              #if the equations continue off each other
              if continued==1:
                for i, line in enumerate(lines):
                  if searchquery in line: #search for the word answer in the line
                    count=1
                    ansnum=0
                    anseq=''                    
                    while 'eedback' not in lines[i+count]: #Only write the answer section
                      line=lines[i+count]
                      eqnum=line.count('=')#find out if there are multiple equations in one line
                      if eqnum==1:
                        if '$overarrowv=sqrt' not in line:#check if there is no vectors in the line
                          line=re.sub('\$\$(.*?)\$\$',r'$\1',line)
                          if '=' in line:
                            line=line.split('=',1)[1]
                            line=line.replace('\\','')
                            line=formulatranslate(line,0,anglesint)
                            anseq=anseq+'$ans'+str(ansnum)+'='+line.rstrip('\n')+';\n'
                            ansnum=ansnum+1
                      elif eqnum>1 and 'quad' not in line:#if there are multiple equations in the line, split equations and write answers.
                        ans=line.split('=',eqnum)[eqnum]
                        ans=formulatranslate(ans,0,anglesint)
                        anseq=''
                        ansnum=0
                        f2.write('$ans'+str(ansnum)+'='+ans.rstrip('\n')+';')
                        ansnum=ansnum+1
                      
                        
                      count=count+1
                      
              if anseq!='': #if there is a sequence of equations for answers, write the sequence
                f2.write(anseq)
              elif continued==0:# if there is not connection between the equations
                for i, line in enumerate(lines):
                    if searchquery in line :# check for the answer section of the document
                        count=1
                        ansnum=0
                        left=''
                        while 'eedback' not in lines[i+count]: # translate and write different types of equations from answer section of original document
                            if '=' in lines[i+count] and 'hat' not in lines[i+count]: #check for vectors and equation
                                line=lines[i+count]
                                if 'qquad' not in line and line.startswith('$$') or line.startswith('['): 
                                    f2.write('$ans'+str(ansnum) +'=')
                                    ansnum=ansnum+1
                                    #check if there are angle calculations in the equation 
                                    num1=line.count('(')
                                    num2=line.count('s(')
                                    num3=line.count('n(')
                                    num4=line.count('t(')
                                    num5=num1-num2-num3-num4
                                    if'(' in line and num5>0:#if there are no angle calculations, find the part within the brackets and translate( might neeed to adjust)
                                      m=re.search("\((.*?)\)", line)
                                      m=formulatranslate(m.group(1),continued,anglesint)
                                      f2.write(m.rstrip('\n'))
                                      f2.write(';\n')                                    
                                    else:
                                      l=line.split('=',1)[1]
                                      l=formulatranslate(l,continued,anglesint)
                                      if 'or' in l:
                                        l=l.split('or',1)[0]
                                      f2.write(l.rstrip('\n'))
                                      f2.write(';\n')
                                 
                                
                                else:
                                    f2.write('$ans'+str(ansnum) +'=')
                                    ansnum=ansnum+1
                                    if'(' in line and '(to' not in line and 'direction)' not in line:
                                      m=re.search("\((.*?)\)", line) 
                                      line=formulatranslate(m.group(1),continued,anglesint)
                                      f2.write(line.rstrip('\n'))
                                      f2.write(';\n')                                    
                                    else:
                                      if 'qquad' in line:
                                        #num=line.count('qquad')
                                        
                                        l1=line.split('qquad',1)[0]
                                        l2=line.split('qquad',1)[1]
                                        if '=' in l1:
                                          l1=l1.split('=',1)[1]
                                        line=formulatranslate(l1,continued,anglesint)
                                        f2.write(line.rstrip('\n'))
                                        if ';' in l1:
                                          f2.write('\n')
                                        else:
                                          f2.write(';\n')                                      
                                        l2=l2.split('=',1)[1]
                                        f2.write('$ans'+str(ansnum) +'=')
                                        ansnum=ansnum+1                                      
                                        line=formulatranslate(l2,continued,anglesint)
                                        f2.write(line.rstrip('\n'))
                                        f2.write(';\n')   
                                      else:
                                        l=line.split('=',1)[1]
                                        l=formulatranslate(l,continued,anglesint)
                                        if 'or' in l:
                                          l=l.split('or',1)[0]
                                        f2.write(l.rstrip('\n'))
                                        f2.write(';\n')
                            elif 'text' in lines[i+count]:
                              f2.write('$ans'+str(ansnum) +'=')
                              ans=formulatranslate(lines[i+count],0,anglesint)
                              f2.write(ans.rstrip('\n')+';')                                
                            else:
                              if '\mathrm{N\cdot m}' in lines[i+count]:
                              #jf 'mathrm ' in lines[i+count]
                                lines[i+count]=lines[i+count].replace('\mathrm{N\cdot m}','')
                                #lines[i+count]=re.sub('mathrm{(.*?)}','',lines[i+count]\)
                                
                              if '=' in lines[i+count]:
                                line=lines[i+count]
                                line=line.split('=')[1]
                              else:
                                line=lines[i+count]
                              a=''
                              initial=0
                              for n in line: #Record single variables and answers
                                  if n.isdigit() or n=='-':
                                      a=a+n
                                      initial=0
                                  elif n.isalpha() and n.isupper():
                                      if initial==0:
                                          m='$'
                                          a=a+m
                                          initial=1
                                      a=a+n
                                      if initial==1 and '$' not in a:
                                          m='$'
                                          a=m+a
                                          initial=1                                        
                                  
                                  elif n==',' or n=='$' or not n.isalpha() or not n.isupper():
                                      if a!='':
                                          f2.write('$ans'+str(ansnum) +'='+a+';\n')
                                          a=''
                                          ansnum=ansnum+1
                                          intial=0
                         
                                    
                            count=count+1
                      
                     
                     
      
                     
                      
      
              #PGML and Question
              anscount=0
              while anscount<ansnum:#count the answers
                anscount=anscount+1
                
              f2.write('\n########################################################\n#PGML\nBEGIN_PGML\n\n')
              searchquery='# Q'# search for question text
              blanks=0
              for i, line in enumerate(lines):
                  if line.startswith(searchquery):
                      count=1
                      ansnum=0
                      while 'ariable' not in lines[i+count] and 'Answer' not in lines[i+count] and 'Range' not in lines[i+count]:
                          data=''
                          if lines[i+count].strip():
                              #looking for where to input the answers
                              if '\_\_\_\_' in lines[i+count]:
                                blanks=1
                                line=lines[i+count]
                                counter = line.count('\_\_\_\_') 
                                while counter>0 and ansnum<anscount:
                                  #line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line)
                                  line=re.sub(r'\\_\\_\\_\\_','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                  counter=counter-1
                                  ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n')                                                                
                              elif '\_\_' in lines[i+count]:
                                  blanks=1
                                  line=lines[i+count]
                                  counter = line.count('\_\_') 
                                  while counter>0 and ansnum<anscount:
                                    #line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line)
                                    line=re.sub(r'\\_\\_','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                  line=translateline(line)
                                  f2.write(line+'\n')                                                                
                          
                          
                              elif '__________' in lines[i+count]:
                                blanks=1
                                line=lines[i+count]
                                counter = line.count('__________')
                                while counter>0:
                                    #line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line)
                                    line=re.sub('__________','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n')  
                                
                              elif '________' in lines[i+count]:
                                  blanks=1
                                  line=lines[i+count]
                                  counter = line.count('________')
                                  while counter>0 and ansnum<anscount:
                                      #line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line)
                                      line=re.sub('________','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                      counter=counter-1
                                      ansnum=ansnum+1
                                  line=translateline(line)
                                  f2.write(line+'\n')
                                  
                              elif '__$' in lines[i+count]:
                                line=lines[i+count]
                                counter = line.count('__$')
                                blanks=1
                                while counter>0:
                                    line=re.sub('__\$','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n')
                                  
                              elif '$_' in lines[i+count]:
                                  line=lines[i+count]
                                  blanks=1
                                  counter = line.count('$_')
                                  while counter>0:
                                      line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                      line=re.sub('=\$___','=[____]{"$ans'+str(ansnum)+'"}',line,1)[1]
                                      counter=counter-1
                                      ansnum=ansnum+1
                                  line=translateline(line)
                                  f2.write(line+'\n')
                                  
                             
                              elif ansnum<anscount and '_____' in lines[i+count]:
                                line=lines[i+count]
                                counter = line.count('_____')
                                blanks=1
                                while counter>0 and ansnum<anscount:
                                    line=re.sub('_____','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n')   
                                
                              elif ansnum<anscount and '__' in lines[i+count] or '__' in lines[i+count]:
                                line=lines[i+count]
                                counter = line.count('__')
                                blanks=1
                                while counter>0 and ansnum<anscount:
                                    line=re.sub('__','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n')                                   
                                  
                                  
                                  #imagesearch
                                  
                              elif ' _'in lines[i+count] and ansnum<anscount:
                                blanks=1
                                line=lines[i+count]
                                counter = line.count(' _')
                                while counter>0:
                                    line=re.sub(' _','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n') 
                                
                              elif '$_______' in lines[i+count] and ansnum<anscount:
                                blanks=1
                                line=lines[i+count]
                                f2.write('works')
                                counter = line.count('$_______')
                                while counter>0:
                                    line=re.sub('\$_______','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n')                                 
                                
                              
                                
                              elif '.png' in lines[i+count]: #insert images
                                  #line=lines[i+count]
                                  #m = re.search("\/(.*?)\]", line)
                                  #f2.write(m.group(1))
                                  imgcount=imgmove(lines[i+count],imgcount,file,f2,'n')
                                  #f2.write('\n$BR\n')
                         
                              elif 'Range' not in lines[i+count]:#check if the lines are only for the question, not including randomizing of variables    
                                  data=lines[i+count]
                                  data=translateline(data)                                
                                  f2.write(data+'\n')
                          count=count+1
                          
                          
              if blanks==0:# if there were no blanks in original question file and there were answers, write blanks for inserting answers
                while anscount>0:
                  f2.write('[____]{"$ans'+str(ansnum)+'"}\n')
                  anscount=anscount-1
                  ansnum=ansnum+1                  
              #ending documentation  
              f2.write('\n')
              f2.write('\n')
              f2.write('END_PGML')
              f2.write('\n')
              f2.write('ENDDOCUMENT();')
              
              
              
              
              
              
#Function to convert True/False questions from Markdown to webwork
#Inputs: None
#Outputs: New file-.pg file for webwork           
def TrueorFalse():
  imgcount=0
  with open(file, 'r', encoding='utf-8') as f:
      f_len=file_len(file)
      with open(newfile, 'w') as f2:

          #Starting the document
          beginfile(f2,file)



          #check if images are a part of the answers
          Answerimg=0
          Qimg=0
          for num, line in enumerate(lines):
              if 'Answer' in line and '###' not in line:
                  count=1
                  while 'eedback' not in lines[num+count]:
                      if '.png' in lines[num+count]:
                          Answerimg=1
                      count=count+1
                     
               #check if images are a part of the answer
          for i, line in enumerate(lines):               
              if 'Question' in line:
                  count=1
                  while 'Answer' not in lines[i+count]:
                      if '.png' in lines[i+count]:
                          Qimg=1
                      count=count+1
                      
           
                      
           #check if there are variables in the question        
          for i, line in enumerate(lines):
            if 'Variable' in line:
              count=0
              while 'Answer' not in lines[i+count]:
                if 'Range' in lines[i+count]:
                    l=lines[i+count]
                    line=lines[i+count]
                    l=l.split('(', 1 )[0]
                    l=l.replace('$','')
                    l=l.replace('[','$')
                    l=l.replace(']','')
                    l=l.replace(':','=')
                    l=l.replace('Range','random(')
                    f2.write(l)
                    m = re.search("\((.*?)\)", line)
                    f2.write(m.group(1))
                    m = re.search("\((.*?)\)", line)
                    f2.write(',1);')
                    f2.write('\n')
                elif '=' in lines[i+count]:
                  l=lines[i+count]
                  l=l.replace('$','')
                  l=l.replace('[','$')
                  l=l.replace(']','')
                  f2.write(l.rstrip('\n')+';\n')                    
                count=count+1
                
          #Find the answers to multiple choice questions
          searchquery='Answer'
          f2.write('$mc1 = RadioButtons([\n')
          #check if answer options are in the Answer section or the Question section
          for i, line in enumerate(lines):
                  if 'Answer' in line and '###' not in line:
                      num=1
                      answernum=0
                      while 'eedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num]:
                              answernum=answernum+1
                          num=num+1
                          
                      
           #If answer options are in the answer section           
          if answernum>1:
              for i, line in enumerate(lines):
                  if 'Answer' in line and '###' not in line:
                      num=1
                      while 'eedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num]:
                              line=lines[i+num]
                              f2.write('"'+line.rstrip('\n')+ '",')
                          num=num+1
          else: 
              a=''
              for i, line in enumerate(lines):
                  if '- [ ]' in line:
                    for n in line: 
                      if n.isalpha():
                        a=a+n
                        initial=0
                      else:
                        if a!='':
                          f2.write('"'+a+'",' )
                          a=''                   
                              
                            
          f2.write('],')  
          #Indicators or correct answers, can be adjusted or add more indicators
          searchquery='Good job'
          searchquery2= 'Well done'
          if answernum==1:#if the answer is in the Answer section, record the answer in new document 
            for i, line in enumerate(lines):
              if 'Answer' in line:
                count=1
                while 'eedback' not in lines[i+count]:
                  if lines[i+count].strip() and not'![' in lines[i+count]:
                    f2.write('\n"'+lines[i+count].rstrip('\n')+ '");')
                    break
                  count=count+1
            else: # use the indicators to find the correct answer
              for i, line in enumerate(lines):
                  if searchquery in line or searchquery2 in line or 'Correct' in line:# find the line with the correct answers, can be modified to cover more correct answer indicators
                      ans=line[0]+line[1] #might need to be modified
                      for i, line in enumerate(lines):
                          if 'Answer' in line:
                              count=0
                              while 'eedback' not in lines[i+count]:
                                  if ans in lines[i+count]:
                                      f2.write('\n"'+lines[i+count].rstrip('\n')+ '");')
                                      break
                                  count=count+1
              
    
                        
          #TEXT and Question
          f2.write('\n')
          f2.write('########################################################')
          f2.write('\n')
          f2.write('# Not in PGML')
          f2.write('\n')
          f2.write('\n')
          f2.write('BEGIN_TEXT')
          f2.write('\n$BR\n')
          f2.write('\n$BR\n')
          searchquery='# Q'
          for i, line in enumerate(lines):
              if searchquery in line:
                  if answernum>1:
                      skiptxt='# A'
                      count=1
                      while skiptxt not in lines[i+count] and 'Variable' not in lines[i+count]:
                          if '![' in lines[i+count]: # find the line with images and add images to new question file
                            imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')                        
                          else: 
                              f2.write(lines[i+count])
                          count=count+1
                  else:
                      #only write the question and skip the answer options
                      skiptxt='a)'
                      count=1
                      while  '# Answer' not in lines[i+count] and 'Variable' not in lines[i+count]:
                          if '![' in lines[i+count]:
                            imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')                       
                          elif skiptxt not in lines[i+count] and 'a.' not in lines[i+count] and '- [ ]' not in lines[i+count]: 
                              f2.write(lines[i+count])
                          count=count+1                        
          # if there are images with answers, write image with the answer           
          if Answerimg==1:
              for i, line in enumerate(lines):
                  if 'Answer' in line:
                      num=1
                      while 'eedback' not in lines[i+num] and 'Variable' not in lines[i+count]:
                          if '![' in lines[i+num]:
                            imgcount=imgmove(lines[i+num],imgcount,file,f2,'mc')
                            count=1
                            n=i+num
                            while 'Answer' not in lines[n-count] and 'Variable' not in lines[i+count]:
                                if lines[n-count].strip():
                                    l=lines[n-count]
                                    anstext=l[0]+l[1]
                                    f2.write(anstext+'\n'+anstext+"\n\n$BR\n$BR")
                                    break
                                count=count+1
                          num=num+1
                              
 
              
         #ending the document
          f2.write('\n')
          f2.write('\n$BR')
          f2.write('\n$BR\n')
          f2.write('\{$mc1->buttons()\}')
          f2.write('\n \n \n \n')
          f2.write('END_TEXT \n \nANS( $mc1->cmp() );')
          f2.write('\n')
          f2.write('ENDDOCUMENT();')
          

  #replacing variables
  with open(newfile, 'r') as f:
      ln = f.readlines()
      data=''
      for i, line in enumerate(ln): 
        if 'random' not in line and ';' not in line:
          line=mctranslate(line)
        data=data+line

  with open(newfile, 'w') as f:
      f.write(data)               
              
              
def Multiplechoice():
  f_len=file_len(file)
  imgcount=0
  with open(file, 'r', encoding="utf-8") as f:
      f_len=file_len(file)
      with open(newfile, 'w', encoding="utf-8") as f2:

                      #Starting the document
          beginfile(f2,file)

                    #check if images are a part of the answer
          Answerimg=0
          Qimg=0
          # check if variables are in question
          for i, line in enumerate(lines):
            if 'Variable' in line:
              count=0
              while 'Answer' not in lines[i+count]:
                if 'Range' in lines[i+count]:
                    l=lines[i+count]
                    line=lines[i+count]
                    l=l.split('(', 1 )[0]
                    l=l.replace('$','')
                    l=l.replace('[','$')
                    l=l.replace(']','')
                    l=l.replace(':','=')
                    l=l.replace('Range','random(')
                    f2.write(l)
                    m = re.search("\((.*?)\)", line)
                    f2.write(m.group(1))
                    m = re.search("\((.*?)\)", line)
  
                    f2.write(',1);')
                    f2.write('\n') 
                elif '=' in lines[i+count]:
                  l=lines[i+count]
                  l=l.replace('$','')
                  l=l.replace('[','$')
                  l=l.replace(']','')
                  f2.write(l)   
                count=count+1 
            #check if images are part of the answer
            if 'Answer' in line and '###' not in line:
                count=1
                while 'eedback' not in lines[i+count] and Answerimg==0:
                    if '.png' in lines[i+count]:
                        Answerimg=1
                    count=count+1
                     
          for i, line in enumerate(lines):
                
              if 'Question' in line:
                  count=1
                  answerrepeat=0 #check if answers are repeated
                  while 'Answer' not in lines[i+count] and answerrepeat<=1:
                      if 'a.' in lines[i+count]:
                        answerrepeat=answerrepeat+1
                      if '.png' in lines[i+count]:
                          Qimg=1
                      count=count+1
                      
  

          #Multiple choice answers and buttons
          f2.write('$mc1 = RadioButtons([\n')
          #finding location of answer
          answernum=0
          options=[] #initializing the multiple choice answer options
          
          #check if answer is in the question section of the document or the answer section of the document
          for i, line in enumerate(lines):
       
                  if 'Answer' in line and '###' not in line:
                      num=1
                      answernum=3
                      number=0
                      while 'eedback' not in lines[i+num] and number==0:
                          if lines[i+num].strip() and '![' not in lines[i+num]:
                              line=lines[i+num]
                              ans=line[0]+line[1]
                              for n, line in enumerate(lines):
                                if '# Question' in line:
                                  number=1
                                  while 'Answer' not in lines[n+number]:
                                    if lines[n+number].startswith(ans):
                                      answernum=0
                                    number=number+1
                          num=num+1
                  

          nofeedback=1 # initialize variable to check if there is no 'Feedback' section of the question
          if answernum>1: # write out the answer options
              for i, line in enumerate(lines):
                  if 'Answer' in line and '###' not in line:
                      num=1
                      nofeedback=0
                      while 'eedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num] and '[]' not in lines[i+num] and '()' not in lines[i+num]: # check for answer line
                              line=lines[i+num]
                              choice='"'+line.rstrip('\n')
                              count=1
                              nextans=chr(ord(line[0]) + 1) # find the next answer letter
                              while not lines[i+num+count].startswith(nextans) and 'eedback' not in lines[i+num+count] and '---' not in lines[i+num+count]: #only write the lines containing the answer
                                if not lines[i+num+count].startswith(nextans) and lines[i+num+count].strip() and '![' not in lines[i+num+count] and '[]' not in lines[i+num+count] and '()' not in lines[i+num+count]:
                                    line=lines[i+num+count]   
                                    choice=choice+line.rstrip('\n')
                                count=count+1
                              choice=choice+'",'
                              choice=re.sub('"(\w),"',r'"\1."',choice) # replace typo: ',' with '.'
                              f2.write(choice)
                              options.append(choice) # record the answers in a list
                              choice=''
                          num=num+1
          else:# find and write answers in the questions section
              ans=''
              for i, line in enumerate(lines):
                  if 'Feedback' in line: # search the feedback section for the initial letters of answer choices
                      num=1
                      while  i+num<f_len:
                              written=0 # variable to check if answer has been written
                              if '![' not in lines[i+num]:
                                  line=lines[i+num]
                                  if line[0].isalpha():
                                    if line[1]==')' or line[1]=='.' or line[1]==',':
                                      ans=line[0]+line[1]
                                      for n, line in enumerate(lines):# search question section for answer choice
                                          if 'Question' in line:
                                              count=0
                                              while 'Answer' not in lines[n+count] and written==0:
                                                  if lines[n+count].startswith(ans):                                                     
                                                    line=lines[n+count]
                                                    choice='"'+line.rstrip('\n')
                                                    number=1
                                                    nextans=chr(ord(line[0]) + 1) # determine the next answer letter
                                                    #find only the answers
                                                    while not lines[n+number+count].startswith(nextans) and 'eedback' not in lines[n+number+count] and '---' not in lines[n+number+count] and n+number+count<f_len and 'Answer' not in lines[n+number+count]:
                                                      if lines[n+number+count].strip() and '![' not in lines[n+number+count] and '[]' not in lines[n+number+count] and '()' not in lines[n+number+count]:
                                                          line=lines[n+number+count]   
                                                          choice=choice+line.rstrip('\n')
                                                      number=number+1
                                                    choice=choice+'",'
                                                    choice=re.sub('"(\w),"',r'"\1."',choice) # replace typo ',' with '.'
                                                    f2.write(choice)
                                                    options.append(choice)
                                                    written=1
                                                    break
                                                  count=count+1                              
                              num=num+1
                              
                  
                                       
          # if there is no feedback section, and answer options  not found in document sections               
          if nofeedback==1 and not options:
            lastopt=''
            num,written=0,0
            for i, line in enumerate(lines): # search for options and write the options(currently for very specific exception)
              if line.startswith('a.') and 'Good job!' not in line and written==0:
                choice='"'+line.rstrip('\n')+'",'
                opt='a.'
                f2.write(choice)
                options.append(choice)
                count=1
                while opt not in lines[i+count] and i+count<f_len-1:
                  written=1
                  if lines[i+count].startswith('b'):
                    choice='"'+lines[i+count].rstrip('\n')+'",'
                    f2.write(choice)
                    options.append(choice)
                  count=count+1                    
                  
                
                
                
                
                
              
              
              
          #find answer                        
          f2.write('],') 
          #Correct answer indicators
          searchquery='Good'
          searchquery2= 'Well done'
          for i, line in enumerate(lines):
              if searchquery in line or searchquery2 in line or 'Correct' in line or 'Good' in line or 'Great' in line: # search and write correct answer
                  ans=line[0]+line[1]
                  for i in range(len(options)): #search for answer letter in the options
                      if ans in options[i]:
                          f2.write('\n'+options[i].rstrip(',')+ ');')
                   
                   #previous method for determining answers              
                  #for i, line in enumerate(lines):
                      #if 'Answer' in line:
                          #count=0
                          #while 'eedback' not in lines[i+count] and '###' not in lines[i+count]:
                              #ansalt=ans.rstrip('.')+','
                              #if '![' not in lines[i+count] and ans in lines[i+count] or lines[i+count].startswith(ansalt):
                                #correctans=lines[i+count].replace(ansalt,ans)
                                #number=1
                                #nextans=chr(ord(line[0]) + 1)
                                #f2.write(nextans)
                                #while not lines[i+number+count].startswith(nextans) and 'eedback' not in lines[i+number+count] and '---' not in lines[i+number+count] and i+number+count<f_len:
                                  #if lines[i+number+count].strip() and '![' not in lines[i+number+count] and '[]' not in lines[i+number+count] and '()' not in lines[i+number+count]:
                                      #line=lines[i+number+count]  
                                      #f2.write(line+'\n')
                                      #f2.write('aaa')
                                      #correctans=correctans+line.rstrip('\n')
                                  #number=number+1 
                                  #answer=correctans.rstrip('\n')
                                  #f2.write('\n"'+answer+ '");')
                                  #break
                              #count=count+1
          
    
                 
                 

                 
                  
                        
          #Question
          f2.write('\n')
          f2.write('########################################################')
          f2.write('\n')
          f2.write('# Not in PGML')
          f2.write('\n')
          f2.write('\n')
          f2.write('BEGIN_TEXT')
          f2.write('\n$BR\n')
          f2.write('\n$BR\n')
          searchquery='# Q'
          #Writing the question text
          for i, line in enumerate(lines):
              if searchquery in line:
                #if answers are in the Answer section
                  if answernum>1:
                      skiptxt='# A'
                      count=1
                      skipimg='.png]' #find a way to get image name
                      while skiptxt not in lines[i+count] and not lines[i+count].startswith('a.') and not lines[i+count].startswith('a)') and 'Variable' not in lines[i+count]:
                          if '![' in lines[i+count] and 'in_to_the_page' not in lines[i+count] and 'out_of_the_page' not in lines[i+count]:#finding and adding image references to code
                            imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')
                            f2.write("\n\n$BR\n")                      
                          elif lines[i+count].strip: 
                              f2.write(lines[i+count])
                              #f2.write("\n$BR\n") # used to add extra lines
                          count=count+1
                  #if question options are in the question section
                  else:
                      skiptxt='a)'
                      count=1
                      while skiptxt not in lines[i+count] and 'a.' not in lines[i+count] and '# Answer' not in lines[i+count] and 'Variable' not in lines[i+count]:
                          if '![' in lines[i+count] and 'in_to_the_page' not in lines[i+count] and 'out_of_the_page' not in lines[i+count]:# insert image references into question text
                            imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')
                            f2.write("\n$BR\n")
                            #m = re.search("\/(.*?)\]", lines[i+count])                        
                          else: 
                              f2.write(lines[i+count])
                          count=count+1 
                          
          #if answers are in the question section, check for images associated with answers
          if answernum<=1: 
            for i, line in enumerate(lines):
              if 'Question' in line and 'Format' not in line and 'Type' not in line:
                count=1
                ansimg=0  
                while 'Answer' not in lines[i+count] and i+count<f_len-1:
                  if lines[i+count].startswith('a.') or lines[i+count].startswith('a)'):
                    ansimg=1
                  if ansimg==1 and '![' in lines[i+count] and 'in_to_the_page' not in lines[i+count] and 'out_of_the_page' not in lines[i+count]:
                    imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc') # insert image references
                    f2.write("\n$BR\n")  
                  count=count+1
                    
                
          # if answers have images and are found in the answer section, write image with answer letter 
          elif Answerimg==1:
              for i, line in enumerate(lines):
                  if 'Answer' in line:
                      num=1
                      try:
                        while 'eedback' not in lines[i+num] and i+num<f_len:
                            if '![' in lines[i+num] and 'in_to_the_page' not in lines[i+count] and 'out_of_the_page' not in lines[i+count]: 
                              imgcount=imgmove(lines[i+num],imgcount,file,f2,'mc')# insert image reference
                              count=1
                              n=i+num
                              while 'Answer' not in lines[n-count]: # add answer text after image
                                  if lines[n-count].strip() and '![' not in lines[n-count]:
                                      l=lines[n-count]
                                      anstext=l[0]+l[1]
                                      anstext=anstext.replace(',','.')
                                      f2.write(anstext+'\n'+"\n")
                                      break
                                  count=count+1
                              if 'eedback' in lines[i+num]:
                                break
                            num=num+1
                      except:
                          continue
 
         
          f2.write('\n\n$BR\n\{$mc1->buttons()\}\n \n \n \nEND_TEXT \n \nANS( $mc1->cmp() );\nENDDOCUMENT();')
  

  #replacing variables
  with open(newfile, 'r') as f:
      ln = f.readlines()
      data=''
      for i, line in enumerate(ln):
        if 'image(' not in line and 'width=>' not in line: # avoid changing image reference
          line=mctranslate(line)
        data=data+line
        try:
          answercheck=re.findall('"'+ans+'(.*?)"',data)
          if answercheck[0]!=answercheck[1]:
            data=data.replace(answercheck[0],answercheck[1])
        except Exception as e:
          continue      
        
  # writing data with replaced variables
  with open(newfile, 'w') as f:
      f.write(data)  
              
              
              
#Function to convert Multiple answer questions from Markdown to webwork
#Inputs: None
#Outputs: New file-.pg file for webwork              
def Multipleanswer():
  imgcount=0
  qtype=0
  ansdetermined=0
  f_len=file_len(file)
  with open(file, 'r', encoding='utf-8') as f:
      with open(newfile, 'w') as f2:
          #Starting the document
          beginfile(f2,file)        
          lines = f.readlines()
          searchquery = 'Key' 
          count=0
          f2.write('$mc = new_checkbox_multiple_choice();\n$mc -> qa (\n')
          skiptxt='a)'
          count=1
          f2.write('"')
          # determine the question type is multiple answers using common indicators in text
          for i,line in enumerate(lines):
            if 'From the list below' in line or'From the options below, select **all the correct representations**' in line:
              qtype=1
           # write the question
          for i,line in enumerate(lines):
            if 'Question:' in line:
              count=1
              while skiptxt not in lines[i+count] and 'a.' not in lines[i+count] and '# Answer' not in lines[i+count] and 'Variable' not in lines[i+count]:
                if '![' not in lines[i+count] and line.rstrip(): 
                    f2.write(lines[i+count].replace('"',''))
                count=count+1 
          f2.write('",')
          #write the correct answers determined from indicators in text
          searchquery='Good job!'
          searchquery2= 'Well done!'
          for i, line in enumerate(lines):
              if searchquery in line or searchquery2 in line or 'Correct.' in line:
                  ans=line[0]+line[1]
                  ansdetermined=1 # check if answer has been found
                  newsearch='Answer'
                  for n, line in enumerate(lines):
                      if 'Answer' in line and 'specific' not in line: # search for answer section
                          avoidq= 'Feedback'
                          count=0
                          num=1
                          extraans=[]
                          while 'Feedback' not in lines[n+count]:
                              if ans in lines[n+count] and '![' not in lines[n+count]:
                                  f2.write('\n"'+lines[n+count].rstrip('\n')+ '",\n')
                              elif '![' not in lines[n+count] and lines[n+count].rstrip() and '#' not in lines[n+count]:
                                extraans.append(lines[n+count])
                                num=num+1
                              count=count+1                      
          if ansdetermined==0:#if answers have not been found
            if qtype==1:
              for n, line in enumerate(lines):
                if 'Answer' in line and 'specific' not in line: # search for answers
                  count=1
                  num=1
                  extraans=[]
                  while 'Feedback' not in lines[n+count]:
                      if lines[n+count].strip() and '![' not in lines[n+count]:
                          f2.write('\n"'+lines[n+count].rstrip('\n')+ '",\n') #write the answers 
                      count=count+1
                  
          f2.write(');\n')
          f2.write('$mc -> makeLast(')
          writtenans=0
          
          #finding location of answer
          #write all answer options from question
          for i, line in enumerate(lines):
                  #search for list from question text if indicators are true
                  if 'From the list below' in line or 'From the options below, select **all the correct representations**' in line:
                    num,write=1,0
                    while 'Answer' not in lines[i+num]:
                            if lines[i+num].startswith('a)') or line.startswith('a.'):
                              write=1
                            if lines[i+num].strip() and '![' not in lines[i+num] and '[]' not in lines[i+num] and '()' not in lines[i+num] and write==1:
                                line=lines[i+num]
                                f2.write('"'+line.rstrip('\n')+ '",\n')
                                writtenans=1
                            num=num+1
                          
                  #search for answer section and check if options are found in the answer section                              
                  elif 'Answer' in line and '###' not in line:
                      num=1
                      answernum=3
                      number=0
                      while 'eedback' not in lines[i+num] and number==0:#avoid feedback section
                          if lines[i+num].strip() and '![' not in lines[i+num]:
                              line=lines[i+num]
                              ans=line[0]+line[1]
                              for n, line in enumerate(lines):
                                if '# Question' in line:
                                  number=1
                                  while 'Answer' not in lines[n+number]:
                                    if ans in lines[n+number]:
                                      answernum=0
                                    number=number+1
                          num=num+1
                          
                      
          # write all answer options from asnwer section           
          if answernum>1 and writtenans==0:
              for i, line in enumerate(lines):
                  if 'Answer' in line and '###' not in line:
                      num=1
                      while 'eedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num] and '[]' not in lines[i+num] and '()' not in lines[i+num]:
                              line=lines[i+num]
                              f2.write('"'+line.rstrip('\n')+ '",')
                          num=num+1
          elif writtenans==0:# search for answer options in question text if answers are not in answer section
              ans=''
              for i, line in enumerate(lines):
                  if 'Feedback' in line:
                      num=1
                      while  i+num<f_len:
                              written=0
                              if '![' not in lines[i+num]:
                                  line=lines[i+num]
                                  if line[0].isalpha():
                                      ans=line[0]+line[1]
                                      
                                      for n, line in enumerate(lines):
                                          if 'Question' in line:
                                              count=0
                                              while 'Answer' not in lines[n+count] and written==0:
                                                  if lines[n+count].startswith(ans):
                                                      f2.write('\n"'+lines[n+count].rstrip('\n')+ '",\n')
                                                      
                                                      written=1
                                                      break
                                                  count=count+1                              
                              num=num+1                               
          f2.write(');\n')

          Answerimg=0
          Qimg=0
          #search for images with answers
          for i, line in enumerate(lines):
              if 'Answer' in line and 'specific' not in line:
                  count=1
                  while 'Feedback' not in lines[i+count] and Answerimg==0:
                      if '.png' in lines[i+count]:
                          Answerimg=1
                      count=count+1
                     
               #check if images are a part of the question
          for i, line in enumerate(lines):
              if 'Question' in line:
                  count=1
                  while 'Answer' not in lines[i+count]:
                      if '.png' in lines[i+count]:
                          Qimg=1
                      count=count+1
                      
          
    
                 
                 
  
                 
                  
  
          #PGML and Question
          f2.write('\n')
          f2.write('########################################################')
          f2.write('\n')
          f2.write('# Not in PGML')
          f2.write('\n')
          f2.write('\n')
          f2.write('BEGIN_TEXT\n')
          f2.write('\n$BR\n')
          #write image references
          if Qimg==1:
              for i, line in enumerate(lines):
                  if 'Question:' in line:
                      num=1
                      while 'Answer' not in lines[i+num]:
                          if '![' in lines[i+num]:

                              imgcount=imgmove(lines[i+num],imgcount,file,f2,'mc')
                              f2.write('\n$BR\n')
                              count=1
                          num=num+1
                              
              f2.write('\n$BR\n')
              searchquery='# Q'
          #write answer image references
          if Answerimg==1:
              for i, line in enumerate(lines):
                  if 'Answer' in line and 'specific' not in line:
                      num=1
                      while 'Feedback' not in lines[i+num]:
                          if '![' in lines[i+num]:
                              imgcount=imgmove(lines[i+num],imgcount,file,f2,'mc')
                              f2.write('\n$BR\n')
                              count=1
                              n=i+num
                              while 'Answer' not in lines[n-count]:
                                  if lines[n-count].strip():
                                      l=lines[n-count]
                                      anstext=l[0]+l[1]
                                      #anstext+"')\}"+
                                      f2.write('\n'+anstext+"\n\n$BR")
                                      break
                                  count=count+1
                          num=num+1
           #end the document               
          f2.write('\{ $mc -> print_q() \}\n')
          f2.write('$BR')
          f2.write('\{ $mc -> print_a() \}\n')
          f2.write('END_TEXT\n  ')                     
      
          f2.write('\nANS( checkbox_cmp( $mc->correct_ans() ) );\nENDDOCUMENT();')
  
  
  #replacing variables
  with open(newfile, 'r') as f:
    ln = f.readlines()
    data=''
    for i, line in enumerate(ln): 
      if 'new_checkbox_multiple_choice' not in line and 'print_q()' not in line and 'print_a()' not in line and 'checkbox_cmp' not in line:#avoid modifying the lines for operation of question
        line=mctranslate(line)
      data=data+line    
   #rewriteing the data to the file
  with open(newfile, 'w') as f:
      f.write(data)

              
           
 
#Input file location
os.chdir(filelocation)
filename=[]
count=1
problemcount=0;
problemset=''
setcount=10 #intial problem set number

#Main function for going through files in folder
#input: folder with question files and image folders
#output: folder with .pg and image files renamed, documents for image errors and documents to upload problem sets
for file in glob.glob("*.md"):
    print(file)
    count=count+1
    imgcount=0
    newfile=file.rstrip('.md')+'.pg'
    newfile=newfile.replace(' ','-')# change file name
    #problem limit for sets
    if problemcount<100:
      problemset=problemset+ 'setUsaskQuestions/'+newfile+ ', 0 \n'
      problemcount=problemcount+1;
    else:
      setname='setusaskmc'+str(setcount)+'.def' # name of the question sets
      with open(setname, 'w') as f:
        f.write('setNumber=Usaskmc'+str(setcount)) # creating problem set
        f.write('\nopenDate = 1/7/00 at 6:00am\ndueDate = 1/20/09 at 6:00am\nanswerDate = 1/21/09 at 6:00\npaperHeaderFile = set34/paperHeaderFile0.pg\nscreenHeaderFile = set34/screenHeaderFile0.pg\nproblemList =\n ' )      
        f.write(problemset)      
      problemcount=0
      setcount=setcount+1
      problemset=''
    #open file, read lines and detemine question type
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        torf=0
        for i, line in enumerate(lines):
            if 'Question Format' in line or 'STATICS-MPA06' in line:#specific question exception and numerical answers
              if 'Numerical' in line or 'STATICS-MPA06' in line:
                for i, line in enumerate(lines):
                  if line.startswith('a.') or line.startswith('a)'):
                    for i, line in enumerate(lines):
                      if line.startswith('b.') or line.startswith('b)'):
                        Multiplechoice() 
                        break
                      break
                    break
                  else:
                    Numerical()
                  
              elif 'Multiple Choice' in line or 'Multiple choice' in line or 'multiple choice'  in line or 'Multi-Select' in line or 'multi-select' in line or 'Multi-select' in line:
                  count=0
                  if 'Multi-Select' in line or 'multi-select' in line or 'Multi-select' in line:
                    Multipleanswer()
                    print('Multi-select')
                  else:
                    for i, line in enumerate(lines):
                          if '- [ ]  Yes' in line:
                            torf=1
                          if 'Good job' in line or 'Well done' in line or 'Correct.' in line:
                              count=count+1
                          if 'all the correct options' in line:
                            count=count+3
                    if count>1:
                          Multipleanswer()
                    elif torf==1:
                      print('Torf')
                      TrueorFalse()                    
                    else:
                          print('MultipleChoice')
                          Multiplechoice()              
              elif 'True' in line or 'true' in line: #check for true or false or multiple choice
                print('Torf')
                TrueorFalse()
              else:
                print(':question format not recognized') #prints if question format is not recognized
                
#set.def file: Used to upload problem sets to webwork
#input: string containing problem set image
#output:set definition file
setname='setusaskmc'+str(setcount)+'.def'
with open(setname, 'w') as f:
  f.write('setNumber=Usaskmc'+str(setcount))
  f.write('\nopenDate = 1/7/00 at 6:00am\ndueDate = 1/20/09 at 6:00am\nanswerDate = 1/21/09 at 6:00\npaperHeaderFile = ASimpleCombinedHeaderFile.pg\nscreenHeaderFile = ASimpleCombinedHeaderFile.pg\nproblemList =\n ' )    
  f.write(problemset)

#Image moving error logs
#input:None
#Output: txt file detailing the errors in moving images
with open('imagemovingerrors.txt','w') as f:
  f.write('Image Scaling Errors\n\n\n\n')
  for i in range(len(imgscaleerrors)):
    f.write(imgscaleerrors[i]+'\n')
  f.write('Image Moving Errors\n\n\n')
  for i in range(len(imgerrormovinglist)):
    f.write(imgerrormovinglist[i]+'\n')  
  
  
                             
