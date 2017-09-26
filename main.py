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
    # TOKEN is a user configurable list of countable objects.  Each object is a list in itself
    # The first sub-object should be the keystroke entered to count that token type.
    # The second sub-object should be the quantity of that value that has been counted.
    # The third sub-object should be the value of a single unit of that object.
    # The fourth sub-object should be the string value name of the object being counted to be drawn on the screen.
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
Token = [[b'P',0,.01,"Penny"],[b'N',0,.05,"Nickel"],[b'D',0,.10,"Dime"],[b'Q',0,.25,"Quarter"]]

#def LoadConfig(): # NOT READY FOR THIS YET ########################################
#	ConfigFile = open("config.txt", 'r')
#	for ReadLine in ConfigFile:
#		AppendLine = ReadLine.split(',')
#		Token.append(AppendLine)
def NewConfig(): # This block of code will erase the contents of Token and replace it with a new list of objects
	ItemCount = int(input("How many types of items do you want to count?"))
	while (ItemCount > 0):
		bind = input("What key would you like to bind this item to?")
		qty = int(input("How many of this item should we start with?"))
		value = Decimal(input("How much is one unit of this item worth?"))
		name = input("What is the name of this item?")
		# AddToken( bind, qty, value, name ) ###############################################################
		ItemCount -= 1
def AddToken(K, int(Q), Decimal(v), N):  # This block f code will add items to the Token Array
############################ WRITE THIS ####################################################################

def GetKey(CoinIn): # Recieve a coin, update all total counts and values
	if CoinIn == b'R':     # Reset All Values and counts to 0
		for i in Token:
			i[1] = 0
	elif CoinIn == b'*':
		NewConfig()
	elif CoinIn == b'X':   # Exit Request
		return('X')
	else:                 # If no input, do nothing
		for i in Token:
			if CoinIn == i[0]:
				i[1] += 1

def PrintList():
		os.system('cls' if os.name == 'nt' else 'clear')
		TotalCoinCount = 0
		TotalCoinValue = 0
		for i in Token:
			print (i[3])
			TotalCoinCount += i[1]
			adder = Decimal(Decimal(i[1] * i[2]).quantize(Decimal('.01'),rounding=ROUND_HALF_UP))
			print (i[1], adder)
			TotalCoinValue += adder
		print ("Total Coins", TotalCoinCount)
		print ("Total Value", TotalCoinValue)
		print (Token)  # DEBUG LINE # ##############################################

a = "a"
# LoadConfig() # DEBUG LINE # ######################################################
print (Token)  # DEBUG LINE # ######################################################
while a != b'X':
	PrintList() # DEBUG LINE # #####################################################
	a = getch.getch().upper()
	GetKey(a)
