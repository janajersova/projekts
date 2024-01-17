import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.imdb.com/list/ls089970003/"
driver.get(url)
time.sleep(2)


agree = driver.find_element(By.CLASS_NAME, "icb-btn.sc-bcXHqe.sc-dkrFOg.sc-iBYQkv.dcvrLS.ddtuHe.dRCGjd")
agree.click()
time.sleep(2)

movie_list = []

print("Vai meklējat konkrētu žanru? (jā/nē)")
choice = input()


if choice == "jā":
    selection = driver.find_element(By.CLASS_NAME, "expand")
    selection.click()
    time.sleep(2)

    print("Izvēlieties žanru: ")
    print("Drāma")
    print("Krimināls")
    print("Asa sižeta")
    print("Mistērijas")
    print("Romantikas")
    print("Biogrāfija")
    print("Ģimenes") 
    print("Vēstures")
    print("Sporta")
    print("Film-Noir")
    print("Mūzikls")
    print("Trilleris")
    print("Piedzīvojumu")
    print("Komēdija")
    print("Kara")
    print("Zinātniskās fantastikas")
    print("Fantāzijas")
    print("Animācijas")
    print("Mūzikas")
    print("Rietumu")
    print("Šausmu")
    
    genre = input()

    wait = WebDriverWait(driver, 60)

    if genre == "Drāma":
        drama = driver.find_element(By.NAME, "Drama")
        drama.click()
        time.sleep(2)
    elif genre == "Krimināls":
        crime = driver.find_element(By.NAME, "Crime")
        crime.click()
        time.sleep(2)
    elif genre == "Asa sižeta":
        action = driver.find_element(By.NAME, "Action")
        action.click()
        time.sleep(2)
    elif genre == "Mistērijas":
        mystery = driver.find_element(By.NAME, "Mystery")
        mystery.click()
        time.sleep(2)
    elif genre == "Romantikas":
        romance = driver.find_element(By.NAME, "Romance")
        romance.click()
        time.sleep(2)
    elif genre == "Biogrāfija":
        biography = driver.find_element(By.NAME, "Biography")
        biography.click()
        time.sleep(2)
    elif genre == "Ģimenes":
        family = driver.find_element(By.NAME, "Family")
        family.click()
        time.sleep(2)
    elif genre == "Vēstures":
        history = driver.find_element(By.NAME, "History")
        history.click()
        time.sleep(2)
    elif genre == "Sporta":
        sport = driver.find_element(By.NAME, "Sport")
        sport.click()
        time.sleep(2)
    elif genre == "Film-Noir":
        film_noir = driver.find_element(By.NAME, "Film-Noir")
        film_noir.click()
        time.sleep(2)
    elif genre == "Mūzikls":
        musical = driver.find_element(By.NAME, "Musical")
        musical.click()
        time.sleep(2)
    elif genre == "Trilleris":
        thriller = driver.find_element(By.NAME, "Thriller")
        thriller.click()
        time.sleep(2)
    elif genre == "Piedzīvojumu":
        adventure = driver.find_element(By.NAME, "Adventure")
        adventure.click()
        time.sleep(2)
    elif genre == "Komēdija":
        comedy = driver.find_element(By.NAME, "Comedy")
        comedy.click()
        time.sleep(2)
    elif genre == "Kara":
        war = driver.find_element(By.NAME, "War")
        war.click()
        time.sleep(2)
    elif genre == "Zinātniskās fantastikas":
        sci_fi = driver.find_element(By.NAME, "Sci-Fi")
        sci_fi.click()
        time.sleep(2)
    elif genre == "Fantāzijas":
        fantasy = driver.find_element(By.NAME, "Fantasy")
        fantasy.click()
        time.sleep(2)
    elif genre == "Animācijas":
        animation = driver.find_element(By.NAME, "Animation")
        animation.click()
        time.sleep(2)
    elif genre == "Mūzikas":
        music = driver.find_element(By.NAME, "Music")
        music.click()
        time.sleep(2)
    elif genre == "Rietumu":
        western = driver.find_element(By.NAME, "Western")
        western.click()
        time.sleep(2)
    elif genre == "Šausmu":
        horror = driver.find_element(By.NAME, "Horror")
        horror.click()
        time.sleep(2)
    else:
        print("Tada žanra nav")
    

charts = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "lister-list")))
# tabulā meklē filmas nosaukumu
movies = charts.find_elements(By.CLASS_NAME, "lister-item-header")
for movie in movies:
    movie_list.append(movie.text)
print(movie_list)

# pabeidz darbu ar pirmo saiti
driver.quit()

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

new_url = "https://wheelrandom.com/"
driver.get(new_url)
time.sleep(2)

accept = driver.find_element(By.CLASS_NAME, "fc-button.fc-cta-consent.fc-primary-button")
accept.click()
time.sleep(2)

text_area = driver.find_element(By.CLASS_NAME, "textarea.can-go-dark")
text_area.clear()
for mov in movie_list:
    text_area.send_keys(mov + Keys.ENTER)


while True:
    wait = WebDriverWait(driver, 60)
    # gaida kamēr visi nosaukumi tiks ierakstīti
    run = wait.until(EC.element_to_be_clickable((By.ID, "wheelContainer")))
    run.click()

    time.sleep(15)

    result = driver.find_element(By.CLASS_NAME, "title")
    print("Laiks paskatīties: " + result.text)

    print("Vai filma ir jau redzēta (jā/nē): ")
    answer = input()

    if answer == "nē":
        print("Patīkamu skatīšanos")
        break  
    else:
        print("Tad izdzēsisim šo filmu un mēģinam vēlreiz")
        remove = driver.find_element(By.CLASS_NAME, "button.is-medium.is-info")
        remove.click()
        continue
        # turpina kamēr lietotājs ievadis "nē"
