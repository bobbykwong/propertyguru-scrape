# from seleniumwire import webdriver # Import from seleniumwire
# from seleniumwire import undetected_chromedriver.v2 as uc # Import from seleniumwire
from math import floor
from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

import random
import time
import json
import undetected_chromedriver.v2 as uc
chrome_options = ChromeOptions()
chrome_options.set_capability('detach', True)
driver = uc.Chrome(options=chrome_options)


def random_scroll():
    time.sleep(random.randint(0,10))
    document_scroll_height = driver.execute_script("return document.body.scrollHeight")
    random_scroll_height = random.randint(0, document_scroll_height)
    driver.execute_script("window.scrollTo(0, {random_height})".format(random_height = random_scroll_height)) 

def nav_property_page(listing):
    time.sleep(random.randint(0,10))
    driver.execute_script("arguments[0].scrollIntoView(false);", listing) 
    time.sleep(random.randint(0,10))
    listing_page_link = listing.find_element_by_class_name('nav-link')
    listing_page_link.click()
    retrieve_property_info()
    # href = listing_page_link.get_attribute('href')

def retrieve_property_info():
    property_data = {
        "name" : "",
        "price" : "",
        "psf" : "",
        "bedroom" : "",
        "bathroom" : "",
        "floor_area" : "",
        "floor_area_unit" : "",
        "street_address" : "",
        "postal_code" : "",
        "address_locality" : "",
        "address_district" : "",
        "mrt_stations" : "",
        "type" : "",
        "tenure" : "",
        "developer" : "",
        "furnishing" : "",
        "floor_level" : "",
        "currently_tenanted" : "",
        "agent_name" : "",
        "agency_name" : "",
        "agent_license" : "",
        "agent_number" : ""
    }
    
    try:
        name = driver.find_element_by_class_name("listing-detail-header-bar").find_element_by_xpath("//h1[@itemprop='name']").get_attribute('innerHTML')
        print('name: ' + name)
        property_data["name"] = name
    except:
        print('cannot find name')

    try:
        price = driver.find_element_by_class_name("listing-detail-summary-bar-price").find_element_by_xpath("//span[@itemprop='price']").get_attribute("content")
        print('price: ' + price)
        property_data["price"] = price
    except:
        print('cannot find price')
    
    try:
        psf = driver.find_element_by_class_name("psf").find_element_by_class_name("price-value").text
        print('psf: ' + psf)
        property_data["psf"] = psf
    except:
        print('cannot find psf')

    try:
        bedroom = driver.find_element_by_xpath("//span[@itemprop='numberOfRooms']").text
        print('bedroom: ' + bedroom)
        property_data["bedroom"] = bedroom
    except:
        print('cannot find bedroom')
    
    try:
        bathroom = driver.find_element_by_class_name("baths").find_element_by_class_name("element-label").text
        print('bathroom: ' + bathroom)
        property_data["bathroom"] = bathroom
    except:
        print('cannot find bathroom')

    try:
        floor_area = driver.find_element_by_xpath("//div[@itemprop='floorSize']").find_element_by_xpath("//meta[@itemprop='value']").get_attribute("content")
        print('floor_area: ' + floor_area)
        property_data["floor_area"] = floor_area
    except:
        print('cannot find floor area')
    
    try:
        floor_area_unit = driver.find_element_by_xpath("//div[@itemprop='floorSize']").find_element_by_xpath("//meta[@itemprop='unitText']").get_attribute("content")
        print('floor_area_unit: ' + floor_area_unit)
        property_data["floor_area_unit"] = floor_area_unit
    except:
        print('cannot find floor area unit')

    try:
        street_address = driver.find_element_by_class_name("listing-address").find_element_by_xpath("//span[@itemprop='streetAddress']").text
        print('street_address: ' + street_address)
        property_data["street_address"] = street_address
    except:
        print('cannot find street address')

    try:
        postal_code = driver.find_element_by_class_name("listing-address").find_element_by_xpath("//span[@itemprop='postalCode']").text
        print('postal_code: ' + postal_code)
        property_data["postal_code"] = postal_code
    except:
        print('cannot find postal code')
    
    try:
        address_locality = driver.find_element_by_class_name("listing-address").find_element_by_xpath("//span[@itemprop='addressLocality']").text
        print('address_locality: ' + address_locality)
        property_data["address_locality"] = address_locality
    except:
        print('cannot find address locality')

    try:
        address_district = driver.find_element_by_class_name("listing-address").text
        print('address_district: ' + address_district)
        property_data["address_district"] = address_district
    except:
        print('cannot find address district')

    try:
        mrt_stations_list = driver.find_elements_by_class_name("mrt-line")
        mrt_stations = []
        for station in mrt_stations_list:
            mrt_stations.append(station.text)
        print('mrt_stations: ')
        print(mrt_stations)
        property_data["mrt_stations"] = mrt_stations
    except:
        print('cannot find mrt_stations')

    try:
        property_details_list = driver.find_element_by_id("details").find_element_by_class_name("listing-details-primary").find_elements_by_xpath("//div[@itemprop='additionalProperty']")
        print(len(property_details_list))
        for detail in property_details_list:
            # print("addition detail is: " + detail.find_element_by_xpath(".//div[@itemprop='name']").text )
            if detail.find_element_by_xpath(".//div[@itemprop='name']").text == 'Type':
                type = detail.find_element_by_xpath(".//div[@itemprop='value']").text
                print('type: ' + type)
                property_data["type"] = type
            elif detail.find_element_by_xpath(".//div[@itemprop='name']").text == 'Tenure':
                tenure = detail.find_element_by_xpath(".//div[@itemprop='value']").text
                print('tenure: ' + tenure)
                property_data["tenure"] = tenure
            elif detail.find_element_by_xpath(".//div[@itemprop='name']").text == 'Developer':
                developer = detail.find_element_by_xpath(".//div[@itemprop='value']").text
                print('developer: ' + developer)
                property_data["developer"] = developer
            elif detail.find_element_by_xpath(".//div[@itemprop='name']").text == 'Furnishing':
                furnishing = detail.find_element_by_xpath(".//div[@itemprop='value']").text
                print('furnishing: ' + furnishing)
                property_data["furnishing"] = furnishing
            elif detail.find_element_by_xpath(".//div[@itemprop='name']").text == 'Floor Level':
                floor_level = detail.find_element_by_xpath(".//div[@itemprop='value']").text
                print('floor_level: ' + floor_level)
                property_data["floor_level"] = floor_level
            elif detail.find_element_by_xpath(".//div[@itemprop='name']").text == 'Currently Tenanted':
                currently_tenanted = detail.find_element_by_xpath(".//div[@itemprop='value']").text
                print('currently_tenanted: ' + currently_tenanted)
                property_data["currently_tenanted"] = currently_tenanted
    except:
        print('cannot find additional details')

    try:
        agent_name = driver.find_element_by_id("contact-form-side").find_element_by_class_name("agent-details-container").find_element_by_class_name("list-group-item-heading").find_element_by_tag_name("a").text
        print('agent_name: ' + agent_name)
        property_data["agent_name"] = agent_name
    except:
        print('cannot find agent name')

    try:
        agency_name = driver.find_element_by_id("contact-form-side").find_element_by_class_name("agent-contact-details").find_element_by_class_name("agency-name").text
        print('agency_name: ' + agency_name)
        property_data["agency_name"] = agency_name
    except:
        print('cannot find agency name')
    
    try:
        agent_license = driver.find_element_by_id("contact-form-side").find_element_by_class_name("agent-contact-details").find_element_by_class_name("agent-license").text
        print('agent_license: ' + agent_license)
        property_data["agent_license"] = agent_license
    except:
        print('cannot find agent license')
        
    try:
        # driver.find_element_by_id("contact-form-side").find_element_by_class_name("agent-contact-options").find_element_by_class_name("js-agent-phone-number").find_element_by_class_name("agent-phone-number").click()
        agent_contact_submit_button = driver.find_element_by_id("contact-form-side").find_element_by_tag_name("button")
        agent_phone_element = driver.find_element_by_id("contact-form-side").find_element_by_class_name("js-agent-phone-number").find_element_by_class_name("agent-phone-number")
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView(false);", agent_contact_submit_button)
        agent_phone_element.click()

        time.sleep(1)
        phone_number_list = driver.find_element_by_id("contact-form-side").find_element_by_class_name("agent-phone").find_elements_by_css_selector(".agent-phone-number-original")
        agent_number = []
        for number in phone_number_list:
            agent_number.append(number.get_attribute('innerHTML'))
        print('agent_number is ')
        print(agent_number)
        property_data["agent_number"] = agent_number
    except:
        print('cannot find agent number')

    with open('property_guru_data.json', mode='r', encoding='utf-8') as feedsjson:
        feeds = json.load(feedsjson)
    with open('property_guru_data.json', 'w') as outfile:
        feeds.append(property_data)
        json.dump(feeds, outfile)
    
    


with driver:
    i = 1
    while i < 20: 
        driver.get('https://propertyguru.com.sg/property-for-sale/' + str(i))  # known url using cloudflare's "under attack mode"

        listings_count = len(driver.find_element_by_id("listings-container").find_elements_by_class_name("listing-card"))
        for listing_num in range(0, listings_count):
            all_listings = driver.find_element_by_id("listings-container").find_elements_by_class_name("listing-card")
            
            random_scroll()
            nav_property_page(all_listings[listing_num])

            time.sleep(random.randint(0,10))
            driver.back()

        i += 1


# def scrape_data(data_list):
#     # Scrape data through table rows and table elements
#     data_rows = driver.find_elements_by_xpath('//tr')

#     for row_index in range(2, len(data_rows)):
#         data_dict = {}
#         data_row = data_rows[row_index].find_elements_by_xpath('.//td')

#         for data_index in range(len(data_row)):
#             data_dict["{0}".format(data_index)] = data_row[data_index].text

#         data_list.append(data_dict)


# # Create a new instance of the Chrome driver (or Firefox)
# # driver = webdriver.Chrome()
# # driver = webdriver.Chrome('/Users/tl0002axtech/Downloads/chromedriver')

# option = webdriver.ChromeOptions()

# #Removes navigator.webdriver flag

# #For ChromeDriver version 79.0.3945.16 or over
# option.add_argument('--disable-blink-features=AutomationControlled')


# #Open Browser
# driver = webdriver.Chrome(executable_path='/Users/tl0002axtech/Downloads/chromedriver',options=option)

# # Set the interceptor on the driver
# # driver.request_interceptor = interceptor

# # All requests will now use 'some_referer' for the referer
# # driver.get('https://mysite')


# user_agent_list = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"]
# headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

# # Create a request interceptor
# def interceptor(request):
#     # del request.headers['authority']  
#     # request.headers['authority'] = 'www.propertyguru.com.sg' 
    
#     del request.headers['accept']  
#     request.headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' 
    
#     del request.headers['accept-encoding']  
#     request.headers['accept-encoding'] = 'gzip, deflate, br'   
    
#     del request.headers['accept-language']  
#     request.headers['accept-language'] = 'en-GB,en-US;q=0.9,en;q=0.8'   
    
#     del request.headers['Sec-Ch-Ua']  
#     request.headers['Sec-Ch-Ua'] = '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"' 
    
#     del request.headers['Sec-Ch-Ua-Mobile']  
#     request.headers['Sec-Ch-Ua-Mobile'] = '?0' 
    
#     del request.headers['Sec-Fetch-Dest']  
#     request.headers['Sec-Fetch-Dest'] = 'document' 
    
#     del request.headers['sec-fetch-mode']  
#     request.headers['sec-fetch-mode'] = 'navigate' 
    
#     del request.headers['sec-fetch-site']  
#     request.headers['sec-fetch-site'] = 'none' 
    
#     del request.headers['sec-fetch-user']  
#     request.headers['sec-fetch-user'] = '?1' 

#     del request.headers['upgrade-insecure-requests']  
#     request.headers['upgrade-insecure-requests'] = '1' 

#     del request.headers['user-agent']  
#     request.headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36' 
    





# driver.request_interceptor = interceptor

# # driver.get('https://www.google.com')
# driver.get('https://www.propertyguru.com.sg')
# # print(driver.requests)
# for thing in driver.requests:
#     print(thing.headers)

# # all_listings = driver.find_element_by_id("listings-container").find_elements_by_class_name("listing-card")

# # for listing in all_listings:
# #     listing_page_link = listing.find_element_by_class_name('nav-link')
# #     href = listing_page_link.get_attribute('href')
# #     time.sleep(4)
# #     driver.get(href)
# # all_data = []

# # for estate_index in range(len(all_estates)//4 * 3 +2, len(all_estates)):
# #     # select estate and search
# #     time.sleep(2)
# #     estate = driver.find_element_by_id("addToProject_{0}".format(estate_index))
# #     print(estate.text)
# #     estate.click()

# #     searchButton = driver.find_element_by_id("searchForm_0")
# #     searchButton.click()

# #     # sometimes when searching for estate, site will return "missing parameters" instead of the sales transaction table. Might have to repeat the process until the table appears / try refreshing the page.
# #     time.sleep(2)
# #     driver.refresh()

# #     # Scrape data from table
# #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//table')))
# #     scrape_data(all_data)
# #     driver.back()

# # json_data = {"data" : all_data}

# # with open('private_property_3.json', 'w') as outfile:
# #     json.dump(json_data, outfile)