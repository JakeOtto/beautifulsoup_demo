#bs demo
# Import the necessary libraries
from bs4 import BeautifulSoup

# Sample HTML content (you can replace this with actual web content)
html_content = """
<html>
<head>
    <title>Sample Web Page</title>
</head>
<body>
    <h1>Welcome to Beautiful Soup Demo</h1>
    <p>This is a simple example of using Beautiful Soup.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
</body>
</html>
"""

# Create a Beautiful Soup object by parsing the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Example 1: Extracting and printing the title of the web page
title = soup.title
print("Web Page Title:", title.text)

# Example 2: Extracting and printing the text within a specific <p> tag
paragraph = soup.find('p')
print("Paragraph Text:", paragraph.text)

# Example 3: Extracting and printing all the items in the <ul> list
list_items = soup.find('ul').find_all('li')
print("List Items:")
for item in list_items:
    print(item.text)


