import requests
import time
from datetime import datetime

webhook_url = ""
MAX_LENGTH=1500

def alert_system(update_content):
    idx = 0
    now = datetime.now()
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S")
    content = f'ตรวจสอบวันที่เวลา: {formatted_now}\n'
    while (idx < len(update_content)):
        for i in range(idx, len(update_content)):
            if (len(content) > MAX_LENGTH):
                break;
            content += update_content[i] + '\n'
            idx+=1
        data = {
            "content":content,
            "username":"น้องแจ้งเตือน"
        }
        try:
            response = requests.post(webhook_url, json=data)
            response.raise_for_status()
            print("Successfully sent notification")
            time.sleep(5)
            content = ""
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Alert System Failed: {e}") from e
    return None