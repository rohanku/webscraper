# webscraper
Python webscraper that finds the number of public pages and the number of wikipedia links on a website.

scrape.py: Iteration 1
Starts at python.org and follows all links, finding the overall average number of wikipedia links per webpage encountered. Problems included that it would start off at zero, but once it reached wikipedia it started growing and fluctuating, so the result was not particularly interesting.

scrape2.py: Iteration 2
Instead of trying to search the entire web and progressively analyze random websites, I decided to analyze specific websites since some websites would freeze the webscraper because of the massive volume of links. Essentially, users can now input certain websites into the script and python will follow all RELATIVE links, instead of exploring external links. It ultimately finds the total number of pages on the website and also counts the number of wikipedia links it finds (and saves the data to websites.csv)

websites.csv:
Stores data foud in scrape2.py.
