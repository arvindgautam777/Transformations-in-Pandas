
def check_age(age):
    if pd.isna(age):
        return "Couldn't determine the age group"
    else:
        if int(age) in range(0, 18):
            return 'kids'
        elif int(age) in range(18, 60):
            return 'Adults'
        elif age >= 60:
            return 'Elders'
        
        
def class_selection(cabin):
    if pd.isna(cabin):
        return "Second Class"
    else:
        if re.match(r'^C.', cabin):
            return 'First Class'
        else:
            return 'Second Class'

def gender(na):
    if re.findall("(Mrs\.|Miss\.)", na):
        return 'Female'
    elif re.findall("Mr\.", na):
        return 'Male'
    else:
        return 'Not Specified'

df = pd.read_excel(r'MyCruiseData.xlsx')
df['Last_Name'] = df['Name'].apply(lambda x: x.split(',')[0])
df['First_Name'] = df['Name'].apply(lambda x: x.split(',')[1].split('(')[0])
df['Called_as'] = df['Name'].str.extract(r"\((\w.*)\)")
df['Group'] = df['Age'].apply(check_age)
df['Class'] = df['Cabin'].apply(class_selection)
df['Gender'] = df['Name'].apply(gender)
df.to_csv('TitanicOutput.csv', index = False)    