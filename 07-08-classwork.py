data = { "people": [
    {"name":"Alice", "age":30, "email":"alice@email.com"},
    {"name":"Bob", "age":40, "email":"bob@email.com"},
    {"name":"Charlie", "age":50}   
]}

# print(data["people"][2])
data["people"][2]["email"] = "charlie@email.com"
# print(data["people"][2])

data["people"][1]["age"] = "41"
# print(data["people"][1])

data["people"].append({"name": "Dorothy", "age": 27, "email": "doro@email.com"})
print(data)


# text = "This is a string"
# text = text.upper()
# text = text.replace("I", "X")
# print(text)


