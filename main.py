import os
import random
import requests
import threading

from colorama import Fore


class stats:
    reported = 0
    error    = 0
    tit      = False

class TikTok:
    def __init__(self) -> None:
        self.session  = requests.Session()

    def get_id(self, username):
        try:
            with self.session as session:
                headers = {'authority': 'www.tiktok.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cookie': 'msToken=cxfL0lxGWTg_UmhgLz8U_Nv3ecxsgvBu5OJ1FtmVgMd3cHWoFCxQnyHSUzoCzEMMh0XeZzSw_gjF8XhG8Qp9qiE7yi9Yjm5B64hK4qdEMnhOvQCK6bL2bP8h6pAAVdphB3w_yBje2nj3iFw=','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',}

                response = session.get(f'https://www.tiktok.com/@{username}', headers=headers)
                return response.text.split('authorId":"')[1].split('","')[0]
        except:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Username Invalid")

    def title(self):
        while stats.tit == False:
            os.system(f'title TikTok Reporter ^| Success: {stats.reported} ^| Errors: {stats.error}')


    def report(self, userId, _proxy_):
        try:
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
                    stats.reported += 1
                    print(f"{Fore.BLUE}[ {Fore.GREEN}+ {Fore.BLUE}]{Fore.RESET} Reported [ {userId} ] ({stats.reported})")
                else:
                    stats.error += 1
                    print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")
        except:
            stats.error += 1
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")



if __name__ == '__main__':
    os.system('cls')
    username  = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Username {Fore.CYAN}> {Fore.WHITE}")
    threads   = int(input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Threads {Fore.CYAN}> {Fore.WHITE}"))
    proxy     = input(f"{Fore.GREEN}[{Fore.CYAN} ? {Fore.GREEN}] Use proxies (y/n) {Fore.CYAN}> {Fore.WHITE}")
    userId    = TikTok().get_id(username)
    threading.Thread(target=TikTok().title).start()
    if proxy == "y":
        _proxy_ = "Use"
        for i in range(threads):
            c = threading.Thread(target=TikTok().report, args=(userId, _proxy_))
            c.start()
        for i in range(threads):
            c.join()
        stats.tit = True
    else:
        _proxy_ = None
        for i in range(threads):
            c = threading.Thread(target=TikTok().report, args=(userId, _proxy_,))
            c.start()
            c.join()
        stats.tit = True
