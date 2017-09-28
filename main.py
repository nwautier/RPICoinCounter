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
Token = []

def LoadConfig():
	ConfigFile = open("config.txt", 'r')
	# Catch "File Doesn't Exist Error", and reidrect to NewConfig() #################
	for ReadLine in ConfigFile:
		b,q,v,n = ReadLine.split(",")
		AddToken( bytes(b, 'utf-8'), int(q), Decimal(v), n[:-1] )
		# Many errors could happen here.  Cascade fix in AddToken? #################

def NewConfig(): # This block of code will erase the contents of Token and replace it with a new list of objects
	del Token[:]
	ItemCount = int(input("How many types of items do you want to count?"))
	print("")
	while (ItemCount > 0):
		TokenDefInput()
		ItemCount -= 1
		print("")

def AddToken(k, q, v, n):  # This block of code will add items to the Token Array
	TokenToAdd = [k,q,v,n]
	Token.append(TokenToAdd)

def TokenDefInput():
		print("What key would you like to bind this item to?")
		bind = getch.getch().upper()
		qty = int(input("How many of this item should we start with?"))
		value = input("How much is one unit of this item worth?")
		value = Decimal(value)
		name = input("What is the name of this item?")
		AddToken( bind, qty, value, name )

def GetKey(TokenIn): # Recieve a Token, update all total counts and values
	if TokenIn == b'R':     # Reset All Values and counts to 0
		for i in Token:
			i[1] = 0
	elif TokenIn == b'/':    # Add a new token to token configuration
		TokenDefInput()
	elif TokenIn == b'*':   # Start a new token  configuration
		NewConfig()
	elif TokenIn == b'X':   # Exit Request
		return('X')
	else:                  # If no input, do nothing
		for i in Token:
			if TokenIn == i[0]:
				i[1] += 1

def PrintList():
		os.system('cls' if os.name == 'nt' else 'clear')
		TotalTokenCount = 0
		TotalTokenValue = 0
		for i in Token:
			print (i[3]) # Print Name of selected Toekn
			TotalTokenCount += i[1]
			adder = Decimal(Decimal(i[1] * i[2]).quantize(Decimal('.01'),rounding=ROUND_HALF_UP)) # Calculate value of tokens
			print (i[1], adder)
			TotalTokenValue += adder
		print ("Total Tokens", TotalTokenCount)
		print ("Total Value", TotalTokenValue)
#		print (Token)  # DEBUG LINE # ##############################################
####################### APPLICATION STARTS RUNNING HERE ############################
a = "a"
LoadConfig()
while a != b'X':
	PrintList()
	a = getch.getch().upper()
	GetKey(a)
