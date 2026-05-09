# CPU Scheduling Algorithms Performance Evaluation

This repository contains the source code and documentation for our Operating Systems project.

## Group Members
- **Faris:** FCFS implementation
- **Hashim:** SRTF implementation
- **Mohammad:** Priority Scheduling implementation
- **Nour:** Round Robin implementation
- **Zina:** SJF implementation

## Project Structure
- `docs/`: Contains the report draft (`REPORT_DRAFT.md`) and standard test cases (`STANDARD_TEST_CASES.md`).
- `[name]/[algorithm]/code/`: Each student should place their `.cpp` source file in their respective folder.

## Submission Requirements Checklist
- [ ] Implement your assigned CPU algorithm in C++.
- [ ] Run the algorithm using the data in `docs/STANDARD_TEST_CASES.md`.
- [ ] Add your results (AWT and ATAT) to the table in `docs/REPORT_DRAFT.md`.
- [ ] Ensure your section in the "Methodology" part of the report is accurate.
- [ ] Prepare the final report in MS Word and PDF format.
- [ ] Include a "Read-Me" file (this file) with the final submission.

## How to Run (General)
Each algorithm should be compiled using a C++ compiler:
```bash
g++ [filename].cpp -o [outputname]
./[outputname]
```
Follow the on-screen prompts for Arrival and Burst times.
