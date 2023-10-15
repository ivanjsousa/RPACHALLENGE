import pyautogui as pg
import time

pg.PAUSE = 0.3
pg.FAILSAFE = True


pg.alert(text="Vamos começar os cadastros!", title="Alerta do Robô", button="Ok")


pg.click(pg.locateCenterOnScreen("img\\start.png", confidence=0.7))
time.sleep(3)



def main():
    with open("dados\\challenge.CSV") as f:
        for line in f:
            line = line.strip()
            line = line.split(";")

            firt_name = line[0]
            last_name = line[1]
            company = line[2]
            role_company = line[3]
            address = line[4]
            email = line[5]
            phone = line[6]

            print("Preenchendo com: ", line)


            pg.click(pg.locateCenterOnScreen("img\\first_name.png", confidence=0.9))
            pg.write(firt_name, interval=0.1)
            time.sleep(0.3)
            
            pg.click(pg.locateCenterOnScreen("img\\last_name.png", confidence=0.8, grayscale=True))
            pg.write(last_name, interval=0.1)
            
            pg.click(pg.locateCenterOnScreen("img\\name_company.png", confidence=0.8))
            pg.write(company, interval=0.1)
            time.sleep(0.3)
            
            pg.click(pg.locateCenterOnScreen("img\\role_company.png", confidence=0.8))
            pg.write(role_company, interval=0.1)
            time.sleep(0.3)
            
            pg.click(pg.locateCenterOnScreen("img\\address.png", confidence=0.8))
            pg.write(address, interval=0.1)
            time.sleep(0.3)
            
            pg.click(pg.locateCenterOnScreen("img\\email.png", confidence=0.8))
            pg.write(email, interval=0.1)
            time.sleep(0.3)
            
            pg.click(pg.locateCenterOnScreen("img\\phone.png", confidence=0.8))
            pg.write(phone, interval=0.1)
            time.sleep(0.3)
            
            pg.click(pg.locateCenterOnScreen("img\\submit.png", confidence=0.7))   
            

if __name__ == '__main__':

    main()
    pg.alert(text="Cadastros finalizados com sucesso!", title="Alerta do Sistema", button="Ok")
