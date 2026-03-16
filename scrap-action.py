import time
import requests
from playwright.sync_api import sync_playwright
import difflib

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
    current_split = current.splitlines()
    past_split = past.splitlines()
    # difflib is better than checking index per index because difflib use LCS idea to approach this problem 
    # for example old content be [a,b,c,d] current content be [X,a,b,c,d] 
    # if using manual checking it will alert all line are new because old line != current content for each line
    first_index = "" if len(past_split) == 0 else past_split[0] 
    d = difflib.Differ()
    # compare(a,b) a is old text and current text b will compare to a 
    diff = d.compare(past_split[1:], current_split)

    added_content = []
    
    for line in diff:
        if line.startswith("+ "):
            added_content.append(line)
    return (added_content, first_index)

def loop():
    content = get_content(url, field)
    try:
        with open(file, "r", encoding="utf-8-sig") as f:
            last_content = f.read().strip()
    except FileNotFoundError as fe:
        print(f"File note found: {fe}")
        last_content = ""
    if content != last_content:
        print("Something Update")
        add_content, th = compare(current=content, past=last_content)
        for change in add_content:
            print(f'มีการเปลี่ยนแปลงดังนี้: {change}')
        idx = th.split()
        idx[1] = int(idx[1])
        with open(file, "w", encoding="utf-8-sig") as f:
            print(f'------------------------')
            content = f'การตรวจสอบครั้งที่ {idx[1] + 1} \n{content}'
            f.write(content)
            f.close()

if __name__ == '__main__':
    loop()