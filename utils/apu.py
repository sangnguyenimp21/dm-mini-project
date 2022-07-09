import streamlit as st
import pandas as pd
import pickle
import utils.helper as helper

def generate_sidebar(path = ''):
    if path == '':
        path = 'sidebar.json'

    user_input_data = []
    data_fields = helper.read_sidebar_fields(path)
    for field in data_fields:
        data_field = data_fields[field]
        type = data_field['type']
        if type == 'text':
            st.text(data_field['value'])
        if type == 'select':
            value = st.sidebar.selectbox(data_field['label'], tuple(data_field['options']))
            user_input_data.append([data_field['field_name'], value , 1])
        if type == 'slider':
            default_value = data_field['default']
            min_value =  data_field['min']
            max_value = data_field['max']
            if default_value < min_value or default_value > max_value:
                default_value = min_value
            value = st.sidebar.slider(data_field['label'], min_value, max_value, default_value)
            user_input_data.append([data_field['field_name'], value , 0])
    
    return user_input_data

def apply_data_input(input_list):
    df = init_input_dataframe()
    for input in input_list:
        input_name = input[0]
        input_value =  input[1]
        is_category = input[2]

        if is_category:
            field = input_name + '_' + input_value
            df[field] = 1
        else:
            df[input_name] = input_value
    return df

def load_model(path = ''):
    if path == '':
        path = './models/default/decision_tree.pkl'
    return pickle.load(open(path, 'rb'))
    

def init_input_dataframe():
    details = {
        'age': [33], 
        'duration': [0], 
        'campaign': [0], 
        'pdays': [0], 
        'previous': [0], 
        'emp.var.rate': [0],
        'cons.price.idx': [0], 
        'cons.conf.idx': [0], 
        'euribor3m': [0], 
        'nr.employed': [0],
        'job_admin.': [0], 
        'job_blue-collar': [0], 
        'job_entrepreneur': [0], 
        'job_housemaid': [0],
        'job_management': [0], 
        'job_retired': [0], 
        'job_self-employed': [0], 
        'job_services': [0],
        'job_student': [0], 
        'job_technician': [0], 
        'job_unemployed': [0], 
        'job_unknown': [0],
        'marital_divorced': [0], 
        'marital_married': [0], 
        'marital_single': [0],
        'marital_unknown': [0], 
        'education_basic.4y': [0], 
        'education_basic.6y': [0],
        'education_basic.9y': [0], 
        'education_high.school': [0],
        'education_professional.course': [0], 
        'education_university.degree': [0],
        'education_unknown': [0], 
        'default_no': [0], 
        'default_unknown': [0], 
        'default_yes': [0],
        'housing_no': [0], 
        'housing_unknown': [0], 
        'housing_yes': [0], 
        'loan_no': [0],
        'loan_unknown': [0], 
        'loan_yes': [0], 
        'contact_cellular': [0], 
        'contact_telephone': [0],
        'month_apr': [0], 
        'month_aug': [0], 
        'month_dec': [0], 
        'month_jul': [0], 
        'month_jun': [0],
        'month_mar': [0], 
        'month_may': [0], 
        'month_nov': [0], 
        'month_oct': [0], 
        'month_sep': [0],
        'day_of_week_fri': [0], 
        'day_of_week_mon': [0], 
        'day_of_week_thu': [0],
        'day_of_week_tue': [0], 
        'day_of_week_wed': [0], 
        'poutcome_failure': [0],
        'poutcome_nonexistent': [0], 
        'poutcome_success': [0]
    }
  
    df = pd.DataFrame(details)

    return df