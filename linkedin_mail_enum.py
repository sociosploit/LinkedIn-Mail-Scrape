#!/usr/bin/env python
from sociosploit import linkedin
from getpass import getpass
import sys

print "\n*************************************************"
print "**  Scrape Phishing Targets                    **"
print "**  by Sociosploit Team                        **"
print "**  ...GONE PHISHING!!!                        **"
print "*************************************************\n\n"

if len(sys.argv) != 4:
    print "Usage - ./LI_TargetEnum.py [Format num] [suffix] [output_file]"
    print "\nFORMATS:"
    print "1 - [first].[last]@[suffix]"
    print "2 - [first][last]@[suffix]"
    print "3 - [first initial][last]@[suffix]"
    print "4 - [first]_[last]@[suffix]\n"
    print "Example - ./LI_TargetEnum.py 1 company.com output.txt"
    print "Example will create email list in the form of john.smith@company.com\n\n"
    sys.exit()

username = raw_input("Enter username for LinkedIn Bot Account:\n")
password = password = getpass("Enter password:\n")
company = raw_input("Enter company name to target:\n")

format = int(sys.argv[1])
suffix = str(sys.argv[2]).lower()
filename = str(sys.argv[3])
file = open(filename,'w')

def format_1(names,suffix):
    emails = []
    for x in names:
        try:
            first = x.split(' ')[0].lower()
            last = x.split(' ')[1].lower()
            emails.append(first + '.' + last + '@' + suffix)
        except:
            pass
    return emails

def format_2(names,suffix):
    emails = []
    for x in names:
        try:
            first = x.split(' ')[0].lower()
            last = x.split(' ')[1].lower()
            emails.append(first + last + '@' + suffix)
        except:
            pass
    return emails

def format_3(names,suffix):
    emails = []
    for x in names:
        try:
            first = x.split(' ')[0].lower()
            last = x.split(' ')[1].lower()
            emails.append(first[0] + last + '@' + suffix)
        except:
            pass
    return emails

def format_4(names,suffix):
    emails = []
    for x in names:
        try:
            first = x.split(' ')[0].lower()
            last = x.split(' ')[1].lower()
            emails.append(first + '_' + last + '@' + suffix)
        except:
            pass
    return emails

# Start Browser and Login
browser = linkedin.start_browser()
loggedin = linkedin.login(browser, username, password)
if loggedin:
    print "[+] Login Successful"
else:
    print "[-] Login Failed"

# Scrape Names
names = linkedin.get_phish_targets(browser, company)

# Create emails
if format == 1:
    emails = format_1(names,suffix)
elif format == 2:
    emails = format_2(names,suffix)
elif format == 3:
    emails = format_3(names,suffix)
elif format == 4:
    emails = format_4(names,suffix)

# Write to file
for email in emails:
    file.write(email+"\n")
file.close()
