# Stop Drop and Roll

## Description

The Fray: The Video Game is one of the greatest hits of the last... well, we don't remember quite how long. Our "computers" these days can't run much more than that, and it has a tendency to get repetitive...

## Solution

In this challenge, you have a script running on a server. Use `nc` (netcat) to interact with it. The script will ask you to send responses based on certain keywords:

- If you see `GORGE`, send back `STOP`.
- If you see `PHREAK`, send back `DROP`.
- If you see `FIRE`, send back `ROLL`.

Sometimes, you may receive multiple keywords at once. For example: `GORGE, FIRE, PHREAK`. In this case, send back `STOP, ROLL, DROP`.

Manually solving this can be very time-consuming. Instead, you can use Python to automate the process by running a solution script in parallel. Additionally, open Wireshark to monitor the packets. After waiting 3-4 minutes, follow the stream and use a filter to search for `HTB` to find the flag.

![Terminal Image](https://github.com/sagar-sehrawat/HTB-CTF-try-out/blob/main/misc/Stop_Drop_Roll/img/Terminal.png)

Here's the solution image for reference:

![Wireshark Image](https://github.com/sagar-sehrawat/HTB-CTF-try-out/blob/main/misc/Stop_Drop_Roll/img/wireshark.png)

## Flag

`HTB{1_wiLl_sT0p_dR0p_4nD_r0Ll_mY_w4Y_oUt!}`
