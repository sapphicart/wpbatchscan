import subprocess
from dotenv import load_dotenv
import os
import click
import sys
from colorama import Fore

load_dotenv()

def scanner(urls:str, enum:str, output_format:str, token:str, output:bool):
    for url in urls:
        try:
            print(f"{Fore.CYAN}[*] Starting wpscan on {url}\n{Fore.RESET}")

            if output:
                res = subprocess.run([
                                "wpscan",
                                "--url", url,
                                "--enumerate", enum,
                                "--api-token", token,
                                "--follow-redirect",
                                "--disable-tls-checks",
                                "--random-user-agent",
                                "-o", f"outputs/{url.split('//', 1)[1]}",
                                "-f", output_format
                ])  
            else:
                res = subprocess.run(f"wpscan --url {url} --enumerate  {enum} --api-token  {token} --follow-redirect --disable-tls-checks --random-user-agent", shell=True)


            if res.returncode != 0:
                print(f"{Fore.RED}[-] Got error while scanning. Please see the log/output for more details.{Fore.RESET}\n")
                continue
            else:
                print(f"{Fore.GREEN}[+] {url} scan completed successfully!{Fore.RESET}")

            if output:
                print(f"{Fore.GREEN}[+] Scan results written to outputs/{url.split('//', 2)[1]}{Fore.RESET}")

        except KeyboardInterrupt:
            print(f"{Fore.YELLOW}[*] Scan aborted by user.{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}[-] An error occured in scanner: {e}{Fore.RESET}")
            sys.exit(1)



@click.command()
@click.option('-u', '--url', help='/path/to/file/containing_urls_to_scan. Required.')
@click.option('-e', '--enum', help='Enumerate plugins, themes and users. Default "vp,vt,u"', default='vp,u,vt')
@click.option('-f', '--format', help='Output format. Choose from options json, cli, cli-no-color. Default "json"', default='json')
@click.option('--cli', help='Use this option if you do not want to output the scan results in specified format.', is_flag=True, default=False)
def main(url, enum, format, cli):
    urls = []
    
    try:
        filename = url
        token = os.getenv('API_TOKEN')

        if not token:
            print(f"{Fore.RED}[-] Error. API Token not found. Please find a free token at {Fore.CYAN}https://wpscan.com{Fore.RESET}.\n{Fore.YELLOW}[*] If you already have a token, please create a .env file with the value API_TOKEN=<your token>{Fore.RESET}")
            sys.exit(1)
        elif not filename:
            print(f"{Fore.RED}[-] Could not parse url file. Did you forget to provide a filename?{Fore.RESET}")
            sys.exit(1)
    

        with open(filename, "r") as f:
            for line in f.readlines():
                urls.append(line.strip())

    except FileNotFoundError as e:
        print(f"{Fore.RED}[-] Error: {e}{Fore.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}[-] An error occured: {e}{Fore.RESET}")
        sys.exit(1)

    
    try:
        if cli:
            scanner(urls, enum, format, token, output=False)
        else:
            scanner(urls, enum, format, token, output=True)
    except Exception as e:
        print(f"{Fore.RED}[-] An error occured: {e}{Fore.RESET}")
        sys.exit(1)



if __name__=="__main__":
    main()

