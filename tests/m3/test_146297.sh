#!/bin/bash

# --- JSON-safe writer: writes 146297.json to OUTPUTS_DIR, else legacy ../outputs/146297.txt ---
function TestOutput {
    local passed="$1"
    local logs="${2:-}"

    if [[ -n "$OUTPUTS_DIR" ]]; then
        mkdir -p "$OUTPUTS_DIR"
        local dest="$OUTPUTS_DIR/146297.json"
    else
        mkdir -p ../outputs
        local dest="../outputs/146297.txt"
    fi

    # Use Python to emit valid JSON (handles quotes, backslashes, and newlines)
    printf '%s' "$logs" | python - "$passed" "$dest" <<'PY'
import json, sys
passed = sys.argv[1].lower() == "true"
dest = sys.argv[2]
log = sys.stdin.read()
with open(dest, "w", encoding="utf-8") as f:
    json.dump({"id":"146297","passed": passed, "log": log}, f)
PY
}

# ---- Helpers ----
error_exit() { TestOutput false "ERROR: $1"; exit 1; }

extract_block() {
  # lines strictly between the markers (exclusive)
  sed -n "/The highest ranking book:/,/Action/ {
    /The highest ranking book:/d
    /Action/d
    p
  }"
}

first_book_line() {
  # first "Book:" line in a block (title line)
  awk 'BEGIN{found=0} /^Book:/{print; exit}'
}

is_empty_block() {
  # true if block is empty/whitespace only
  [[ -z "${1//[[:space:]]/}" ]]
}

# ---- Generate inputs ----
if ! python input_generator.py; then
    error_exit "input_generator.py failed to execute properly."
fi

[[ -f "input_2.txt" ]] || error_exit "input_2.txt not found."

catalog_num=$(sed -n '3 s/[^0-9]//gp' input_2.txt)

expected_output=$(python mainCP.py < input_2.txt) || error_exit "Python solution script failed."
student_output=$(python main.py  < input_2.txt)  || error_exit "Python script main.py failed."

# Books added to shopping cart (same as before)
books=$(echo "$expected_output" | awk '/All books in shopping cart:/,/The highest ranking book:/ {if ($1 == "Book:" || $1 == "Rank:") {print; if ($1 == "Rank:") print ""}}')

# Extract best-seller blocks
expected=$(printf '%s' "$expected_output" | extract_block) || error_exit "Issue encountered while generating expected outcome."
returned=$(printf '%s' "$student_output"  | extract_block) || error_exit "The expected outcome was not returned."

# Optional: compare just the top "Book:" line when blocks differ
expected_book=$(printf '%s' "$expected" | first_book_line)
returned_book=$(printf '%s' "$returned" | first_book_line)

# Construct message (goes into JSON, no stdout)
msg="Testing cartBestSeller() on catalog $catalog_num...

STUDENT OUTPUT:
$student_output
-------------------------------------------
FEEDBACK:

* What this tester did:
      1. Loaded catalog $catalog_num
      2. Added the following books: 
      $books
      3. Requested the best-seller in the cart

* Expected the best-seller book information:
$expected"

# ---- Pass/fail logic ----
# Pass if the blocks match exactly,
# OR both blocks are empty,
# OR the first 'Book:' line matches (title match).
if [[ "$expected" == "$returned" ]] \
   || ( is_empty_block "$expected" && is_empty_block "$returned" ) \
   || [[ -n "$expected_book" && "$expected_book" == "$returned_book" ]]; then

    TestOutput true "$msg\n\nRESULT: Best-seller book was CORRECTLY identified.\n\nTest PASSED."
else
    TestOutput false "$msg\n\nRESULT: INCORRECT identification or an UNEXPECTED ERROR occurred.\n\nTest FAILED."
fi
