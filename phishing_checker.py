
from urllib.parse import urlparse
import ipaddress


def check_url(url):
    warnings = []
    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    if "@" in url:
        warnings.append("URL contains an @ symbol")

    if len(url) > 100:
        warnings.append("URL is longer than 100 characters")

    try:
        ipaddress.ip_address(hostname)
        warnings.append("URL uses an IP address instead of a domain name")
    except ValueError:
        pass

    if len(hostname.split(".")) >= 5:
        warnings.append("Hostname has 5 or more segments")

    if "xn--" in hostname.lower():
        warnings.append("Hostname contains a punycode marker")

    if parsed.scheme.lower() == "http":
        warnings.append("URL uses HTTP instead of HTTPS")

    return warnings


def main():
    print("=== Phishing URL Awareness Checker ===")
    url = input("Enter a URL to check: ")

    warnings = check_url(url)

    if warnings:
        print("\nWarning signs found:")
        for warning in warnings:
            print("-", warning)
    else:
        print("\nNo warning signs detected by these checks.")

    print("\nNote: This tool does not prove whether a URL is safe.")


if __name__ == "__main__":
    main()
