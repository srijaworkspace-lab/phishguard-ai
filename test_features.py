from url_features import *

url = input("Enter URL: ")

print("URL Length:", url_length(url))
print("HTTPS:", has_https(url))
print("IP Address:", has_ip(url))
print("Hyphen:", has_hyphen(url))
print("Dot Count:", count_dots(url))
print("Suspicious Words:", suspicious_words(url))
print("Domain Length:", domain_length(url))
print("Subdomains:", subdomain_count(url))