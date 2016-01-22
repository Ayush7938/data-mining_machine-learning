#Digit Recognition of hand written digits, by taking the input as different values of pixels of digits from 0-9 from 
#the training data set of 42000 cases in the form of csv file. Then applying the machine learning decision tree algorithm 
#on the test data set to predict the digits.



import csv
from sklearn import tree

def digitRecognition():
    print ("Start")

    f= open("train.csv","r")
    lines= f.readlines()

    labels=[]
    pixels=[]
    count = 0
    for i in range(len(lines)):
        
        
        if count>0:
            line=map(int,lines[i].split(","))            
            #map(int, line)
            #print (line)
            labels.append(line[0])
            
            del line[0]
            pixels.append(line)
            
            if count==(len(lines)-1):
                break
        count= count+1
        #print (pixels)
  
    #print(labels)
    #print(pixels)
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(pixels, labels)
    #print(clf)
    #print(clf.predict(pixels[0]))
    #print("label value:",labels[0])
    
    
    
    f2= open("test.csv","r")
    lines2= f2.readlines()
    testpx=[]
    cnt=0    
    for i in range(len(lines2)):
        
        if cnt>0:        
            line2=map(int,lines2[i].split(","))
        
            testpx.append(line2)
        cnt=cnt+1
        
        if cnt==(len(lines2)):
            break

    #print(testpx)
    x=clf.predict(testpx)
    print(x)
    print(x[0])
    
    f3= open("submission.txt","w")
     
    f3.write("ImageId,Label")
    f3.write("\n")
    count=1    
    for i in range(len(x)):
        temp= str(count)+","+str(x[i])        
              
        f3.write(temp)
        f3.write("\n")
        count=count+1
        
   
    f.close()
    f2.close()
    f3.close()
    
    
