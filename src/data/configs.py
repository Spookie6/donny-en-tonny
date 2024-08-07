import toml, sys

path = sys.path[0].split("\\")
path.pop()
path = "\\".join(path)

sys.path.append(path)

class Configs:
    def __init__(self):
        with open("src/data/configs.toml") as file:
            self.toml_dict = toml.load(file)

    def setData(self, name, value) -> None:
        self.toml_dict[name] = value

    def save(self):
        with open("src/data/configs.toml", "w") as file:
            toml.dump(self.toml_dict, file)