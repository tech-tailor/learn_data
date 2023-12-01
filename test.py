from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import selenium
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

print('the diver has gotten the url')

# Find the element you want to click (for example, a button with id='myButton')
element_to_click = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, ".lmc__itemMore"))
)

# Perform the click action
element_to_click.click()


# Find the element you want to click (for example, a button with id='myButton')
element_two_to_click = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "lmenu_198"))
)
element_two_to_click.click()

# Find the element you want to click (for example, a button with id='myButton')
element_three_to_click = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, ".lmc__templateHref"))
)
element_three_to_click.click()

# Find the element you want to click (for example, a button with id='myButton')
element_four_to_click = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "li3"))
)

element_four_to_click.click()





print('the diver is now on the page')
try:
    element_present = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-table__row'))
    )
    print("Element is present!")

    page_source = driver.page_source


    #div_elements = driver.find_element_by_tag_name("div")
    #for div_element in div_elements:
    #class_attribute = driver.get_attributes("class")
    #print(class_attribute)



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






driver.quit()
