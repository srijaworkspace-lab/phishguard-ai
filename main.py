from feature_extraction import *

url = input("Enter URL: ")

print("URL Length:", url_length(url))
print("HTTPS Present:", has_https(url))
print("@ Symbol Present:", has_at_symbol(url))
print("IP Address Present:", has_ip(url))