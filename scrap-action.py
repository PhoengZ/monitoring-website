import time
import requests
from playwright.sync_api import sync_playwright


url = "https://sites.google.com/view/ssukree/courses/2110571-neural-network-22025?authuser=0"
field = "body"
file = "last_file.txt"
def get_content(url, select_field):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            page.goto(url=url, wait_until='networkidle')
            content = page.inner_text(selector=select_field)
            return content
        except Exception as e:
            print(f'Error occured: {e}')
            return None
        finally:
            browser.close()

def compare(current, past):
    return None


def loop():
    content = get_content(url, field)
    try:
        with open(file, "r") as f:
            last_content = f.read().strip()
            f.close()
    except FileNotFoundError as fe:
        print(f"File note found: {fe}")
        last_content = ""
    # if content != last_content:
    #     print("Something Update")

    #     with open(file, "w") as f:
    #         f.write(content)
    #         f.close()
    split_current = content.splitlines()
    split_past = last_content.splitlines()
    print(split_current)
    print('----------------------------------------')
    print(split_past)

if __name__ == '__main__':
    loop()