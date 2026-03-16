from playwright.sync_api import sync_playwright
import difflib
from alert import alert_system

url = ""
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
    d = difflib.Differ()
    # compare(a,b) a is old text and current text b will compare to a 
    diff = d.compare(past_split, current_split)

    added_content = []
    
    for line in diff:
        if line.startswith("+ "):
            added_content.append(line[2:])
    return added_content

def loop():
    content = get_content(url, field)
    try:
        with open(file, "r", encoding="utf-8-sig") as f:
            full_data = f.read().strip()
            lines = full_data.splitlines()
            if len(lines) > 0:
                header = lines[0]
                past_web_content = "\n".join(lines[1:]).strip()
            else:
                header = "การตรวจสอบครั้งที่ 0"
                past_web_content = ""
    except FileNotFoundError:
        header = "การตรวจสอบครั้งที่ 0"
        past_web_content = ""
    try:
        if content != past_web_content:
            print("Something Update")
            add_content= compare(current=content, past=past_web_content)
            for change in add_content:
                print(f'มีการเปลี่ยนแปลงดังนี้: {change}')
            current_count = int(header.split()[-1])
            with open(file, "w", encoding="utf-8-sig") as f:
                print(f'------------------------')
                content = f'การเปลี่ยนแปลงครั้งที่ {current_count + 1}\n{content}'
                f.write(content)
        else:
            add_content = ["ไม่มีการเปลี่ยนแปลง"]
        alert_system(add_content)
    except Exception as e:
        print(f"Logging error for debugging: {e}")

if __name__ == '__main__':
    loop()