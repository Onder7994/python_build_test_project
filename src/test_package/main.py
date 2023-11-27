from test_package.depends.yaml_reader import YamlReader
from test_package.depends.cli import CommandLineParser

args = CommandLineParser.create_parser().parse_args()
cmd_args = CommandLineParser(**vars(args))

read_yaml = YamlReader(cmd_args.file)

def main():
    yaml_data = read_yaml.read_yaml()
    print(yaml_data)

if __name__ == "__main__":
    main()