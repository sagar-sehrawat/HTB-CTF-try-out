#!/usr/bin/env python3

from pwn import *


context.log_level= 'ERROR'

io = remote('83.136.255.205', 43208)

for index in range(104):
    io.sendlineafter(b': ',str(index).encode())
    res=io.recvline().decode()
    print("".join(res),end="")

io.close()

