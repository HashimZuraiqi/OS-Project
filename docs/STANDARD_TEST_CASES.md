# Standard Test Cases for Performance Comparison

To ensure a fair comparison between our implemented CPU scheduling algorithms in the final report, all team members should run their code using the following standard test cases. 

Record the **Average Waiting Time (AWT)** and **Average Turnaround Time (ATAT)** for each.

## Test Case 1: Simple Varied Workload
Use this to fill out the main results table in the report.

| Process | Arrival Time | Burst Time | Priority (1=High) |
| :--- | :--- | :--- | :--- |
| P1 | 0 | 10 | 3 |
| P2 | 1 | 4 | 1 |
| P3 | 2 | 5 | 4 |
| P4 | 3 | 3 | 2 |

**Settings:**
- **Round Robin:** Use Time Quantum = 2.
- **Priority:** Use the priority values above (smaller number is higher priority).

---

## Test Case 2: Convoy Effect Scenario
(Mainly for FCFS vs SJF/SRTF comparison)

| Process | Arrival Time | Burst Time |
| :--- | :--- | :--- |
| P1 | 0 | 25 |
| P2 | 1 | 2 |
| P3 | 2 | 2 |
| P4 | 3 | 2 |

---

## Instructions for Team Members:
1. Compile your algorithm.
2. Run the program and input the data from **Test Case 1**.
3. Copy the **Average Waiting Time** and **Average Turnaround Time** into our shared Results table in `docs/REPORT_DRAFT.md`.
4. (Optional) Run **Test Case 2** to see how your algorithm handles the convoy effect for the "Main Discussion" section of the report.
