
# Importing ways 

# User Defined Package
# import cool
# print(cool.to_upper_case("Sai"))

from useful.cool import to_upper_case
from math import sqrt as square 

def main():
    print(to_upper_case("Sai"))

    # inbuilt package

    # alias with the as syntax if you want

    print(square(25))

if __name__ == '__main__':
    main()
