#!/usr/bin/env python3
"""
Gradescope-compatible test for id=146296.
Writes result to /outputs/146296.json so the runner does NOT fall back to unittest.
"""

import json, os, re, subprocess
from pathlib import Path

TEST_ID = "146296"

def write_result(passed: bool, log: str) -> None:
    # The runner patches open("/outputs/...") -> <student_dir>/__outputs__/
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
    start = "The following book matching the given title was found at catalog index"
    for ln in lines:
        if start in ln:
            in_block = True
            continue
        if in_block and ln.strip().startswith("Action"):
            break
        if in_block:
            out.append(ln)
    return "\n".join(out).strip()

def extract_index(text: str) -> str:
    m = re.search(r"The following book matching the given title was found at catalog index\s+(\d+):", text)
    return m.group(1) if m else ""

def main() -> None:
    try:
        # 1) Generate inputs
        r = run(["python", "input_generator.py"])
        if r.returncode != 0:
            write_result(False, f"ERROR: input_generator.py failed.\nSTDOUT:\n{r.stdout}\n\nSTDERR:\n{r.stderr}")
            return
        if not Path("input_1.txt").exists():
            write_result(False, "ERROR: input_1.txt not found.")
            return

        # 2) Expected (solution)
        exp = run(["python", "mainCP.py"], Path("input_1.txt"))
        if exp.returncode != 0:
            write_result(False, f"ERROR: mainCP.py failed.\nSTDOUT:\n{exp.stdout}\n\nSTDERR:\n{exp.stderr}")
            return

        # 3) Student
        stu = run(["python", "main.py"], Path("input_1.txt"))
        if stu.returncode != 0:
            write_result(False, f"ERROR: main.py failed.\nSTDOUT:\n{stu.stdout}\n\nSTDERR:\n{stu.stderr}")
            return

        # 4) Parse inputs (catalog num and title just for log)
        try:
            lines = Path("input_1.txt").read_text(encoding="utf-8").splitlines()
        except Exception as e:
            lines = []
        catalog_num = re.sub(r"\D", "", lines[2]) if len(lines) >= 3 else "?"
        title = lines[5].rstrip("\n") if len(lines) >= 6 else "?"

        expected_idx = extract_index(exp.stdout)
        returned_idx = extract_index(stu.stdout)
        expected_block = extract_block(exp.stdout)
        returned_block = extract_block(stu.stdout)

        # 5) Decide
        if expected_idx and expected_idx == returned_idx:
            if expected_block.strip() == returned_block.strip() or (not expected_block.strip() and not returned_block.strip()):
                passed = True
                reason = "Index matched; details matched or both empty."
            else:
                passed = True
                reason = "Index matched; ignoring non-critical formatting differences in details."
        else:
            passed = False
            reason = f"Incorrect or missing index (expected {expected_idx or 'n/a'}, got {returned_idx or 'n/a'})."

        # 6) Log
        log = f"""Testing idxOfTitle('{title}') on catalog {catalog_num}...

STUDENT STDOUT:
{stu.stdout}

STUDENT STDERR:
{stu.stderr}

-------------------------------------------
FEEDBACK:

* Expected index: {expected_idx}
* Returned index: {returned_idx}

* Expected matching book block:
{expected_block}

* Returned matching book block:
{returned_block}

RESULT: {"PASS" if passed else "FAIL"}
REASON: {reason}
"""
        write_result(passed, log)

    except Exception as e:
        write_result(False, f"ERROR: {e}")

if __name__ == "__main__":
    main()
