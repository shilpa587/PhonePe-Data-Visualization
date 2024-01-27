#Required libraries for the program
import streamlit as st 
import mysql.connector
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import altair as alt

#******************************

#Establish connection to MYSQL:
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Shilpapraj234",
)
mycursor = mydb.cursor()
mycursor.execute("USE PhonePe")

#******************************

# MySql to DataFrame
Aggregated_Transaction_DF = pd.read_sql("Select * from Aggregated_Transaction",mydb)
Aggregated_User_DF = pd.read_sql("Select * from Aggregated_User",mydb)
Map_Transaction_DF = pd.read_sql("Select * from Map_Transaction",mydb)
Map_User_DF = pd.read_sql("Select * from Map_User",mydb)
Top_Transaction_DF = pd.read_sql("Select * from Top_Transaction",mydb)
Top_User_DF = pd.read_sql("Select * from Top_User",mydb)

#******************************
# Page configuration
st.set_page_config(
    page_title="PhonePd Dashboard",
    page_icon=":large_purple_square:",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#******************************

# Sidebar
with st.sidebar:
    st.title(':large_purple_square: PhonePd Dashboard')
    
    year_list = list(Aggregated_Transaction_DF.Year.unique())[::-1]
    Quarter_list=list(Aggregated_Transaction_DF['Quarter'].unique())[::-1]
    
    selected_year = st.selectbox('Select a year', year_list)
    selected_quarter= st.selectbox('Select a Quarter', Quarter_list)

    Aggregated_Transaction_DF_selected_year = Aggregated_Transaction_DF[(Aggregated_Transaction_DF.Year == selected_year) & (Aggregated_Transaction_DF.Quarter == selected_quarter)]
    Aggregated_Transaction_DF_selected_year_sorted = Aggregated_Transaction_DF_selected_year.sort_values(by="Transaction_amount", ascending=False)

    Aggregated_User_DF_selected_year = Aggregated_User_DF[(Aggregated_User_DF.Year == selected_year) & (Aggregated_User_DF.Quarter==selected_quarter)]
    Aggregated_User_DF_selected_year_sorted = Aggregated_User_DF_selected_year.sort_values(by="Registered_User_count", ascending=False)
    
    Map_Transaction_DF_selected_year = Map_Transaction_DF[(Map_Transaction_DF.Year == selected_year) & (Map_Transaction_DF.Quarter == selected_quarter)]
    Map_Transaction_DF_selected_year_sorted = Map_Transaction_DF_selected_year.sort_values(by="Area_Transaction_amount", ascending=False)

    Map_User_DF_selected_year = Map_User_DF[(Map_User_DF.Year == selected_year) & (Map_User_DF.Quarter==selected_quarter)]
    Map_User_DF_selected_year_sorted = Map_User_DF_selected_year.sort_values(by="Area_Registered_User_count", ascending=False)

    Top_Transaction_DF_selected_year = Top_Transaction_DF[(Top_Transaction_DF.Year == selected_year) & (Top_Transaction_DF.Quarter == selected_quarter)]
    Top_Transaction_DF_selected_year_sorted = Top_Transaction_DF_selected_year.sort_values(by="Top_Area_Transaction_amount", ascending=False)
    
    Top_User_DF_selected_year = Top_User_DF[(Top_User_DF.Year == selected_year) & (Top_User_DF.Quarter==selected_quarter)]
    Top_User_DF_selected_year_sorted = Top_User_DF_selected_year.sort_values(by="Top_Area_Registered_User_count", ascending=False)

#******************************
    
# Choropleth map Function
def make_choropleth(input_df, input_id, input_column):
    fig = px.choropleth(input_df,                               
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations=input_id, 
                        color=input_column, 
                        color_continuous_scale='blues',
                        #range_color=(0, input_df[input_column].max()),
                        scope='asia'
                        )
    fig.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        margin=dict(l=0, r=0, t=0, b=0),
        height=350
    )
    return fig.update_geos(fitbounds="locations", visible=True)

#******************************

# Pie Chart Function
def MakePie(input_df,Value,Name,hover,Title):
    fig = px.pie(
        input_df, 
        title=Title,
        values=Value,
        names=Name,
        color_discrete_sequence=px.colors.sequential.Blues[::-1],
        hover_data=hover,
        labels={hover:hover}
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig,use_container_width=True)

#******************************
#Bar Chart Function
    
def MakeBar(input_df,Value,Name,hover,Title):    
    fig = px.bar(
                input_df,
                title=Title,
                x=Name,
                y=Value,
                orientation='v',
                color=hover,
                color_continuous_scale=px.colors.sequential.Blues
            )
    st.plotly_chart(fig,use_container_width=True)
    
#******************************
#To match the statenames in the dataframes to Choropleth geojason State names, create state names dataframe to feed into dataframes

all_states = [
    'Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal pradesh', 'Assam',
    'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra & Nagar Haveli & Daman & Diu', 
    'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 
    'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 
    'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
    'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 
    'Uttarakhand', 'West Bengal'
    ]
states = pd.DataFrame(all_states)

#******************************

# Dashboard Main Panel

selected_Data = st.selectbox('Select Data',['Select ', 'Aggregated', 'Map','Top'])
selected_Analysis=st.selectbox('Select Type Of Analysis',['Select ', 'Transaction Analysis', 'User Analysis'])

#Aggregated
if selected_Data== 'Aggregated':
    df1=Aggregated_Transaction_DF_selected_year.groupby('State').agg({'Transaction_count':'sum','Transaction_amount':'sum'})
    df1=df1.reset_index()
    df1sorted=df1.sort_values(by='State',ascending=True)
    df1sorted.State=states #We can safely replace the state column with required format of state names since all our data frames have 36 states in same order
    
    df2=Aggregated_User_DF_selected_year.groupby('State')['Registered_User_count'].sum()
    df2=df2.reset_index()
    df2sorted=df2.sort_values(by='State',ascending=True)
    df2sorted.State=states

    df3=Aggregated_User_DF_selected_year.groupby('Device_Brand')['Registered_User_count'].sum()
    df3=df3.reset_index()
    df3sorted=df3.sort_values(by='Registered_User_count',ascending=False)

    col1,col2= st.columns(2)

    if selected_Analysis=='Transaction Analysis':
        choropleth1 = make_choropleth(df1sorted, 'State', 'Transaction_amount')

        with col1:
            st.plotly_chart(choropleth1, use_container_width=True)
            MakeBar(df1sorted,'Transaction_count','State','Transaction_amount','State-Wise Transaction Counts')
        with col2:
            MakePie(df1sorted,'Transaction_amount','State','Transaction_count','State-wise breakdown of Total Transaction Amount ')
            st.dataframe(df1.sort_values(by='Transaction_amount',ascending=False),hide_index=True)

    elif selected_Analysis=='User Analysis':
        choropleth2= make_choropleth(df2sorted, 'State', 'Registered_User_count')

        with col1:
            st.plotly_chart(choropleth2, use_container_width=True)
            MakePie(df3sorted,'Registered_User_count','Device_Brand','Registered_User_count','DeviceBrand-wise breakdown of Total Registered User')
        with col2:
            MakePie(df2sorted,'Registered_User_count','State','Registered_User_count','State-wise breakdown of Total Registered User')
            cola,colb= st.columns(2)

            with cola:
                st.dataframe(df3.sort_values(by='Registered_User_count',ascending=False),hide_index=True, height=300,width=300)      
            with colb:         
                st.dataframe(df2.sort_values(by='Registered_User_count',ascending=False),hide_index=True, height=300,width=300)

#Map            
elif selected_Data== 'Map':
    selected_state=st.selectbox('Select State',Map_Transaction_DF.State.unique())
    Map_Transaction_DF_selected_year_selected_state=Map_Transaction_DF_selected_year[Map_Transaction_DF_selected_year.State==selected_state]
    df1=Map_Transaction_DF_selected_year_selected_state.groupby('District_Name').agg({'Area_Transaction_count':'sum','Area_Transaction_amount':'sum'})
    df1=df1.reset_index()

    Map_User_DF_selected_year_selected_state=Map_User_DF_selected_year[Map_User_DF_selected_year.State==selected_state]
    df2=Map_User_DF_selected_year_selected_state.groupby('District_Name').agg({'Area_Registered_User_count':'sum','Area_app_opens':'sum'})
    df2=df2.reset_index()

    col1,col2= st.columns(2)

    if selected_Analysis=='Transaction Analysis':
        with col1:
            MakePie(df1,'Area_Transaction_amount','District_Name','Area_Transaction_count','District-wise breakdown of Total Transaction Amount')        
            MakeBar(df1,'Area_Transaction_count','District_Name','Area_Transaction_amount','District-Wise Transaction Counts')
        with col2:
            st.dataframe(df1.sort_values(by='Area_Transaction_amount',ascending=False),hide_index=True,width=500)

    elif selected_Analysis=='User Analysis':
        with col1:
            MakePie(df2,'Area_Registered_User_count','District_Name','Area_app_opens','District-Wise breakdown of Total Registered User')        
            MakeBar(df2,'Area_app_opens','District_Name','Area_Registered_User_count','District-Wise App Open Count')
        with col2:
            st.dataframe(df2.sort_values(by='Area_Registered_User_count',ascending=False),hide_index=True,width=500)
            st.dataframe(df2.sort_values(by='Area_app_opens',ascending=False),hide_index=True,width=500)

#Top
elif selected_Data== 'Top':
    replacement_dict = {'SOUTH ANDAMANS': 'south andaman', 'NORTH AND MIDDLE ANDAMAN': 'north and middle andaman','NICOBARS': 'nicobars','CHANDIGARH':'chandigarh'} #Top data is treating few districts names as case sensitive. They need to be cleaned and considered as same to avoid data descrepency
    Top_Transaction_DF_selected_year['Top_District_Name']=Top_Transaction_DF_selected_year['Top_District_Name'].replace(replacement_dict)
    Top_User_DF_selected_year['Top_District_Name']=Top_User_DF_selected_year['Top_District_Name'].replace(replacement_dict)

    selected_state=st.selectbox('Select State',Top_Transaction_DF.State.unique())

    Top_Transaction_DF_selected_year_selected_state=Top_Transaction_DF_selected_year[Top_Transaction_DF_selected_year.State==selected_state]
    df1=Top_Transaction_DF_selected_year_selected_state.groupby('Top_District_Name').agg({'Top_Area_Transaction_count':'sum','Top_Area_Transaction_amount':'sum'})
    df1=df1.reset_index()

    Top_User_DF_selected_year_selected_state=Top_User_DF_selected_year[Top_User_DF_selected_year.State==selected_state]
    df2=Top_User_DF_selected_year_selected_state.groupby('Top_District_Name')['Top_Area_Registered_User_count'].sum()
    df2=df2.reset_index()

    col1,col2= st.columns(2)

    if selected_Analysis=='Transaction Analysis':
        with col1:
            MakePie(df1,'Top_Area_Transaction_amount','Top_District_Name','Top_Area_Transaction_count','District-Wise breakdown of Total Transaction Amount')        
            MakeBar(df1,'Top_Area_Transaction_count','Top_District_Name','Top_Area_Transaction_count','District-Wise Total Transaction Count')
        with col2:
            st.dataframe(df1.sort_values(by='Top_Area_Transaction_amount',ascending=False),hide_index=True,width=500)
            st.dataframe(df1.sort_values(by='Top_Area_Transaction_count',ascending=False),hide_index=True,width=500)

    elif selected_Analysis=='User Analysis':
        with col1:
            MakePie(df2,'Top_Area_Registered_User_count','Top_District_Name','Top_Area_Registered_User_count','District-Wise breakdown of Total User Count')        
            MakeBar(df2,'Top_Area_Registered_User_count','Top_District_Name','Top_Area_Registered_User_count','District-Wise Total User Count Chart')
        with col2:
            st.dataframe(df2.sort_values(by='Top_Area_Registered_User_count',ascending=False),hide_index=True,width=500)

#*************************************************************************************************************************************************************************************************