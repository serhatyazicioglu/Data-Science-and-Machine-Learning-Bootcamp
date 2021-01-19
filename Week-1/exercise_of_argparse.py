import argparse

parser = argparse.ArgumentParser(description="Letter Grade Calculation")

parser.add_argument("midterm", help="Please enter your midterm grade", type=int)
parser.add_argument("quiz_1", help="Please enter your first quiz grade", type=int)
parser.add_argument("quiz_2", help="Please enter your second quiz grade", type=int)
parser.add_argument("final", help="Please enter your final grade", type=int)

args = parser.parse_args()

result = (args.midterm * 40 / 100) + (args.quiz_1 * 5 / 100) + (args.quiz_2 * 5 / 100) + (args.final * 50 / 100)

if result > 85:
    print("Your Letter Grade: AA")
elif 75 <= result < 85:
    print("Your Letter Grade: BB")
elif 65 <= result < 75:
    print("Your Letter Grade: CC")
elif 50 <= result < 65:
    print("Your Letter Grade: DD")
else:
    print("Your Letter Grade: FF")