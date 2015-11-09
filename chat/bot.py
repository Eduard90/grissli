import re
import time
import requests
from lxml import html

class Bot(object):
    # Need better regexps ... But ... What for? It's only test, not more
    commands = [
       ('GET_TITLE', "дай мне заголовок сайта (.*)"),
       ('GET_TITLES', "дай мне все варианты заголовков с сайтов (.*)"),
       ('GET_H1', "дай мне H1 с сайта (.*)"),
       ('REMIND', "напомни мне (\w+) через (\d+) (секунд|минут)"),
    ]

    @staticmethod
    def parse_command_string(command_str):
        """
        Parse string for get command and arguments (from string)
        :param command_str:
        :return:
        """
        if command_str.startswith("Бот, "):
            for pattern in Bot.commands:
                match = re.search(pattern[1], command_str)
                if match:
                    command = pattern[0]
                    return {'command': command, 'args': [arg for arg in match.groups()]}
        return False

    @staticmethod
    def run_command(command, args):
        if command == 'GET_TITLE':
            return Bot.command_GET_TITLE(*args)
        elif command == 'GET_TITLES':
            return Bot.command_GET_TITLES(*args)
        elif command == 'GET_H1':
            return Bot.command_GET_H1(*args)
        elif command == 'REMIND':
            return Bot.command_REMIND(*args)

    @staticmethod
    def command_GET_TITLES(urls):
        urls = urls.split(',')
        titles = []
        for url in urls:
            title = Bot.command_GET_TITLE(url.strip())
            titles.append(title)
        return ", ".join(titles)

    @staticmethod
    def command_GET_TITLE(url):
        try:
            resp = requests.get(url)
            dom = html.fromstring(resp.text)
            title = dom.cssselect('title')
            title_str = ""
            if len(title):
                title_str = title[0].text

            return title_str
        except requests.RequestException:
            return "Nein :("

    @staticmethod
    def command_GET_H1(url):
        resp = requests.get(url)
        dom = html.fromstring(resp.text)
        h1 = dom.cssselect('h1')
        h1_str = "H1 не существует"
        if len(h1):
            h1_str = h1[0].text

        return h1_str

    @staticmethod
    def command_REMIND(text, delay, measure, created):
        default_sleep = 5
        cur_timestamp = int(time.time())
        created = int(created)
        delay = int(delay)
        if measure == 'секунд':
            real_delay = delay
        else:
            real_delay = delay * 60  # Minutes to seconds

        hz = created + real_delay  # Some eggs
        if cur_timestamp >= hz:
            # Return result
            return text
        else:
            # Sleep ...
            if (hz - cur_timestamp) <= default_sleep:
                time.sleep((hz - cur_timestamp))
                return text
            else:
                time.sleep(default_sleep)
                return -1