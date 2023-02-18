# Problem: https://www.hackerrank.com/challenges/whats-your-name/problem
# Score: 10


def print_full_name(first_name, last_name):
    print("Hello {} {}! You just delved into python.".format(first_name, last_name))


# Alternative solution 01

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Alternative Solution 02

def print_full_name(first, last):
    salute = "Hello %s %s! You just delved into python."
    print(salute % (first, last))

# Alternative Solution 03
def print_full_name(first_name,last_name) :
    print("Hello",first_name,last_name+"! You just delved into python.")


