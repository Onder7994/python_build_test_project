import yaml
from dataclasses import dataclass

@dataclass
class YamlReader:
    yaml_path: str

    def read_yaml(self):
        with open(self.yaml_path, "r") as yaml_file:
            data = yaml.safe_load(yaml_file)
        return data
