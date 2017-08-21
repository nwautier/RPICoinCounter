# RPICoinCounter
A hardware/software solution to count unsorted coins using a Raspberry PI B+.
---------------
Latest News

Release Candidate 0.1.2 is now available!
This is a fully-functioning version of the core product that runs in Python 3.x.x. (Most Recently Tested in 3.6.1)  The software is driven by an array that can be easily changed to localize to your preferred currency type, allowing the custom selection of input keys, values, and display names.

Raspberry PI is currently unsupported.  RPI support is the cornerstone of RC 0.2.0, slated for release whenever someone gets around to it.

I realize that this software isn't the most useful in the world, but it is a functional base to build on top of.
---------------
Overview

Raspberry PI is currently unsupported.  RPI support is the cornerstone of RC 0.2.0, slated for release whenever someone gets around to it.

I realize that this software isn't the most useful in the world, but it is a functional base to build on top of.
---------------
Overview
After the holiday season of 2014, I picked up an inexpensive coin sorter from my local CVS Drugstore for five bucks.  I thought it was going to be awesome to never count coins or pay a bank or Coinstar to count for me again, but then I realized that this inexpensive device is just as cheap in quality as it was in price.

Not only is there no counting function on the device, but the coin rollers aren't even correctly measured.  What should be a 50 roll of pennies overflows somewhere around 27 coins...  Instead of $10 in quarters, I end up somewhere around $8.25 when the machine starts jamming...  And occasionally, my $5 roll of dimes has close to $5.50.

I decided to do something about it.

Rather than throwing it out and buying something better, I wanted to learn to make it better myself.  I'll document my progress thorughout, but here's where I will write the software that makes the coin counter work!

Here's a link to where you can get an inexpensive sorter of your own:

http://amzn.to/2uDZ1Ng

---------------

Future Features

  Raspberry PI GPIO Support
    Activate / Deactivate motor system, integrate numerous sensors on various GPIO pin configurations
  Notify user when a coin wrapper is full
    Perhaps haulting the counting process and waiting for input to restart
    Perhaps changing the wrapper itself
  External config file
  Saving results to an external file for audit or continuous operation across multiple sessions.

---------------
As of now, this whole project is software.  I will work on building the hardware another day.

