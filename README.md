# source-founder
check if the source code compressed and uploaded to the server by mistake 
# Discription 
- Some times the developer (by mistake) upload the source code of the subdomain to the server and it is accessible by anyone ( information disclosure vulnerability ) 
- So i decided not to waste time on this step of recon and automate it with this tool 
- This tool take a list of subdomains and check for the source code with multiple compressed extensions ( "zip","bak","tar","gizp","rar","7z","iso","bz2","gz","apk","cab","jar","bzip2","deb","ace") and you could add any other extension to this list and check for the response code for each file like this http://www.example.com ==> http://www.example.com/www.example.com.zip , http://www.example.com/www.example.com.rar ... etc 
- Some server respond with 200 response code even the file doesn't exist so to avoid false positive i have added that if the response code is 200 the tool get the content length and you could check if all extension give the same content length so this is a false positive 
- Also i made the output colorized so it is easy for your eyes to get the response code just by color 

# Install 

git clone https://github.com/smackerdodi/source-founder.git
cd source-founder 
pip3 install -r requirements.txt

# Usage 

python3 source-founder.py sub.txt output.txt 
sub.txt : File contain subdomains begin with http or https 
output.txt : File contain the output of the tool 
