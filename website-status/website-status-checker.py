"""
Script reading the file containing web page names,
checks if the page 'exists', eg returns code 2xx or 3xx after polling,
returns the .txt file containing only working pages adresses

"""

import requests


def normalize_url(url: str) -> str:
    """Function that adds http's if they are not at the beginning of the url"""
    url = url.strip()

    if not url:  # if empty line in file
        return " "

    if not url.startswith(("http://", "https://")):  # startswith takes tuple
        url = "https://" + url

    return url


working_pages = []

with open("input_urls.txt", "r", encoding="UTF-8") as file:
    for strona in file.readlines():
        url = normalize_url(strona)

        if not url:
            continue

        try:
            response = requests.get(
                url, timeout=5
            )  # if page reading connection takes too long, move to another

            if 200 <= response.status_code < 400:
                working_pages.append(url)

        except requests.RequestException:
            print("Error while checking URL:", url)

with open("working_pages.txt", "w") as outcome:  # saving outcome file
    outcome.write("\n".join(working_pages) + "\n")
