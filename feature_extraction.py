import re

# URL length
def url_length(url):
    return len(url)

# Check HTTPS
def has_https(url):
    return 1 if "https" in url else 0

# Check @ symbol
def has_at_symbol(url):
    return 1 if "@" in url else 0

# Check IP address
def has_ip(url):
    pattern = r'\\d+\\.\\d+\\.\\d+\\.\\d+'

    return 1 if re.search(pattern, url) else 0
# Count dots in URL
def count_dots(url):
    return url.count('.')

# Check hyphen
def has_hyphen(url):
    return 1 if '-' in url else 0

# Check suspicious words
def has_suspicious_words(url):

    suspicious_words = [
        'login',
        'secure',
        'update',
        'bank',
        'verify',
        'account',
        'free',
        'bonus'
    ]

    for word in suspicious_words:
        if word in url.lower():
            return 1

    return 0