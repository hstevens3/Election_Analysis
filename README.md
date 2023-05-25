# Module 3 Python Scripts

# Election_Analysis

## Overview of Election Audit

Using the starter code provided, this challenge is to produce analysis results for auditing of election data. The objective is to learn how to write and run Python scripts to read in data, loop through data and perform calculations, and output the results to the terminal window and a text file. 

## Election-Audit Results

The election results data used for the analysis included 369,711 total vote records. The voter turnout was summarized for each county and the total and percentage votes per candidate were also summarized. The output from the terminal window shows the results summary. 

- 369,711 votes were cast in this congressional election
- The counties (and percent of votes) included in the analysis are Jefferson (10.5%), Arapahoe (6.7%), and Denver (82.8%).
- Denver is the county with the largest number of votes at 306,055
- Three candidates received votes.
- The winner is Diana DeGette receiving 73.8% of the vote.

---

![Election Analysis ](/resources/terminal_output.png)

---


## Summary

This script can be expanded to summarize the results by other factors. Currently the input file contains only columns for candidate and county. If additional information was added such as precinct, state, office, etc then the vote counts can be calculated and totaled in a similar fashion as is done for candidate and county. Another option would be to use nested for loops so that the winning candidate within each county can be determined if that is of interest to see which way a county voted. 
