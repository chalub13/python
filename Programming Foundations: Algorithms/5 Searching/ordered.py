# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        # alculate the middle point
        midPt = (lowerIdx + upperIdx) // 2

        # if item is found, return the index
        if item == itemlist[midPt]:
            return midPt

        # otherwise get the next midpoint
        elif itemlist[midPt] > item:
            upperIdx = midPt - 1
        else:
            lowerIdx = midPt + 1

    if lowerIdx > upperIdx:
        return None


print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))
