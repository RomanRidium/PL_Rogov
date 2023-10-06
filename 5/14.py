#14
s = "альбом выкинул хомяк яблоня сегодня"
for w in s.split():
    if w.startswith("а") or w.endswith("я"):
        print(w)