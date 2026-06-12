web_bookmarks = []
maximum_bookmarks = 5
while len(web_bookmarks) < maximum_bookmarks:
    web = input("Enter Web URL without https://")
    web_bookmarks.append(web)
index = 0
web_bookmarks.sort()
while index < len(web_bookmarks):
    print(f"https://{web_bookmarks[index]}")
    index += 1