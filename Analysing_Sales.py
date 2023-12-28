import csv
import matplotlib.pyplot as plt

# Specify the path to your CSV file
file_path = 'SalesForCourse_quizz_table.csv'

# Create an empty list to store dictionaries
data_list = []

# Open the CSV file
with open(file_path, 'r') as file:
    # Create a CSV reader object with a dictionary reader
    csv_reader = csv.DictReader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append each row (dictionary) to the list
        data_list.append(row)


#Data_list is an array of dictionaries

# Now, data_list contains a list of dictionaries representing each row in the CSV file
# You can access and manipulate the data as needed
#for data in data_list:
#    print(data.get('Year'))


#**************************************
##Printing specifics from dictionaries
#row1=data_list[0] #row1 is a dictionary
#printing the month
#print (row1.get('Month'))
#***************************************

#was checking year how year is saved in the dictionaries
#row1=data_list[0] #row1 is a dictionary
#printing the month
#year=row1.get('Year')
#yearfl=float(year)
#print (yearfl)
#print (type(yearfl))


#$ Sorting the data---> into years*******************************************
Twenty16=[]
Twenty15=[]

for data in data_list:
    year=data.get('Year')
    #print (year)
    if year=='2016.0':
        #print("2016 Data")
        #print(data)

        Twenty16.append(data)
    elif year=='2015.0':
         Twenty15.append(data)
    else:
        #print (data)
        continue

#for data in Twenty16:
#     print (data)
    
#****************************************************************************


#$ Analysing and getting what is being bought

##Arrays to store product categories
categories=[]
categoryCount=[]
categoriesPure=[]
accessories=[]


cat=''
currentCat=''

for data in Twenty16:
    currentCatt=data.get('Product Category')
    categoriesPure.append(currentCatt)

#loop to add different categories
for data in Twenty16:
    currentCat=data.get('Product Category')
    #print("CurrentCat: ",currentCat)
    #print("cat:",cat)
    if cat!=currentCat:
        #print("Here")
        if (categories.__contains__(currentCat)):
            continue
        else: 
            categories.append(currentCat)
    else:
         continue
    cat=data.get('Product Category')

print("Printing categories")
print(categories)


#loop to count the number of times an entry exists
count=0
i=0
for catgry in categories:
    for data in Twenty16:
        currentCat=data.get('Product Category')
        if catgry==currentCat:
            count=count+1
        else:
            continue
    categoryCount.append(count)
        

print(categoryCount)
plt.hist(categoriesPure)
#***************************************************


#$Histogram of Accessories**************************

for data in Twenty16:
    currentCat=data.get('Product Category')
    #print("CurrentCat: ",currentCat)
    #print("cat:",cat)
    if currentCat=='Accessories':
        accessories.append(data.get('Sub Category'))
    else:
        continue

#****************************************************