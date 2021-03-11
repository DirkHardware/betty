import os
import glob

filepath = 'arraytest.txt'
selected = {}

# with open("/home/anderson/.config/autostart/play.desktop", "r") as file:
#     # .readlines() returns the text as a list of lines
#     list_of_lines = file.readlines()
#     print(list_of_lines)
#     for cnt, line in enumerate(list_of_lines):
#         print("{} {}".format(cnt, line))


def check_betty():
    betty = False
    path = '/home/anderson/.config/autostart'
    # I need to better understand what os.path.join is doing
    for filename in glob.glob(os.path.join(path, '*')):
        with open(os.path.join(os.getcwd(), filename), 'r') as file:  # open in readonly mode
            list_of_lines = file.readlines()
            separator = ' '
            file_string = separator.join(list_of_lines)
            if "Betty" in file_string and "play " in file_string:
                print("A Betty file is present")
            elif "Betty" not in file_string and "play " in file_string:  # This was as true even when it wasn't because
                # 'play' is a substring of "NoDisplay". Remember to add be careful with substrings!
                print("An audio play command was found that is not in the betty list. Add it?")


def list_betty():
    with open("/home/anderson/.config/betty/bettyconfig", "r") as file:
        list_of_lines = file.readlines()
        # print(list_of_lines)
        for cnt, line in enumerate(list_of_lines):
            split_list = line.split(':')
            if cnt == 0:
                print("Selected startup audio: {}\n".format(split_list[0]))
            else:
                print(split_list[0])
                if split_list[1] == '\n':
                    ask = input('This sound has no corresponding file, would you like to add one? (Y/n): ')
                    if 'Y' in ask or 'y' in ask:
                        inp_path = input('Enter file path: ')
                        print(str(os.path.isfile(inp_path)))
                        # This if statement is not being tripped, but why?
                        # Why does the process finish HERE?
                        if os.path.isfile(inp_path) is True:
                            print("This is a valid file")
                        else:
                            print("This is not a valid file")
                else:
                    print(split_list[1])


check_betty()
list_betty()

# with open("/home/anderson/.config/autostart/play.desktop", "r") as file:
#     # .readlines() returns the text as a list of lines
#     list_of_lines = file.readlines()
#     print(list_of_lines)
#     for cnt, line in enumerate(list_of_lines):
#         print("{} {}".format(cnt, line))
