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
#
 
 
 #input file location below
filelocation=r'C:\Users\ptemm\Downloads\Module 1 Dec 2\GE 124 Question Database - Module 1 c7df8e2393214b0a9d40fca105b01948'
#'C:\Users\ptemm\Downloads\Export-814d98e7-2abf-4127-a900-6ab08c4fe6c8\GE 124 Question Database - Module 1 c7df8e2393214b0a9d40fca105b01948'
#moving and renaming images
imglinelist=[]
newimglinelist=[]
imgerrormovinglist=[]
imgscaleerrors=[]
def imgmove(imgline,imgcount,filename,filetowrite,qtype):
  #print(imgline)
  if imgline in imglinelist:
    imgindex=imglinelist.index(imgline)
    linetowrite=newimglinelist[imgindex]
    filetowrite.write(linetowrite)
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
    subfolders = [ f.path for f in os.scandir(r'C:\Users\ptemm\OneDrive\Testing Module 1 Usask') if f.is_dir() ]
    width,height=0,0
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
      #print('image not found!')
      imgerrormovinglist.append(originpath)
      #print(originpath)
      #print(newname)
      pass
    imgcount=imgcount+1
    if qtype=='n':
      newimgname=newimgname.replace(' ','-')
      newimgline='[@ image( "'+newimgname+'", width=>['+str(width)+'], height=>['+str(height)+']) @]*\n'
      newimglinelist.append(newimgline)
      filetowrite.write(newimgline)
      filetowrite.write('END_PGML\nBEGIN_PGML\n')
    else:
      newimgname=newimgname.replace(' ','-')
      filetowrite.write('\n$BR\n')
      newimgline='\{ image("'+ newimgname +'" , width=>'+str(width)+', height=>'+str(height)+') \}'
      newimglinelist.append(newimgline)
      filetowrite.write(newimgline) 

  return imgcount
  
  
  
  
def formulatranslate(l,continuation,anglesint):
  l=re.sub('sqrt{(.*?)}',r'sqrt(\1)',l)
  l=re.sub('frac{(.*?)}{(.*?)}',r'(\1)/(\2)',l)
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
    ##l=l.replace('arccos','(180/pi)*arccos)' #for degrees
  
  return l
  
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


                           
  
def file_len(file):
  with open(file, 'r', encoding='utf-8') as f:
    for i, l in enumerate(f):
      pass
  return i + 1  

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
  line=line.replace('left(','')
  line=line.replace('right)','')
  line=line.replace('$\\','')
  line=line.replace('$','')
  line=line.replace('\\','')
  line=re.sub('\[(.)\]',r'[`[$\1]`]',line)
  line=line.replace('\\times',r'*')
  line=re.sub('overrightarrow{(.*?)}',r'[`\\overrightarrow{\1}`]',line)
  line=re.sub('cdot',r'[`\\cdot`]',line)
  line=re.sub('~~','',line)
  line=line.replace('**','')
  line=line.replace('}$','')
  line=re.sub('hat{(.)}',r'[`\\hat{\1}`]',line)
  line=line.replace('\cos','[`cos`]')
  line=line.replace('\sin','[`sin`]')
  line=line.replace('\tan','[`tan`]') 
  line=line.replace('quad',' ')
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
  line=line.replace('}^[`^','}[`^')
  line=re.sub('\(hat\{\[`\[(.*?)\]`\]i\}\)',r'[`[\1]`][`\\hat{i}`]',line) 
  while '_[' in line or ']_' in line:
          line=line.replace('_[','[')
          line=line.replace(']_',']')  
  return line

def mctranslate(data):
  #data=re.search
  data=data.replace('overrightarrow{}','arrow1')
  data=re.sub('bold{(.*?)}_(w*?)',r'mathbf-/-\1_\2',data)
  if 'begin{vmatrix}' in data:
    m=re.search(r"begin{vmatrix}(.*?)end{vmatrix}", data)
    data=sub('((\w*)_(\w*))',r'\\(\1'+'\\)', data,1)
    p=re.search(r"begin{vmatrix}(.*?)end{vmatrix}", data)
    data=data.replace(p.group(0),m.group(0))
  elif 'overrightarrow ' in data:
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
    #data=sub('(\w*)_(\w*)',r'\\(\\\1'+'\\)', data)
    #print('1')
  data=data.replace(',]', ']')
  if 'random' not in data:
    data=data.replace('$', '')
  data=data.replace('\\left(','')
  data=data.replace('\\right)','')
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
  #data=data.replace('force vectors in red,', 'force vectors') #MODULE 2 
  
  
  x='alpha\\'

  data=data.replace( x , '(alpha\)' )
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
  data=data.replace('\cos','\(\cos\)')
  data=data.replace('\sin','\(\sin\)')
  data=data.replace('\tan','\(\tan\)')
  data=data.replace('\\theta','\(\\theta\)')
  data=data.replace('\\alpha','\(\\alpha\)')
  data=data.replace('\\beta','\(\\beta\)')
  data=data.replace('\\gamma','\(\\gamma\)')
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
  data=data.replace('//i/','\\')
  
  
  #data=data.replace('9.81m/s^2','9.81 \(m/s^2\)')
  
  #data=data.replace('{\(','\(')#only for the case of formatting usask mc3q96 If it doesnt work, one fix formatting could work and this can be deleted
  #data=data.replace('\)}','\)')


  
      

  #data=data.replace('rep','')
  #        \begin{vmatrix}B_x&B_y\A_x&A_y\)\\end{vmatrix}
  #\begin{vmatrix}A_x&B_x\\A_y&B_y\\\end{vmatrix}
  #data=re.sub(r'begin{vmatrix}(\.*?)\\',r'test',data)
  #\begin{vmatrix}A_x&B_x\\A_y&B_y\end{vmatrix}\( \hat{k} \)
  #data=data.replace('overrightarrow',r'\overrightarrow')
  #data=data.replace('(sum\)','(\sum\)')
  return data
 
 
#dictate degrees or radians
def Numerical():
      imgcount=0
      anglesint=0
      with open(file, 'r', encoding='utf-8') as f:
          f_len=file_len(file)
          with open(newfile, 'w') as f2:
            #Starting the document
              beginfile(f2,file)

      #finding variables
              anglesint=0
              searchquery='Variable'
              for i, line in enumerate(lines):
                if 'Range' in line:
                    if 'alpha'in line or 'beta' in line or 'gamma' in line:
                      anglesint=1
                    l=line.split('(', 1 )[0]
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
                    
                if searchquery in line:
                  n=1
                  while 'Answer' not in lines[i+n]:
                    #f2.write('substitueavoid3')
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
              #magnitude of vectorcheck
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
                          if 'alpha' in line or 'beta'in line or 'gamma' in line and written==0:
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
                        count=count+1#need to adjust later                  
              f2.write('\n')
              searchquery='Answer'
              continued=0
              #check if the answers carry over
              for i, line in enumerate(lines):
                if searchquery in line :
                  count=1
                  ansnum=0
                  left=''
                  while 'eedback' not in lines[i+count] and continued==0:
                    if '=' in lines[i+count] and not left and '$$' in lines[i+count]:
                      
                      m=re.search('\$\$(.*?)=',lines[i+count])
                      try:
                        left=m.group(1) 
                      except:
                        pass
                    elif '=' in lines[i+count] and left in lines[i+count] and left != '' and continued==0:
                      continued=1

                      left=''
                    count=count+1

              ansnum=0 
              anseq=''
              if continued==1:
                for i, line in enumerate(lines):
                  if searchquery in line:
                    count=1
                    ansnum=0
                    anseq=''                    
                    while 'eedback' not in lines[i+count]: 
                      line=lines[i+count]
                      eqnum=line.count('=')
                      if eqnum==1:
                        if '$overarrowv=sqrt' not in line:
                          line=re.sub('\$\$(.*?)\$\$',r'$\1',line)
                          if '=' in line:
                            line=line.split('=',1)[1]
                            line=line.replace('\\','')
                            line=formulatranslate(line,0,anglesint)
                            anseq=anseq+'$ans'+str(ansnum)+'='+line.rstrip('\n')+';\n'
                            ansnum=ansnum+1
                      elif eqnum>1 and 'quad' not in line:
                        ans=line.split('=',eqnum)[eqnum]
                        ans=formulatranslate(ans,0,anglesint)
                        anseq=''
                        ansnum=0
                        f2.write('$ans'+str(ansnum)+'='+ans.rstrip('\n')+';')
                        ansnum=ansnum+1
                      
                        
                      count=count+1
                      
              if anseq!='':
                f2.write(anseq)
              elif continued==0:
                for i, line in enumerate(lines):
                    if searchquery in line :
                        count=1
                        ansnum=0
                        left=''
                        while 'eedback' not in lines[i+count]:
                            if '=' in lines[i+count] and 'hat' not in lines[i+count]:
                                line=lines[i+count]
                                if 'qquad' not in line and line.startswith('$$') or line.startswith('['):
                                    f2.write('$ans'+str(ansnum) +'=')
                                    ansnum=ansnum+1
                                    num1=line.count('(')
                                    num2=line.count('s(')
                                    num3=line.count('n(')
                                    num4=line.count('t(')
                                    num5=num1-num2-num3-num4                                     
                                    if'(' in line and num5>0:
                                      m=re.search("\((.*?)\)", line)
                                      m=formulatranslate(m.group(1),continued,anglesint)
                                      f2.write(m.rstrip('\n'))
                                      f2.write(';\n')                                    
                                    else:
                                      l=line.split('=',1)[1]
                                      l=formulatranslate(l,continued,anglesint)
                                      if 'or' in l:
                                        l=l.split('or',1)[0]
                                      #l=re.sub('\w{3,}',r'',l)
                                      
                                      
                                      
                                      #l=re.sub('\$(.)\$',r'$\1*$',line)
                                      f2.write(l.rstrip('\n'))
                                      f2.write(';\n')
                                 
                                
                                else:
                                    f2.write('$ans'+str(ansnum) +'=')
                                    ansnum=ansnum+1
                                    if'(' in line:
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
                                        l=l.replace('$','')
                                        l=l.replace('\\','')
                                                                          
                                        l=l.replace('[','$')#could use re.sub
                                        l=re.sub('cos(.*?)\]',r'cos(\1*pi/180)',l)
                                        l=re.sub('sin(.*?)\]',r'sin(\1*pi/180)',l)
                                        l=re.sub('tan(.*?)\]',r'tan(\1*pi/180)',l) 
                                        l=l.replace(']$','*$')
                                        l=l.replace(']','')
                                        l=l.replace('^','**')
                                        l=re.sub('sqrt{(.*?)}',r'sqrt(\1)',l)
                                        l=l.replace('{','')
                                        l=l.replace('}','')
                                        l=l.replace('[','$')
                                        l=l.replace(']','')
                                        l=l.replace('frac','')
                                        l=l.replace('overrightarrow','')
                                        l=l.replace('|','')
                                        l=l.replace('\\','')
                                        l=l.replace('right','')
                                        l=l.replace('left','')
                                        l=l.replace('alpha','')
                                        l=l.replace('beta','')
                                        l=l.replace('gamma','')
                                        if 'or' in l:
                                          l=l.split('or',1)[0]
                                        f2.write(l.rstrip('\n'))
                                        f2.write(';\n')
                            elif 'text' in lines[i+count]:
                              f2.write('$ans'+str(ansnum) +'=')
                              ans=formulatranslate(lines[i+count],0,anglesint)
                              f2.write(ans.rstrip('\n')+';')                                
                            else:
                              if '=' in lines[i+count]:
                                line=lines[i+count]
                                line=line.split('=')[1]
                              else:
                                line=lines[i+count]
                              a=''
                              initial=0
                              for n in line: 
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
              while anscount<ansnum:
                anscount=anscount+1
                
              f2.write('\n########################################################\n#PGML\nBEGIN_PGML\n\n')
              searchquery='# Q'
              blanks=0
              for i, line in enumerate(lines):
                  if line.startswith(searchquery):
                      count=1
                      ansnum=0
                      while 'ariable' not in lines[i+count] and 'Answer' not in lines[i+count] and 'Range' not in lines[i+count]:
                          data=''
                          if lines[i+count].strip():
                              #looking for where to input the answers
                              if '\_\_' in lines[i+count]:
                                  blanks=1
                                  line=lines[i+count]
                                  counter = line.count('\_\_') 
                                  while counter>=0:
                                    #line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line)
                                    line=re.sub(r'\\_\\_','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                  line=translateline(line)
                                  f2.write(line+'\n')                                   
                                  #l=line.split('=',1)[0]
                                  #e=line.split('_\,',1)[1]
                                  #f#2.write(l+'='+'[_]{"\$ans'+str(ansnum)+'"}'+e.rstrip('\n')+'\n\n')
                                  ##ansnum=ansnum+1                              
                          
                          
                              elif '__________' in lines[i+count]:
                                blanks=1
                                line=lines[i+count]
                                counter = line.count('__________')
                                while counter>=0:
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
                                  while counter>=0:
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
                                while counter>=0:
                                    line=re.sub('__\$','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n')                                
                                  
                              elif '$_' in lines[i+count]:
                                  line=lines[i+count]
                                  blanks=1
                                  counter = line.count('$_')
                                  while counter>=0:
                                      line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                      counter=counter-1
                                      ansnum=ansnum+1
                                  line=translateline(line)
                                  f2.write(line+'\n')
                                  
                             
                                
                              elif '__' in lines[i+count] or '__' in lines[i+count]:
                                line=lines[i+count]
                                counter = line.count('__')
                                blanks=1
                                while counter>0:
                                    line=re.sub('__','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n')                                   
                                  
                                  
                                  #imagesearch
                                  
                              elif ' _'in lines[i+count]:
                                blanks=1
                                line=lines[i+count]
                                counter = line.count(' _')
                                while counter>0:
                                    line=re.sub(' _','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n')                                 
                                
                              elif '.png' in lines[i+count]:
                                  #line=lines[i+count]
                                  #m = re.search("\/(.*?)\]", line)
                                  #f2.write(m.group(1))
                                  imgcount=imgmove(lines[i+count],imgcount,file,f2,'n')
                                  #f2.write('\n$BR\n')
                         
                              elif 'Range' not in lines[i+count]:    
                                  data=lines[i+count]
                                  data=translateline(data)
                                  #if 'Express' in data:
                                    #print(data)                                  
                                  f2.write(data+'\n')
                          count=count+1
                          
                          
              if blanks==0:
                while anscount>0:
                  f2.write('[____]{"$ans'+str(ansnum)+'"}\n')
                  anscount=anscount-1
                  ansnum=ansnum+1                  
                
              f2.write('\n')
              f2.write('\n')
              f2.write('END_PGML')
              f2.write('\n')
              f2.write('ENDDOCUMENT();')
              
              
              
              
              
              
#setUsaskMCQuestions/STATICS-ASV01 01 01 faefa0460d484e039accabc59f8495a0.pg              
def TrueorFalse():
  imgcount=0
  with open(file, 'r', encoding='utf-8') as f:
      f_len=file_len(file)
      with open(newfile, 'w') as f2:

                      #Starting the document
          beginfile(f2,file)



                    #check if images are a part of the answer
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
                
          #MC answers if image is outside the answer choices
          searchquery='Answer'
          f2.write('$mc1 = RadioButtons([\n')
          for i, line in enumerate(lines):
                  if 'Answer' in line and '###' not in line:
                      num=1
                      answernum=0
                      while 'eedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num]:
                              answernum=answernum+1
                          num=num+1
                          
                      
                      
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
                    #for n in line:
                      #while  i+num<f_len:
                              #written=0
                              #if '![' not in lines[i+num]:
                                  #line=lines[i+num]
                                  #if line[0].isalpha():
                                      #ans=line[0]+line[1]
                                      
                                      #for n, line in enumerate(lines):
                                          #if 'Question' in line:
                                              #count=0
                                              #while 'Answer' not in lines[n+count] and written==0:
                                                  #if lines[n+count].startswith(ans):
                                                      #f2.write('\n"'+lines[n+count].rstrip('\n')+ '",')
                                                      
                                                      #written=1
                                                      #break
                                                  #count=count+1                              
                              #num=num+1
                              
                                
                                                  
              
                                                  
          f2.write('],')                    
          searchquery='Good job'
          searchquery2= 'Well done'
          if answernum==1:
            for i, line in enumerate(lines):
              if 'Answer' in line:
                count=1
                while 'eedback' not in lines[i+count]:
                  if lines[i+count].strip() and not'![' in lines[i+count]:
                    f2.write('\n"'+lines[i+count].rstrip('\n')+ '");')
                    break
                  count=count+1
            else:
              for i, line in enumerate(lines):
                  if searchquery in line or searchquery2 in line or 'Correct' in line:
                      ans=line[0]+line[1]
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
                      skipimg='.png]' #find a way to get image name
                      while skiptxt not in lines[i+count] and 'Variable' not in lines[i+count]:
                          if '![' in lines[i+count]:
                            imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')
                            #m = re.search("\/(.*?)\]", lines[i+count])                        
                          else: 
                              f2.write(lines[i+count])
                          count=count+1
                  else:
                      skiptxt='a)'
                      count=1
                      skipimg='.png]' #find a way to get image name
                      while  '# Answer' not in lines[i+count] and 'Variable' not in lines[i+count]:
                          if '![' in lines[i+count]:
                            imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')
                            #m = re.search("\/(.*?)\]", lines[i+count])                        
                          elif skiptxt not in lines[i+count] and 'a.' not in lines[i+count] and '- [ ]' not in lines[i+count]: 
                              f2.write(lines[i+count])
                          count=count+1                        
                      
          if Answerimg==1:
              for i, line in enumerate(lines):
                  if 'Answer' in line:
                      num=1
                      while 'eedback' not in lines[i+num] and 'Variable' not in lines[i+count]:
                          if '![' in lines[i+num]:
                            imgcount=imgmove(lines[i+num],imgcount,file,f2,'mc')
                            #m = re.search("\/(.*?)\]", lines[i+num])
                            #f2.write('\n$BR\n')
                            #f2.write('\{ image("'+ m.group(1) +'" , width=>400, height=>400,tex_size=>700, extra_html_tags=>'+"'alt=")
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
                              
 
              
         
          f2.write('\n')
          f2.write('\n$BR')
          f2.write('\n$BR\n')
          f2.write('\{$mc1->buttons()\}')
          f2.write('\n \n \n \n')
          f2.write('END_TEXT \n \nANS( $mc1->cmp() );')
          searchquery='_ '
          for i, line in enumerate(lines):
              if searchquery in line:
                      f2.write(line)
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
            if 'Answer' in line and '###' not in line:
                count=1
                while 'eedback' not in lines[i+count] and Answerimg==0:
                    if '.png' in lines[i+count]:
                        Answerimg=1
                    count=count+1
                     
               #check if images are a part of the answer
          for i, line in enumerate(lines):
                
              if 'Question' in line:
                  count=1
                  answerrepeat=0
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
                              #answernum=answernum+1
                          num=num+1
                  
                          
                                
          if answernum>1:
              for i, line in enumerate(lines):
                  if 'Answer' in line and '###' not in line:
                      num=1
                      while 'eedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num] and '[]' not in lines[i+num] and '()' not in lines[i+num]:
                              line=lines[i+num]
                              choice='"'+line.rstrip('\n')+ '",'
                              choice=re.sub('"(\w),"',r'"\1."',choice)
                              f2.write(choice)
                          num=num+1
          else:
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
                                                      f2.write('\n"'+lines[n+count].rstrip('\n')+ '",')
                                                      
                                                      written=1
                                                      break
                                                  count=count+1                              
                              num=num+1
                              
                                
                                                  
              
          #find answer                        
          f2.write('],') 
          searchquery='Good'
          searchquery2= 'Well done'
          for i, line in enumerate(lines):
              if searchquery in line or searchquery2 in line or 'Correct' in line or 'Good' in line or 'Great' in line:
                  ans=line[0]+line[1]
                  #print(ans)
                  for i, line in enumerate(lines):
                      if 'Answer' in line:
                          count=0
                          while 'eedback' not in lines[i+count] and '###' not in lines[i+count]:
                              ansalt=ans.rstrip('.')+','
                              if ans in lines[i+count] or lines[i+count].startswith(ansalt):
                                  line=lines[i+count].replace(ansalt,ans)
                                  answer='"'+line.rstrip('\n')+'"'
                                  f2.write('\n"'+line.rstrip('\n')+ '");')
                                  break
                              count=count+1
          
    
                 
                 

                 
                  
                        
          #PGML and Question
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
                      skipimg='.png]' #find a way to get image name
                      while skiptxt not in lines[i+count] and not lines[i+count].startswith('a.') and not lines[i+count].startswith('a)') and 'Variable' not in lines[i+count]:
                          if '![' in lines[i+count] and 'in_to_the_page' not in lines[i+count] and 'out_of_the_page' not in lines[i+count]:
                            imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')
                            f2.write("\n\n$BR\n$BR")
                            #m = re.search("\/(.*?)\]", lines[i+count])                        
                          elif lines[i+count].strip: 
                              f2.write(lines[i+count])
                          count=count+1
                  else:
                      skiptxt='a)'
                      count=1
                      #skipimg='.png]' #find a way to get image name
                      while skiptxt not in lines[i+count] and 'a.' not in lines[i+count] and '# Answer' not in lines[i+count] and 'Variable' not in lines[i+count]:
                          if '![' in lines[i+count] and 'in_to_the_page' not in lines[i+count] and 'out_of_the_page' not in lines[i+count]:
                            imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')
                            f2.write("\n\n$BR\n$BR")
                            #m = re.search("\/(.*?)\]", lines[i+count])                        
                          else: 
                              f2.write(lines[i+count])
                          count=count+1                        
          if answernum<=1: 
            for i, line in enumerate(lines):
              count=0
              ansimg=0
              if 'Question' in line:
                while 'Answer' not in lines[i+count]:
                  if lines[i+count].startswith('a.') or lines[i+count].startswith('a)'):
                    ansimg=1
                  if ansimg==1 and '![' in lines[i+count] and 'in_to_the_page' not in lines[i+count] and 'out_of_the_page' not in lines[i+count]:
                    imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')
                    f2.write("\n\n$BR\n$BR")  
                  count=count+1
                    
                
            
          elif Answerimg==1:
              for i, line in enumerate(lines):
                  if 'Answer' in line:
                      num=1
                      try:
                        while 'eedback' not in lines[i+num] and i+num<f_len:
                            if '![' in lines[i+num] and 'in_to_the_page' not in lines[i+count] and 'out_of_the_page' not in lines[i+count]: 
                              imgcount=imgmove(lines[i+num],imgcount,file,f2,'mc')
                              #f2.write("\n\n$BR\n$BR") 
                              #f2.write('tex_size=>700, extra_html_tags=>'+"'alt=")                            
                              #m = re.search("\/(.*?)\]", lines[i+num])
                              #f2.write('\n$BR\n')
                              count=1
                              n=i+num
                              while 'Answer' not in lines[n-count]:
                                  if lines[n-count].strip() and '![' not in lines[n-count]:
                                      l=lines[n-count]
                                      anstext=l[0]+l[1]
                                      anstext=anstext.replace(',','.')
                                      f2.write(anstext+'\n'+"\n\n$BR\n$BR")
                                      break
                                  count=count+1
                              if 'eedback' in lines[i+num]:
                                break
                            num=num+1
                      except:
                          continue
                              
                          
                      
                  

            
                  
              
              
              
         
          f2.write('\n\n$BR\n$BR\n\{$mc1->buttons()\}\n \n \n \nEND_TEXT \n \nANS( $mc1->cmp() );\nENDDOCUMENT();')
  
          #searchquery='_ '
          #for i, line in enumerate(lines):
              #if searchquery in line:
                      #f2.write(line)
         
          


  #replacing variables
  with open(newfile, 'r') as f:
      ln = f.readlines()
      data=''
      for i, line in enumerate(ln):      
        line=mctranslate(line)
        data=data+line
      try:
        answercheck=re.findall('"'+ans+'(.*?)"',data)
        if answercheck[0]!=answercheck[1]:
          data=data.replace(answercheck[0],answercheck[1])
      except Exception as e:
        print(e)      
        

  with open(newfile, 'w') as f:
      f.write(data)  
              
              
              
              
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
          for i,line in enumerate(lines):
            if 'From the list below' in line:
              qtype=1
            
          for i,line in enumerate(lines):
            if 'Question:' in line:
              count=1
              while skiptxt not in lines[i+count] and 'a.' not in lines[i+count] and '# Answer' not in lines[i+count] and 'Variable' not in lines[i+count]:
                if '![' not in lines[i+count] and line.rstrip(): 
                    f2.write(lines[i+count].replace('"',''))
                count=count+1 
          f2.write('",')
          searchquery='Good job!'
          searchquery2= 'Well done!'
          for i, line in enumerate(lines):
              if searchquery in line or searchquery2 in line or 'Correct.' in line:
                  ans=line[0]+line[1]
                  ansdetermined=1
                  newsearch='Answer'
                  for n, line in enumerate(lines):
                      if 'Answer' in line and 'specific' not in line:
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
          if ansdetermined==0:
            if qtype==1:
              for n, line in enumerate(lines):
                if 'Answer' in line and 'specific' not in line:
                  count=1
                  num=1
                  extraans=[]
                  while 'Feedback' not in lines[n+count]:
                      if lines[n+count].strip() and '![' not in lines[n+count]:
                          f2.write('\n"'+lines[n+count].rstrip('\n')+ '",\n')  
                      count=count+1
                  
              
          #"\( e^{x^2} e^{1/x} \)$BR",
          #"\( e^{x^2} e^{x^{-1}} \)$BR",                
          #"\( e^{ (x^3+1) / x } \)$BR",
          f2.write(');\n')
          f2.write('$mc -> makeLast(')
          writtenans=0
          #Multiple choice answers and buttons
          #finding location of answer
        
          for i, line in enumerate(lines):
                  if 'From the list below' in line:
                    num,write=1,0
                    while 'Answer' not in lines[i+num]:
                            if lines[i+num].startswith('a)') or line.startswith('a.'):
                              write=1
                            if lines[i+num].strip() and '![' not in lines[i+num] and '[]' not in lines[i+num] and '()' not in lines[i+num] and write==1:
                                line=lines[i+num]
                                f2.write('"'+line.rstrip('\n')+ '",\n')
                                writtenans=1
                            num=num+1
                          
                                               
                  elif 'Answer' in line and '###' not in line:
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
                                    if ans in lines[n+number]:
                                      answernum=0
                                    number=number+1
                              #answernum=answernum+1
                          num=num+1
                          
                      
                      
          if answernum>1 and writtenans==0:
              for i, line in enumerate(lines):
                  if 'Answer' in line and '###' not in line:
                      num=1
                      while 'eedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num] and '[]' not in lines[i+num] and '()' not in lines[i+num]:
                              line=lines[i+num]
                              f2.write('"'+line.rstrip('\n')+ '",')
                          num=num+1
          elif writtenans==0:
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
          #"\( \displaystyle \frac{ e^{x^2} }{ e^x } \)$BR",
          #"\( e^{x^2} + e^{1/x} \)$BR",
          #);
          #$mc -> makeLast("None of the above");

          Answerimg=0
          Qimg=0
          for i, line in enumerate(lines):
              if 'Answer' in line and 'specific' not in line:
                  count=1
                  while 'Feedback' not in lines[i+count] and Answerimg==0:
                      if '.png' in lines[i+count]:
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
                      
           
                      
                   
  
  #MC answers if image is outside the answer choices
          #searchquery='Answer'
          #f2.write('$mc1 = RadioButtons([\n')
          #if Answerimg ==1:
              #for i, line in enumerate(lines):
                  #if 'Answer' in line:
                      #num=1
                      #while 'Feedback' not in lines[i+num]:
                          #if lines[i+num].strip() and '![' not in lines[i+num]:
                              #line=lines[i+num]
                              #f2.write('"'+line[0]+line[1]+ '",')
                          #num=num+1
                      #f2.write('],')
                  #searchquery='Good job'
                  #searchquery2= 'Well done'
              #for i, line in enumerate(lines):
                  #count=0
                  #if searchquery in line or searchquery2 in line or 'Correct.' in line:
                      #ans=line[0]+line[1]
                      #count=count+1
                      #f2.write('\n"'+ans+ '");')
                  
                          
                          
          #else:
              #for i, line in enumerate(lines):
                  #if 'Answer' in line:
                      #num=1
                      #while 'Feedback' not in lines[i+num]:
                          #if lines[i+num].strip():
                              #f2.write('"'+lines[i+num].rstrip('\n')+ '",')
                          #num=num+1
                      #f2.write('],')
                  #searchquery='Good job'
                  #searchquery2= 'Well done'
                  #for i, line in enumerate(lines):
                      #if searchquery in line or searchquery2 in line or 'Correct.' in line:
                          #ans=line[0]+line[1]
                          #newsearch='Answer'
                          #for n, line in enumerate(lines):
                              #if 'Answer' in line:
                                  #avoidq= 'Feedback'
                                  #count=0
                                  #while 'Feedback' not in lines[n+count]:
                                      #if ans in lines[n+count]:
                                          #f2.write('\n"'+lines[n+count].rstrip('\n')+ '");')
                                          #break
                                      #count=count+1
                                  #break
                              #break
          
    
                 
                 
  
                 
                  
  
          #PGML and Question
          f2.write('\n')
          f2.write('########################################################')
          f2.write('\n')
          f2.write('# Not in PGML')
          f2.write('\n')
          f2.write('\n')
          f2.write('BEGIN_TEXT\n')
          f2.write('\n$BR\n')
          if Qimg==1:
              for i, line in enumerate(lines):
                  if 'Question:' in line:
                      num=1
                      while 'Answer' not in lines[i+num]:
                          if '![' in lines[i+num]:
                              #m = re.search("\/(.*?)\]", lines[i+num])
                              imgcount=imgmove(lines[i+num],imgcount,file,f2,'mc')
                              f2.write('\n$BR\n')
                              #f2.write('\{ image("'+ m.group(1) +'" , width=>400, height=>400,tex_size=>700, extra_html_tags=>'+"'alt=")
                              count=1
                          num=num+1
                              
              #f2.write('\{ image("'+ imgname +'.png" , width=>400, height=>400)\}')#copy image name
              f2.write('\n$BR\n')
              searchquery='# Q'
              #for i, line in enumerate(lines):
                  #if searchquery in line:
                      #skiptxt='# A'
                      #count=1
                      #skipimg='.png]' #find a way to get image name
                      #while skiptxt not in lines[i+count]:
                          #if skipimg not in lines[i+count]:
                              #f2.write(lines[i+count])
                          #count=count+1
          if Answerimg==1:
              for i, line in enumerate(lines):
                  if 'Answer' in line and 'specific' not in line:
                      num=1
                      while 'Feedback' not in lines[i+num]:
                          if '![' in lines[i+num]:
                              #m = re.search("\/(.*?)\]", lines[i+num])
                              imgcount=imgmove(lines[i+num],imgcount,file,f2,'mc')
                              f2.write('\n$BR\n')
                              #f2.write('\{ image("'+ m.group(1) +'" , width=>400, height=>400,tex_size=>700, extra_html_tags=>'+"'alt=")
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
          f2.write('\{ $mc -> print_q() \}\n')
          f2.write('$BR')
          f2.write('\{ $mc -> print_a() \}\n')
          f2.write('END_TEXT\n  ')                     
      
          f2.write('\nANS( checkbox_cmp( $mc->correct_ans() ) );\nENDDOCUMENT();')
          
          #searchquery='_ '
          #for i, line in enumerate(lines):
              #if searchquery in line:
                      #f2.write(line)
          
  
  
  #replacing variables
  with open(newfile, 'r') as f:
    ln = f.readlines()
    data=''
    for i, line in enumerate(ln): 
      if 'new_checkbox_multiple_choice' not in line and 'print_q()' not in line and 'print_a()' not in line and 'checkbox_cmp' not in line:
        line=mctranslate(line)
      data=data+line    
      #data = f.read()
      #data=data.replace(',]', ']')
      #data=data.replace('$', '')
      ##specifcally search within line for string
      #data=data.replace('vec','hbc')
      #data=data.replace('\hbc{', '\( '+'\hbc{')
      #data=data.replace('hbc','vec')
      #data=data.replace('}=', '} \)=')
      #data=data.replace('\hat{i}','\( \hat{i} \)' )
      #data=data.replace('\hat{j}', '\( \hat{j} \)')
      #data=data.replace('\hat{k}', '\( \hat{k} \)')
      #data=data.replace('mc', '$mc')
      #data=data.replace(',)',')')
      #data=data.replace('BR', '$BR')
      #data=data.replace('**','')
      #x='alpha\\'
      #data=data.replace( x , '(alpha\)' )
      
  
  
  
  with open(newfile, 'w') as f:
      f.write(data)

              
              
              
              
 
                
                
 
#Input file location
os.chdir(filelocation)
filename=[]
count=1
problemcount=0;
problemset=''
setcount=10
for file in glob.glob("*.md"):
    print(file)
    count=count+1
    imgcount=0
    newfile=file.rstrip('.md')+'.pg'
    newfile=newfile.replace(' ','-')
    #print(newfile)
    if problemcount<100:
      problemset=problemset+ 'setUsaskMCQuestions/'+newfile+ ', 0 \n'
      problemcount=problemcount+1;
    else:
      setname='setusaskmc'+str(setcount)+'.def'
      with open(setname, 'w') as f:
        f.write('setNumber=Usaskmc'+str(setcount))
        f.write('\nopenDate = 1/7/00 at 6:00am\ndueDate = 1/20/09 at 6:00am\nanswerDate = 1/21/09 at 6:00\npaperHeaderFile = set34/paperHeaderFile0.pg\nscreenHeaderFile = set34/screenHeaderFile0.pg\nproblemList =\n ' )      
        f.write(problemset)      
      problemcount=0
      setcount=setcount+1
      problemset=''

    #copying comments
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        torf=0
        for i, line in enumerate(lines):
            if 'Question Format' in line:
              if 'Numerical' in line:
                for i, line in enumerate(lines):
                  if 'a.' in line or 'a)' in line:
                    for i, line in enumerate(lines):
                      if 'b.' or 'b)' in line:
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
              elif 'True' in line or 'true' in line:
                print('Torf')
                TrueorFalse()
              else:
                print(':question format not recognized')
                
#print set.def file
setname='setusaskmc'+str(setcount)+'.def'
with open(setname, 'w') as f:
  f.write('setNumber=Usaskmc'+str(setcount))
  f.write('\nopenDate = 1/7/00 at 6:00am\ndueDate = 1/20/09 at 6:00am\nanswerDate = 1/21/09 at 6:00\npaperHeaderFile = set34/paperHeaderFile0.pg\nscreenHeaderFile = set34/screenHeaderFile0.pg\nproblemList =\n ' )    
  f.write(problemset)

with open('imagemovingerrors.txt','w') as f:
  f.write('Image Scaling Errors\n\n\n\n')
  for i in range(len(imgscaleerrors)):
    f.write(imgscaleerrors[i]+'\n')
  f.write('Image Moving Errors\n\n\n')
  for i in range(len(imgerrormovinglist)):
    f.write(imgerrormovinglist[i]+'\n')  
  
  
                             
