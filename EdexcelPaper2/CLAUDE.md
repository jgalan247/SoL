# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains materials for the **Pearson Edexcel GCSE Computer Science Paper 2 (1CP2/02) — Application of Computational Thinking**, Summer 2025 exam. Total marks: 75.

It includes the question paper PDF, the mark scheme PDF, and a `Coding/` directory with six Python starter files (`Q01.py`–`Q06.py`) containing deliberately buggy or incomplete code for students to fix or complete during the exam.

## Running Code

All files are standalone Python 3 scripts with no external dependencies (only `time`, `turtle`, and `random` from the standard library). Run any file with:

```
python3 Coding/Q01.py
```

Finished answers should be saved as `Q01FINISHED.py`, `Q02FINISHED.py`, etc. in a `COMPLETED CODING` folder (per exam instructions). The original starter files in `Coding/` must not be overwritten.

## Question Summary

| File | Marks | Task Type | Description |
|------|-------|-----------|-------------|
| Q01.py | 9 | Bug fixing | Meal discount calculator — fix 9 syntax, type, name, and logic errors |
| Q02.py | 10 | Code completion | Rocket countdown timer — fill in blanks (import time, while loop, sleep) |
| Q03.py | 15 | Code reordering | String/ASCII processing — rearrange scrambled lines into correct order |
| Q04.py | 11 | Code completion | Multiplication square — write values to a file using provided constants |
| Q05.py | 15 | Code completion | Turtle graphics — draw lines and 9 coloured circles using turtle/random |
| Q06.py | 15 | Write from scratch | Record validation — validate keys and signals in a 2D array, requires a subprogram |

## Key Conventions

- The starter files use Edexcel's coding style: spaces before parentheses in function calls (e.g., `print ("hello")`), `camelCase` variable names, section divider comments, and explicit global variable declarations at the top.
- Q03's lines are deliberately scrambled — the indentation is already correct, only the line order needs changing.
- Q04 must use the provided constants (`OUT_FILE`, `COMMA`, `LF`) rather than hard-coded values.
- Q06 requires at least one user-defined subprogram and must work regardless of the number of records in `theRecords`.

## Reference Documents

- `1CP2_02_0625_QU.pdf` — Full question paper with requirements and test data
- `1CP2_02_0625_MS.pdf` — Official mark scheme with per-mark-point answers and marking guidance
