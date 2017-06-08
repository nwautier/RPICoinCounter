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

TotalCoinCount = 0
TotalCoinValue = 0
TotalsUpdate()

def TotalsUpdate(): # Update TotalCount and TotalValue
	global Token
	TotalCoinCount = 0
	TotalCoinValue = 0
	for i in Token:
		TotalCoinCount += Token[1][i]
		TotalValue += Token[1][i] * Token[2][i]
#############################

def UpdateValues(CoinIn): # Recieve a coin, update all total counts and values
	global Token
	CoinIn = CoinIn.upper()
	if CoinIn == b'R':     # Reset All Values and counts to 0
		CountQuarter = 0
		CountDime = 0
		CountNickel = 0
		CountPenny = 0
		ValueQuarter = (CountQuarter * .25)
		ValueDime = (CountDime * .10)
		ValueNickel = (CountNickel * .05)
		ValuePenny = (CountPenny * .01)
		TotalsUpdate()
	elif CoinIn == b'Q':  # Quarter
		CountQuarter += 1
		ValueQuarter = (CountQuarter * .25)
		TotalsUpdate()
	elif CoinIn == b'D':  # Dime
		CountDime += 1
		ValueDime = (CountDime * .10)
		TotalsUpdate()
	elif CoinIn == b'N':  # Nickels
		CountNickel += 1
		ValueNickel = CountNickel * .05
		TotalsUpdate()
	elif CoinIn == b'P':  # Penny
		CountPenny += 1
		ValuePenny = (CountPenny * .01)
		TotalsUpdate()
	elif CoinIn == b'X':  # Exit Request
		return('X')
	else:                 # If no input, do nothing
		return()

UpdateValues("R")
def ListCount():
		os.system('cls' if os.name == 'nt' else 'clear')
		print ("Quarters")
		print (CountQuarter, Decimal(Decimal(ValueQuarter).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
		print ("Dimes")
		print (CountDime, Decimal(Decimal(ValueDime).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
		print ("Nickels")
		print (CountNickel, Decimal(Decimal(ValueNickel).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
		print ("Pennies")
		print (CountPenny, Decimal(Decimal(ValuePenny).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
		print ("Totals")
		print (CountTotalCoins, Decimal(Decimal(ValueTotalCoins).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))

global a
a = "a"

while a != b'X':
	ListCount()
	a = getch.getch()
	UpdateValues(a)
