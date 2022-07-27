import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

def login(user, senha):
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    pyautogui.press("tab", presses=16)
    pyautogui.press("enter")
    pyperclip.copy("https://segespais.caedufjf.net/seges/login.faces")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write(user)
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)

def chose_semestre(s):
    if s == '1.0':
        pyautogui.press("tab")
    elif s == '1.1':
        pyautogui.press("tab", presses=2)
    elif s == '2.0':
        pyautogui.press("tab", presses=3)
    elif s == '2.1':
        pyautogui.press("tab", presses=4)
    elif s == '3.0':
        pyautogui.press("tab", presses=5)
    elif s == '3.1':
        pyautogui.press("tab", presses=6)
    else:
        print("ERROR: semestre errado")
    pyautogui.press("enter")

def assina_falta(list_faltas):
    list_alunos= ['1','2','3','4','5','6','7','8','9','10',
        '11','12','13','14','15','16','17','18','19','20',
        '21','22','23','24','25','26','27','28','29','30',
        '31','32','33','34','35','36']
    
    for aluno in list_alunos:
        if aluno in list_faltas:
            pyautogui.press("enter")
        pyautogui.press("tab")

def convert_to_list(string):
    li = list(string.split(" "))
    return li

def main():
    user = "11496012720"
    senha = "Eze2022@"
    semestre = input("Semestre: ")
    data = input("Data: ")
    faltas = input("Lista de alunos que faltaram: ")
    list_faltas = convert_to_list(faltas)

    login(user, senha)
    # Entra no diario online
    pyautogui.click(x=580, y=227)
    pyautogui.click(x=580, y=356)
    # Seleciona Sedu2022
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("down", presses=10)
    pyautogui.press("enter")
    pyautogui.press("tab", presses=2)
    pyautogui.press("enter")
    time.sleep(5)

    # Seleciona a materia
    pyautogui.press("tab", presses=4)
    pyautogui.press("enter")
    time.sleep(5)
    
    # Seleciona o semestre
    chose_semestre(semestre)
    time.sleep(5)

    pyautogui.press("tab", presses=4)
    pyautogui.press("enter")
    time.sleep(3)

    # Seleciona a data
    if data==None:
        pyautogui.press("tab", presses=5)
        pyautogui.press("enter")
    else:
        pyautogui.press("tab", presses=3)
        pyautogui.write(data)
        pyautogui.press("tab", presses=2)
        pyautogui.press("enter")
    time.sleep(20)

    pyautogui.press("tab", presses=12)
    assina_falta(list_faltas)
    pyautogui.press("enter")

if __name__ == "__main__":
    main()