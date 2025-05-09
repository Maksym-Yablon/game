import os
import time
import random
import sys
import sounddevice as sd
from scipy.io import wavfile
from colorama import init, Fore, Style

def start_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def color_text(text = "Hello", color = Fore.YELLOW):
    print(color + text + Style.RESET_ALL)     

def typewriter_effect(text, delay=0.05):
    """Функція для анімації друку тексту."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # Перехід на новий рядок після завершення друку

def game_screen():
    typewriter_effect("Завантаження гри", delay=0.05)
    for _ in range(10):  # цикл анімації крапок
        time.sleep(0.2)
        print(".", end="", flush=True)
    typewriter_effect("\nГра завантажена!", delay=0.05)   
    time.sleep(0.5) 
    typewriter_effect("Починаємо!", delay=0.05)    
    time.sleep(1)

def game_screen2():
    banner = r"""
██╗███╗   ██╗    ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗    
██║████╗  ██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║    
██║██╔██╗ ██║    ███████╗█████╗  ███████║██████╔╝██║     ███████║    
██║██║╚██╗██║    ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║    
██║██║ ╚████║    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║    
╚═╝╚═╝  ╚═══╝    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    
                                                                     
     ██████╗ ███████╗    ██╗     ██╗ ██████╗ ██╗  ██╗████████╗       
    ██╔═══██╗██╔════╝    ██║     ██║██╔════╝ ██║  ██║╚══██╔══╝       
    ██║   ██║█████╗      ██║     ██║██║  ███╗███████║   ██║          
    ██║   ██║██╔══╝      ██║     ██║██║   ██║██╔══██║   ██║          
    ╚██████╔╝██║         ███████╗██║╚██████╔╝██║  ██║   ██║          
     ╚═════╝ ╚═╝         ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝          
     """
    typewriter_effect(banner, delay=0.001)  # Виклик функції з анімацією друку
    time.sleep(1)
    input ("Натисніть Enter, щоб почати гру...")
    start_game(True)

def start_game(stargames = False):
    start_screen()
    if stargames == True:
        menu()

def games():
    typewriter_effect("🎬 ВСТУП: Єва-Ліза прокидається в темряві. Мами немає. Світло у вікні блимає.\n")
    typewriter_effect    ("Вона вирушає на пошуки мами, але виявляє, що світ змінився.\n") 
    typewriter_effect  ("Вона не знає, що сталося. Вона не знає, що робити.\n")
    start_screen()
    color_text(text= "1️⃣ Залишитися вдома", color=Fore.LIGHTMAGENTA_EX)
    color_text(text= "2️⃣ Вийти на вулицю", color=Fore.LIGHTMAGENTA_EX)

    igra = 0
    try:
        igra = int(input("Виберіть опцію (1-3): "))
    except ValueError:
        print("Будь ласка, введіть число від 1 до 3.")
        continue
    if igra == 1:
        typewriter_effect("Вибір: Залишитися вдома.\n")
        time.sleep(1)
        typewriter_effect("Єва-Ліза вирішує залишитися вдома, сподіваючись, що мама повернеться.\n")
        time.sleep(1)
        typewriter_effect("Вона чекає, але час минає, і вона відчуває себе самотньою.\n")
        time.sleep(1)
        typewriter_effect("Вона чує дивні звуки з-за дверей.\n")
        time.sleep(1)
        typewriter_effect("Вона вирішує перевірити, що відбувається.\n")
        time.sleep(1)
        
    elif igra == 2:
        typewriter_effect("Вибір: Вийти на вулицю.\n")
        time.sleep(1)
        typewriter_effect("Єва-Ліза вирішує вийти на вулицю, сподіваючись знайти маму.\n")
        time.sleep(1)
        typewriter_effect("Вона виходить з дому і бачить, що світ змінився...\n")
        time.sleep(1)
        typewriter_effect("Вулиці порожні, а будинки виглядають покинутими.\n")
        time.sleep(1)
        typewriter_effect("Вона відчуває страх, але вирішує йти далі.\n")
        time.sleep(1)
        typewriter_effect("Вона чує дивні звуки і бачить тіні вдалині.\n")
        time.sleep(1)   
        typewriter_effect("Ця тінь наближається до неї, і вона відчуває страх.\n")




        time.sleep(1)
        typewriter_effect("Вона намагається втекти, але тінь наздоганяє її.\n")
        time.sleep(1)
        typewriter_effect("Вона відчуває, як щось холодне торкається її плеча.\n")
        time.sleep(1)
        typewriter_effect("Вона обертається і бачить, що це Тім.\n")
        time.sleep(1)

    
        



    
    

     


         
def menu():
    choice = 0
    sound_on = True
    sound_txt = "ВКЛ🔊"
    
    while True:
        start_screen()
        color_text(text="1 - Почати гру🎮", color=Fore.LIGHTMAGENTA_EX)
        time.sleep(1)
        color_text(text=f"2 - Звук({sound_txt})", color=Fore.LIGHTGREEN_EX)
        time.sleep(1)
        color_text(text="3 - Вихід з гри❌", color=Fore.LIGHTBLUE_EX)
        
        try:
            choice = int(input("Виберіть опцію (1-3): "))
        except ValueError:
            print("Будь ласка, введіть число від 1 до 3.")
            continue
        
        if choice == 1:
            games()
            break
        elif choice == 2:
            if sound_on:
                sound_on = False
                sound_txt = "ВИКЛ🔈"
            else:
                sound_on = True
                sound_txt = "ВКЛ🔊"
        elif choice == 3:
            print("...")
            break
        else:
            print("Будь ласка, виберіть правильну опцію.")
          

start_screen()
game_screen()
start_screen()
game_screen2()