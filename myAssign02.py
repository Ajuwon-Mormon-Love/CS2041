import csv
#Enter your file name
def introduce_file():
    file_name = input("Please enter the data file: ")
    return file_name
# With this function we open the file, read it and get the average
def avg_comm_rate(file_name):
    count = 0
    total_rate = 0
    with open(file_name, "r") as handle:
        lines = handle.readline().splitlines()
        lines.pop(0)
        for lines in handle:
            line = lines.split(",")
            count = count + 1
            x = float((line[6]))
            total_rate = total_rate + x 
    comm_rate = total_rate/count
    handle.close()
    return comm_rate
# Creat Function to find the maximum comm_rate 
def high_comm_rate(file_name):
    global words_max
    #data = []
    max_line = ""
    max_comm_rate = 0.0
    with open(file_name, "r") as file:
        lines = file.readline().splitlines()
        lines.pop(0)
        for lines in file:
            line = lines.split(",")
            x = float((line[6]))
            if (max_comm_rate < x):
                max_comm_rate = x
                max_line = lines 
                words_max = max_line.split(",")
    return max_comm_rate
# Creat Function to find the minimum comm_rate 
def lowest_comm_rate(file_name):
    global words_min
    #data = []
    min_line = ""
    min_comm_rate = 1.0
    with open(file_name, "r") as file:
        lines = file.readline().splitlines()
        lines.pop(0)
        for lines in file:
            line = lines.split(",")
            x = float((line[6]))
            if (min_comm_rate > x):
                min_comm_rate = x
                min_line = lines 
                words_min = min_line.split(",") 
    return min_comm_rate


def main():
    file_name = introduce_file()
    comm_rate = avg_comm_rate(file_name)
    max_line = high_comm_rate(file_name)
    max_comm_rate = high_comm_rate(file_name)
    min_comm_rate = lowest_comm_rate(file_name)
    print()
    print("The average commercial rate is:", comm_rate)
    print()
    print("The highest rate is:") 
    print(words_max[2],"(" + words_max[0]+ ",",words_max[3] + ") - $" + 
str(max_comm_rate))
    print()
    print("The lowest rate is:") 
    print(words_min[2],"(" + words_min[0]+ ",",words_min[3] + ") - $" + 
str(min_comm_rate))
if __name__ == "__main__":
   main() 