from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.scrapethissite.com/pages/forms/")

time.sleep(5)

teams = driver.find_elements(By.CLASS_NAME, "team")
data = []
for team in teams:
    time.sleep(3)
    team_names = driver.find_elements(By.CLASS_NAME, "name")
    years = driver.find_elements(By.CLASS_NAME, "year")
    wins = driver.find_elements(By.CLASS_NAME, "wins")
    losses = driver.find_elements(By.CLASS_NAME, "losses")
    goalfor = driver.find_elements(By.CLASS_NAME, "gf")
    for team_name, year, win, loss, goal in zip(team_names, years, wins, losses, goalfor):
        data.append([team_name.text, year.text, win.text, loss.text, goal.text])
        

driver.quit()

with open ('sports_compilation.csv', 'w', newline="")as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Team name', 'year', 'win', 'losses', 'goal for'])
    writer.writerows(data)

print('data written to csv...')