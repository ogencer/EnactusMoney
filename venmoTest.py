#!/usr/bin/python3
import subprocess

cmd = "venmo charge @BerkayAydin 2.00 \"Deneme 1 2\""

subprocess.call(cmd, shell=True)
