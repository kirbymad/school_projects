
points = 0 #I Put 0 as a starting point. Every one regardless their acccessibility need,class year and student status will start with 0)
#check for accessibility needs

accessibility_needs = str(input ("Do you have accessibility needs? Answer with yes or no:"))  #If they answer yes they will get 100 points)
if accessibility_needs == "yes" :           #(I put "Yes" as a string here)
   points += 100


#check for class year 
class_year = int(input("Enter your class year(1,2,3 or 4):"))
 #I tried to make the process easier but putting integers instead of strings such as- Freshman, Senior etc.)
if   class_year == 4:            #Increment points by 40 points
   points += 50
elif class_year == 3:            # Increment points by 40 points
   points += 40
elif class_year == 2:            # Increment points by 30 points
   points += 30
elif class_year == 1:            #Increment points by 20 points
   points += 20


#check for international students status
international = str(input("Are you an international student? Answer with yes or no:")) #International students will answer with a string
if international == "yes":
   points += 10                        #Increment points by 10 point 
else:
 print("your points are :", points)    #Increment points by 0 point  
                            

#In the console we will get the points each students get for their answers.
#Based on that people with the highest mark will get the first choice to pick a dorm.




