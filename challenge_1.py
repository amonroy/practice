#This is from https://www.reddit.com/r/dailyprogrammer/comments/39ws1x/20150615_challenge_218_easy_todo_list_part_1/
#Challenge #218 [Easy] To-do list (Part 1)

def addItem(list,item):
    """ this function adds an item, only works if you have a list."""
    print "I added this item: ", item
    list.append(item)

def viewList(list):
    """ this function show you your list, which you need for this to work."""
    for i in list:
        print i

def deleteItem(list,item):
    """ this function deletes an item, only works if you have a list."""
    print "I deleted this item:", item
    list.remove(item)
