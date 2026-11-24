# AoC-Cpp-Template

Advent Of Code template for use in C++

**Project setup**

- Requires CMake 3.20+, a C++23 compiler, Python 3.12+, `uv`, and `just`.
- Open in VS Code and use the included dev container, or install the tools above locally.
- Configure and build with `just configure` and `just build 1`.
- Run one day's tests with `just test 1`; test fixtures live in `day-01/tests/part1/` and `day-01/tests/part2/` as paired `.input` and `.expected` files.

**Creating a day**

- `just new-day 1 --no-download` creates `day-01` without requiring an AoC session.
- `just new-day 1 --year 2025` creates the scaffold and downloads that year's input. The year defaults to `AOC_YEAR` or the current year.
- Set `AOC_SESSION` in a root `.env` file before downloading inputs. Never commit `.env` or `input.txt`.
- Existing day directories are not overwritten unless `--force` is passed; existing `input.txt` is preserved.

Generated solvers take `const InputFile&` and return `int64_t`. Replace the placeholder sample fixtures with actual examples and expected answers before relying on sample tests.

**Runtime options**

- `--input <path>` / `--input=<path>`: override the puzzle input file.
- `--test-dir <path>` / `--test-dir=<path>`: override the sample tests directory.
- `--skip-part1`, `--skip-part2`, `--only-part1`, `--only-part2`: choose which parts run.
- `--sample`, `--samples`, `--run-samples`: run sample fixtures only; shorthands include `--sample-part1` and `--sample-part2`.
- `--run-input`, `--input-only`, `--puzzle`: run puzzle input without GoogleTest.
- `--no-color`: disable colored result output.
