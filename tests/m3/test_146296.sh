
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

# Tolerant block extractor:
#  - normalizes CRLF
#  - matches "The highest ranking book:" or "The highest-ranking book:" (hyphen tolerant)
#  - stops at the first line that starts with "Action" (case-insensitive, allows leading spaces)
extract_block() {
  tr -d '\r' | awk '
    BEGIN { IGNORECASE=1; inblk=0 }
    $0 ~ /The highest[ -]ranking book:/ { inblk=1; next }
    inblk && $0 ~ /^[[:space:]]*Action/ { exit }
    inblk { print }
  '
}

# first "Book:" line (title) within a block; allow leading spaces
first_book_line() {
  awk '/^[[:space:]]*Book:/{print; exit}'
}

is_empty_block() {
  [[ -z "${1//[[:space:]]/}" ]]
}

# ---- Generate inputs ----
if ! python input_generator.py >/dev/null 2>&1; then
    error_exit "input_generator.py failed to execute properly."
fi

[[ -f "input_2.txt" ]] || error_exit "input_2.txt not found."

catalog_num=$(sed -n '3 s/[^0-9]//gp' input_2.txt)

# Redirect student/solution stderr to keep grader output clean
expected_output=$(python mainCP.py < input_2.txt 2>/dev/null) || error_exit "Python solution script failed."
student_output=$(python main.py  < input_2.txt 2>/dev/null) || error_exit "Python script main.py failed."

# Books added to shopping cart (same logic as before)
books=$(printf '%s' "$expected_output" | awk '/All books in shopping cart:/,/The highest[ -]ranking book:/{if ($1=="Book:" || $1=="Rank:"){print; if($1=="Rank:") print ""}}')

# Extract best-seller blocks using tolerant extractor
expected=$(printf '%s' "$expected_output" | extract_block) || error_exit "Issue encountered while generating expected outcome."
returned=$(printf '%s' "$student_output"  | extract_block) || error_exit "The expected outcome was not returned."

# Compare only the first "Book:" line as an additional lenient check
expected_book=$(printf '%s' "$expected" | first_book_line)
returned_book=$(printf '%s' "$returned" | first_book_line)

# Construct message (goes into JSON, no stdout from tester)
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
# Pass if:
#  1) blocks match exactly, OR
#  2) both blocks are empty (students printed only headers), OR
#  3) the first 'Book:' line matches (title equality).
if [[ "$expected" == "$returned" ]] \
   || ( is_empty_block "$expected" && is_empty_block "$returned" ) \
   || [[ -n "$expected_book" && "$expected_book" == "$returned_book" ]]; then

    TestOutput true "$msg\n\nRESULT: Best-seller book was CORRECTLY identified.\n\nTest PASSED."
else
    TestOutput false "$msg\n\nRESULT: INCORRECT identification or an UNEXPECTED ERROR occurred.\n\nTest FAILED."
fi
