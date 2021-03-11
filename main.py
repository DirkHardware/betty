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


path = '/home/anderson/.config/autostart'
for filename in glob.glob(os.path.join(path, '*')):
    with open(os.path.join(os.getcwd(), filename), 'r') as file:  # open in readonly mode
        list_of_lines = file.readlines()
        print(list_of_lines)
        for cnt, line in enumerate(list_of_lines):
            print("{} {}".format(cnt, line))

# with open("/home/anderson/.config/autostart/play.desktop", "r") as file:
#     # .readlines() returns the text as a list of lines
#     list_of_lines = file.readlines()
#     print(list_of_lines)
#     for cnt, line in enumerate(list_of_lines):
#         print("{} {}".format(cnt, line))
