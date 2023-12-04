from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import selenium
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def get_teams(country):
    print("Python Executable:", sys.executable)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    print('start')
    # Set the path to your chromedriver executable
    england = "lmenu_198"
    france = "lmenu_77"
    try:
        # Create a WebDriver instance with the correct argument name
        driver = webdriver.Chrome(options=chrome_options)
        print('the driver has connected with chrome')

        url = "https://www.livescore.in"
        # Now you can use the driver for your automation tasks
        driver.get(url)
    except TimeoutException as e:
        print('error start: ', e)

    print('the driver has gotten the url')
    
    try:
        # Find the element you want to click (for example, a button with id='myButton')
        element_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".lmc__itemMore"))
        )
        ##print('more is going to be clicked')

        # Scroll to the element using JavaScript
        driver.execute_script("arguments[0].scrollIntoView();", element_to_click)
        # Click on the element using JavaScript
        driver.execute_script("arguments[0].click();", element_to_click)
    except TimeoutException as e:
        print('error clicking more: ', e)

    print('url after clicking more: ', driver.current_url)

    ##print('click country ')
    try:
        # Find the element you want to click (for example, a button with id='myButton')
        element_two_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, france))
        )
        # Scroll to the element using JavaScript
        driver.execute_script("arguments[0].scrollIntoView();", element_two_to_click)
        # Click on the element using JavaScript
        driver.execute_script("arguments[0].click();", element_two_to_click)
    except TimeoutException as e:
        print('error clicking on the country: ', e)
        

    print('url after clicking country: ', driver.current_url)
    

    
    ##print('checking if the league is ready')
    # make sure  the league is ready
    try:
        element_present = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.lmc__template'))
        )
        #all the leagues int the chosen country
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        leagues_in_the_country = soup.find_all('span', class_="lmc__template")
        #print(leagues_in_the_country)
    except TimeoutException as e:
        print('error checking available list of leagues: ', e)

    for league in leagues_in_the_country[:3]:
        #print(league)
        league_text = league.find('a').text.strip()
        #league_class = league.find('span')['class']
        ##print(league_text)
        #print(league_class)
        #print(league)
        
        ##print('check if more will be here again')
        try: 
            more_to_click = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".lmc__itemMore"))
            )
            ##print('more is going to be clicked')
            # Scroll to the element using JavaScript
            driver.execute_script("arguments[0].scrollIntoView();", more_to_click)
            # Click on the element using JavaScript
            driver.execute_script("arguments[0].click();", more_to_click)
        except TimeoutException as e:
            print('error from checking more again: ', e)

        
        ##print('check if country should be clicked again')
        try:
            # Find the element you want to click (for example, a button with id='myButton')
            country_to_click = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, france))
            )
            # Scroll to the element using JavaScript
            driver.execute_script("arguments[0].scrollIntoView();", country_to_click)
            # Click on the element using JavaScript
            driver.execute_script("arguments[0].click();", country_to_click)
        except TimeoutException as e:
            print('error from checking country again: ', e)
        

        # Find the element you want to click (for example, a button with id='myButton')
        ##print('click league')
        
        try:
            print(league_text)
            league_to_click = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, league_text))
            
            )
            # Scroll to the element using JavaScript
            driver.execute_script("arguments[0].scrollIntoView();", league_to_click)

            # Click on the element using JavaScript
            driver.execute_script("arguments[0].click();", league_to_click)
        except TimeoutException as e:
            print('error from clicking league : ', e)
        
        print('url after clicking the league: ' , driver.current_url)
        
        # Find the element you want to click (for example, a button with id='myButton')
        print('check if standing is there to be clicked')
        try:
            standing_to_click = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "li3"))
            )

            # Scroll to the element using JavaScript
            driver.execute_script("arguments[0].scrollIntoView();", standing_to_click)

            # Click on the element using JavaScript
            driver.execute_script("arguments[0].click();", standing_to_click)
            #print('3rd click')
        except TimeoutException as e:
            print('error from checking standing: ', e)




        print('url after clicking the standing: ', driver.current_url)
        ##print('the diver is now on the page')
        try:
            element_present = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-table__row'))
            )
            print("Element is present!")

            page_source = driver.page_source

            soup = BeautifulSoup(page_source, 'lxml')

            league_country = soup.find('h1').text.strip()
            #league_name = soup.find('div', class_="heading__name").text
            league_teams = soup.find_all('div', class_="ui-table__row")
            if league_teams:
                total_league_teams = 0
                try:
                    for league_team in league_teams:
                        total_league_teams += 1
                        rank = int(league_team.find('div', class_='tableCellRank').text.rstrip('.'))
                        team_name = league_team.find('a', class_="tableCellParticipant__name").text.strip()
                        matches_played = league_team.find('span', class_="table__cell--value").text.strip()
                        points = league_team.find('span', class_="table__cell--points") .text.strip()
                        last_matches_div = league_team.find_all('div', class_="tableCellFormIcon")

                        last_matches = []
                        last_played_with = []
                        for last_match in last_matches_div:
                            text_content = last_match.get_text().strip()
                            last_matches.append(text_content)
                            
                            teams_played_with = last_match['title'][16:].replace('\n', '').replace('b]', '').strip()
                            last_played_with.append(teams_played_with)
                        
                        

                        last_matches.pop(0) #remove the value of upcoming match whhich is ?
                        last_5_matches = last_played_with.copy()
                        last_5_matches.pop(0)
                        next_match = last_played_with.copy()
                        next_match[0]
                        #print(rank, team_name, matches_played, points, last_matches, last_played_with)

                        match_data ={
                            'rank': rank,
                            'team_name': team_name,
                            'matches_played': matches_played,
                            'points': points,
                            'last_matches': last_matches,
                            'next_match': next_match,
                            'last_5_matches': last_5_matches
                        }

                        
                        #print(match_data)
                        #print('')

                        if last_matches[:2] == ['L', 'L'] and rank <= 4:
                            print(match_data)
                            print('')


                    
                    print(league_country, 'total_league_teams:', total_league_teams)
                    print('')
                    print('')

                except Exception as e:
                    print('error: ', e)
                    driver.quit()



            else:
                print("Target div not found.")
                driver.quit()

        except Exception as e:
            print("error: ", e)
            driver.quit()



    print('finished')
    driver.quit()


get_teams('test')
