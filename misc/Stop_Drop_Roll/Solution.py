#!/usr/bin/env python3

from pwn import remote

# Mapping of scenarios to responses
from pwn import *

# Define the dictionary mapping scenarios to actions
scenario_actions = {"GORGE": "STOP", "PHREAK": "DROP", "FIRE": "ROLL"}
# Connect to the remote service
io = remote("94.237.49.212", 46304)
# Receive initial messages
io.recvuntil(b"===== THE FRAY: THE VIDEO GAME =====\nWelcome!\n")
io.recvuntil(b"Are you ready? (y/n) ")
io.sendline(b"y")
io.recvuntil(b"Ok then! Let's go!\n")
# Loop until no more scenarios are provided
while True:
    # Receive the scenario
    scenario_line = io.recvuntil(b"What do you do? ")
    # Extract the scenario
    scenario = scenario_line.split(b"\n")[0]
    # Check if the scenario is empty, indicating the end of the game
    if not scenario:
        break
    # Split the scenario into individual actions
    actions = scenario.split(b", ")
    # Map each action to its corresponding response and join them with "-"
    response = "-".join([scenario_actions[action.decode()] for action in actions])
    # Send the response
    io.sendline(response)
    
