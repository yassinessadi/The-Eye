

def main():
    domain = input("Enter the domain: ")
    keyword = input("Enter the keyword: ")
    dorks = generate_google_dorks(domain, keyword)
    print(dorks)

if __name__ == "__main__":
    main()
