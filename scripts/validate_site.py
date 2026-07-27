#!/usr/bin/env python3
"""Validate built routes and basic accessibility hooks for the weekly site."""

from __future__ import annotations

import argparse
import json
import sys
from html.parser import HTMLParser
from pathlib import Path


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.h1_count = 0
        self.tabs = 0
        self.panels = 0
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.external_assets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        element_id = values.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)
        if tag == "h1":
            self.h1_count += 1
        if values.get("role") == "tab":
            self.tabs += 1
        if values.get("role") == "tabpanel":
            self.panels += 1
        if tag == "script" and values.get("src"):
            self.external_assets.append(values["src"] or "")
        if tag == "link" and "stylesheet" in (values.get("rel") or ""):
            self.external_assets.append(values.get("href") or "")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    required = (root / "index.html", root / "archive.html", root / ".nojekyll")
    for path in required:
        if not path.exists():
            errors.append(f"missing built route: {path}")

    manifest_path = root / "reports.json"
    if not manifest_path.is_file():
        errors.append(f"missing manifest: {manifest_path}")
        return errors

    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    latest = payload.get("latest")
    for report in payload.get("reports", []):
        report_file = root / str(report.get("path", "")) / "index.html"
        if not report_file.is_file():
            errors.append(f"missing report: {report_file}")
    if not latest:
        errors.append("manifest latest is empty")

    index_path = root / "index.html"
    if index_path.is_file():
        parser = PageParser()
        parser.feed(index_path.read_text(encoding="utf-8"))
        if parser.h1_count != 1:
            errors.append(f"latest page must contain one h1, found {parser.h1_count}")
        if parser.tabs < 4 or parser.tabs != parser.panels:
            errors.append(f"expected matching report tabs/panels, found {parser.tabs}/{parser.panels}")
        if parser.duplicate_ids:
            errors.append(f"duplicate ids: {sorted(parser.duplicate_ids)}")
        if parser.external_assets:
            errors.append(f"external assets are not allowed: {parser.external_assets}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path, nargs="?", default=Path("_site"))
    args = parser.parse_args()
    errors = validate(args.site.resolve())
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAIL: {len(errors)} error(s)")
        return 1
    print(f"PASS: {args.site.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
