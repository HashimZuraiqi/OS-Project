# First-Come First-Served (FCFS) – CPU Scheduling Algorithm

## What is FCFS?

First-Come First-Served (FCFS) is the simplest CPU scheduling algorithm.
Processes are executed in the order they arrive in the ready queue.
Once a process starts running, it runs to completion without interruption — this is what makes it **non-preemptive**.

### Key Metrics
| Metric | Formula |
|---|---|
| Completion Time | Time when the process finishes execution |
| Turnaround Time | Completion Time − Arrival Time |
| Waiting Time | Turnaround Time − Burst Time |

---

## Files

```
faris/fcfs/
├── README.md       ← You are here
└── code/
    └── fcfs.cpp    ← FCFS implementation in C++
```

---

## Requirements

- A C++ compiler (g++ recommended)
- Works on Windows, Linux, and macOS

---

## How to Compile and Run

### Linux / macOS
Open a terminal in the `faris/fcfs/code/` directory and run:

```bash
g++ -o fcfs fcfs.cpp
./fcfs
```

### Windows
Open Command Prompt in the `faris/fcfs/code/` directory and run:

```bash
g++ -o fcfs.exe fcfs.cpp
fcfs.exe
```

---

## Expected Output

For each test case the program prints:
1. A **Gantt Chart** showing the execution timeline (including idle gaps)
2. A **Results Table** with Completion Time, Turnaround Time, and Waiting Time per process
3. **Average Turnaround Time** and **Average Waiting Time**

Example output for Test Case 4:

```
--- Gantt Chart ---
 +----------+----------+----------+----------+----------+
 |  P1      |  IDLE    |  P2      |  IDLE    |  P3      |
 +----------+----------+----------+----------+----------+
 0          4          10         13         15         20

--- FCFS Scheduling Results ---
Process Arrival Time  Burst Time  Completion Time   Turnaround Time   Waiting Time
------------------------------------------------------------------------------------
P1      0             4           4                 4                 0
P2      10            3           13                3                 0
P3      15            5           20                5                 0
------------------------------------------------------------------------------------

Average Turnaround Time : 4.00 ms
Average Waiting Time    : 0.00 ms
```

---

## Test Cases

The program includes 4 hardcoded test cases, each demonstrating a different scenario:

| # | Description | Purpose |
|---|---|---|
| 1 | All processes arrive at time 0 | Baseline — no idle time, pure ordering |
| 2 | Staggered arrival times | Shows how waiting time builds with back-to-back processes |
| 3 | Convoy effect | One long process blocks several short ones |
| 4 | CPU idle gaps | Processes arrive late, CPU sits idle between them |

---

## Notes

- Processes are sorted by arrival time before scheduling begins.
- If two processes have the same arrival time, they are scheduled in the order they appear in the code.
- The Gantt chart explicitly shows **IDLE** periods where the CPU is waiting for the next process to arrive.