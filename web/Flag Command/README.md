# Flag Command

## Description

Embark on the "Dimensional Escape Quest" where you wake up in a mysterious forest maze that's not quite of this world. Navigate singing squirrels, mischievous nymphs, and grumpy wizards in a whimsical labyrinth that may lead to otherworldly surprises. Will you conquer the enchanted maze or find yourself lost in a different dimension of magical challenges? The journey unfolds in this mystical escape!

## Solution

The first step is to check the source code, hidden files, and comments, but in this case, nothing was found initially. I tried various payloads, suspecting a command injection vulnerability, but after some time, I intercepted the requests using developer tools (you can also use Burp Suite).

I noticed an interesting request option:

![Request Options Screenshot](https://github.com/sagar-sehrawat/HTB-CTF-try-out/blob/main/web/Flag%20Command/img1.png)

I found a secret message in this request, which seemed to be the key to escaping the forest. After entering it, I got no immediate response, so I started the game. Eventually, I got a hit and received the flag:

![Flag Screenshot](https://github.com/sagar-sehrawat/HTB-CTF-try-out/blob/main/web/Flag%20Command/img2.png)
