# JSFinder


 JSFinder Tool

This Python tool automates reconnaissance for a given URL using Katana to extract potential JavaScript files, checks their status codes with httpx, and  and shows valid JS links 
Features

    Extracts all JavaScript links from a website.
    Checks each JS link for HTTP 200 status.
    Saves valid links to js.txt file.
    Displays results in yellow text.

Usage

    Clone the repository.
    Install required tools (katana, httpx).
    Run the script:

    bash

    python jsfinder.py

Dependencies

    Katana
    Httpx
    Python 3.x
