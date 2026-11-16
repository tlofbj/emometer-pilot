import argparse
import json
import os
import tempfile


def format_json(path, indent):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    # Write to a temp file first so a failure can't leave the original truncated.
    directory = os.path.dirname(os.path.abspath(path))
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=directory, delete=False, suffix=".tmp"
    ) as tmp:
        json.dump(data, tmp, indent=indent, ensure_ascii=False)
        tmp.write("\n")
    os.replace(tmp.name, path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pretty-print a JSON file in place.")
    parser.add_argument("path", nargs="?", default="words.json")
    parser.add_argument("--indent", type=int, default=2)
    args = parser.parse_args()

    format_json(args.path, args.indent)
    print(f"Formatted {args.path} with indent={args.indent}")
