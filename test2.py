from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import selenium
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def get_teams(**kwargs):
    #countries = {
            #"Italy":"italy",
            #"France":"france",
            #"England":"england",
            #"Denmark": "denmark",
           # "Brasil": "brazil",
           # "Belgium": "belgium",
           # "Germany": "germany",
           # "Chile": "chile",
           # "Portugal": "portugal",
           # "Poland": "poland",
           # "Ireland": "ireland",
           # "Netherlands": "netherlands",
       # }
    for country, no_of_league in kwargs.items(): 
        #print("Python Executable:", sys.executable)

        print('starting with:', country)
        # Set the path to your chromedriver executable
        try:
            width, height = 800, 600
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--pageLoadStrategy=eager")
            chrome_options.add_argument("--disable-network-throttling")
            chrome_options.add_argument(f"--window-size={width},{height}")
            chrome_options.add_argument("--disk-cache-size=1")
            chrome_options.add_argument("--media-cache-size=1")

            # Create a WebDriver instance with the correct argument name
            driver = webdriver.Chrome(options=chrome_options)
            ##print('the driver has connected with chrome')

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
            print('more is going to be clicked')

            # Scroll to the element using JavaScript
            driver.execute_script("arguments[0].scrollIntoView();", element_to_click)
            # Click on the element using JavaScript
            driver.execute_script("arguments[0].click();", element_to_click)
        except Exception as e:
            print('error clicking more: ', e)

        print('url after clicking more: ', driver.current_url)
        
        print('click country ')
        try:
            # Find the element you want to click (for example, a button with id='myButton')
            ##print(country)
            country_selector = f'a[href="/football/{country}/"]'
            ##print(country_selector)
            element_two_to_click = WebDriverWait(driver, 7).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, country_selector))
            )
            # Scroll to the element using JavaScript
            ##print('country_to_click object1',  element_two_to_click)
            driver.execute_script("arguments[0].scrollIntoView();", element_two_to_click)
            # Click on the element using JavaScript
            driver.execute_script("arguments[0].click();", element_two_to_click)
        except TimeoutException as e:
            print('error clicking on the country: ', e)
            

        ##print('url after clicking country: ', driver.current_url)
        

        
        ##print('checking if the league is ready')
        # make sure  the league is ready
        try:
            element_present = WebDriverWait(driver, 7).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.lmc__template'))
            )
            #all the leagues int the chosen country
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')
            leagues_in_the_country = soup.find_all('span', class_="lmc__template")
            #print(leagues_in_the_country)
        except TimeoutException as e:
            print('error checking available list of leagues: ', e)

        league_count = 0
        for league in leagues_in_the_country[:no_of_league]:
            league_count += 1
            league_text = league.find('a').text.strip()
            league_href = league.find('a')['href'].strip()
            ##print('league_href', league_href)
            #league_class = league.find('span')['class']
            print(league_text)
            print('league_count:', league_count)
            #print(league_class)
            #print(league)
            
            if league_count > 1:
                ##print('check if more will be here again')
                try: 
                    more_to_click = WebDriverWait(driver, 7).until(
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
                    country_to_click = WebDriverWait(driver, 7).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, country_selector))
                    )
                    # Scroll to the element using JavaScript
                    ##print('country_to_click object', country_to_click) 
                    driver.execute_script("arguments[0].scrollIntoView();", country_to_click)
                    # Click on the element using JavaScript
                    driver.execute_script("arguments[0].click();", country_to_click)
                except TimeoutException as e:
                    print('error from checking country again: ', e)
                

                # Find the element you want to click (for example, a button with id='myButton')
                ##print('click league')
            else:
                pass

            print('no error so far')
            try:
                league_href = league.find('a')['href'].strip()
                league_selector = f'a[href="{league_href}"]'
                ##print('league_selector', league_selector)
                league_to_click = WebDriverWait(driver, 40).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, league_selector)) 
                )
                # Scroll to the element using JavaScript
                print('league to click', league_to_click)
                driver.execute_script("arguments[0].scrollIntoView();", league_to_click)

                # Click on the element using JavaScript
                driver.execute_script("arguments[0].click();", league_to_click)
            except Exception as e:
                print('error from clicking league : ', e)
            
            print('url after clicking the league: ' , driver.current_url)
            
            # Find the element you want to click (for example, a button with id='myButton')
            ##print('check if standing is there to be clicked')
            try:
                standing_to_click = WebDriverWait(driver, 7).until(
                    EC.element_to_be_clickable((By.ID, "li3"))
                )

                # Scroll to the element using JavaScript
                driver.execute_script("arguments[0].scrollIntoView();", standing_to_click)

                # Click on the element using JavaScript
                driver.execute_script("arguments[0].click();", standing_to_click)
                #print('3rd click')
            except TimeoutException as e:
                print('error from checking standing: ', e)




            ##print('url after clicking the standing: ', driver.current_url)
            ##print('the diver is now on the page')
            try:
                element_present = WebDriverWait(driver, 7).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.ui-table__row'))
                )
                ##print("Element is present!")

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
                                print("top 4 team with last double loss")
                                print(match_data)
                                print('')
                                with open("league_result.txt", "a") as file:
                                    file.write(str(match_data) + '\n')

                            #get total league name and rank at a go for the next search
                            all_ranks_and_names =[]
                            no_of_all_teams = 0
                            for league_rank_and_name in league_teams:
                                no_of_all_teams += 1
                                just_rank = int(league_rank_and_name.find('div', class_='tableCellRank').text.rstrip('.'))
                                just_team_name = league_rank_and_name.find('a', class_="tableCellParticipant__name").text.strip()

                                just_data ={
                                    'just_rank': just_rank,
                                    'just_team_name': just_team_name,
                                }
                                all_ranks_and_names.append(just_data)
                                continue
                            
                            #check top 4 teams with last match loss and playing last top 4 buttom
                            if last_matches[:1] == ['L'] and rank <= 4:
                                #print(match_data0
                                nextmatch_teams = next_match[0]
                                nextmatch_opponent = nextmatch_teams[:-10]   #remove date attached to the teams
                                match_date = nextmatch_teams[-10:]
                                teams = nextmatch_opponent.split('-')
                                print(teams)
                                if team_name == teams[1].strip():
                                    opponent = teams[0].strip()
                                else:
                                    opponent = teams[1].strip()
                                
                                
                                
                                                               
                                #print(all_rank_and_name)
                                #print(no_of_all_teams)
                                
                                #search for opponent rank
                                opponent_rank = 0
                                for all_rank_and_name in all_ranks_and_names:
                                    #print(all_rank_and_name)
                                    if all_rank_and_name['just_team_name'] == opponent:
                                        opponent_rank += all_rank_and_name['just_rank']
                                        break  
                                
                                print('top teams with last loss playing an opponents')
                                print(f"nextmatch: {nextmatch_opponent} --- {match_date}")
                                print(f"team with advantage: {team_name}, rank: {rank}")
                                print(f"opponents: {opponent},  rank: {opponent_rank}")
                                print()
                                
                                #print(opponent_rank)
                                if opponent_rank >= (no_of_all_teams - 5):
                                    print("top team with last loss playing opponenents in the bottom 5")
                                    print(f" {team_name}-{rank} vs {opponent}-{opponent_rank} --- {match_date}")
                                    with open("league_result.txt", "a") as file:
                                        file.write("top teams with last loss playing opponenents in the bottom 5" + "\n" + str(f"{team_name}-{rank} vs {opponent}-{opponent_rank} --- {match_date}") + "\n")
                           

                        league_details = league_country, 'total_league_teams:', total_league_teams
                        print(league_details)
                        print('')
                        print('')
                        with open("league_result.txt", "a") as file:
                            file.write(str(league_details) + '\n' + '\n')

                    except Exception as e:
                        print('error1: ', e)
                        driver.quit()

                else:
                    print("Target div not found.")
                    driver.quit()

            except Exception as e:
                print("error2: ", e)
                driver.quit()

        print('finished')
        print()
        driver.quit()


import sys
def main():
    max_retries = 10
    retries = 0

    if len(sys.argv) < 2:
        print(f"usage: python3 script.py country league_no")
        sys.exit(1)

    else:
        while retries < max_retries:
            args = sys.argv[1:]
            team_dict = {}
            for  item in args:
                country, value= item.split('=')
                team_dict[country] = int(value)
            try:
                get_teams(**team_dict)

                break
            except Exception as e:
                print(f"caught an exception: {e}")
                retries += 1
                print(f"Retrying... ({retries}/{max_retries})")
                time.sleep(2)

        if retries == max_retries:
            print("max retries reach, cant finish")
        else:
            print("operation successfully")

if __name__ == "__main__":
    main()
    


#serbia=2, scotland=2, uruguay=1, mexico=2, japan=2, ireland=2, denmark=2, bahrain=2, finland=2, qatar=2, slovenia=2, croatia=2, france=3, germany=3, iran=2, italy=4, portugal=3, spain=4, turkey=3, england=4, australia=2, albania=2, brazil=3, netherlands=2 
