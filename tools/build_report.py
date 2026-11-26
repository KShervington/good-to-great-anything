"""Fill the report template with a JSON data file.

Usage: python tools/build_report.py examples/linewright/report-data.json examples/linewright/report.html
"""
import json
import re
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "skills" / "good-to-great-anything" / "assets" / "report-template.html"
BLOCK = re.compile(r'(<script type="application/json" id="report-data">)\n.*?\n(</script>)', re.S)


def build(data_path: str, out_path: str) -> None:
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    blob = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<" + "\\" + "/")
    html, n = BLOCK.subn(lambda m: m.group(1) + "\n" + blob + "\n" + m.group(2), TEMPLATE.read_text(encoding="utf-8"))
    if n != 1:
        sys.exit("report-data block not found in template")
    Path(out_path).write_text(html, encoding="utf-8", newline="\n")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build(sys.argv[1], sys.argv[2])
