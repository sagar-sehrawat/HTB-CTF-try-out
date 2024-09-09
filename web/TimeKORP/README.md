# TimeKORP

## Description

Are you ready to unravel the mysteries and expose the truth hidden within KROP's digital domain? Join the challenge and prove your prowess in the world of cybersecurity. Remember, time is money, but in this case, the rewards may be far greater than you imagine.

## Solution

First, check out the site:

![Site Screenshot](https://github.com/sagar-sehrawat/HTB-CTF-try-out/blob/main/web/TimeKORP/site.png)

After examining all the files, I found something interesting in the `#TimeModel.php` file:

![TimeModel.php Screenshot](https://github.com/sagar-sehrawat/HTB-CTF-try-out/blob/main/web/TimeKORP/cmd.png)

It executes the `date` command, which is a sign of a command injection vulnerability.

I tried different payloads and successfully got a hit with this approach.
