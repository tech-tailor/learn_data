from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import selenium
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

print("Python Executable:", sys.executable)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

print('start')
# Set the path to your chromedriver executable

# Create a WebDriver instance with the correct argument name
driver = webdriver.Chrome(options=chrome_options)
print('the driver has connected with chrome')

url = "https://www.livescore.in"
# Now you can use the driver for your automation tasks
driver.get(url)

print('the driver has gotten the url')


for i in range(10):
    # Find the element you want to click (for example, a button with id='myButton')
    element_to_click = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".lmc__itemMore"))
    )

    print('it is going to be clicked')
    # Scroll to the element using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", element_to_click)

    # Click on the element using JavaScript
    driver.execute_script("arguments[0].click();", element_to_click)


    # Find the element you want to click (for example, a button with id='myButton')
    element_two_to_click = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "lmenu_198"))
    )

    # Scroll to the element using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", element_two_to_click)

    # Click on the element using JavaScript
    driver.execute_script("arguments[0].click();", element_two_to_click)

    # make sure  the league is ready
    element_present = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.lmc__template'))
    )
    print('Akin')
    '''
    #all the leagues int the chosen country
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    leagues_in_the_country = soup.find_all('span', class_="lmc__template")
    #print(leagues_in_the_country)
    for league in leagues_in_the_country:
    #print(league)
    league_text = league.find('a').text
    league_class = league.find('span')['class']
    print(league_text)
    print(league_class)
    #print(league)
    '''

    # Find the element you want to click (for example, a button with id='myButton')
    try:
        element_three_to_click = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".lmc__templateHref"))
        
        )
        # Scroll to the element using JavaScript
        driver.execute_script("arguments[0].scrollIntoView();", element_three_to_click)

        # Click on the element using JavaScript
        driver.execute_script("arguments[0].click();", element_three_to_click)
        #print('2nd click')
    except Exception:
        pass

    # Find the element you want to click (for example, a button with id='myButton')
    element_four_to_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "li3"))
    )

    # Scroll to the element using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", element_four_to_click)

    # Click on the element using JavaScript
    driver.execute_script("arguments[0].click();", element_four_to_click)
    #print('3rd click')





    print('the diver is now on the page')
    try:
        element_present = WebDriverWait(driver, 30).until(
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
            

            except Exception as e:
                print('error: ', e)



        else:
            print("Target div not found.")

    except Exception as e:
        print("error: ", e)



print('finished')
driver.quit()
