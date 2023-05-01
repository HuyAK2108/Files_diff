import sys

class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

# Get File from arguments
file_1 = sys.argv[1]
file_2 = sys.argv[2]
# Open File in Read Mode
file_1 = open(file_1, 'r', encoding="UTF-8")
file_2 = open(file_2, 'r', encoding="UTF-8")
# Read File line by line
file_1_line = file_1.readline()
file_2_line = file_2.readline()

line_no = 1
ret = 1

print(f"Comparing file\n--- {file_1.name}\n+++ {file_2.name}")
print(f"{colors.bold}{colors.fg.orange}❌ Difference Lines in Both Files{colors.reset}")

while file_1_line != '' or file_2_line != '':
    # Removing whitespaces
    file_1_line = file_1_line.rstrip()
    file_2_line = file_2_line.rstrip()
    
    # Compare the lines from both file
    if file_1_line != file_2_line:
        ret = 0
        # Line number
        print(f"{colors.fg.cyan}line {line_no}")
        # First file
        print(f"{colors.fg.red}-{file_1_line}")
        # Second file
        print(f"{colors.fg.green}+{file_2_line}")
        
    # Read the next line from the file
    file_1_line = file_1.readline()
    file_2_line = file_2.readline()
 
    line_no += 1
    
file_1.close()
file_2.close()

if ret == 1:
    print(f"{colors.bold}{colors.fg.green}✅ Both files are the same !")
print(colors.reset)
