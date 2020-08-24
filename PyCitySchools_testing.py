#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Add the Pandas dependency.
import pandas as pd


# In[2]:


# Files to load
school_data_to_load = "schools_complete.csv"
student_data_to_load = "students_complete.csv"


# In[3]:


# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
school_data_df


# In[4]:


# Determine if there are any missing values in the school data.
school_data_df.count()


# In[6]:


# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)
student_data_df


# In[7]:


# Determine if there are any missing values in the student data.
student_data_df.count()


# In[9]:


# Determine if there are any missing values in the school data.
school_data_df.isnull()


# In[10]:


# Determine if there are any missing values in the student data.
student_data_df.isnull()


# In[11]:


# Determine if there are any missing values in the student data.
student_data_df.isnull().sum()


# In[12]:


# Determine if there are not any missing values in the school data.
school_data_df.notnull()


# In[13]:


# Determine if there are not any missing values in the student data.
student_data_df.notnull().sum()


# In[14]:


# Determine data types for the student DataFrame.
student_data_df.dtypes


# In[15]:


# Put the student names in a list.
student_names = student_data_df["student_name"].tolist()
student_names


# In[16]:


# Split the student name and determine the length of the split name.
for name in student_names:
    print(name.split(), len(name.split()))


# In[17]:


# Create a new list and use it for the for loop to iterate through the list.
students_to_fix = []

# Use an if statement to check the length of the name.
# If the name is greater than or equal to "3", add the name to the list.

for name in student_names:
    if len(name.split()) >= 3:
        students_to_fix.append(name)

# Get the length of the students whose names are greater than or equal to "3".
len(students_to_fix)


# In[18]:


# Add the prefixes less than or equal to 4 to a new list.
prefixes = []
for name in students_to_fix:
    if len(name.split()[0]) <= 4:
        prefixes.append(name.split()[0])

print(prefixes)


# In[19]:


# Add the suffixes less than or equal to 3 to a new list.
suffixes = []
for name in students_to_fix:
    if len(name.split()[-1]) <= 3:
        suffixes.append(name.split()[-1])

print(suffixes)


# In[20]:


# Get the unique items in the "prefixes" list.
set(prefixes)


# In[21]:


# Get the unique items in the "suffixes" list.
set(suffixes)


# In[22]:


# Strip "Mrs." from the student names
for name in students_to_fix:
    print(name.strip("Mrs."))


# In[23]:


# Replace "Dr." with an empty string.
name = "Dr. Linda Santiago"
name.replace("Dr.", "")


# In[24]:


# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]


# In[26]:


# Iterate through the "prefixes_suffixes" list and replace them with an empty space, "" when it appears in the student's name.
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")


# In[27]:


student_data_df


# In[28]:


# Put the cleaned students' names in another list.
student_names = student_data_df["student_name"].tolist()
student_names


# In[29]:


# Create a new list and use it for the for loop to iterate through the list.
students_fixed = []

# Use an if statement to check the length of the name.

# If the name is greater than or equal to 3, add the name to the list.

for name in student_names:
    if len(name.split()) >= 3:
        students_fixed.append(name)

# Get the length of the students' names that are greater than or equal to 3.
len(students_fixed)


# In[30]:


# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]


# In[31]:


# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")


# In[32]:


student_data_df


# In[33]:


# Combine the data into a single dataset.
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()


# In[48]:


# Get the total number of students.
student_count_1 = school_data_complete_df.count()
student_count


# In[49]:


student_count = school_data_complete_df["Student ID"].count()
student_count


# In[35]:


# Calculate the total number of schools.
school_count = school_data_df["school_name"].count()
school_count


# In[36]:


# Calculate the total number of schools
school_count_2 = school_data_complete_df["school_name"].unique()
school_count_2


# In[37]:


# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget


# In[38]:


# Calculate the average reading score.
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# In[39]:


# Calculate the average math score.
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# In[40]:


passing_math = school_data_complete_df["math_score"] >= 70
passing_reading = school_data_complete_df["reading_score"] >= 70


# In[41]:


# Get all the students who are passing math in a new DataFrame.
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math.head()


# In[43]:


# Get all the students that are passing reading in a new DataFrame.
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]
passing_reading.head()


# In[44]:


# Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()
passing_math_count


# In[45]:


# Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()
passing_reading_count


# In[52]:


# Calculate the percent that passed math.
passing_math_percentage = passing_math_count / float(student_count) * 100
passing_math_percentage


# In[53]:


# Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / float(student_count) * 100
passing_reading_percentage


# In[54]:


# Calculate the students who passed both math and reading.
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]

passing_math_reading.head()


# In[55]:


# Calculate the number of students who passed both math and reading.
overall_passing_math_reading_count = passing_math_reading["student_name"].count()
overall_passing_math_reading_count


# In[56]:


# Calculate the overall passing percentage.
overall_passing_percentage = overall_passing_math_reading_count / student_count * 100
overall_passing_percentage


# In[57]:


# Adding a list of values with keys to create a new DataFrame.
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df


# In[58]:


# Define a function that calculates the percentage of students that passed both # math and reading and prints the passing percentage to the output when the
# function is called.
def passing_math_percent(pass_math_count, student_count):
    return pass_math_count / float(student_count) * 100


# In[59]:


# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

district_summary_df["Total Students"]


# In[60]:


# Format "Total Budget" to have the comma for a thousands separator, a decimal separator, and a "$".

district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

district_summary_df["Total Budget"]


# In[61]:


# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)


# In[62]:


district_summary_df


# In[63]:


# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
district_summary_df


# In[64]:


# Determine the school type.
per_school_types = school_data_df.set_index(["school_name"])["type"]
per_school_types


# In[65]:


# Add the per_school_types into a DataFrame for testing.
df = pd.DataFrame(per_school_types)
df


# In[66]:


# Calculate the total student count.
per_school_counts = school_data_df["size"]
per_school_counts


# In[67]:


# Calculate the total student count.
per_school_counts = school_data_df.set_index(["school_name"])["size"]
per_school_counts


# In[68]:


# Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()
per_school_counts


# In[69]:


# Calculate the total school budget.
per_school_budget = school_data_df.set_index(["school_name"])["budget"]
per_school_budget


# In[70]:


# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts
per_school_capita


# In[71]:


# Calculate the math scores.
student_school_math = student_data_df.set_index(["school_name"])["math_score"]


# In[72]:


student_school_math


# In[73]:


# Calculate the average math scores.
per_school_averages = school_data_complete_df.groupby(["school_name"]).mean()
per_school_averages


# In[74]:


# Calculate the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]

per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]


# In[75]:


# Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]

per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]


# In[76]:


# Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]

per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]


# In[77]:


# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100

per_school_passing_reading = per_school_passing_reading / per_school_counts * 100


# In[78]:


# Calculate the students who passed both math and reading.
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]

per_passing_math_reading.head()


# In[79]:


# Calculate the number of students who passed both math and reading.
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]


# In[80]:


# Calculate the overall passing percentage.
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100


# In[81]:


# Adding a list of values with keys to create a new DataFrame.

per_school_summary_df = pd.DataFrame({
             "School Type": per_school_types,
             "Total Students": per_school_counts,
             "Total School Budget": per_school_budget,
             "Per Student Budget": per_school_capita,
             "Average Math Score": per_school_math,
           "Average Reading Score": per_school_reading,
           "% Passing Math": per_school_passing_math,
           "% Passing Reading": per_school_passing_reading,
           "% Overall Passing": per_overall_passing_percentage})
per_school_summary_df.head()


# In[82]:


# Format the Total School Budget and the Per Student Budget columns.
per_school_summary_df["Total School Budget"] = per_school_summary_df["Total School Budget"].map("${:,.2f}".format)

per_school_summary_df["Per Student Budget"] = per_school_summary_df["Per Student Budget"].map("${:,.2f}".format)


# Display the data frame
per_school_summary_df


# In[84]:


# Reorder the columns in the order you want them to appear.
new_column_order = ["School Type", "Total Students", "Total School Budget", "Per Student Budget", "Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]

# Assign district summary df the new column order.
per_school_summary_df = per_school_summary_df[new_column_order]

per_school_summary_df


# In[85]:


# Sort and show top five schools.
top_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=False)

top_schools.head()


# In[86]:


# Sort and show top five schools.
bottom_schools = per_school_summary_df.sort_values(["% Overall Passing"], ascending=True)

bottom_schools.head()


# In[87]:


# Create a grade level DataFrames.
ninth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "9th")]

tenth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "10th")]

eleventh_graders = school_data_complete_df[(school_data_complete_df["grade"] == "11th")]

twelfth_graders = school_data_complete_df[(school_data_complete_df["grade"] == "12th")]


# In[88]:


# Group each school Series by the school name for the average math score.
ninth_grade_math_scores = ninth_graders.groupby(["school_name"]).mean()["math_score"]

tenth_grade_math_scores = tenth_graders.groupby(["school_name"]).mean()["math_score"]

eleventh_grade_math_scores = eleventh_graders.groupby(["school_name"]).mean()["math_score"]

twelfth_grade_math_scores = twelfth_graders.groupby(["school_name"]).mean()["math_score"]


# In[89]:


# Group each school Series by the school name for the average reading score.
ninth_grade_reading_scores = ninth_graders.groupby(["school_name"]).mean()["reading_score"]

tenth_grade_reading_scores = tenth_graders.groupby(["school_name"]).mean()["reading_score"]

eleventh_grade_reading_scores = eleventh_graders.groupby(["school_name"]).mean()["reading_score"]

twelfth_grade_reading_scores = twelfth_graders.groupby(["school_name"]).mean()["reading_score"]


# In[90]:


# Combine each Series for average math scores by school into single DataFrame.
math_scores_by_grade = pd.DataFrame({
               "9th": ninth_grade_math_scores,
               "10th": tenth_grade_math_scores,
               "11th": eleventh_grade_math_scores,
               "12th": twelfth_grade_math_scores})

math_scores_by_grade.head()


# In[91]:


# Combine each Series for average reading scores by school into single DataFrame.
reading_scores_by_grade = pd.DataFrame({
              "9th": ninth_grade_reading_scores,
              "10th": tenth_grade_reading_scores,
              "11th": eleventh_grade_reading_scores,
              "12th": twelfth_grade_reading_scores})

reading_scores_by_grade.head()


# In[92]:


# Format each grade column.
math_scores_by_grade["9th"] = math_scores_by_grade["9th"].map("{:.1f}".format)

math_scores_by_grade["10th"] = math_scores_by_grade["10th"].map("{:.1f}".format)

math_scores_by_grade["11th"] = math_scores_by_grade["11th"].map("{:.1f}".format)

math_scores_by_grade["12th"] = math_scores_by_grade["12th"].map("{:.1f}".format)

# Make sure the columns are in the correct order.
math_scores_by_grade = math_scores_by_grade[
                 ["9th", "10th", "11th", "12th"]]

# Remove the index name.
math_scores_by_grade.index.name = None
# Display the DataFrame.
math_scores_by_grade.head()


# In[97]:


# Format each grade column.
reading_scores_by_grade["9th"] = reading_scores_by_grade["9th"].map("{:,.1f}".format)

reading_scores_by_grade["10th"] = reading_scores_by_grade["10th"].map("{:,.1f}".format)

reading_scores_by_grade["11th"] = reading_scores_by_grade["11th"].map("{:,.1f}".format)

reading_scores_by_grade["12th"] = reading_scores_by_grade["12th"].map("{:,.1f}".format)

# Make sure the columns are in the correct order.
reading_scores_by_grade = reading_scores_by_grade[
                 ["9th", "10th", "11th", "12th"]]

# Remove the index name.
reading_scores_by_grade.index.name = None
# Display the data frame.
reading_scores_by_grade.head()


# In[98]:


# Get the descriptive statistics for the per_school_capita.
per_school_capita.describe()


# In[99]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [585, 615, 645, 675]
pd.cut(per_school_capita, spending_bins)


# In[100]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 615, 645, 675]
per_school_capita.groupby(pd.cut(per_school_capita, spending_bins)).count()


# In[101]:


# Cut the per_school_capita into the spending ranges.
spending_bins = [0, 585, 630, 645, 675]
per_school_capita.groupby(pd.cut(per_school_capita, spending_bins)).count()


# In[102]:


# Establish the spending bins and group names.
spending_bins = [0, 585, 630, 645, 675]
group_names = ["<$584", "$585-629", "$630-644", "$645-675"]


# In[103]:


# Categorize spending based on the bins.
per_school_summary_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, labels=group_names)

per_school_summary_df


# In[104]:


# Calculate averages for the desired columns.
spending_math_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]

spending_reading_scores = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]

spending_passing_math = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]

spending_passing_reading = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]

overall_passing_spending = per_school_summary_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Overall Passing"]


# In[105]:


# Assemble into DataFrame.
spending_summary_df = pd.DataFrame({
          "Average Math Score" : spending_math_scores,
          "Average Reading Score": spending_reading_scores,
          "% Passing Math": spending_passing_math,
          "% Passing Reading": spending_passing_reading,
          "% Overall Passing": overall_passing_spending})

spending_summary_df


# In[106]:


# Formatting
spending_summary_df["Average Math Score"] = spending_summary_df["Average Math Score"].map("{:.1f}".format)

spending_summary_df["Average Reading Score"] = spending_summary_df["Average Reading Score"].map("{:.1f}".format)

spending_summary_df["% Passing Math"] = spending_summary_df["% Passing Math"].map("{:.0f}".format)

spending_summary_df["% Passing Reading"] = spending_summary_df["% Passing Reading"].map("{:.0f}".format)

spending_summary_df["% Overall Passing"] = spending_summary_df["% Overall Passing"].map("{:.0f}".format)

spending_summary_df


# In[107]:


# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[108]:


# Categorize spending based on the bins.
per_school_summary_df["School Size"] = pd.cut(per_school_summary_df["Total Students"], size_bins, labels=group_names)

per_school_summary_df.head()


# In[109]:


# Calculate averages for the desired columns.
size_math_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Math Score"]

size_reading_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Reading Score"]

size_passing_math = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Math"]

size_passing_reading = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Reading"]

size_overall_passing = per_school_summary_df.groupby(["School Size"]).mean()["% Overall Passing"]


# In[110]:


# Assemble into DataFrame.
size_summary_df = pd.DataFrame({
          "Average Math Score" : size_math_scores,
          "Average Reading Score": size_reading_scores,
          "% Passing Math": size_passing_math,
          "% Passing Reading": size_passing_reading,
          "% Overall Passing": size_overall_passing})

size_summary_df


# In[111]:


# Formatting.
size_summary_df["Average Math Score"] = size_summary_df["Average Math Score"].map("{:.1f}".format)

size_summary_df["Average Reading Score"] = size_summary_df["Average Reading Score"].map("{:.1f}".format)

size_summary_df["% Passing Math"] = size_summary_df["% Passing Math"].map("{:.0f}".format)

size_summary_df["% Passing Reading"] = size_summary_df["% Passing Reading"].map("{:.0f}".format)

size_summary_df["% Overall Passing"] = size_summary_df["% Overall Passing"].map("{:.0f}".format)

size_summary_df


# In[112]:


# Calculate averages for the desired columns.
type_math_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Math Score"]

type_reading_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Reading Score"]

type_passing_math = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Math"]

type_passing_reading = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Reading"]

type_overall_passing = per_school_summary_df.groupby(["School Type"]).mean()["% Overall Passing"]


# In[113]:


# Assemble into DataFrame.
type_summary_df = pd.DataFrame({
          "Average Math Score" : type_math_scores,
          "Average Reading Score": type_reading_scores,
          "% Passing Math": type_passing_math,
          "% Passing Reading": type_passing_reading,
          "% Overall Passing": type_overall_passing})

type_summary_df


# In[114]:


# Formatting
type_summary_df["Average Math Score"] = type_summary_df["Average Math Score"].map("{:.1f}".format)

type_summary_df["Average Reading Score"] = type_summary_df["Average Reading Score"].map("{:.1f}".format)

type_summary_df["% Passing Math"] = type_summary_df["% Passing Math"].map("{:.0f}".format)

type_summary_df["% Passing Reading"] = type_summary_df["% Passing Reading"].map("{:.0f}".format)

type_summary_df["% Overall Passing"] = type_summary_df["% Overall Passing"].map("{:.0f}".format)

type_summary_df


# In[ ]:




