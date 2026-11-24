# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "advent-of-code-data",
#     "jinja2",
#     "python-dotenv",
# ]
# ///
"""Generate a day scaffold, optionally downloading its puzzle input."""

from __future__ import annotations

import argparse
import os
import shutil
from datetime import date
from pathlib import Path

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "cpp-day-template"


def create_new_day(day: int, *, force: bool = False) -> Path:
    target = ROOT / f"day-{day:02d}"
    if target.exists() and not force:
        raise FileExistsError(f"{target.name} already exists (use --force to update scaffold files)")

    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)), autoescape=False)
    skip_dirs = {"partials"}
    for root, dirs, files in os.walk(TEMPLATE_DIR):
        dirs[:] = [directory for directory in dirs if directory not in skip_dirs]
        relative = Path(root).relative_to(TEMPLATE_DIR)
        output_dir = target / relative
        output_dir.mkdir(parents=True, exist_ok=True)

        for filename in files:
            template_path = Path(root) / filename
            output_path = output_dir / filename
            if filename.endswith(".j2"):
                output_path = output_path.with_suffix("")
                if output_path.exists() and not force:
                    raise FileExistsError(f"{output_path} exists (use --force to update scaffold files)")
                output_path.write_text(
                    env.get_template(str((relative / filename).as_posix())).render(day=day),
                    encoding="utf-8",
                )
            elif not output_path.exists() or force:
                shutil.copy2(template_path, output_path)
    return target


def download_input(day: int, year: int, target: Path) -> None:
    from aocd import get_data

    input_path = target / "input.txt"
    if input_path.exists():
        raise FileExistsError(f"{input_path} already exists; refusing to overwrite puzzle input")
    data = get_data(day=day, year=year)
    input_path.write_text(data, encoding="utf-8")


def main() -> int:
    load_dotenv(ROOT / ".env")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("day", type=int, help="puzzle day (1-25)")
    parser.add_argument(
        "--year", type=int,
        default=int(os.environ.get("AOC_YEAR", date.today().year)),
        help="Advent of Code year (default: AOC_YEAR or current year)",
    )
    parser.add_argument("--no-download", action="store_true", help="create scaffold without fetching input")
    parser.add_argument("--force", action="store_true", help="overwrite scaffold files; preserve existing input.txt")
    args = parser.parse_args()
    if not 1 <= args.day <= 25:
        parser.error("day must be between 1 and 25")
    if not 2015 <= args.year <= date.today().year:
        parser.error(f"year must be between 2015 and {date.today().year}")

    try:
        target = create_new_day(args.day, force=args.force)
        if not args.no_download:
            download_input(args.day, args.year, target)
    except Exception as exc:
        parser.exit(1, f"error: {exc}\n")
    print(f"Created {target.relative_to(ROOT)} for AoC {args.year}.")
    if args.no_download:
        print("No puzzle input downloaded; add your input.txt when available.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
