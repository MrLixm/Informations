"""

"""
import os
import pprint
from pathlib import Path
from typing import Set

COLORS = {
    "grey": (125, 125, 125),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}


def process_image(img_path: Path):

    # check the image passed is not an already converted image
    for color in COLORS.keys():
        if img_path.stem.endswith(color):
            print(f"[process_image]         Ignoring {img_path}")
            return

    svg_content = img_path.read_text(encoding="utf-8")

    for color_name, color in COLORS.items():

        new_path = img_path.parent / f"{img_path.stem}.{color_name}.svg"
        new_svg_content = svg_content.replace("currentColor", f"rgb{color}")
        new_path.write_text(new_svg_content, encoding="utf-8")
        print(f"[process_image]     - New svg {new_path} created.")

    print(f"[process_image] Svg {img_path} finished.")
    return


def get_svgs_from_root(root_dir: Path) -> Set[Path]:
    out = set()
    for entry in os.scandir(root_dir):
        entry = Path(entry.path)
        if entry.is_dir():
            out.update(get_svgs_from_root(entry))
        elif entry.suffix == ".svg":
            out.add(entry)
    return out


def run():

    icons_root = Path("../images/icons").resolve()
    svgs_set = get_svgs_from_root(icons_root)
    for svg_path in svgs_set:
        process_image(svg_path)

    print("[run] Finished.")
    return


if __name__ == '__main__':
    run()
