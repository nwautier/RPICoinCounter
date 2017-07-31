#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2015 Nicholas Wautier <nicholas dot wautier at wautierent dot com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

from decimal import *
import os
import getch

# Declarations and initializations
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # TOKEN is  a user configurable list of countable objects.  Each object is a list in itself
    # The first sub-object should be the keystroke entered to count that token type.
    # The second sub-object should be the quantity of that value that has been counted.
    # The third sub-object should be the value of a single unit of that object.
    # The fourth sub-object should be the string value name of the object being counted to be drawn on the screen.
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
Token = [["P",0,.01,"Penny"],["N",0,.05,"Nickel"],["D",0,.10,"Dime"],["Q",0,.25,"Quarter"]]

def TotalsUpdate(): # Update TotalCount and TotalValue
	global Token
	TotalCoinCount = 0
	TotalCoinValue = 0
	for i in Token:
		TotalCoinCount += Token[i][1]
		TotalValue += (Token[i][1] * Token[i][2])

def Input(CoinIn): # Recieve a coin, update all total counts and values
# In Progress
	global Token
	CoinIn = CoinIn.upper()
	if CoinIn == b'R':     # Reset All Values and counts to 0
		# Reset Code Goes Here
		return('X')
	elif CoinIn == b'X':  # Exit Request
		return('X')
	else:                 # If no input, do nothing
		for i in Token:
			if CoinIn == Token[i][0]:
				Token[i][1] += 1

def PrintList():
		os.system('cls' if os.name == 'nt' else 'clear')
		for i in Token:
			print(Token[i][3])
			print(Token[i][1], Decimal(Decimal(Token[i][1] * Token[i][2]).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)))
			print(TotalCoinCount)
			print(TotalCoinValue)
global a
a = "a"

while a != b'X':
	PrintList()
	a = getch.getch()
	Input(a)
