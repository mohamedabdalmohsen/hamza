def searchItems(items, search):
    if search not in items:
        print("unavailable now")
    if search == "microwave":
        print("name:microwave")
        print("price:200$")
        print("year:2022")
    if search == "rich dad poor dad":
        print("name:rich dad poor dad")
        print("price:20$")
        print("year:2015")
search = input("Search ")
items = ["microwave","rich dad poor dad"]
searchItems(items, search)
