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

# betty = False
# path = '/home/anderson/.config/autostart'
# for filename in glob.glob(os.path.join(path, '*')):
#     with open(os.path.join(os.getcwd(), filename), 'r') as file:  # open in readonly mode
#         list_of_lines = file.readlines()
#         separator = ' '
#         file_string = separator.join(list_of_lines)
#         print(file_string)
#         if "Betty" in file_string and "play " in file_string:
#             print("A Betty file is present")
#         elif "Betty" not in file_string and "play " in file_string:  # This is currently returning as true because
#             # 'play' is a substring of "NoDisplay". Remember to add a space after play when searching for it as a
#             # command.
#             print("An audio play command was found that is not in the betty list. Add it?")

with open("/home/anderson/.config/betty/bettyconfig", "r") as file:
    list_of_lines = file.readlines()
    print(list_of_lines)
    for cnt, line in enumerate(list_of_lines):
        split_list = line.split(':')
        # print(split_list)
        # print(split_list[0])
        if cnt == 0:
            print("Selected startup audio: {}".format([split_list[0]]))
        if split_list[1] == '\n':
            print('This sound has no corresponding file')
        else:
            print(split_list[1])

# with open("/home/anderson/.config/autostart/play.desktop", "r") as file:
#     # .readlines() returns the text as a list of lines
#     list_of_lines = file.readlines()
#     print(list_of_lines)
#     for cnt, line in enumerate(list_of_lines):
#         print("{} {}".format(cnt, line))
