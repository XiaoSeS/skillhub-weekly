#!/usr/bin/env python3
"""Build the SkillHub weekly report site from self-contained report files."""

from __future__ import annotations

import argparse
import json
import shutil
from html import escape
from pathlib import Path


def load_manifest(source: Path) -> tuple[str, list[dict[str, str]]]:
    manifest_path = source / "reports.json"
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    latest = payload.get("latest")
    reports = payload.get("reports")
    if not isinstance(latest, str) or not latest:
        raise ValueError("reports.json must define a non-empty latest week")
    if not isinstance(reports, list) or not reports:
        raise ValueError("reports.json must contain at least one report")

    required = {"week", "title", "period", "snapshot", "path"}
    normalized: list[dict[str, str]] = []
    for index, report in enumerate(reports):
        if not isinstance(report, dict) or not required.issubset(report):
            missing = required - set(report) if isinstance(report, dict) else required
            raise ValueError(f"report #{index + 1} is missing fields: {sorted(missing)}")
        normalized.append({key: str(report[key]) for key in required})

    weeks = {report["week"] for report in normalized}
    if latest not in weeks:
        raise ValueError(f"latest week {latest!r} is not present in reports")
    return latest, sorted(normalized, key=lambda item: item["week"], reverse=True)


def render_archive(latest: str, reports: list[dict[str, str]]) -> str:
    rows = "\n".join(
        f"""        <li>
          <div>
            <a href="./{escape(report['path'], quote=True)}">{escape(report['title'])}</a>
            <p>{escape(report['period'])} · 快照 {escape(report['snapshot'])}</p>
          </div>
          {'<span class="latest">最新</span>' if report['week'] == latest else ''}
        </li>"""
        for report in reports
    )
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>SkillHub 开源周报归档</title>
  <style>
    :root {{ color-scheme: light; --ink:#182230; --muted:#667085; --line:#d8dee8; --navy:#17365d; --bg:#edf1f5; }}
    * {{ box-sizing: border-box; }}
    body {{ margin:0; background:var(--bg); color:var(--ink); font:15px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif; }}
    main {{ width:min(760px,calc(100% - 32px)); margin:32px auto; padding:34px 38px; background:#fff; border-top:6px solid var(--navy); }}
    h1 {{ margin:0; color:var(--navy); font-size:30px; }}
    .intro {{ margin:8px 0 28px; color:var(--muted); }}
    ul {{ margin:0; padding:0; list-style:none; border-top:1px solid var(--line); }}
    li {{ display:flex; justify-content:space-between; gap:20px; padding:16px 0; border-bottom:1px solid var(--line); }}
    a {{ color:#175ea8; font-weight:750; text-underline-offset:3px; }}
    p {{ margin:3px 0 0; color:var(--muted); font-size:12px; }}
    .latest {{ align-self:flex-start; padding:2px 8px; color:#166b45; border:1px solid currentColor; border-radius:999px; font-size:11px; font-weight:800; }}
    .back {{ display:inline-block; margin-top:24px; font-size:13px; }}
    :focus-visible {{ outline:3px solid #2e79c7; outline-offset:3px; }}
    @media (max-width:600px) {{ main {{ width:100%; min-height:100vh; margin:0; padding:28px 18px; }} }}
  </style>
</head>
<body>
  <main>
    <h1>SkillHub 开源周报归档</h1>
    <p class="intro">共 {len(reports)} 期，按统计周期倒序排列。</p>
    <ul>
{rows}
    </ul>
    <a class="back" href="./">返回最新周报</a>
  </main>
</body>
</html>
"""


def build(source: Path, output: Path) -> None:
    latest, reports = load_manifest(source)
    latest_report = next(report for report in reports if report["week"] == latest)
    latest_source = source / latest_report["path"] / "index.html"
    if not latest_source.is_file():
        raise FileNotFoundError(f"latest report not found: {latest_source}")

    for report in reports:
        report_file = source / report["path"] / "index.html"
        if not report_file.is_file():
            raise FileNotFoundError(f"report not found: {report_file}")

    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(source, output)

    latest_html = latest_source.read_text(encoding="utf-8")
    latest_html = latest_html.replace('href="../../archive.html"', 'href="./archive.html"')
    (output / "index.html").write_text(latest_html, encoding="utf-8")
    (output / "archive.html").write_text(
        render_archive(latest, reports),
        encoding="utf-8",
    )
    (output / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Built {len(reports)} report(s); latest={latest}; output={output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("site"))
    parser.add_argument("--output", type=Path, default=Path("_site"))
    args = parser.parse_args()
    build(args.source.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()
