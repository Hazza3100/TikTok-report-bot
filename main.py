import os
import random
import requests
import threading

from colorama import Fore

reported = 0

class TikTok:
    def __init__(self) -> None:
        self.session  = requests.Session()

    def report(self, userId, _proxy_):
        try:
            global reported
            with self.session as session:
                reason          = random.randint(0, 12000)
                fake_engagement = 9010
                headers = {
                    'authority'         : 'www.tiktok.com',
                    'accept'            : '*/*',
                    'accept-language'   : 'en-US,en;q=0.9',
                    'referer'           : 'https://www.tiktok.com/',
                    'sec-ch-ua'         : '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                    'sec-ch-ua-mobile'  : '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest'    : 'empty',
                    'sec-fetch-mode'    : 'cors',
                    'sec-fetch-site'    : 'same-origin',
                    'user-agent'        : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                }
                if _proxy_ == None:
                    response = session.get(f'https://www.tiktok.com/aweme/v1/aweme/feedback/?report_type=user&object_id={userId}&owner_id={userId}&reason={reason}', headers=headers)
                else:
                    proxy = random.choice(open('proxies.txt', 'r').read().splitlines())
                    proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                    response = session.get(f'https://www.tiktok.com/aweme/v1/aweme/feedback/?report_type=user&object_id={userId}&owner_id={userId}&reason={reason}', headers=headers, proxies=proxies)
                if response.json()['status_msg'] == "Thanks for your feedback":
                    reported += 1
                    print(f"{Fore.BLUE}[ {Fore.GREEN}+ {Fore.BLUE}]{Fore.RESET} Reported [ {userId} ] ({reported})")
                else:
                    print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")



if __name__ == '__main__':
    os.system('cls')
    userId  = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] User ID {Fore.CYAN}> {Fore.WHITE}")
    threads = int(input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Threads {Fore.CYAN}> {Fore.WHITE}"))
    proxy   = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Use proxies (y/n) {Fore.CYAN}> {Fore.WHITE}")
    if proxy == "y":
        _proxy_ = "Use"
        for i in range(threads):
            threading.Thread(target=TikTok().report, args=(userId, _proxy_)).start()
    else:
        _proxy_ = None
        for i in range(threads):
            threading.Thread(target=TikTok().report, args=(userId,)).start()
