"""Validate local profile links and SVG assets without external dependencies."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


def main():
    root = Path(__file__).resolve().parents[2]
    readme = (root / "README.md").read_text(encoding="utf-8")
    references = re.findall(r'(?:src|href)="([^"]+)"', readme)
    references += re.findall(r"\]\(([^)]+)\)", readme)
    checked = 0
    for reference in references:
        url = urlsplit(reference)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (root / unquote(url.path)).resolve()
        if not target.is_relative_to(root) or not target.is_file():
            raise ValueError(f"Invalid local reference: {reference}")
        checked += 1
    for asset in (root / "assets").rglob("*.svg"):
        ET.parse(asset)
    print(f"PROFILE_ASSETS_OK references={checked}")


if __name__ == "__main__":
    main()
