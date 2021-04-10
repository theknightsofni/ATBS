#! python3
# mclip.py - A multi-clipboard program
# Send automatic messages when busy during a conference call

TEXT = {'agree': """Yes, I agree. That sounds good to me.""",
        'busy': """Sorry, I'm in the middle of a conference call. Can I follow up with you after?""",
        'thank': """Thank you!"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line argument is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

