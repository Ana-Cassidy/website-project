from bs4 import BeautifulSoup
import requests
import pandas as pd


with open("index.html", "r") as file: 
    html_content = file.read()

# print(html_content)
    

souped_html = BeautifulSoup(html_content, "lxml")

# print(souped_html)

topics = souped_html.find_all('h4')

my_fav_things={
    "Topics": ["1st Place(gold)","2nd Place(silver)","3rd Place(bronze)"],
}

for each_topic in topics:
    # print(each_topic.text.strip())
    # topics_name.append(each_topic.text.strip())
    # names = tuple(topics_name)
    item_1 = each_topic.find_next(class_="first-item")
    item_2 = each_topic.find_next(class_="second-item")
    item_3 = each_topic.find_next(class_="third-item")
    items_in_topics=[]
    for first in item_1:
        # first_items=[]
        items_in_topics.append(first)
        # topic_first = tuple(first_items)
    for second in item_2:
        # second_items=[]
        items_in_topics.append(second)
        # topic_second = tuple(second_items)
    for third in item_3:
        # third_items=[]
        items_in_topics.append(third)
        # topic_third = tuple(third_items)
    my_fav_things[each_topic.text.strip()] = items_in_topics

df = pd.DataFrame(my_fav_things)

df.to_excel("Ana's Website.xlsx", index=False)


# print(df)
# print(names)
# print()
# print(topic_first)
# print()
# print(topic_second)
# print()
# print(topic_third)
# print(my_fav_things)
# print(topics)