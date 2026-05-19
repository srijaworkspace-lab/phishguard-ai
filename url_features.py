import re
import tldextract

# URL Length
def url_length(url):
    return len(url)

# HTTPS Check
def has_https(url):
    return 1 if url.startswith("https://") else 0

# IP Address Check
def has_ip(url):

    pattern = r'\\d+\\.\\d+\\.\\d+\\.\\d+'

    return 1 if re.search(pattern, url) else 0

# Hyphen Check
def has_hyphen(url):
    return 1 if "-" in url else 0

# Count Dots
def count_dots(url):
    return url.count('.')

# Suspicious Words
def suspicious_words(url):

    words = [
        "login",
        "secure",
        "bank",
        "verify",
        "account",
        "update",
        "free",
        "bonus"
    ]

    for word in words:
        if word in url.lower():
            return 1

    return 0

# Domain Length
def domain_length(url):

    extracted = tldextract.extract(url)

    domain = extracted.domain

    return len(domain)

# Number of Subdomains
def subdomain_count(url):

    extracted = tldextract.extract(url)

    subdomain = extracted.subdomain

    if subdomain == "":
        return 0

    return len(subdomain.split('.'))