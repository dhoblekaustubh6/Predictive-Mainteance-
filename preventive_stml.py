import streamlit as st 
import numpy as np
import pickle 

st.title("Industrial Equipment Health Monitoring System")
st.markdown("To check whether a component is likely to **fail or not** ," \
"Please enter the component details below.")
st.sidebar.subheader("Ensuring mechanical health through intelligent failure prediction")
st.sidebar.title("Predictive Asset Reliability Dashboard")
st.sidebar.markdown("This predictive maintenance system evaluates the condition of each mechanical component and identifies potential failure risks." 
"Provide component data for diagnostics and reliability assessment.")

# load model 
model=pickle.load(open("C:/Users/HP/Downloads/preventive_model (1).pkl","rb"))

# user Input 
with st.container():
    col1,col2,col3=st.columns(3)

    with col1:
        Component_Id = st.number_input("component_id")
        Maintenance_Count=st.number_input("maintenance_count",min_value=0)
        Operating_hours=st.number_input("operating_hours")
        Temperature=st.number_input("temperature_C",min_value=20)
        Energy_Used=st.number_input("energy_consumption_kWh",min_value=10)
        Ambient_temp=st.number_input("ambient_temp_C",min_value=20)
        
    with col2:
        Component_Name=st.selectbox("component_name",["Bearing (0)","Compressor (1)","Gearbox (2)","Motor (3)","Pump (4)"])
        RPM=st.number_input("rpm")
        Vibration=st.number_input("vibration_mm_s")
        Load=st.number_input("load_percentage",min_value=20)
        Noise_Load=st.number_input("noise_level_db",min_value=50)
        Humidity=st.number_input("humidity_percent",min_value=20)
    
    with col3:
        Last_Maintenance=st.number_input("last_maintenance_days")
        Lubrication_Quality=st.number_input("oil_quality_index")
        Pressure_Bar=st.number_input("pressure_bar",min_value=1)
        Torque=st.number_input("torque_Nm",min_value=10)
        Efficiency=st.number_input("machine_efficiency",min_value=0.0)
        Maintenance_risk=st.number_input("maintenance_risk",min_value=0)
    
# input prepare

input_data = np.array([[Component_Id, Maintenance_Count, Last_Maintenance, Operating_hours,
                        Temperature, Energy_Used, RPM, Vibration, Load, Noise_Load,
                        Lubrication_Quality, Pressure_Bar, Torque, Efficiency,Humidity,Maintenance_risk,Ambient_temp,
                        int(Component_Name[-2])]]).reshape(1, -1)


# Button
if st.button("Predict Failure"):
    prediction = model.predict(input_data)
    print("Prediction:", prediction)

    if prediction[0] == 1:
        st.error(" Maintenance required — Failure risk is HIGH if ignored.")
    else:
        st.success(" No immediate maintenance required — Failure risk is LOW.")

    st.info(" We appreciate your time.")
    st.success("Thank you for using the system.")

else:
    st.info("Click the button to predict the failure.")
