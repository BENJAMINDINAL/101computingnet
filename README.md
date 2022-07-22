# 101computingnet
Did you know that in the UK (and also in most European countries), the eggs you buy in a shop must be stamped with a code that can help you find out more about how and where your eggs were produced. This code is helpful to distinguish organic and free range eggs from eggs from more industrial production (e.g. barn or caged hen eggs).

Here is how the code works:
Python Challenge
For this challenge you will need to write a Python script that:

Takes one input from the end-user: the code as it appear on a stamped egg. (Just the code, not the Best Before Date)
Use this code to output the farming method this egg originated from: (Organic, Free range, Barn or Cage)
Output the country of Origin: e.g.:
UK: United Kingdom
NL: Netherlands
FR: France
BE: Belgium
DE: Germany
ES: Spain
Output the farm/producer ID
Extension Task #1: Defensive Design
Update your code to automatically reject any invalid code:

A valid code contains at least 7 alphanumerical characters,
A valid code should start with a number digit between 0 and 3.
Extension Task #2: Country Codes
For our code to be complete, we need to recognise all the possible two-letter country codes. We have stored the full list of country codes in the following CSV file.
