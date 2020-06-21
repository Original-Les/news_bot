From coding a bot that reads the news (Python tutorial) by Aaron Jack: 
src= https://www.youtube.com/watch?v=1UMHhJEaVTQ&list=PLCrU-fJHyC3sVq98fHh2h3fZXdZRv1cZi&index=12&t=0s

Build a bot that filters feeds based on interests and sends links to email.

Tools:
 - Install redis memory store
 - pip3 install python redis client
 - import requests module to fetch page
 - import beautifulsoup to parse markup


Required:

1. Need a source
  - Headless browser like Puppeteer (javascript) or Selenium (python) to handle javascript on websites
  - If the page is not javascript heavy a simple get request should do the trick

2. Run the source code through a parser
  - Allows navigation through plain text with loops
  - Interaction with the DOM eg:getElementByClass

3. Storage from the parser
  - Use eg: Redis memory store

$. From storage send via email
