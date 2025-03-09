import argparse
def add_numbers(a, b):
    result = a + b
    return result

parser = argparse.ArgumentParser()
parser.add_argument('--x', type=int, help='First number')
parser.add_argument('--y', type=int, help='Second number')
args = parser.parse_args()
x = args.x
y = args.y
sum_result = add_numbers(x, y)
print(sum_result)