# sourcery skip: switch
import streamlit as st 
import pandas as pd 
import numpy as np 
import joblib

from xgboost import XGBRegressor
#from streamlit_extras.let_it_rain import rain 


r=st.sidebar.radio('Main Menu',['Home','Car Price Prediction'])
#Home Page
if r == 'Home':
    st.title('CARDEKHO - USED CAR PRICE PREDICTION :car:')
    st.subheader("Data has been taken from the Cardekho website and processed for your usage using Machine Learning")
    st.markdown("*you can predict the car price of your preferred model here* :sunglasses:")
    st.image("cardekho_logo.png")
#Second page
elif r== 'Car Price Prediction':
    left_column,right_column=st.columns(2)
    s1=left_column.selectbox("What is the Fuel type of the car?",('Petrol', 'Diesel', 'Electric', 'Cng', 'Lpg'))
    if s1=="Petrol":
        p1=4
    elif s1=="Diesel":
        p1=1
    elif s1=="Electric" :
        p1=2
    elif s1=="Cng":
        p1=0
    elif s1=="Lpg":
        p1=3 
    s2=right_column.selectbox("What is the Body type of the car?",('Minivans', 'SUV', 'Hatchback', 'Sedan', 'MUV', 'Hybrids', 'Coupe','Convertibles', 'Wagon', 'Pickup Trucks'))
    if s2=="Minivans":
        p2=5
    elif s2=="SUV":
        p2=7
    elif s2=="Hatchback" :
        p2=2
    elif s2=="Sedan":
        p2=8
    elif s2=="MUV":
        p2=4  
    elif s2=="Hybrids":
        p2=3
    elif s2=="Coupe":
        p2=1 
    elif s2=="Convertibles":
        p2=0  
    elif s2=="Wagon":
        p2=9  
    elif s2=="Pickup Trucks":
        p2=6  

    s3=left_column.selectbox("What is the transmission type of the car?",('Automatic', 'Manual'))
    if s3=="Automatic":
        p3=0
    elif s3=="Manual":
        p3=1

    p4=right_column.selectbox("How much owners previously owned had the car?",(0,1,2,3,4,5))
    p5=left_column.slider("How many kilometers driven?",0,500000)
    p6=right_column.slider("Which year the car model belongs to",1985,2023)
    s7=left_column.selectbox("Which car model brand you prefer?",('Maruti', 'Nissan', 'Hyundai', 'Honda', 'Mercedes-Benz', 'BMW',
       'Ford', 'Tata', 'Jeep', 'Audi', 'Toyota', 'Mahindra', 'Renault',
       'Chevrolet', 'Volkswagen', 'Datsun', 'Kia', 'Fiat', 'Land Rover',
       'MG', 'Skoda', 'Isuzu', 'Mini', 'Volvo', 'Jaguar', 'Citroen',
       'Mitsubishi', 'Lexus',
       'Porsche', 'Hindustan Motors', 'Opel'))
    if s7=="Maruti":
        p7=20
    elif s7=="Nissan":
        p7=24
    elif s7=="Hyundai":
        p7=1
    elif s7=="Honda":
        p7=9
    elif s7=="Mercedes-Benz":
        p7=21
    elif s7=="BMW":
        p7=1
    elif s7=="Ford":
        p7=6
    elif s7=="Tata":
        p7=29
    elif s7=="Jeep":
        p7=12
    elif s7=="Audi":
        p7=0
    elif s7=="Toyota":
        p7=30
    elif s7=="Mahindra":
        p7=17
    elif s7=="Renault":
        p7=27
    elif s7=="Chevrolet":
        p7=2
    elif s7=="Volkswagen":
        p7=31
    elif s7=="Datsun":
        p7=4
    elif s7=="Kia":
        p7=13
    elif s7=="Fiat":
        p7=5
    elif s7=="Land Rover":
        p7=14
    elif s7=="MG":
        p7=16
    elif s7=="Skoda":
        p7=28
    elif s7=="Isuzu":
        p7=10
    elif s7=="Mini":
        p7=22
    elif s7=="Volvo":
        p7=32
    elif s7=="Jaguar":
        p7=11
    elif s7=="Citroen":
        p7=3
    elif s7=="Mitsubishi":
        p7=23
    elif s7=="Lexus":
        p7=15
    elif s7=="Porsche":
        p7=26
    elif s7=="Hindustan Motors":
        p7=7
    elif s7=="Opel":
        p7=25
        
        
    s8=right_column.selectbox("Which city you belong to?",('Chennai', 'Delhi', 'Jaipur', 'Kolkata', 'Bangalore'))
    if s8=="Chennai":
        p8=1
    elif s8=="Delhi":
        p8=2
    elif s8=="Jaipur":
        p8=3
    elif s8=="Kolkata":
        p8=4
    elif s8=="Bangalore":
        p8=0
    p9=left_column.slider("How much engine displacement you prefer?",6,5000)
    p10=right_column.slider("How much mileage you prefer?",7,35)

    # load the model from disk
    model=joblib.load('car_price_predictor_xg')
    
    data_new=pd.DataFrame({
        'FuelType':p1,	
        'BodyType':p2,	
        'KmsDriven':p5,
        'Transmission':p3,
        'OwnerNo':p4,
        'ModelBrand':p7,
        'ModelYear':p6,
        'Engine':p9,
        'Mileage':p10,
        'City':p8
    },index=[0])
    
    if st.button('Predict'):
        pred = model.predict(data_new)
        st.balloons()
        
        st.success("The estimated used car price is {:.2f} Lakhs".format(pred[0]))
