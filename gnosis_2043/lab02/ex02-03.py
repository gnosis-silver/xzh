# runtime + debug with parameters (4 points)
import argparse

def process_parameters(word, first_num, second_num):
    last_letter = word[-1]
    print("The last letter in '{0}' is '{1}'".format(word, last_letter))
    print(f"For {first_num} and {second_num}:")
    print("\tSum = {0}".format(first_num + second_num))
    print("\tDifference = {0}".format(first_num - second_num))
    print("\tProduct = {0}".format(first_num * second_num))
    if second_num != 0:
        print("\tQuotient = {0}".format(first_num / second_num))
    else:
        print("\tQuotient nonexistence")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Debug with parameters exercise.")
    parser.add_argument("--word", type=str, required=True, help="An english word")
    parser.add_argument("--first_num", type=int, required=True, help="First whole number")
    parser.add_argument("--second_num", type=int, required=True, help="Second whole number")
    args = parser.parse_args()

    ###### parameters: word: school, first_num: 10, second_num: 0 ######
    ###### Your task: debug with above parameters and fix the error ######
    process_parameters(args.word, args.first_num, args.second_num)
