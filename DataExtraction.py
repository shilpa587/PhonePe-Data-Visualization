
#git clone https://github.com/PhonePe/pulse.git

#Once created the clone of GIT-HUB repository then,


#******************************

#Required libraries for the program
import pandas as pd
import numpy as np
import json
import os
import mysql.connector

#******************************

#direct the path to get the Aggregated Trasaction Data for all states

AT_path="pulse/data/aggregated/transaction/country/india/state/"
agg_trans_state_list=os.listdir(AT_path)

#Extract the AT data to create a dataframe

AT_columns={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for state in agg_trans_state_list:
    states_path=AT_path+state+"/"
    agg_yr=os.listdir(states_path)
    for year in agg_yr:
        year_path=states_path+year+"/"
        agg_yr_list=os.listdir(year_path)
        for file in agg_yr_list:
            final_file=year_path+file
            Data=open(final_file,'r')#json file level
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              AT_columns['Transaction_type'].append(Name)
              AT_columns['Transaction_count'].append(count)
              AT_columns['Transaction_amount'].append(amount)
              AT_columns['State'].append(state)
              AT_columns['Year'].append(year)
              AT_columns['Quarter'].append(int(file.strip('.json')))
agg_Trans=pd.DataFrame(AT_columns)

#******************************

#direct the path to get the Aggregated User Data for all states
AU_path="pulse/data/aggregated/user/country/india/state/"
agg_User_state_list=os.listdir(AU_path)

#Extract the AU data to create a dataframe

AU_columns={'State':[], 'Year':[],'Quarter':[],'Device_Brand':[], 'Registered_User_count':[], 'Brand_Percentage_Share':[]}
for state in agg_User_state_list:
    states_path=AU_path+state+"/"
    agg_yr=os.listdir(states_path)
    for year in agg_yr:
        year_path=states_path+year+"/"
        agg_yr_list=os.listdir(year_path)
        for file in agg_yr_list:
            final_file=year_path+file
            Data=open(final_file,'r')#json file level
            A=json.load(Data)
            if A['data']['usersByDevice']:
                for z in A['data']['usersByDevice']:
                    name=z['brand']
                    count=z['count']
                    perc=z['percentage']
                    AU_columns['Device_Brand'].append(name)
                    AU_columns['Registered_User_count'].append(count)
                    AU_columns['Brand_Percentage_Share'].append(perc)
                    AU_columns['State'].append(state)
                    AU_columns['Year'].append(year)
                    AU_columns['Quarter'].append(int(file.strip('.json')))  
agg_users=pd.DataFrame(AU_columns)

#******************************

#direct the path to get the Map Transaction Data for all states
MT_path="pulse/data/map/transaction/hover/country/india/state/"
map_trans_state_list=os.listdir(MT_path)

#Extract the MT data to create a dataframe

MT_columns={'State':[], 'Year':[],'Quarter':[],'District_Name':[], 'Area_Transaction_count':[], 'Area_Transaction_amount':[]}
for state in map_trans_state_list:
    states_path=MT_path+state+"/"
    map_yr=os.listdir(states_path)
    for year in map_yr:
        year_path=states_path+year+"/"
        map_yr_list=os.listdir(year_path)
        for file in map_yr_list:
            final_file=year_path+file
            Data=open(final_file,'r')#json file level
            D=json.load(Data)
            for z in D['data']['hoverDataList']:
              Name=z['name']
              count=z['metric'][0]['count']
              amount=z['metric'][0]['amount']
              MT_columns['District_Name'].append(Name)
              MT_columns['Area_Transaction_count'].append(count)
              MT_columns['Area_Transaction_amount'].append(amount)
              MT_columns['State'].append(state)
              MT_columns['Year'].append(year)
              MT_columns['Quarter'].append(int(file.strip('.json')))
map_Trans=pd.DataFrame(MT_columns)

#******************************

#direct the path to get the Map User Data for all states
MU_path="pulse/data/map/user/hover/country/india/state/"
map_User_state_list=os.listdir(MU_path)

#Extract the MU data to create a dataframe

MU_columns={'State':[], 'Year':[],'Quarter':[],'District_Name':[], 'Area_Registered_User_count':[], 'Area_app_opens':[]}
for state in map_User_state_list:
    states_path=MU_path+state+"/"
    map_yr=os.listdir(states_path)
    for year in map_yr:
        year_path=states_path+year+"/"
        map_yr_list=os.listdir(year_path)
        for file in map_yr_list:
            final_file=year_path+file
            Data=open(final_file,'r')#json file level
            A=json.load(Data)
            for z in A['data']['hoverData'].items():
                name=z[0]
                count=z[1]['registeredUsers']
                app_open=z[1]['appOpens']
                MU_columns['District_Name'].append(name)
                MU_columns['Area_Registered_User_count'].append(count)
                MU_columns['Area_app_opens'].append(app_open)
                MU_columns['State'].append(state)
                MU_columns['Year'].append(year)
                MU_columns['Quarter'].append(int(file.strip('.json'))) 
map_users=pd.DataFrame(MU_columns)


#******************************
#TOP Transaction data has PINCODE wise data and DISTRICT wise data

#******************************
#direct the path to get the Top Trasaction District wise Data for all states

TTD_path="pulse/data/top/transaction/country/india/state/"
top_trans_dist_state_list=os.listdir(TTD_path)

#Extract the TTD data to create a dataframe

TTD_columns={'State':[], 'Year':[],'Quarter':[],'Top_District_Name':[],'Top_Area_Transaction_count':[], 'Top_Area_Transaction_amount':[]}
for state in top_trans_dist_state_list:
    states_path=TTD_path+state+"/"
    top_yr=os.listdir(states_path)
    for year in top_yr:
        year_path=states_path+year+"/"
        top_yr_list=os.listdir(year_path)
        for file in top_yr_list:
            final_file=year_path+file
            Data=open(final_file,'r')#json file level
            D=json.load(Data)
            for z in D['data']['districts']:
              Name=z['entityName']
              count=z['metric']['count']
              amount=z['metric']['amount']
              TTD_columns['Top_District_Name'].append(Name)
              TTD_columns['Top_Area_Transaction_count'].append(count)
              TTD_columns['Top_Area_Transaction_amount'].append(amount)
              TTD_columns['State'].append(state)
              TTD_columns['Year'].append(year)
              TTD_columns['Quarter'].append(int(file.strip('.json')))
top_Trans_dist=pd.DataFrame(TTD_columns)


#******************************
#direct the path to get the Top Trasaction Pincodewise Data for all states

TTP_path="pulse/data/top/transaction/country/india/state/"
top_trans_pin_state_list=os.listdir(TTP_path)

#Extract the Top Transaction PINCODE wise data to create a dataframe

TTP_columns={'State':[], 'Year':[],'Quarter':[],'Top_pincode_Name':[],'District':[],'Top_Area_Transaction_count':[], 'Top_Area_Transaction_amount':[]}
for state in top_trans_pin_state_list:
    states_path=TTP_path+state+"/"
    top_yr=os.listdir(states_path)
    for year in top_yr:
        year_path=states_path+year+"/"
        top_yr_list=os.listdir(year_path)
        for file in top_yr_list:
            final_file=year_path+file
            Data=open(final_file,'r')#json file level
            D=json.load(Data)
            for z in D['data']['pincodes']:
              Name=z['entityName']
              count=z['metric']['count']
              amount=z['metric']['amount']
              TTP_columns['Top_pincode_Name'].append(Name)
              TTP_columns['District'].append(np.nan) #Create a null district column
              TTP_columns['Top_Area_Transaction_count'].append(count)
              TTP_columns['Top_Area_Transaction_amount'].append(amount)
              TTP_columns['State'].append(state)
              TTP_columns['Year'].append(year)
              TTP_columns['Quarter'].append(int(file.strip('.json')))
top_Trans_pin=pd.DataFrame(TTP_columns)

#******************************

#CONVERTING PINCODES to DISTRICT to maintain uniform data

file=pd.read_csv("pincodes.csv")
df=pd.DataFrame(file)
print(df)

#Maintain same data type before we merge the dataframes:

df['Top_pincode_Name']=df['Top_pincode_Name'].astype('string')
top_Trans_pin['Top_pincode_Name']=top_Trans_pin['Top_pincode_Name'].astype('string')


top_Trans_pin_merged_df = pd.merge(top_Trans_pin, df, on='Top_pincode_Name', how='left')
print(top_Trans_pin_merged_df.info())
print(top_Trans_pin_merged_df[top_Trans_pin_merged_df['District Name'].isnull()])#2 NaNs observed in DISTRICT Name column from LADAK state 
top_Trans_pin_merged_df['District Name'].fillna('KARGIL',inplace=True) #NaNs are replaced with one of LADAK DISTRICT "KARGIL"

top_Trans_pin_new=top_Trans_pin_merged_df.drop(['District','Top_pincode_Name'], axis=1) #We no longer need the old District column and Pincode column
#top_Trans_pin_new is the final dataframe where PINCODES converted to DISTRICT

#******************************

#TOP User data has PINCODE wise data and DISTRICT wise data

#******************************

#direct the path to get the Top User District wise Data for all states
TUD_path="pulse/data/top/user/country/india/state/"
top_user_dist_state_list=os.listdir(TUD_path)

#Extract the TUD data to create a dataframe

TUD_columns={'State':[], 'Year':[],'Quarter':[],'Top_District_Name':[],'Top_Area_Registered_User_count':[]}
for state in top_user_dist_state_list:
    states_path=TUD_path+state+"/"
    top_yr=os.listdir(states_path)
    for year in top_yr:
        year_path=states_path+year+"/"
        top_yr_list=os.listdir(year_path)
        for file in top_yr_list:
            final_file=year_path+file
            Data=open(final_file,'r')#json file level
            D=json.load(Data)
            for z in D['data']['districts']:
              Name=z['name']
              count=z['registeredUsers']
              TUD_columns['Top_District_Name'].append(Name)
              TUD_columns['Top_Area_Registered_User_count'].append(count)
              TUD_columns['State'].append(state)
              TUD_columns['Year'].append(year)
              TUD_columns['Quarter'].append(int(file.strip('.json')))
top_users_dist=pd.DataFrame(TUD_columns)


#******************************

#direct the path to get the Top Users Pincodewise Data for all states
TUP_path="pulse/data/top/user/country/india/state/"
top_user_pin_state_list=os.listdir(TUP_path)

#Extract the TUP data to create a dataframe

TUP_columns={'State':[], 'Year':[],'Quarter':[],'Top_pincode_Name':[],'District':[],'Top_Area_Registered_User_count':[]}
for state in top_user_pin_state_list:
    states_path=TUP_path+state+"/"
    top_yr=os.listdir(states_path)
    for year in top_yr:
        year_path=states_path+year+"/"
        top_yr_list=os.listdir(year_path)
        for file in top_yr_list:
            final_file=year_path+file
            Data=open(final_file,'r')#json file level
            D=json.load(Data)
            for z in D['data']['pincodes']:
              Name=z['name']
              count=z['registeredUsers']
              TUP_columns['Top_pincode_Name'].append(Name)
              TUP_columns['District'].append(np.nan)
              TUP_columns['Top_Area_Registered_User_count'].append(count)
              TUP_columns['State'].append(state)
              TUP_columns['Year'].append(year)
              TUP_columns['Quarter'].append(int(file.strip('.json')))
top_users_pin=pd.DataFrame(TUP_columns)


#******************************
#CONVERTING PINCODES to DISTRICT to maintain uniform data
#Maintain same data type before we merge the dataframes:

df['Top_pincode_Name']=df['Top_pincode_Name'].astype('string')
top_users_pin['Top_pincode_Name']=top_users_pin['Top_pincode_Name'].astype('string')


top_users_pin_merged_df = pd.merge(top_users_pin, df, on='Top_pincode_Name', how='left')
print(top_Trans_pin_merged_df.info())
print(top_Trans_pin_merged_df[top_Trans_pin_merged_df['District Name'].isnull()])#No NaNs observed in DISTRICT Name column

top_users_pin_new=top_users_pin_merged_df.drop(['District','Top_pincode_Name'], axis=1) #We no longer need the old District column and Pincode column

#top_users_pin_new is the final dataframe where PINCODES converted to DISTRICT

#******************************

#Establish connection to MYSQL:
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Shilpapraj234"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Phonepe")
mycursor.execute("USE Phonepe")
mycursor.execute('''
CREATE TABLE IF NOT EXISTS Aggregated_Transaction(
State varchar(255), 
Year int, 
Quarter int, 
Transaction_type varchar(255), 
Transaction_count int, 
Transaction_amount double)''')
for index,row in agg_Trans.iterrows():
    mycursor.execute("INSERT INTO Aggregated_Transaction(State,Year,Quarter,Transaction_type,Transaction_count,Transaction_amount)VALUES(%s,%s,%s,%s,%s,%s)", tuple(row))

mycursor.execute('''
CREATE TABLE IF NOT EXISTS Aggregated_User(
State varchar(255), 
Year int, 
Quarter int, 
Device_Brand varchar(255), 
Registered_User_count int, 
Brand_Percentage_Share float)''')
for index,row in agg_users.iterrows():
    mycursor.execute("INSERT INTO Aggregated_User(State,Year,Quarter,Device_Brand,Registered_User_count,Brand_Percentage_Share)VALUES(%s,%s,%s,%s,%s,%s)", tuple(row))

mycursor.execute('''
CREATE TABLE IF NOT EXISTS Map_Transaction(
State varchar(255), 
Year int, 
Quarter int, 
District_Name varchar(255), 
Area_Transaction_count int, 
Area_Transaction_amount double)''')
for index,row in map_Trans.iterrows():
    mycursor.execute("INSERT INTO Map_Transaction(State,Year,Quarter,District_Name,Area_Transaction_count,Area_Transaction_amount)VALUES(%s,%s,%s,%s,%s,%s)", tuple(row))

mycursor.execute('''
CREATE TABLE IF NOT EXISTS Map_User(
State varchar(255), 
Year int, 
Quarter int, 
District_Name varchar(255), 
Area_Registered_User_count int, 
Area_app_opens int)''')
for index,row in map_users.iterrows():
    mycursor.execute("INSERT INTO Map_User(State,Year,Quarter,District_Name,Area_Registered_User_count,Area_app_opens)VALUES(%s,%s,%s,%s,%s,%s)", tuple(row))

mycursor.execute('''
CREATE TABLE IF NOT EXISTS Top_Transaction(
State varchar(255), 
Year int, 
Quarter int, 
Top_District_Name varchar(255), 
Top_Area_Transaction_count int, 
Top_Area_Transaction_amount double)''')
for index,row in top_Trans_dist.iterrows():
    mycursor.execute("INSERT INTO Top_Transaction(State,Year,Quarter,Top_District_Name,Top_Area_Transaction_count,Top_Area_Transaction_amount)VALUES(%s,%s,%s,%s,%s,%s)", tuple(row))
for index,row in top_Trans_pin_new.iterrows():
    mycursor.execute("INSERT INTO Top_Transaction(State,Year,Quarter,Top_Area_Transaction_count,Top_Area_Transaction_amount,Top_District_Name)VALUES(%s,%s,%s,%s,%s,%s)", tuple(row))


mycursor.execute('''
CREATE TABLE IF NOT EXISTS Top_User(
State varchar(255), 
Year int, 
Quarter int, 
Top_District_Name varchar(255), 
Top_Area_Registered_User_count int)''')
for index,row in top_users_dist.iterrows():
    mycursor.execute("INSERT INTO Top_User(State,Year,Quarter,Top_District_Name,Top_Area_Registered_User_count)VALUES(%s,%s,%s,%s,%s)", tuple(row))
for index,row in top_users_pin_new.iterrows():
    mycursor.execute("INSERT INTO Top_User(State,Year,Quarter,Top_Area_Registered_User_count,Top_District_Name)VALUES(%s,%s,%s,%s,%s)", tuple(row))


mycursor.execute("show tables")
print(mycursor.fetchall())
print("Tables created in database sucessfully")
mycursor.execute("commit;")

#*******************************************************************************************************************************************************************
