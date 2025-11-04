#!/usr/bin/env python3
"""
Gradescope-compatible test for id=146297.
Writes result to /outputs/146297.json so the runner does NOT fall back to unittest.
"""

import json, os, re, subprocess
from pathlib import Path

TEST_ID = "146297"

def write_result(passed: bool, log: str) -> None:
    if not log.strip():
        log = "(no log captured)"
    with open(f"/outputs/{TEST_ID}.json", "w", encoding="utf-8") as f:
        json.dump({"id": TEST_ID, "passed": bool(passed), "log": log}, f)

def run(cmd, stdin_path: Path | None = None):
    return subprocess.run(
        cmd,
        stdin=(open(stdin_path, "r", encoding="utf-8") if stdin_path else None),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

def extract_block(text: str) -> str:
    lines = text.splitlines()
    out, in_block = [], False
    # tolerant of "highest-ranking" vs "highest ranking"
    start_re = re.compile(r"The highest[ -]ranking book:", re.IGNORECASE)
    for ln in lines:
        if start_re.search(ln):
            in_block = True
            continue
        if in_block and re.match(r"^\s*Action", ln, re.IGNORECASE):
            break
        if in_block:
            out.append(ln)
    return "\n".join(out).strip()

def first_book_line(block: str) -> str:
    for ln in block.splitlines():
        if ln.strip().startswith("Book:"):
            return ln.strip()
    return ""

def is_empty(block: str) -> bool:
    return block.strip() == ""

def main() -> None:
    try:
        # 1) Generate inputs
        r = run(["python", "input_generator.py"])
        if r.returncode != 0:
            write_result(False, f"ERROR: input_generator.py failed.\nSTDOUT:\n{r.stdout}\n\nSTDERR:\n{r.stderr}")
            return
        if not Path("input_2.txt").exists():
            write_result(False, "ERROR: input_2.txt not found.")
            return

        # 2) Expected (solution)
        exp = run(["python", "mainCP.py"], Path("input_2.txt"))
        if exp.returncode != 0:
            write_result(False, f"ERROR: mainCP.py failed.\nSTDOUT:\n{exp.stdout}\n\nSTDERR:\n{exp.stderr}")
            return

        # 3) Student
        stu = run(["python", "main.py"], Path("input_2.txt"))
        if stu.returncode != 0:
            write_result(False, f"ERROR: main.py failed.\nSTDOUT:\n{stu.stdout}\n\nSTDERR:\n{stu.stderr}")
            return

        # 4) Extract data
        try:
            lines = Path("input_2.txt").read_text(encoding="utf-8").splitlines()
            catalog_num = re.sub(r"\D", "", lines[2]) if len(lines) >= 3 else "?"
        except Exception:
            catalog_num = "?"

        books_section = []
        in_cart = False
        for ln in exp.stdout.splitlines():
            if "All books in shopping cart:" in ln:
                in_cart = True
                continue
            if in_cart and re.search(r"The highest[ -]ranking book:", ln, re.IGNORECASE):
                break
            if in_cart and (ln.strip().startswith("Book:") or ln.strip().startswith("Rank:")):
                books_section.append(ln)
                if ln.strip().startswith("Rank:"):
                    books_section.append("")  # blank line like awk did
        books_text = "\n".join(books_section)

        expected_block = extract_block(exp.stdout)
        returned_block = extract_block(stu.stdout)
        expected_book = first_book_line(expected_block)
        returned_book = first_book_line(returned_block)

        # 5) Decide
        if expected_block == returned_block:
            passed = True
            reason = "Blocks matched exactly."
        elif is_empty(expected_block) and is_empty(returned_block):
            passed = True
            reason = "Both blocks empty; treated as formatting-only difference."
        elif expected_book and expected_book == returned_book:
            passed = True
            reason = "Best-seller title matched."
        else:
            passed = False
            reason = "Output mismatch (book block or title differ)."

        # 6) Log
        log = f"""Testing cartBestSeller() on catalog {catalog_num}...

STUDENT STDOUT:
{stu.stdout}

STUDENT STDERR:
{stu.stderr}

-------------------------------------------
FEEDBACK:

* What this tester did:
      1. Loaded catalog {catalog_num}
      2. Added the following books:
{books_text}
      3. Requested the best-seller in the cart

* Expected best-seller block:
{expected_block}

* Returned best-seller block:
{returned_block}

* Expected first 'Book:' line: {expected_book}
* Returned first 'Book:' line: {returned_book}

RESULT: {"PASS" if passed else "FAIL"}
REASON: {reason}
"""
        write_result(passed, log)

    except Exception as e:
        write_result(False, f"ERROR: {e}")

if __name__ == "__main__":
    main()
