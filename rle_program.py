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


def to_hex_string(data):
    char_values = {
        '10': 'a',
        '11': 'b',
        '12': 'c',
        '13': 'd',
        '14': 'e',
        '15': 'f'
    }

    hex_string = ''

    for value in data:
        value = str(value)
        if value in char_values:
            hex_string += char_values[value]
        else:
            hex_string += value
    return hex_string


def count_runs(flat_data):
    current = flat_data[0]
    runs_count = 1
    curr_run_len = 0
    for num in flat_data[1:]:
        curr_run_len += 1
        if current != num:
            runs_count += 1
            current = num
            curr_run_len = 0
        if curr_run_len == 15:
            runs_count += 1
            curr_run_len = 0

    return runs_count


def encode_rle(flat_data):
    current = flat_data[0]
    count = 1
    encoded_rle = []
    for num in flat_data[1:]:
        if current == num:
            count += 1
            if count == 15:
                encoded_rle.append(count)
                encoded_rle.append(current)
                count = 0
        else:
            encoded_rle.append(count)
            encoded_rle.append(current)
            count = 1
            current = num
    encoded_rle.append(count)
    encoded_rle.append(current)
    return encoded_rle


def get_decoded_length(rle_data):
    rle_decoded_len = 0

    for i in range(len(rle_data)):
        if i % 2 == 0:
            rle_decoded_len += rle_data[i]
    return rle_decoded_len


def decode_rle(rle_data):
    decoded_rle = []
    for i in range(0, len(rle_data), 2):
        value = rle_data[i + 1]
        decoded_rle.extend([value] * rle_data[i])
    return decoded_rle


def string_to_data(data_string):
    data = []

    char_values = {
        'A': 10,
        'a': 10,
        'B': 11,
        'b': 11,
        'C': 12,
        'c': 12,
        'D': 13,
        'd': 13,
        'E': 14,
        'e': 14,
        'F': 15,
        'f': 15
    }

    for value in data_string:
        if value in 'ABCDEFabcdef':
            data.append(int(char_values[value]))
        else:
            data.append(int(value))
    return data


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
