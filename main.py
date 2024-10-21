import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

driver = webdriver.Chrome()
driver.get('https://www.nepalstock.com.np/')
time.sleep(10)

def find_company_details(driver, company_name, time_out):
    xpath = f'//a[contains(text(), "{company_name}")]'

    company_button = WebDriverWait(driver, time_out).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    company_button.click()
    time.sleep(10)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[-1])

    company_details = []

    company_meta = driver.find_elements(By.CLASS_NAME, "company__title--metas")
    company_meta1 = company_meta[0]
    company_meta1_div = company_meta1.find_element(By.TAG_NAME, "div")
    company_meta1_li = company_meta1_div.find_elements(By.TAG_NAME, "li")


    company_meta2 = company_meta[1] if len(company_meta) > 1 else None
    company_meta2_li = company_meta2.find_elements(By.TAG_NAME, "li")

    tables = driver.find_elements(By.CLASS_NAME, "table")
    table1 = tables[0]
    table1_tbody = table1.find_element(By.TAG_NAME, "tbody")
    table1_tr = table1_tbody.find_elements(By.TAG_NAME, "tr")

    table1_th_tr1 = table1_tr[0].find_element(By.TAG_NAME, "th")
    table1_tr2_td = table1_tr[1].find_element(By.TAG_NAME, "td")
    table1_tr3_td = table1_tr[2].find_element(By.TAG_NAME, "td")
    table1_tr5_td = table1_tr[4].find_element(By.TAG_NAME, "td")
    table1_tr6_td = table1_tr[5].find_element(By.TAG_NAME, "td")
    table1_tr7_td = table1_tr[6].find_element(By.TAG_NAME, "td")
    table1_tr8_td = table1_tr[7].find_element(By.TAG_NAME, "td")
    table1_tr9_td = table1_tr[8].find_element(By.TAG_NAME, "td")
    table1_tr10_td = table1_tr[9].find_element(By.TAG_NAME, "td")
    table1_tr11_td = table1_tr[10].find_element(By.TAG_NAME, "td")
    table1_tr12_td = table1_tr[11].find_element(By.TAG_NAME, "td")
    table1_tr13_td = table1_tr[12].find_element(By.TAG_NAME, "td")
    table1_tr14_td = table1_tr[13].find_element(By.TAG_NAME, "td")

    company = {
        "company_name" : driver.find_element(By.XPATH, "(//h1)[1]").text,
        "company_email_address" : company_meta1_li[0].find_element(By.TAG_NAME, "strong").text,
        "company_sector": company_meta1_li[1].find_element(By.TAG_NAME, "strong").text,
        "company_permitted_to_trade" : company_meta2_li[0].text,
        "company_status" : company_meta2_li[1].text,
        "date_as_of" : table1_th_tr1.find_element(By.TAG_NAME, "span").text,
        "Instrument_type" : table1_tr2_td.text,
        "Listing_date" : table1_tr3_td.text,
        "Total_traded_Quantity" : table1_tr5_td.text,
        "Total_Trades" : table1_tr6_td.text,
        "Previous_day_close_price" : table1_tr7_td.text,
        "High_price/Low_price" : table1_tr8_td.text,
        "52_week_High/52_week_Low" : table1_tr9_td.text,
        "Open_price" : table1_tr10_td.text,
        "Close_price*" : table1_tr11_td.text,
        "total_listed_shares" : table1_tr12_td.text,
        "total_paidup_value" : table1_tr13_td.text,
        "market_cap" : table1_tr14_td.text,
    }

    company_details.append(company)

    company_tab_div = driver.find_element(By.ID, 'companytabs')
    profile_btn = company_tab_div.find_element(By.ID, 'profileTab')
    profile_btn.click()
    profile_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'profile_section'))
    )
    paragraph_div = profile_section.find_element(By.CLASS_NAME, 'col-sm-4')
    paragraphs = paragraph_div.find_element(By.XPATH, '(//p)[1]')
    profile_text = paragraphs.text if paragraphs else ""
    profile = []

    profile_detail = {
        "profile_text" : profile_text
    }

    profile.append(profile_detail)

    contact_btn = company_tab_div.find_element(By.ID, 'contactTab')
    contact_btn.click()
    contact = []
    contact_section = driver.find_element(By.ID, 'contact')

    contact_ul = WebDriverWait(contact_section, 10).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "ul"))  # Note the tuple
    )

    contact_ul_li = contact_ul[2].find_elements(By.TAG_NAME, "li")

    contact_detail = {
        "address" : contact_ul[0].find_element(By.TAG_NAME, "strong").text,
        "contact_person" : contact_ul[1].find_element(By.TAG_NAME, "strong").text,
        "email_address" : contact_ul_li[0].find_element(By.TAG_NAME, "strong").text,
        "phone_number" : contact_ul_li[1].find_element(By.TAG_NAME, "strong").text,
        "fax_number" : contact_ul_li[2].find_element(By.TAG_NAME, "strong").text if len(contact_ul_li) >= 3 else ""
    }

    contact.append(contact_detail)

    ownership_structure = []

    ownership_btn = company_tab_div.find_element(By.ID, 'ownershipTab')
    ownership_btn.click()
    time.sleep(10)

    ownership_div = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'ownership'))
        )

    ownership_table = ownership_div.find_element(By.TAG_NAME, 'table')
    ownership_table_tbody = ownership_table.find_element(By.TAG_NAME, "tbody")
    ownership_table_tr = ownership_table_tbody.find_elements(By.TAG_NAME, "tr")

    ownership_detail = {
        "Date" : ownership_table_tr[0].find_elements(By.TAG_NAME, "span")[0].text,
        "Promoter_shares" : ownership_table_tr[1].find_element(By.TAG_NAME, "td").text,
        "public_shares" : ownership_table_tr[2].find_element(By.TAG_NAME, "td").text,
        "Total_listed_shares" : ownership_table_tr[3].find_element(By.TAG_NAME, "td").text
    }

    ownership_structure.append(ownership_detail)

    board_of_directors = []

    bof_btn = driver.find_element(By.ID, 'boardOfDirectorTab')
    bof_btn.click()
    time.sleep(10)

    bod_div = driver.find_element(By.ID, 'boardOfDirector')
    member_div = bod_div.find_element(By.CLASS_NAME, 'row')
    members = member_div.find_elements(By.XPATH, "col-sm-4")

    for m in members:
        member = m.find_element(By.CLASS_NAME, "team-member")
        bod_members = {
            "name" : member.find_element(By.TAG_NAME, "h4").text,
            "designation" : member.find_element(By.TAG_NAME, "p").text
        }
        board_of_directors.append(bod_members)

    floor_sheet_btn = driver.find_element(By.ID, 'floorsheet-tab')
    floor_sheet_btn.click()

    time.sleep(10)

    floor_sheet = []

    try:
        floorsheet_div = WebDriverWait(driver, time_out).until(
            EC.presence_of_element_located((By.ID, 'floorsheets'))
        )
        floorsheet_table = floorsheet_div.find_element(By.TAG_NAME, 'table')

        # Scrape the static table info
        floorsheet_info_table = floorsheet_div.find_element(By.CLASS_NAME, 'table__bordertable__border--notbb')
        floorsheet_info_table_tbody = floorsheet_info_table.find_element(By.TAG_NAME, "tbody")
        floorsheet_info_table_tr = floorsheet_info_table_tbody.find_element(By.TAG_NAME, "tr")
        floorsheet_info_table_tds = floorsheet_info_table_tr.find_elements(By.TAG_NAME, "td")

        floorsheet_info = {
            "total_trades": floorsheet_info_table_tds[0].text,
            "total_quantity": floorsheet_info_table_tds[1].text,
            "total_amount": floorsheet_info_table_tds[2].text
        }
        floor_sheet.append(floorsheet_info)

        # Now handle pagination
        pagination_control = WebDriverWait(driver, time_out).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ngx-pagination'))
        )

        # Use a loop for pagination and collecting data
        while True:
            floorsheet_table_tbody = floorsheet_table.find_element(By.TAG_NAME, 'tbody')
            floorsheet_table_trs = floorsheet_table_tbody.find_elements(By.TAG_NAME, "tr")

            for floorsheet_tr in floorsheet_table_trs:
                floorsheet_tr_tds = floorsheet_tr.find_elements(By.TAG_NAME, "td")
                if len(floorsheet_tr_tds) >= 7:
                    floorsheet_details = {
                        "SN": floorsheet_tr_tds[0].text,
                        "Contract-No.": floorsheet_tr_tds[1].text,
                        "Buyer": floorsheet_tr_tds[2].text,
                        "Seller": floorsheet_tr_tds[3].text,
                        "Quantity": floorsheet_tr_tds[4].text,
                        "Rate": floorsheet_tr_tds[5].text,
                        "Amount": floorsheet_tr_tds[6].text,
                    }
                    floor_sheet.append(floorsheet_details)

            # Click the "Next" button if available
            try:
                next_button = WebDriverWait(pagination_control, time_out).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'pagination-next'))
                )
                if "disabled" in next_button.get_attribute("class"):
                    print("No more pages. Ending pagination.")
                    break

                next_button.click()
                WebDriverWait(driver, time_out).until(
                    EC.staleness_of(floorsheet_table_trs[0])  # Ensure the table has refreshed
                )
                time.sleep(1)  # Small delay after clicking

            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException) as e:
                print(f"Pagination ended or interrupted: {e}")
                break

    except TimeoutException:
        print("Timeout: Floorsheet data could not be retrieved.")

    corporate_action = []

    try:
        # Click the corporate actions tab
        corporate_action_btn = WebDriverWait(driver, time_out).until(
            EC.element_to_be_clickable((By.ID, 'corporateActionsTab'))
        )
        corporate_action_btn.click()

        WebDriverWait(driver, time_out).until(
            EC.presence_of_element_located((By.ID, 'companytabcontent'))
        )
        corporate_action_div = driver.find_element(By.ID, 'companytabcontent')
        corporate_action_table = corporate_action_div.find_element(By.TAG_NAME, 'table')

        # Scraping table data
        while True:
            corporate_action_table_tbody = corporate_action_table.find_element(By.TAG_NAME, 'tbody')
            corporate_action_table_trs = corporate_action_table_tbody.find_elements(By.TAG_NAME, 'tr')

            for corporate_action_table_tr in corporate_action_table_trs:
                corporate_action_table_tr_tds = corporate_action_table_tr.find_elements(By.TAG_NAME, "td")
                if len(corporate_action_table_tr_tds) >= 7:
                    corporate_action_details = {
                        "SN": corporate_action_table_tr_tds[0].text,
                        "fiscal_year": corporate_action_table_tr_tds[1].text,
                        "date": corporate_action_table_tr_tds[2].text,
                        "status": corporate_action_table_tr_tds[3].text,
                        "bonus_percentage": corporate_action_table_tr_tds[4].text,
                        "right_percentage": corporate_action_table_tr_tds[5].text,
                        "cash_dividend": corporate_action_table_tr_tds[6].text,
                    }
                    corporate_action.append(corporate_action_details)

            # Click the "Next" button if available
            try:
                next_button = WebDriverWait(driver, time_out).until(
                    EC.element_to_be_clickable((By.XPATH, ".//li/a[normalize-space(text())='Next']"))
                )

                # Check if the "Next" button is disabled
                if "disabled" in next_button.get_attribute("class"):
                    print("No more pages. Ending pagination.")
                    break

                next_button.click()

                # Wait for the next page to load
                WebDriverWait(driver, time_out).until(
                    EC.staleness_of(corporate_action_table_trs[0])
                )
                time.sleep(1)  # Short delay to allow page loading

            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
                print("Pagination ended or interrupted.")
                break

    except TimeoutException:
        print("Timeout: Corporate action data could not be retrieved.")

    company_financials = []

    try:
        # Click the financials tab
        financial_btn = WebDriverWait(driver, time_out).until(
            EC.element_to_be_clickable((By.ID, 'financialsTab'))
        )
        financial_btn.click()

        WebDriverWait(driver, time_out).until(
            EC.presence_of_element_located((By.ID, 'financial'))
        )
        financial_div = driver.find_element(By.ID, 'financial')
        financial_table = financial_div.find_element(By.TAG_NAME, 'table')

        # Scraping the financial table data
        while True:
            financial_table_tbody = financial_table.find_element(By.XPATH, '(//tbody)[1]')
            financial_table_trs = financial_table_tbody.find_elements(By.TAG_NAME, 'tr')

            for financial_table_tr in financial_table_trs:
                financial_table_tr_tds = financial_table_tr.find_elements(By.TAG_NAME, "td")
                if len(financial_table_tr_tds) >= 11:
                    financial_details = {
                        "SN": financial_table_tr_tds[0].text,
                        "fiscal_year": financial_table_tr_tds[1].text,
                        "report_type": financial_table_tr_tds[2].text,
                        "Quater": financial_table_tr_tds[3].text,
                        "net_worth_per_share": financial_table_tr_tds[4].text,
                        "profit_amount": financial_table_tr_tds[5].text,
                        "paid_up_capital": financial_table_tr_tds[6].text,
                        "PE": financial_table_tr_tds[7].text,
                        "EPS": financial_table_tr_tds[8].text,
                        "published_date": financial_table_tr_tds[9].text,
                        "approved_date": financial_table_tr_tds[10].text,
                    }
                    company_financials.append(financial_details)

            # Click the "Next" button if available
            try:
                next_button = WebDriverWait(driver, time_out).until(
                    EC.element_to_be_clickable((By.XPATH, ".//li/a[normalize-space(text())='Next']"))
                )

                # Check if the "Next" button is disabled
                if "disabled" in next_button.get_attribute("class"):
                    print("No more pages. Ending pagination.")
                    break

                next_button.click()

                # Wait for the next page to load
                WebDriverWait(driver, time_out).until(
                    EC.staleness_of(financial_table_trs[0])
                )
                time.sleep(1)  # Short delay to allow page loading

            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
                print("Pagination ended or interrupted.")
                break

    except TimeoutException:
        print("Timeout: Financial data could not be retrieved.")

    company_agm = []

    try:
        # Click the AGM tab
        agm_btn = WebDriverWait(driver, time_out).until(
            EC.element_to_be_clickable((By.ID, 'agmTab'))
        )
        agm_btn.click()

        WebDriverWait(driver, time_out).until(
            EC.presence_of_element_located((By.ID, 'agm'))
        )
        agm_div = driver.find_element(By.ID, 'agm')
        agm_table = agm_div.find_element(By.TAG_NAME, 'table')

        # Scraping the AGM table data
        while True:
            agm_table_tbody = agm_table.find_element(By.TAG_NAME, 'tbody')
            agm_table_trs = agm_table_tbody.find_elements(By.TAG_NAME, 'tr')

            for agm_table_tr in agm_table_trs:
                agm_table_tr_tds = agm_table_tr.find_elements(By.TAG_NAME, "td")
                if len(agm_table_tr_tds) >= 11:
                    agm_details = {
                        "SN": agm_table_tr_tds[0].text,
                        "AGM_type": agm_table_tr_tds[1].text,
                        "AGM_date": agm_table_tr_tds[2].text,
                        "Venue": agm_table_tr_tds[3].text,
                        "Cash_dividend": agm_table_tr_tds[4].text,
                        "bonus_share": agm_table_tr_tds[5].text,
                        "AGM_number": agm_table_tr_tds[6].text,
                        "book_closure_date": agm_table_tr_tds[7].text,
                        "Agenda": agm_table_tr_tds[8].text,
                        "published_date": agm_table_tr_tds[9].text,
                        "approved_date": agm_table_tr_tds[10].text,
                    }
                    company_agm.append(agm_details)

            # Click the "Next" button if available
            try:
                next_button = WebDriverWait(driver, time_out).until(
                    EC.element_to_be_clickable((By.XPATH, ".//li/a[normalize-space(text())='Next']"))
                )

                # Check if the "Next" button is disabled
                if "disabled" in next_button.get_attribute("class"):
                    print("No more pages. Ending pagination.")
                    break

                next_button.click()

                # Wait for the next page to load
                WebDriverWait(driver, time_out).until(
                    EC.staleness_of(agm_table_trs[0])
                )
                time.sleep(1)  # Small delay for page load

            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
                print("Pagination ended or interrupted.")
                break

    except TimeoutException:
        print("Timeout: AGM data could not be retrieved.")

    company_news = []

    try:
        # Click the company news tab
        company_news_btn = WebDriverWait(driver, time_out).until(
            EC.element_to_be_clickable((By.ID, 'corporateNewsTab'))
        )
        company_news_btn.click()

        WebDriverWait(driver, time_out).until(
            EC.presence_of_element_located((By.ID, 'corporateNews'))
        )

        # Scraping the company news table data
        while True:
            company_news_div = driver.find_element(By.ID, 'corporateNews')
            company_news_table = company_news_div.find_element(By.TAG_NAME, 'table')
            company_news_table_tbody = company_news_table.find_element(By.TAG_NAME, 'tbody')
            company_news_table_trs = company_news_table_tbody.find_elements(By.TAG_NAME, 'tr')

            for company_news_table_tr in company_news_table_trs:
                company_news_table_tr_tds = company_news_table_tr.find_elements(By.TAG_NAME, "td")
                if len(company_news_table_tr_tds) >= 5:
                    company_news_details = {
                        "SN": company_news_table_tr_tds[0].text,
                        "news_title": company_news_table_tr_tds[1].text,
                        "news_body": company_news_table_tr_tds[2].text,
                        "published_date": company_news_table_tr_tds[3].text,
                        "approved_date": company_news_table_tr_tds[4].text,
                    }
                    company_news.append(company_news_details)

            # Handle pagination by clicking the "Next" button if it exists
            try:
                next_button = WebDriverWait(driver, time_out).until(
                    EC.element_to_be_clickable((By.XPATH, ".//li/a[normalize-space(text())='Next']"))
                )

                # Check if the "Next" button is disabled
                if "disabled" in next_button.get_attribute("class"):
                    print("No more pages. Ending pagination.")
                    break

                next_button.click()

                # Wait for the next page to load and refresh the table
                WebDriverWait(driver, time_out).until(
                    EC.staleness_of(company_news_table_trs[0])  # Wait for the table to become stale (refresh)
                )
                time.sleep(1)  # Small delay to allow page loading

            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
                print("Pagination ended or interrupted.")
                break

    except TimeoutException:
        print("Timeout: Company news data could not be retrieved.")

    dividend = []

    try:
        # Click the dividend tab
        dividend_btn = WebDriverWait(driver, time_out).until(
            EC.element_to_be_clickable((By.ID, 'dividendTab'))
        )
        dividend_btn.click()

        WebDriverWait(driver, time_out).until(
            EC.presence_of_element_located((By.ID, 'dividend'))
        )
        dividend_div = driver.find_element(By.ID, 'dividend')
        dividend_table = dividend_div.find_element(By.TAG_NAME, 'table')

        # Scraping the dividend table data
        while True:
            dividend_table_tbody = dividend_table.find_element(By.TAG_NAME, 'tbody')
            dividend_table_trs = dividend_table_tbody.find_elements(By.TAG_NAME, 'tr')

            for dividend_table_tr in dividend_table_trs:
                dividend_table_tr_tds = dividend_table_tr.find_elements(By.TAG_NAME, "td")
                if len(dividend_table_tr_tds) >= 7:
                    dividend_details = {
                        "SN": dividend_table_tr_tds[0].text,
                        "fiscal_year": dividend_table_tr_tds[1].text,
                        "cash": dividend_table_tr_tds[2].text,
                        "bonus_share": dividend_table_tr_tds[3].text,
                        "right_share": dividend_table_tr_tds[4].text,
                        "published_date": dividend_table_tr_tds[5].text,
                        "approved_date": dividend_table_tr_tds[6].text,
                    }
                    dividend.append(dividend_details)

            # Pagination handling
            try:
                next_button = WebDriverWait(driver, time_out).until(
                    EC.element_to_be_clickable((By.XPATH, ".//li/a[normalize-space(text())='Next']"))
                )

                # Check if the "Next" button is disabled
                if "disabled" in next_button.get_attribute("class"):
                    print("No more pages. Ending pagination.")
                    break

                next_button.click()
                WebDriverWait(driver, time_out).until(
                    EC.staleness_of(dividend_table_trs[0])
                )
                time.sleep(1)  # Small delay for the page to load

            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
                print("Pagination ended or interrupted.")
                break

    except TimeoutException:
        print("Timeout: Dividend data could not be retrieved.")

    market_depth = []

    try:
        # Click the market depth tab
        market_depth_btn = WebDriverWait(driver, time_out).until(
            EC.element_to_be_clickable((By.ID, 'marketDepthTab'))
        )
        market_depth_btn.click()

        WebDriverWait(driver, time_out).until(
            EC.presence_of_element_located((By.ID, 'marketDepth'))
        )
        market_depth_div = driver.find_element(By.ID, 'marketDepth')
        market_depth_table = market_depth_div.find_element(By.TAG_NAME, 'table')

        # Scraping the market depth table data
        while True:
            market_depth_table_tbody = market_depth_table.find_element(By.TAG_NAME, 'tbody')
            market_depth_table_trs = market_depth_table_tbody.find_elements(By.TAG_NAME, 'tr')

            for market_depth_table_tr in market_depth_table_trs:
                market_depth_table_tr_tds = market_depth_table_tr.find_elements(By.TAG_NAME, "td")
                if len(market_depth_table_tr_tds) >= 6:
                    market_data = {
                        "buy_orders": market_depth_table_tr_tds[0].text,
                        "buy_quantity": market_depth_table_tr_tds[1].text,
                        "buy_price": market_depth_table_tr_tds[2].text,
                        "sell_orders": market_depth_table_tr_tds[3].text,
                        "sell_quantity": market_depth_table_tr_tds[4].text,
                        "sell_price": market_depth_table_tr_tds[5].text,
                    }
                    market_depth.append(market_data)

            # Pagination handling
            try:
                next_button = WebDriverWait(driver, time_out).until(
                    EC.element_to_be_clickable((By.XPATH, ".//li/a[normalize-space(text())='Next']"))
                )

                # Check if the "Next" button is disabled
                if "disabled" in next_button.get_attribute("class"):
                    print("No more pages. Ending pagination.")
                    break

                next_button.click()
                WebDriverWait(driver, time_out).until(
                    EC.staleness_of(market_depth_table_trs[0])
                )
                time.sleep(1)  # Small delay for the page to load

            except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
                print("Pagination ended or interrupted.")
                break

        # Scrape the footer data (if applicable)
        market_depth_table_tfoot = market_depth_table.find_element(By.TAG_NAME, 'tfoot')
        market_depth_table_tfoot_trs = market_depth_table_tfoot.find_elements(By.TAG_NAME, "tr")
        market_depth_table_tfoot_tds = market_depth_table_tfoot_trs[0].find_elements(By.TAG_NAME, "td")

        market_footer_data = {
            "Total buy quantity": market_depth_table_tfoot_tds[1].text,
            "Total sell quantity": market_depth_table_tfoot_tds[3].text,
        }
        market_depth.append(market_footer_data)

    except TimeoutException:
        print("Timeout: Market depth data could not be retrieved.")

    with open('company_details.json', 'w') as json_file:
        json.dump(company_details, json_file, indent=4)

    with open('profile_text.json', 'w') as json_file:
        json.dump(profile_text, json_file, indent=4)

    with open('contact.json', 'w') as json_file:
        json.dump(contact, json_file, indent=4)

    with open('ownership_structure.json', 'w') as json_file:
        json.dump(ownership_structure, json_file, indent=4)

    with open('board_of_directors.json', 'w') as json_file:
        json.dump(board_of_directors, json_file, indent=4)

    with open('floorsheet.json', 'w') as json_file:
        json.dump(floor_sheet, json_file, indent=4)

    with open('corporate_action.json', 'w') as json_file:
        json.dump(corporate_action, json_file, indent=4)

    with open('financials.json', 'w') as json_file:
        json.dump(company_financials, json_file, indent=4)

    with open('company_agm.json', 'w') as json_file:
        json.dump(company_agm, json_file, indent=4)

    with open('company_news.json', 'w') as json_file:
        json.dump(company_news, json_file, indent=4)

    with open('dividend.json', 'w') as json_file:
        json.dump(dividend, json_file, indent=4)

    with open('market_depth.json', 'w') as json_file:
        json.dump(market_depth, json_file, indent=4)


find_company_details(driver, 'CORBL', 10)

driver.quit()