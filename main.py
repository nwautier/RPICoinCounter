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
global CountQuarter
CountQuarter = 0
global ValueQuarter
ValueQuarter = .25
global CountDime
CountDime = 0
global ValueDime
ValueDime = .10
global CountNickle
CountNickle = 0
global ValueNickle
ValueNickle = .05
global CountPenny
CountPenny = 0
global ValuePenny
ValuePenny = .01
global CountTotalCoins
CountTotalCoins = (CountQuarter + CountDime + CountNickle + CountPenny)
global ValueTotalCoins
ValueTotalCoins = (ValueQuarter + ValueDime + ValueNickle + ValuePenny)



def TotalsUpdate(): # Update TotalCount and TotalValue
	CountTotalCoins = (CountQuarter + CountDime + CountNickle + CountPenny)
	ValueTotalCoins = (ValueQuarter + ValueDime + ValueNickle + ValuePenny)

TotalsUpdate()

def UpdateValues(CoinIn): # Recieve a coin, update all total counts and values
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
		ValueDime = (CountDime * .25)
		TotalsUpdate()
	elif CoinIn == "N":  # Nickle
		CountNickle += 1
		ValueNickle = (CountNickle * .25)
		TotalsUpdate()
	elif CoinIn == "P":  # Penny
		CountPenny += 1
		ValuePenny = (CountPenny * .25)
		TotalsUpdate()
	else:                 # If no input, do nothing
		return()

def ListCount():
		print ("  Q    D    N    P  ")
		print ("  %s    %s    %s    %s  ") % (CountQuarter, CountDime, CountNickle, CountPenny)


global a
a="FIRST RUN"

while a:
	ListCount()
	a=input("Whatcha Got?")
	UpdateValues(a)
