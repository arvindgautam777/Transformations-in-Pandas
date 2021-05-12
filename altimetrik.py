import pandas as pd
import re
import schedule

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
        return "Not mentioned"
    else:
        if re.match(r'^C.', cabin):
            return 'First Class'
        else:
            return 'Second Class'

def gender(name):
    if re.findall("(Mrs\.|Miss\.)", name):
        return 'Female'
    elif re.findall("Mr\.", name):
        return 'Male'
    else:
        return 'Not Specified'

def transformation():
    df = pd.read_excel(r'MyCruiseData.xlsx')
    df['Last_Name'] = df['Name'].apply(lambda x: x.split(',')[0])
    df['First_Name'] = df['Name'].apply(lambda x: x.split(',')[1].split('(')[0])
    df['Called_as'] = df['Name'].str.extract(r"\((\w.*)\)")
    df['Group'] = df['Age'].apply(check_age)
    df['Class'] = df['Cabin'].apply(class_selection)
    df['Gender'] = df['Name'].apply(gender)
    df.to_csv('TitanicOutput.csv', index = False)  
    print('Process Completed')

if __name__ == '__main__':
    
    schedule.every(30).minutes.do(geeks)
    while True:
        schedule.run_pending()
        time.sleep(1)

