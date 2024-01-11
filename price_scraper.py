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
    PATH = '/Users/sohanadhinsa/Desktop/chromedriver-mac-arm64/chromedriver'
    driver = webdriver.Chrome(executable_path=PATH)

    leaving_from = flight_info['Departure']
    going_to = flight_info['Arrival']
    trip_date = flight_info['Date']



    #Go to Expedia
    driver.get("https://www.expedia.ca")


    # to use selenium when need too use xpath to navigate too a specific place on the website 
    flight_xpath = '//a[@aria-controls="search_form_product_selector_flights"]'
    flight_element= WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, flight_xpath))
        )
    flight_element.click()
    time.sleep(0.2)

    #Click on one-way
    oneway_xpath = '//a[@aria-controls="FlightSearchForm_ONE_WAY"]'
    one_way_element = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, oneway_xpath))
    )
    one_way_element.click()
    time.sleep(0.2)


    # Leaving From 
    leaving_from_xpath = '//button[@aria-label="Leaving from"]'
    leaving_from_element =WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, leaving_from_xpath))
        )
    leaving_from_element.clear
    leaving_from_element.click()
    time.sleep(1)
    leaving_from_element.send_keys(leaving_from)

    time.sleep(1) # need this otherwise its too fast for the browser 
    leaving_from_element.send_keys(Keys.DOWN, Keys.RETURN)


    


