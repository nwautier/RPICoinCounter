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



# Declarations and initializations

CountQuarter = 0
ValueQuarter = .25
CountDime = 0
ValueDime = .10
CountNickle = 0
ValueNickle = .05
CountPenny = 0
ValuePenny = .01
CountTotalCoins = (CountQuarter + CountDime + CountNickle + CountPenny)
ValueTotalCoins = (ValueQuarter + ValueDime + ValueNickle + ValuePenny)

def TotalsUpdate(): # Update TotalCount and TotalValue
	global CountQuarter
	global ValueQuarter
	global CountDime
	global ValueDime
	global CountNickle
	global ValueNickle
	global CountPenny
	global ValuePenny
	global CountTotalCoins
	global ValueTotalCoins
	CountTotalCoins = (CountQuarter + CountDime + CountNickle + CountPenny)
	ValueTotalCoins = (ValueQuarter + ValueDime + ValueNickle + ValuePenny)

TotalsUpdate()

def UpdateValues(CoinIn): # Recieve a coin, update all total counts and values
	global CountQuarter
	global ValueQuarter
	global CountDime
	global ValueDime
	global CountNickle
	global ValueNickle
	global CountPenny
	global ValuePenny
	global CountTotalCoins
	global ValueTotalCoins
	CoinIn = CoinIn.upper()
	if CoinIn == "RESET":     # Update All Values from current Counts
		ValueQuarter = (CountQuarter * .25)
		ValueDime = (CountDime * .10)
		ValueNickle = (CountNickle * .05)
		ValuePenny = (CountPenny * .01)
		TotalsUpdate()
	elif CoinIn == "Q":  # Quarter
		CountQuarter += 1
		ValueQuarter = (CountQuarter * .25)		
		TotalsUpdate()
	elif CoinIn == "D":  # Dime
		CountDime += 1
		ValueDime = (CountDime * .10)
		TotalsUpdate()
	elif CoinIn == "N":  # Nickle
		CountNickle += 1
		ValueNickle = (CountNickle * .05)
		TotalsUpdate()
	elif CoinIn == "P":  # Penny
		CountPenny += 1
		ValuePenny = (CountPenny * .01)
		TotalsUpdate()
	else:                 # If no input, do nothing
		return()

UpdateValues("RESET")

def ListCount():
		print ("Quarters")
		print (CountQuarter, ValueQuarter)
		print ("Dimes")
		print (CountDime, ValueDime)
		print ("Nickles")
		print (CountNickle, ValueNickle)
		print ("Pennies")
		print (CountPenny, ValuePenny)
		print ("Totals")
		print (CountTotalCoins, ValueTotalCoins)

global a
a="FIRST RUN"

while a:
	ListCount()
	a=input("Whatcha Got?")
	UpdateValues(a)
