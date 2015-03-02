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

#  Declarations and initializations
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

UpdateValues()

def UpdateValues(CoinIn) # Recieve a single coin and update all relevent counts & values
	if CoinIn == "":     # Update All Values from current Counts
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
	else                 # If no input, do nothing
		return()
		
def TotalsUpdate() # Update TotalCount and TotalValue
	CountTotalCoins = (CountQuarter + CountDime + CountNickle + CountPenny)
	ValueTotalCoins = (ValueQuarter + ValueDime + ValueNickle + ValuePenny)

		
