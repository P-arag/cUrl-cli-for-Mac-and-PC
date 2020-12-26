from colorama import init
import pyfiglet
from termcolor import colored
import click
import requests
import json as json_module
from bs4 import BeautifulSoup


@click.command()
@click.option('--url', '-u')
@click.option("--json/--not-json", default=True)
def main(url, json):
    init()
    headline = colored(pyfiglet.figlet_format("c U r l"), "magenta")
    print(headline)

    print(colored("Getting " + url + " .............", "green"))
    content = get(url, json)
    if content is not None:
        print(colored(content, "yellow"))


def get(url, json):
    if url is not None:
        try:
            page = requests.get(url)
            if json is True:
                return json_module.dumps(page.json(), indent=4)
            else:
                soup = BeautifulSoup(page.content, "html.parser")
                return soup.prettify()

        except requests.exceptions.RequestException as err:
            print(colored(err, "red"))
    else:
        print(colored("No url found!!!!, try  curl -u <url>"))


if __name__ == "__main__":
    main()
