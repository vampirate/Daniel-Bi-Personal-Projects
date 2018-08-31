import sys, json, numpy as np


def main():
    #get our data as an array from read_in()
    temp = sys.stdin.readlines()
    lines = json.loads(temp[0])

    #return the sum to the output stream
    print (lines)

#start process
if __name__ == '__main__':
    main()