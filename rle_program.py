from console_gfx import ConsoleGfx


def print_menu():
    print('Welcome to the RLE image encoder!\n\n'
          'Displaying Spectrum Image:')
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print('\n\n'
          'RLE Menu\n'
          '--------\n'
          '0. Exit\n'
          '1. Load File\n'
          '2. Load Test Image\n'
          '3. Read RLE String\n'
          '4. Read RLE Hex String\n'
          '5. Read Data Hex String\n'
          '6. Display Image\n'
          '7. Display RLE String\n'
          '8. Display Hex RLE Data\n'
          '9. Display Hex Flat Data\n'
          '\n')

def load_file():
    file = input('Enter name of file to load: ')
    ConsoleGfx.load_file(file)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    program_on = True
    while program_on:
        print_menu()
        menu_option = input('Select a Menu Option: ')

        if menu_option == '1':
            load_file()
        elif menu_option == '2':
            ConsoleGfx.test_image
            print('Test image data loaded.')
        elif menu_option == '3':
            pass
        elif menu_option == '4':
            pass
        elif menu_option == '5':
            pass
        elif menu_option == '6':
            ConsoleGfx.display_image(ConsoleGfx.test_image)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
