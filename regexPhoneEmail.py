#! python 3

import re, pyperclip

# Create a regex for phone numbers
re.compile(r'''
# 415-555-000, 555-0000, (415) 555-0000, 555-0000 ext 1234, ext. 123, x1234
(
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
(\s|-)                          # first separator
\d\d\d                          # first 3 digits
-                               # separator
\d\d\d\d                        # last 4 digits
(((ext(\.)?\s)|x)               # extension word part(optional)
(\d{2,5}))?                     # extension number (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex =  re.compile(r'''
# some.+_thing@(\d{2,6}))?.com

[a-zA-Z0-9_.+]+                 # name part
@                               # @ symbol
[a-zA-Z0-9_.+]+                 # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# Copy the extracted email/phone to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
