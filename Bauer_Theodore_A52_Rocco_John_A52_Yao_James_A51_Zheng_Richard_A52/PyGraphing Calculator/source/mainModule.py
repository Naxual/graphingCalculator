# mainModule.py

import Gui


def main():
    try:
        calculator = Gui.Gui()
    except:
        print("Error in gui generation")

main()