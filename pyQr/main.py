#import This Libs before run Code
#pip install

import pyqrcode
import png
import pyqrcode


# Enter your Website
web_Link = 'www.facebook.com'

# Create QR
url = pyqrcode.create(web_Link)

# Save As svg
# You can change file name & scale
url.svg('myqr.svg', scale=8)

# Save As png
# You can change file name & scale
url.png('myqr.png', scale=6)
