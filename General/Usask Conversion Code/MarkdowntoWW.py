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

#This script converts Markdown into Webwork Questions
#
 
 # \_ is a blank
 # _ is also a blank
 #if there are variable parameters, do a certain way
 #input file location below
filelocation=r'C:\Users\ptemm\Downloads\Export-2401a9dd-4c35-488b-bd51-4af373634d6a\GE 124 Question Database - Module 2 9cc673d992ce47c1b4b615581a5f7d90'
#moving and renaming images
def imgmove(imgline,imgcount,filename,filetowrite,qtype):
  m = re.search("\/(.*?)\]", imgline)
  filename=filename.rstrip('.md')
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
  try:
    os.rename(originpath,newname)
  except:
    pass
  imgcount=imgcount+1
  if qtype=='n':
    filetowrite.write('[@ image( "'+newimgname+'", width=>[$width], height=>[$height]) @]*\n')
    filetowrite.write('END_PGML\nBEGIN_PGML\n')
  else:
    filetowrite.write('\n$BR\n')
    filetowrite.write('\{ image("'+ newimgname +'" , width=>400, height=>400) \}')   
  return imgcount
  
  
#def writeans(line):
  
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
  #line=line.replace('__','[__]')
  line=re.sub('text{(.)}',r'[`\1`]',line)
  line=line.replace('\cdot','[`\\cdot`]')
  line=line.replace('left(','')
  line=line.replace('right)','')
  line=line.replace('$\\','')
  line=line.replace('$','')
  line=line.replace('\\','')
  line=re.sub('\[(.)\]',r'[`[$\1]`]',line)
  line=line.replace('\\times',r'*')
  line=re.sub('overrightarrow{(.)}',r'[`\\overrightarrow{\1}`]',line)
  line=re.sub('~~','',line)
  line=line.replace('**','')
  line=line.replace('}$','')
  line=re.sub('hat{(.)}',r'[`\\hat{\1}`]',line)
  line=line.replace('\cos','[`cos`]')
  line=line.replace('\sin','[`sin`]')
  line=line.replace('\tan','[`tan`]') 
  line=re.sub('mathrm{(.)}',r'[`\1`]',line)
  if '_' in line:
    line=re.sub(' (._.) ',r'[`\1`]',line)
  return line

def mctranslate(data):
  if 'begin{vmatrix}' in data:
    m=re.search(r"begin{vmatrix}(.*?)end{vmatrix}", data)
    data=sub('((\w*)_(\w*))',r'\\(\1'+'\\)', data)
    p=re.search(r"begin{vmatrix}(.*?)end{vmatrix}", data)
    data=data.replace(p.group(0),m.group(0))
  else:
    data=sub('((\w*)_(\w*))',r'\\(\1'+'\\)', data)
  data=data.replace(',]', ']')
  data=data.replace('$', '')
  #specifcally search within line for string
  data=data.replace('vec','hbc')
  data=data.replace('\hbc{', '\( '+'\hbc{')
  data=data.replace('hbc','vec')
  #data=data.replace('}=', '} \)='
  data=re.sub('hat{(.)}',r'[`\\hat{\1}`]',data)
  data=data.replace('mc', '$mc')
  data=data.replace(r'times','( \\times\)')
  data=data.replace('BR', '$BR')
  data=data.replace('**','')
  data=data.replace('\cdot','\(\cdot\)')
  data=data.replace('\\\\\\','')
  x='alpha\\'

  data=data.replace( x , '(alpha\)' )
  o= '(\\\overrightarrow{.}\\\)' 
  
  data=sub('\\\overrightarrow{(.)}_', r'11111111111111{\1}',data)
  data=sub('\\\overrightarrow{(.)}', r'\(\\overrightarrow{\1}\\)',data)
  data=data.replace('\\(\\(\\', r'\(\\')
  data=sub('11111111111111{(.)}', r'\\overrightarrow{\1}_',data)
  data=data.replace('\\)\\)',r'\\)')
  data=sub('\\)_(.)',r'_\1 \\)',data)
  data=data.replace('\\_','_')
  #data=data.replace('overright','123')
  #data=data.replace('\\\\','\\')
  data=data.replace('\(BEGIN_TEXT\)','BEGIN_TEXT')
  data=data.replace('\(END_TEXT\)','END_TEXT')
  #replacecos,sin,tan,theta
  data=data.replace('\cos','\(\cos\)')
  data=data.replace('\sin','\(\sin\)')
  data=data.replace('\tan','\(\tan\)')
  data=data.replace('\\theta','\(\\theta\)')
  #        \begin{vmatrix}B_x&B_y\A_x&A_y\)\\end{vmatrix}
  #\begin{vmatrix}A_x&B_x\\A_y&B_y\\\end{vmatrix}
  #data=re.sub(r'begin{vmatrix}(\.*?)\\',r'test',data)
  #\begin{vmatrix}A_x&B_x\\A_y&B_y\end{vmatrix}\( \hat{k} \)
  return data
 
 
 
def Numerical():
      imgcount=0
      with open(file, 'r', encoding='utf-8') as f:
          f_len=file_len(file)
          with open(newfile, 'w') as f2:
            #Starting the document
              beginfile(f2,file)

      #finding variables
      
              searchquery='Variable'
              for i, line in enumerate(lines):
                if 'Range' in line:
                    f2.write('random(')
                    m = re.search("\((.*?)\)", line)
                    f2.write(m.group(1))
                    m = re.search("\((.*?)\)", line)

                    f2.write(',1);')
                    f2.write('\n')                  
                elif searchquery in line:
                      n=1
                      while 'Answer' not in lines[i+n]:
                          #f2.write('substitueavoid3')
                          if lines[i+n].strip():
                              m = lines[i+n]
                              m=m.split(':',1)[0]
                              m=m.replace('[','')
                              m=m.replace(']','')
                              f2.write(m+'=')
                              
                              line=lines[i+n]
                              if ':' in line and '=' in line:
                                  line=line.split('=',1)[1]
                              else:   
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
              searchquery='Answer'
              for i, line in enumerate(lines):
                  if searchquery in line :
                      count=1
                      ansnum=0
                      while 'eedback' not in lines[i+count]:
                          if '=' in lines[i+count]:
                              line=lines[i+count]
                              if line.startswith('$$'):
                                  f2.write('$ans'+str(ansnum) +'=')
                                  ansnum=ansnum+1
                                  if'(' in line:
                                    m=re.search("\((.*?)\)", line) 
                                    f2.write(m.group(1).rstrip('\n'))
                                    f2.write(';\n')                                    
                                  else:
                                    l=line.split('=',1)[1]
                                    l=l.replace('$$','')
                                    l=l.replace('[','$')#could use re.sub
                                    l=l.replace(']','')
                                    f2.write(l.rstrip('\n'))
                                    f2.write(';\n')
                               
                              
                              else:
                                  f2.write(lines[i+2].rstrip('\n') + ';')
                                  f2.write('\n')
                                  
                              
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
              f2.write('\n')
              f2.write('########################################################')
              f2.write('\n')
              f2.write('#PGML')
              f2.write('\n')
              f2.write('BEGIN_PGML')
              f2.write('\n')
              f2.write('\n')
              searchquery='# Q'
              for i, line in enumerate(lines):
                  if line.startswith(searchquery):
                      count=1
                      ansnum=0
                      while 'ariable' not in lines[i+count] and 'Answer' not in lines[i+count]:
                          data=''
                          #m = re.search("\[(.*?)\]", lines[i+count]) #add for loop to print text
                          #print(m.group(1))
                          if lines[i+count].strip():
                              #looking for where to input the answers
                              if '\_\_' in lines[i+count]:
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
                          
                          
                          
                              elif '________' in lines[i+count]:
                                  line=lines[i+count]
                                  counter = line.count('________')
                                  while counter>=0:
                                      #line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line)
                                      line=re.sub('________','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                      counter=counter-1
                                      ansnum=ansnum+1
                                  #line=translateline(line)
                                  f2.write(line+'\n')
                                  
                              elif '$_' in lines[i+count]:
                                  line=lines[i+count]
                                  counter = line.count('$_')
                                  while counter>=0:
                                      line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                      #line=re.sub('________','[____]{"$ans'+str(ansnum)+'"}',line)
                                      counter=counter-1
                                      ansnum=ansnum+1
                                  line=translateline(line)
                                  f2.write(line+'\n')
                                  
                              elif '__$' in lines[i+count]:
                                line=lines[i+count]
                                counter = line.count('__$')
                                while counter>=0:
                                    line=re.sub('__\$','[____]{"$ans'+str(ansnum)+'"}',line,1)
                                    #line=re.sub('________','[____]{"$ans'+str(ansnum)+'"}',line)
                                    counter=counter-1
                                    ansnum=ansnum+1
                                line=translateline(line)
                                f2.write(line+'\n')                                
                                  
                                  
                                  #imagesearch
                                  
                              elif '.png' in lines[i+count]:
                                  #line=lines[i+count]
                                  #m = re.search("\/(.*?)\]", line)
                                  #f2.write(m.group(1))
                                  imgcount=imgmove(lines[i+count],imgcount,file,f2,'n')
                                  f2.write('\n$BR\n')
                                                                
                                  
                                      
                                     
                                                             
                              else:    
                                  data=data+lines[i+count]
                                  #data=data.replace('[','a7')
                                  #data=data.replace(']','a8')
                                  data=translateline(data)
                                  f2.write(data+'\n')
                          count=count+1
                      
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
                          f2.write(a+'",' )
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
                      while skiptxt not in lines[i+count]:
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
                      while  '# Answer' not in lines[i+count]:
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
                      while 'eedback' not in lines[i+num]:
                          if '![' in lines[i+num]:
                            imgcount=imgmove(lines[i+num],imgcount,file,f2,'mc')
                            #m = re.search("\/(.*?)\]", lines[i+num])
                            #f2.write('\n$BR\n')
                            #f2.write('\{ image("'+ m.group(1) +'" , width=>400, height=>400,tex_size=>700, extra_html_tags=>'+"'alt=")
                            count=1
                            n=i+num
                            while 'Answer' not in lines[n-count]:
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
                      
           
                      
                   

          #MC answers if image is outside the answer choices
          searchquery='Answer'
          f2.write('$mc1 = RadioButtons([\n')
          for i, line in enumerate(lines):
                  if 'Answer' in line and '###' not in line:
                      num=1
                      answernum=3
                      while 'eedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num]:
                              line=lines[i+num]
                              ans=line[0]+line[1]
                              for n, line in enumerate(lines):
                                if '# Question' in line:
                                  number=1
                                  while 'Answer' not in lines[n+number]:
                                    #print(line)
                                    if ans in lines[n+number]:
                                      answernum=0
                                    number=number+1
                              #answernum=answernum+1
                              print(answernum)
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
                              
                                
                                                  
              
                                   
          f2.write('],') 
          searchquery='Good'
          searchquery2= 'Well done'
          for i, line in enumerate(lines):
              if searchquery in line or searchquery2 in line or 'Correct' in line or 'Good' in line:
                  ans=line[0]+line[1]
                  for i, line in enumerate(lines):
                      if 'Answer' in line:
                          count=0
                          while 'eedback' not in lines[i+count]:
                              if ans in lines[i+count]:
                                  f2.write('\n"'+lines[i+count].rstrip('\n')+ '");')
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
                      print('aaaaaa')
                      skiptxt='# A'
                      count=1
                      skipimg='.png]' #find a way to get image name
                      while skiptxt not in lines[i+count] and 'a.' not in lines[i+count] and 'a)' not in lines[i+count]:
                          print(count)
                          if '![' in lines[i+count]:
                            imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')
                            #m = re.search("\/(.*?)\]", lines[i+count])                        
                          elif lines[i+count].strip: 
                              f2.write(lines[i+count])
                          count=count+1
                  else:
                      skiptxt='a)'
                      count=1
                      #skipimg='.png]' #find a way to get image name
                      while skiptxt not in lines[i+count] and 'a.' not in lines[i+count] and '# Answer' not in lines[i+count]:
                          if '![' in lines[i+count]:
                            imgcount=imgmove(lines[i+count],imgcount,file,f2,'mc')
                            #m = re.search("\/(.*?)\]", lines[i+count])                        
                          else: 
                              f2.write(lines[i+count])
                          count=count+1                        
                      
          if Answerimg==1:
              for i, line in enumerate(lines):
                  if 'Answer' in line:
                      num=1
                      try:
                        while 'eedback' not in lines[i+num] and i+num<f_len:
                            print(lines[i+num])
                            if '![' in lines[i+num]:
                              imgcount=imgmove(lines[i+num],imgcount,file,f2,'mc')
                              #f2.write('tex_size=>700, extra_html_tags=>'+"'alt=")                            
                              #m = re.search("\/(.*?)\]", lines[i+num])
                              #f2.write('\n$BR\n')
                              count=1
                              n=i+num
                              while 'Answer' not in lines[n-count]:
                                  if lines[n-count].strip():
                                      l=lines[n-count]
                                      anstext=l[0]+l[1]
                                      f2.write(anstext+'\n'+anstext+"\n\n$BR\n$BR")
                                      break
                                  count=count+1
                              if 'eedback' in lines[i+num]:
                                break
                            num=num+1
                      except:
                          continue
                              
                          
                      
                  

            
                  
              
              
              
         
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
        line=mctranslate(line)
        data=data+line

  with open(newfile, 'w') as f:
      f.write(data)  
              
              
              
              
def Multipleanswer():
  imgcount=0
  with open(file, 'r', encoding='utf-8') as f:
      with open(newfile, 'w') as f2:
          lines = f.readlines()
          searchquery = 'Key'
          count=0
          for i, line in enumerate(lines):
              if line.startswith(searchquery) or line.startswith('Automatic'):
                      f2.write('#')
                      f2.write('DESCRIPTION')
                      f2.write('\n')
                      while count< 5:
                          f2.write('#')
                          f2.write(lines[i+count])#might need to make it a little more efficient
                          count=count+1
                      f2.write('#')
                      f2.write(lines[i+7])
                      f2.write('#')
                      f2.write(lines[i+13])
                      f2.write('#')
                      f2.write(' END DESCRIPTION')
  
                      #Starting the document
                      f2.write('\n')
                      f2.write('\n')
                      f2.write('########################################################')
                      f2.write('\n')
                      f2.write('DOCUMENT();')
                      f2.write('\n')
                      f2.write('\n')
                      f2.write('loadMacros(')
                      f2.write('\n')
                      f2.write('"PGstandard.pl",	# Standard macros for PG language')
                      f2.write('\n')
                      f2.write('"MathObjects.pl",')
                      f2.write('\n')
                      f2.write('"PGML.pl",')
                      f2.write('\n')
                      f2.write('"parserPopUp.pl",')
                      f2.write('\n')
                      f2.write('"parserMultiAnswer.pl",')
                      f2.write('\n')
                      f2.write('"parserRadioButtons.pl",')
                      f2.write('\n')
                      f2.write('"weightedGrader.pl",')
                      f2.write('\n')
                      f2.write('#"source.pl",')
                      f2.write('\n')
                      f2.write('#"PGcourse.pl",')
                      f2.write('\n')
                      f2.write(');')
                      f2.write('\n')
                      f2.write('TEXT(beginproblem());')
                      f2.write('\n')
                      f2.write('\n')
                      f2.write('########################################################')
                      f2.write('\n')
                      f2.write('\n')
                      f2.write('#Setup')
                      f2.write('\n')
                      f2.write('\n')
  
  
  
                    #check if images are a part of the answer
          Answerimg=0
          Qimg=0
          for i, line in enumerate(lines):
              if 'Answer' in line:
                  count=1
                  while 'Feedback' not in lines[i+count]:
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
          searchquery='Answer'
          f2.write('$mc1 = RadioButtons([\n')
          if Answerimg ==1:
              for i, line in enumerate(lines):
                  if 'Answer' in line:
                      num=1
                      while 'Feedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num]:
                              line=lines[i+num]
                              f2.write('"'+line[0]+line[1]+ '",')
                          num=num+1
                      f2.write('],')
                  searchquery='Good job'
                  searchquery2= 'Well done'
              for i, line in enumerate(lines):
                  count=0
                  if searchquery in line or searchquery2 in line or 'Correct.' in line:
                      ans=line[0]+line[1]
                      count=count+1
                      f2.write('\n"'+ans+ '");')
                  
                          
                          
          else:
              for i, line in enumerate(lines):
                  if 'Answer' in line:
                      num=1
                      while 'Feedback' not in lines[i+num]:
                          if lines[i+num].strip():
                              f2.write('"'+lines[i+num].rstrip('\n')+ '",')
                          num=num+1
                      f2.write('],')
                  searchquery='Good job'
                  searchquery2= 'Well done'
                  for i, line in enumerate(lines):
                      if searchquery in line or searchquery2 in line or 'Correct.' in line:
                          ans=line[0]+line[1]
                          newsearch='Answer'
                          for n, line in enumerate(lines):
                              if 'Answer' in line:
                                  avoidq= 'Feedback'
                                  count=0
                                  while 'Feedback' not in lines[n+count]:
                                      if ans in lines[n+count]:
                                          f2.write('\n"'+lines[n+count].rstrip('\n')+ '");')
                                          break
                                      count=count+1
                                  break
                              break
          
    
                 
                 
  
                 
                  
  
          #PGML and Question
          f2.write('\n')
          f2.write('########################################################')
          f2.write('\n')
          f2.write('# Not in PGML')
          f2.write('\n')
          f2.write('\n')
          f2.write('BEGIN_TEXT')
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
              for i, line in enumerate(lines):
                  if searchquery in line:
                      skiptxt='# A'
                      count=1
                      skipimg='.png]' #find a way to get image name
                      while skiptxt not in lines[i+count]:
                          if skipimg not in lines[i+count]:
                              f2.write(lines[i+count])
                          count=count+1
          if Answerimg==1:
              for i, line in enumerate(lines):
                  if 'Answer' in line:
                      num=1
                      while 'Feedback' not in lines[i+num]:
                          if '![' in lines[i+num]:
                              #m = re.search("\/(.*?)\]", lines[i+num])
                              imgcount=imgmove(lines[i+num],imgcount,file,f2,mc)
                              f2.write('\n$BR\n')
                              f2.write('\{ image("'+ m.group(1) +'" , width=>400, height=>400,tex_size=>700, extra_html_tags=>'+"'alt=")
                              count=1
                              n=i+num
                              while 'Answer' not in lines[n-count]:
                                  if lines[n-count].strip():
                                      l=lines[n-count]
                                      anstext=l[0]+l[1]
                                      f2.write(anstext+"')\}"+'\n'+anstext+"\n\n$BR")
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
      data = f.read()
      data=data.replace(',]', ']')
      data=data.replace('$', '')
      #specifcally search within line for string
      data=data.replace('vec','hbc')
      data=data.replace('\hbc{', '\( '+'\hbc{')
      data=data.replace('hbc','vec')
      data=data.replace('}=', '} \)=')
      data=data.replace('\hat{i}','\( \hat{i} \)' )
      data=data.replace('\hat{j}', '\( \hat{j} \)')
      data=data.replace('\hat{k}', '\( \hat{k} \)')
      data=data.replace('mc', '$mc')
      data=data.replace('BR', '$BR')
      data=data.replace('**','')
      x='alpha\\'
      data=data.replace( x , '(alpha\)' )
  
  
  
  with open(newfile, 'w') as f:
      f.write(data)

              
              
              
              
 
                
                
 
#Input file location
os.chdir(filelocation)
filename=[]
count=1
for file in glob.glob("*.md"):
    print(file)
    count=count+1
    imgcount=0
    newfile=file.rstrip('.md')+'.pg'

    #copying comments
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if 'Question Format' in line:
              if 'Numerical' in line:
                  Numerical()
              elif 'Multiple Choice' in line or 'Multiple choice' in line or 'multiple choice'  in line:
                  count=0
                  for i, line in enumerate(lines):
                        if 'Good job' in line or 'Well done' in line or 'Correct.' in line:
                            count=count+1
                  if count>1:
                        Multipleanswer()
                  else:
                        Multiplechoice()              
              elif 'True' in line or 'true' in line:
                TrueorFalse()
              else:
                print(':question format not recognized')
                             
