import requests

r = requests.get('https://raw.githubusercontent.com/ehmatthes/pcc/master/chapter_10/pi_million_digits.txt')

pi_string = r.text

for rs in r:
    pi_string += rs.strip()
    
birthday = raw_input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
