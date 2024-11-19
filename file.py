import sys

def finder(s : str) -> float:
    arr = s.split(' ')
    if len(arr) != 2:
        print("Badly formatted line: ", s)
    else:
        try:
            f1 = float(arr[0])
            f2 = float(arr[1])
            print(f1 + f2)
        except ValueError:
            print("Bad value in line: ", s)

try:
    f = open(sys.argv[1], 'r')
    lines = f.read().splitlines()
    f.close()
    for line in lines:
       finder(line)
except FileNotFoundError:
    print("File not found")
except IndexError:
    print("File name not given")

