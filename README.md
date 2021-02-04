# Mars Facts Web Scraper

For this assignment, I was tasked with building a web application that scrapes various websites for data related to the Mission to Mars, and displaying that information in a HTML page.

I used Jupyter Notebook, BeautifulSoup, Pandas, and Splinter to scrape the data from four different webpages related to mars. The Jupyter Notebook can be found in the 'Mission to Mars' folder.

After scraping the websites, I converted my Jupyter Notebook into a python script called 'scrape_mars' where a function called 'scrape' would execute all of my code, scraping the four websites and returning the data in a single mars dictionary. 

Once the scrape function was completed, I created an app.py that would use Flask and Pymongo to call my scrape function, import the webscraping data, and store the data in a Mongo database. I defined a root route to query my Mongo database and display the data using an HTML template. I set up a single HTML file that would take my mars dictionary and display all of the data using HTML elements and bootstrap. On the final application, all data is displayed and by pressing the 'scrape for new data' button, the application would scrape all of the four websites and pull in/display any new data. 

Below are screenshots of my final application, which can also be found in the 'screenshots' folder. My python files as well as HTML template can be found in the 'Mission to Mars' folder.


<img width="1315" alt="Screen Shot 2020-12-10 at 2 09 57 PM" src="https://user-images.githubusercontent.com/69160361/101830597-fa8ce880-3af1-11eb-8ecc-0d60da0029c6.png">

<img width="1316" alt="Screen Shot 2020-12-10 at 2 10 12 PM" src="https://user-images.githubusercontent.com/69160361/101830624-09739b00-3af2-11eb-9c6f-3ad79afe86c5.png">
