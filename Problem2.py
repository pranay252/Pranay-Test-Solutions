import random
import string
import webbrowser

# Dictionary to store the short URL to original URL mapping
url_mapping = {}

def generate_short_url(original_url):
    """Generate a short URL for the given original URL."""
    # Generate a random 5-character string
    short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    short_url = f"https://short.url/{short_id}"
    
    # Map the short URL to the original URL
    url_mapping[short_url] = original_url
    
    return short_url

def navigate_to_original_url(short_url):
    """Open the browser to navigate to the original URL using the short URL."""
    if short_url in url_mapping:
        original_url = url_mapping[short_url]
        print(f"Navigating to {original_url}")
        webbrowser.open(original_url)
    else:
        print("Short URL not found in the system.")

def main():
    while True:
        print("\n--- URL Shortener ---")
        print("1. Generate Short URL")
        print("2. Navigate to Original URL")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            original_url = input("Enter the original URL: ")
            short_url = generate_short_url(original_url)
            print(f"Short URL: {short_url}")
        
        elif choice == '2':
            short_url = input("Enter the short URL: ")
            navigate_to_original_url(short_url)
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")
main()
