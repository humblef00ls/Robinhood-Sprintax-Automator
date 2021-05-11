from selenium import webdriver
import pandas as pd
import time 

path = "/Users/aparimeya/Documents/Taxman9000/chromedriver"

sec_trades = pd.read_csv('trades_sec.csv')
sec_trades['sell_date'] = sec_trades['sell_date'].astype(str) + '20'
sec_trades['buy_date'] = sec_trades['buy_date'].astype(str) + '20'

cryp_trades = pd.read_csv('trades_cryp.csv')
cryp_trades['sell_date'] = cryp_trades['sell_date'].astype(str) + '20'
cryp_trades['buy_date'] = cryp_trades['buy_date'].astype(str) + '20'

payers_name = 'Robinhood Securities LLC'
payers_name_cryp = 'Robinhood Crypto LLC'
address = '500 Colonial Center Parkway Suite 100'
address_cryp = '85 Willow Road'
city = 'Lake Mary'
city_cryp = 'Menlo Park'
state = 'FL'
state_cryp = 'CA'
zip = '32746'
zip_cryp = '4025'
payers_tin = '38-4019216'
payers_tin_cryp = '46-4364776'
state_tax_widthheld = '0'
fed_tax_widthheld = '0'

# payers_name_el = address_el = city_el = state_el = zip_el = payers_tin_el = state_select_el = state_tax_widthheld_el = None

def openChrome():
    global driver
    driver = webdriver.Chrome(path)
    driver.get("https://www.sprintax.com/ots/lets-talk-money-2020.html")

def setupInfo():
    global payers_name_el
    payers_name_el = driver.find_element_by_xpath('//*[@id="__employer_details_employer_name"]')
    global address_el
    address_el = driver.find_element_by_xpath('//*[@id="__employer_details_employer_address"]')
    global city_el
    city_el = driver.find_element_by_xpath('//*[@id="__employer_details_employer_city"]')
    global state_el
    state_el = driver.find_element_by_xpath('//*[@id="__employer_details_employer_state"]')
    global zip_el
    zip_el = driver.find_element_by_xpath('//*[@id="__employer_details_employer_zip_code"]')
    global payers_tin_el
    payers_tin_el = driver.find_element_by_xpath('//*[@id="payers_federal_id"]')
    global state_select_el
    state_select_el = driver.find_element_by_xpath('//*[@id="statecode"]/option[34]') #hardwired to North Carolina, use element inspect to find your state's exact xpath and copy and paste here
    global state_tax_widthheld_el
    state_tax_widthheld_el = driver.find_element_by_xpath('//*[@id="state_income_tax"]')
    global next_btn 
    next_btn = driver.find_element_by_xpath('//*[@id="footer"]/div[1]/div[3]/a') 

def runInfo(crypto=False):
    state_tax_widthheld_el.send_keys(state_tax_widthheld)
    state_select_el.click()
    if crypto:
        payers_name_el.send_keys(payers_name_cryp)
        address_el.send_keys(address_cryp)
        city_el.send_keys(city_cryp)
        state_el.send_keys(state_cryp)
        zip_el.send_keys(zip_cryp)
        payers_tin_el.send_keys(payers_tin_cryp)
    else:
        payers_name_el.send_keys(payers_name)
        address_el.send_keys(address)
        city_el.send_keys(city)
        state_el.send_keys(state)
        zip_el.send_keys(zip)
        payers_tin_el.send_keys(payers_tin)

def setupTrade():
    global descp_el
    descp_el = driver.find_element_by_xpath('//*[@id="description"]') 
    global buy_date_el
    buy_date_el = driver.find_element_by_xpath('//*[@id="date_of_acquistion"]')
    global sell_date_el
    sell_date_el =  driver.find_element_by_xpath('//*[@id="date_of_sale"]') 
    global proceeds_el
    proceeds_el = driver.find_element_by_xpath('//*[@id="stocks_bonds"]') 
    global cost_el
    cost_el = driver.find_element_by_xpath('//*[@id="costs_other_basic"]') 
    global fed_tax_widthheld_el
    fed_tax_widthheld_el = driver.find_element_by_xpath('//*[@id="federal_income_tax"]') 
    global gross_rep_el
    gross_rep_el = driver.find_element_by_xpath('//*[@id="sim_reported_irs1"]/a') 
    global short_trm_el
    short_trm_el = driver.find_element_by_xpath('//*[@id="sim_gain_or_lost1"]/a') 

def runTrade(index, crypto = False):
    gross_rep_el.click()
    short_trm_el.click()
    fed_tax_widthheld_el.send_keys(fed_tax_widthheld)
    if crypto:
        descp_el.send_keys(str(cryp_trades.iloc[index]['descp']))
        buy_date_el.send_keys(str(cryp_trades.iloc[index]['buy_date']))
        sell_date_el.send_keys(str(cryp_trades.iloc[index]['sell_date']))
        proceeds_el.send_keys(str(cryp_trades.iloc[index]['proceeds']))
        cost_el.send_keys(str(cryp_trades.iloc[index]['cost']))
    else:
        descp_el.send_keys(str(sec_trades.iloc[index]['descp']))
        buy_date_el.send_keys(str(sec_trades.iloc[index]['buy_date']))
        sell_date_el.send_keys(str(sec_trades.iloc[index]['sell_date']))
        proceeds_el.send_keys(str(sec_trades.iloc[index]['proceeds']))
        cost_el.send_keys(str(sec_trades.iloc[index]['cost']))

def execute(index,cryp=False):
    setupInfo()                                          
    runInfo(cryp)
    setupTrade()                                         
    runTrade(index,cryp)

def loop(start, end, cryp=False):
    while start <= end:
        execute(start,cryp)
        start+=1
        next_btn.click()
        time.sleep(5)

