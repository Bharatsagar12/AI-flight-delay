# ============================================
# ADVANCED WEB SCRAPER
# WITH CSV + SEARCH + TIMESTAMP
# ============================================

# Import libraries
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Website URL
url = "https://news.ycombinator.com/"

try:

    print("Connecting to website...\n")

    # Send request
    response = requests.get(url)

    # Check connection
    if response.status_code == 200:

        print("Website connected successfully!")
        print("Status Code:", response.status_code)

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines
        headlines = soup.find_all("span", class_="titleline")

        print("\n===================================")
        print("     FILTERED NEWS HEADLINES")
        print("===================================\n")

        # --------------------------------------------
        # USER INPUT
        # --------------------------------------------
        keyword = input("Enter keyword to search news: ").lower()

        found = False

        # --------------------------------------------
        # CURRENT DATE AND TIME
        # --------------------------------------------
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # --------------------------------------------
        # CREATE CSV FILE
        # --------------------------------------------
        with open("filtered_news.csv", "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            # CSV headings
            writer.writerow(["S.No", "Headline", "Link", "Date & Time"])

            # Loop through headlines
            for i, headline in enumerate(headlines, start=1):

                # Extract title
                title = headline.get_text()

                # Extract link
                link = headline.a["href"]

                # --------------------------------------------
                # FILTER KEYWORD
                # --------------------------------------------
                if keyword in title.lower():

                    found = True

                    # Display result
                    print(f"{i}. {title}")
                    print("Link:", link)
                    print("Scraped At:", current_time)
                    print("-" * 50)

                    # Save into CSV
                    writer.writerow([i, title, link, current_time])

        # --------------------------------------------
        # NO RESULTS
        # --------------------------------------------
        if not found:
            print("\nNo matching news found.")

        else:
            print("\nFiltered news saved into filtered_news.csv")

    else:
        print("Failed to connect website")

except Exception as e:
    print("Error:", e)

# ============================================
# END
# ============================================