from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from home.models import Task

from pathlib import Path,os
BASE_DIR = Path(__file__).resolve().parent.parent
import pytesseract	

    # adds image processing capabilities
from PIL import Image	

    # converts the text to speech
import pyttsx3		

    #translates into the mentioned language
from googletrans import Translator
# Create your views here.
def home(request):
    context={'success':False}
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        img1=request.POST['img1']
        print(title,desc,img1)
        ins=Task(taskTitle=title,taskDesc=desc,taskImage=img1)
        ins.save()
        context={'success':True}


    return render(request,'index.html',context)
def tasks(request):
    allTasks=Task.objects.all()
    # print(allTasks)
    for item in allTasks:
        print(item.taskImage)
    context={'tasks':allTasks,'count':1} 
    
    	

    # opening an image from the source path
    # img = Image.open(item.taskImage)	
    img = Image.open(os.path.join(BASE_DIR,'Capture.png'))


    # describes image format in the output
    print(img)						
    # path where the tesseract module is installed
    pytesseract.pytesseract.tesseract_cmd ='C:/Python310/Lib/site-packages/Tesseract-OCR/tesseract.exe'
    # converts the image to result and saves it into result variable
    result = pytesseract.image_to_string(img)
    # write text in a text file and save it to source path
    with open('abc.txt',mode ='w') as file:	
        
                    file.write(result)
                    print(result)
                    
   

 
      
    return render(request,'tasks.html',context)  

   