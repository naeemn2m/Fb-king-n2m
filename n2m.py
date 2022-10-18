import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')

        os.system('xdg-open https://www.facebook.com/https://www.facebook.com/profile.php?id=100069562290530')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from free import main1
 
        main1()
 
 
 
elif bit == "32bit":
 
        from free import main1
 
 
        main1()
