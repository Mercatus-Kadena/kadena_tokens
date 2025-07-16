import yaml
from pathlib import Path
import sys
import magic

class UniqueKeyLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        mapping = set()
        for key_node, value_node in node.value:
            if ':merge' in key_node.tag:
                continue
            key = self.construct_object(key_node, deep=deep)
            if key in mapping:
                raise ValueError(f"Duplicate {key!r} key found in YAML.")
            mapping.add(key)
        return super().construct_mapping(node, deep)


try:
    with open("../tokens.yaml") as fd:
        data = yaml.load(fd, Loader=UniqueKeyLoader)
except Exception as ex:
    print("Error when parsing YAML file")
    print(str(ex))
    sys.exit(1)




mainnet = data["development"]

failure = False

for token_mod, token in mainnet.items():
    if "name" not in token:
        print("{:s} - token name missing".format(token_mod))
        failure = True
        continue

    token_name = token["name"]

    if "symbol" not in token:
        print("Token {:s} - symbol missing".format(token_name))
        failure = True
        continue

    img = Path("..", token["img"])
    if not img.exists():
        print("Token {:s} - Image missing: {!s}".format(token_name, img))
        failure = True
        continue

    img_type = magic.from_file(img, mime=True)
    if not img_type.startswith("image"):
        failure = True
        print("Token {:s} - Invalid image: {!s}".format(token_name, img))

    if img.stat().st_size > 100000:
        print("Token {:s} - Image file > 100 kB: {!s}".format(token_name, img))
        failure = True

    if "precision" not in token or not isinstance(token["precision"], int):
        failure = True
        print("Token {:s} - Precision invalid".format(token_name))

    if "socials" not in token or not isinstance(token["socials"], list):
        failure = True
        print("Token {:s} - Invalid Socials".format(token_name))
    else:
        for soc_item in token["socials"]:
            if soc_item.get("type", "") not in ["website", "github", "twitter", "discord", "telegram", "reddit"]:
                print("Token {:s} - Invalid Social item: {!s}".format(token_name, soc_item))
                failure = True
            if "url" not in soc_item:
                print("Token {:s} - Invalid Social item: {!s}".format(token_name, soc_item))

                failure = True

if not failure:
    print("Token Database Valid")
    sys.exit(0)
else:
    sys.exit(1)
