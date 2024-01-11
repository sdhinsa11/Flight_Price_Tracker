from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


import pandas as pd

import smtplib
from email.message import EmailMessage

import sched


departure_flight_inputs = {'Depature': " YEG",
                           'Arrival': " PHX",
                           'Date': "May 16, 2024"}

return_flight_inpurt = {'Depature': " PHX",
                        'Arrival': " YEG",
                        'Date': "May 21, 2024"}

def find_cheapest_flights(flight_info):
    PATH = r"/Users/sohanadhinsa/Desktop/chromedriver-mac-arm64/chromedriver"
    driver = webdriver.Chrome(executable_path=PATH)

    leaving_from = flight_info['Departure']
    going_to = flight_info['Arrival']
    trip_date = flight_info['Date']


    #Go to Expedia
    driver.get("https://www.expedia.ca")



    


