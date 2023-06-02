# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

isRaining = True
isSunny = True

if isRaining and isSunny:
    print('We might see a rainbow')
else:
    print('We might not')


ages = [12, 15, 23, 29, 37, 42, 49, 52]
for age in ages:
    isAdult = age > 17;
    if not isAdult:
        print('Being ' + str(age) + ' does not make you an adult.')