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


if __name__ == '__main__':
    program_on = True
    image_data = None
    while program_on:
        print_menu()
        menu_option = input('Select a Menu Option: ')

        if menu_option == '0':
            program_on = False
        if menu_option == '1':
            filename = input('Enter name of file to load: ')
            image_data = ConsoleGfx.load_file(filename)
        elif menu_option == '2':
            image_data = ConsoleGfx.test_image
            print('Test image data loaded.')
        elif menu_option == '3':
            pass
        elif menu_option == '4':
            pass
        elif menu_option == '5':
            pass
        elif menu_option == '6':
            print('Displaying image...')
            if image_data is None:
                print('(no data)')
            else:
                ConsoleGfx.display_image(image_data)
        elif menu_option == '7':
            if image_data is None:
                print('RLE representation: (no data)')
            else:
                pass
        elif menu_option == '8':
            if image_data is None:
                print('RLE hex values: (no data)')
            else:
                pass
        elif menu_option == '9':
            if image_data is None:
                print('Flat hex values: (no data)')
            else:
                pass
        else:
            print('Error! Invalid input.\n')

