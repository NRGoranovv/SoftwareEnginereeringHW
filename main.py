from library import get_status_code

def main():
    url = "https://example.com"
    status_code = get_status_code(url)
    print(f"The status code for {url} is {status_code}")

if __name__ == "__main__":
    main()
