# import toml

# toml_dict = None

# with open("./test.toml") as file:
#     toml_dict = toml.load(file)
    
# print(toml_dict["resolution"])
# toml_dict["resolution"] = [1280, 720]
# print(toml_dict["resolution"])

# with open("./test.toml", "w") as file:
#     toml.dump(toml_dict, file)

RESOLUTIONS = ([1280, 720], [1920, 1080], [2560, 1440])
str = "1440"

for res in RESOLUTIONS:
    if int(str) in res:
        print(res)