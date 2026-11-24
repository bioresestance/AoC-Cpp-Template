# Generate a scaffold offline with: just new-day 1 --no-download
new-day day *args:
    uv run util/new-day.py {{day}} {{args}}

build day:
    cmake --build build --target day-$(python3 -c 'import sys; print(f"{int(sys.argv[1]):02}")' {{day}})

test day:
    cmake --build build --target day-$(python3 -c 'import sys; print(f"{int(sys.argv[1]):02}")' {{day}})
    ctest --test-dir build --output-on-failure -L '^day-0?{{day}}$' --no-tests=error

clean:
    cmake -E rm -rf build

configure:
    cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
