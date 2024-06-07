boxes = [
    {
        "id": 0,
        "active": True
    },
    {
        "id": 1,
        "active": False
    }
]

activebox = list(filter(lambda x : x["active"], boxes))
print(activebox)

print(boxes.index(activebox[0]))