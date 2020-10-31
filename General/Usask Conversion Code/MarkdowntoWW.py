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
 #
def beginfile(f2):
  
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
  f2.write('\n#"source.pl",\n')
  f2.write('\n')
  f2.write('\n#"PGcourse.pl",\n);\n')
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
                           
  
def file_len(file):
  with open(file, 'r', encoding='utf-8') as f:
    for i, l in enumerate(f):
      pass
  return i + 1  

def translateline(line):
  line=re.sub('text{(.)}',r'[`\1`]',line)
  line=line.replace('\cdot','[`\\cdot`]')
  line=line.replace('$\\','')
  line=line.replace('$','')
  line=line.replace('\\','')
  line=re.sub('\[(.)\]',r'[`[$\1]`]',line)
  line=line.replace('\\times',r'*')
  line=re.sub('overrightarrow{(.)}',r'[`\\overrightarrow{\1}`]',line)
  line=re.sub('~~','',line)
  line=line.replace('**','')
  line=line.replace('}$','')
  if '_' in line:
    line=re.sub(' (._.) ',r'[`\1`]',line)
  return line
 
 
 
def Numerical():
      with open(file, 'r', encoding='utf-8') as f:
          f_len=file_len(file)
          with open(newfile, 'w') as f2:
              lines = f.readlines()
              searchquery = 'Key'
              count=0
              for i, line in enumerate(lines):
                  if line.startswith(searchquery):
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
                          beginfile(f2)
                          
                       
      
      #finding variables
      
              searchquery='Variable'
              for i, line in enumerate(lines):
                  if searchquery in line:
                      n=1
                      while 'Answer' not in lines[i+n]:
                          #f2.write('substitueavoid3')
                          if lines[i+n].strip():
                              m = lines[i+n]
                              m=m.split(':',1)[0]
                              m=m.replace('[','')
                              m=m.replace(']','')
                              f2.write(m+'=')
                              if 'Range' in lines[i+n]:
                                  f2.write('random(')
                                  m = re.search("\((.*?)\)", lines[i+n])
                                  f2.write(m.group(1))
                                  m = re.search("\((.*?)\)", lines[i+n])
                                                                
                                  
                                  f2.write(',1);')
                                  f2.write('\n')
                              else:
                                      line=lines[i+n]
                                      if ':' in line and '=' in line:
                                          line=line.split('=',1)[1]
                                      else:   
                                          line=line.split(':',1)[1]
                                      print(line)
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
                      count=0
                      ansnum=0
                      while 'eedback' not in lines[i+count]:
                          if '=' in lines[i+count]:
                              print('eq')
                              line=lines[i+count]
                              if line.startswith('$$'):
                                  f2.write('$ans'+str(ansnum) +'=')
                                  ansnum=ansnum+1
                                  m=re.search("\((.*?)\)", line) 
                                  f2.write(m.group(1).rstrip('\n'))
                                  f2.write(';\n')
                               
                              
                              else:
                                  f2.write(lines[i+2].rstrip('\n') + ';')
                                  f2.write('\n')
                                  
                              
                          else:
                              line=lines[i+count]
                              a=''
                              initial=0
                              for n in line:
                                  print(n)   
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
                                  
                                  elif n==',' or n=='$':
                                      if a!='':
                                          print(a)
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
                      #print('1')
                      count=1
                      ansnum=0
                      while 'ariable' not in lines[i+count] and 'Answer' not in lines[i+count]:
                          #print('2')
                          data=''
                          #m = re.search("\[(.*?)\]", lines[i+count]) #add for loop to print text
                          #print(m.group(1))
                          if lines[i+count].strip():
                              #looking for where to input the answers
                              if '\_\_' in lines[i+count]:
                                  line=lines[i+count]
                                  l=line.split('=',1)[0]
                                  e=line.split('_\,',1)[1]
                                  print(e)
                                  f2.write(l+'='+'substituteavoid4{"\$ans'+str(ansnum)+'"}'+e.rstrip('\n')+'\n\n')
                                  f2.write('$BR\n')
                                  ansnum=ansnum+1
                          
                          
                          
                              elif '________' in lines[i+count]:
                                  line=lines[i+count]
                                  counter = line.count('________')
                                  while counter>=0:
                                      #line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line)
                                      line=re.sub('________','[____]{"$ans'+str(ansnum)+'"}',line)
                                      counter=counter-1
                                      ansnum=ansnum+1
                                  line=translateline(line)
                                  f2.write(line+'\n')
                                  
                              elif '$_' in lines[i+count]:
                                  line=lines[i+count]
                                  counter = line.count('$_')
                                  while counter>=0:
                                      line=re.sub('\$___\$','[____]{"$ans'+str(ansnum)+'"}',line)
                                      #line=re.sub('________','[____]{"$ans'+str(ansnum)+'"}',line)
                                      counter=counter-1
                                      ansnum=ansnum+1
                                  line=translateline(line)
                                  f2.write(line+'\n')
                                  
                                  
                                  #imagesearch
                                  
                              elif '.png' in lines[i+count]:
                                  line=lines[i+count]
                                  m = re.search("\/(.*?)\]", line)
                                  #print(lines[i+num])
                                  #print(m.group(1))
                                  f2.write(m.group(1))
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
              
              
              
              
              
              
              
              
              
def Multiplechoice():
  with open(file, 'r', encoding='utf-8') as f:
      f_len=file_len(file)
      with open(newfile, 'w') as f2:
          lines = f.readlines()
          searchquery = 'Key'
          count=0
          for i, line in enumerate(lines):
              done=0
              print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
              if line.startswith(searchquery) or line.startswith('Automatic') and done==0:
                      done=1
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
                      beginfile(f2)



                    #check if images are a part of the answer
          Answerimg=0
          Qimg=0
          for num, line in enumerate(lines):
              if 'Answer' in line and '###' not in line:
                  count=1
                  print(line)
                  while 'eedback' not in lines[num+count]:
                      if '.png' in lines[num+count]:
                          print('found')
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
                      print(line)
                      num=1
                      answernum=0
                      while 'eedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num]:
                              answernum=answernum+1
                          num=num+1
                          
                      
                      
          if answernum>2:
              for i, line in enumerate(lines):
                  if 'Answer' in line and '###' not in line:
                      print(line)
                      num=1
                      while 'eedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num]:
                              line=lines[i+num]
                              f2.write('"'+line.rstrip('\n')+ '",')
                              print(lines[i+num])
                          num=num+1
          else:
              for i, line in enumerate(lines):
                  if 'Feedback' in line:
                      print(line)
                      num=1
                      while  i+num<f_len:
                              written=0
                              if lines[i+num].strip() and '![' not in lines[i+num]  and ans not in lines[i+num]:
                                  line=lines[i+num]
                                  if line[0].isalpha():
                                      ans=line[0]+line[1]
                                      print(ans)
                                      for n, line in enumerate(lines):
                                          if 'Question' in line:
                                              count=0
                                              while 'Answer' not in lines[n+count] and written==0:
                                                  if lines[n+count].startswith(ans):
                                                      print(lines[n+count])
                                                      f2.write('\n"'+lines[n+count].rstrip('\n')+ '",')
                                                      
                                                      written=1
                                                      break
                                                  count=count+1
                                                  
                              num=num+1
              
                                                  
          f2.write('],')                    
          searchquery='Good job!'
          searchquery2= 'Well done!'
          for i, line in enumerate(lines):
              if searchquery in line or searchquery2 in line or 'Correct' in line:
                  print('found')
                  ans=line[0]+line[1]
                  print(ans)
                  for i, line in enumerate(lines):
                      if 'Answer' in line:
                          print('wow')
                          count=0
                          while 'eedback' not in lines[i+count]:
                              print('lost')
                              if ans in lines[i+count]:
                                  print('found')
                                  print(lines[i+count])
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
          if Qimg==1:
              for i, line in enumerate(lines):
                  if 'Question:' in line:
                      num=1
                      while 'Answer' not in lines[i+num]:
                          if '![' in lines[i+num]:
                              m = re.search("\/(.*?)\]", lines[i+num])
                              #print(lines[i+num])
                              #print(m.group(1))
                              f2.write('\n$BR\n')
                              print(lines[i+num])
                          num=num+1
                              
              f2.write('\{ image("'+ imgname +'.png" , width=>400, height=>400)\}')#copy image name
          f2.write('\n$BR\n')
          searchquery='# Q'
          for i, line in enumerate(lines):
              if searchquery in line:
                  if answernum>2:
                      skiptxt='# A'
                      count=1
                      skipimg='.png]' #find a way to get image name
                      while skiptxt not in lines[i+count]:
                          if skipimg not in lines[i+count]:
                              f2.write(lines[i+count])
                          count=count+1
                  else:
                      skiptxt='a)'
                      count=1
                      skipimg='.png]' #find a way to get image name
                      while skiptxt not in lines[i+count]:
                          print(lines[i+count])
                          if skipimg not in lines[i+count]:
                              f2.write(lines[i+count])
                          count=count+1                        
                      
          if Answerimg==1:
              for i, line in enumerate(lines):
                  if 'Answer' in line:
                      num=1
                      while 'eedback' not in lines[i+num]:
                          if '![' in lines[i+num]:
                              m = re.search("\/(.*?)\]", lines[i+num])
                              #print(lines[i+num])
                              #print(m.group(1))
                              f2.write('\n$BR\n')
                              f2.write('\{ image("'+ m.group(1) +'" , width=>400, height=>400,tex_size=>700, extra_html_tags=>'+"'alt=")
                              count=1
                              n=i+num
                              print(lines[i+num])
                              while 'Answer' not in lines[n-count]:
                                  print(lines[n-count])
                                  if lines[n-count].strip():
                                      l=lines[n-count]
                                      print(l)
                                      print(i)
                                      print(lines[n-count])
                                      anstext=l[0]+l[1]
                                      print(anstext)
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
      data=data.replace('\cdot','\(\cdot\)')
      x='alpha\\'
      print(x)

      data=data.replace( x , '(alpha\)' )
      o= '(\\\overrightarrow{.}\\\)' 
      #print(o)
      data=sub(o, r'(\1)', data)
      data=data.replace('(\\','\\(\\')
      


  with open(newfile, 'w') as f:
      print('shifting values')
      f.write(data)  
              
              
              
              
def Multipleanswer():
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
                          print('found')
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
                      print(line)
                      num=1
                      while 'Feedback' not in lines[i+num]:
                          if lines[i+num].strip() and '![' not in lines[i+num]:
                              line=lines[i+num]
                              f2.write('"'+line[0]+line[1]+ '",')
                              print(lines[i+num])
                          num=num+1
                      f2.write('],')
                  searchquery='Good job!'
                  searchquery2= 'Well done!'
              for i, line in enumerate(lines):
                  count=0
                  if searchquery in line or searchquery2 in line or 'Correct.' in line:
                      ans=line[0]+line[1]
                      count=count+1
                      print(ans)
                      f2.write('\n"'+ans+ '");')
                  
                          
                          
          else:
              for i, line in enumerate(lines):
                  if 'Answer' in line:
                      print(line)
                      num=1
                      while 'Feedback' not in lines[i+num]:
                          if lines[i+num].strip():
                              f2.write('"'+lines[i+num].rstrip('\n')+ '",')
                              print(lines[i+num])
                          num=num+1
                      f2.write('],')
                  searchquery='Good job!'
                  searchquery2= 'Well done!'
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
                                          print(lines[n+count])
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
                              m = re.search("\/(.*?)\]", lines[i+num])
                              #print(lines[i+num])
                              #print(m.group(1))
                              f2.write('\n$BR\n')
                              f2.write('\{ image("'+ m.group(1) +'" , width=>400, height=>400,tex_size=>700, extra_html_tags=>'+"'alt=")
                              count=1
                              print(lines[i+num])
                          num=num+1
                              
              f2.write('\{ image("'+ imgname +'.png" , width=>400, height=>400)\}')#copy image name
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
                              m = re.search("\/(.*?)\]", lines[i+num])
                              #print(lines[i+num])
                              #print(m.group(1))
                              f2.write('\n$BR\n')
                              f2.write('\{ image("'+ m.group(1) +'" , width=>400, height=>400,tex_size=>700, extra_html_tags=>'+"'alt=")
                              count=1
                              n=i+num
                              print(lines[i+num])
                              while 'Answer' not in lines[n-count]:
                                  print(lines[n-count])
                                  if lines[n-count].strip():
                                      l=lines[n-count]
                                      print(l)
                                      print(i)
                                      print(lines[n-count])
                                      anstext=l[0]+l[1]
                                      print(anstext)
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
      print(x)
      data=data.replace( x , '(alpha\)' )
  
  
  
  with open(newfile, 'w') as f:
      print('shifting values')
      f.write(data)

              
              
              
              
 
                
                
 

os.chdir(r"C:\Users\ptemm\OneDrive\Desktop")
filename=[]
count=1
for file in glob.glob("*.md"):
    print(file)
    count=count+1
    newfile=file.rstrip('.md')+'.pg'

    #os.rename("C:\Users\ptemm\Downloads\Oct 22 Notion Exports\Oct 22 Notion Exports\Numerical Fill in the Blank\Export-6fce60a0-1d5b-4136-b9b3-d3e3dd238e96.zip\+file.png", "path/to/new/destination/for/file.foo")
    #shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
    #os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")    

    #copying comments
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if 'Question Format' in line:
                  if 'Numerical' in line:
                      Numerical()
                  if 'Multiple Choice' in line:
                      count=0
                      for i, line in enumerate(lines):
                            if 'Good job!' in line or 'Well done!' in line or 'Correct.' in line:
                                count=count+1
                      if count>1:
                            Multipleanswer()
                      else:
                            Multiplechoice()
                             
