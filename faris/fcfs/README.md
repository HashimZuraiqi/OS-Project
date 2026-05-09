# First-Come First-Served (FCFS) – CPU Scheduling Algorithm

## What is FCFS?

First-Come First-Served (FCFS) is the simplest CPU scheduling algorithm.

- Processes are executed in the order they arrive in the ready queue.
- Once a process starts running, it runs to completion without interruption — this is what makes it non-preemptive.

## Key Metrics

| Metric | Formula |
|--------|---------|
| Completion Time | Time when the process finishes execution |
| Turnaround Time | Completion Time − Arrival Time |
| Waiting Time | Turnaround Time − Burst Time |

## Files

```
faris/fcfs/
├── README.md       ← You are here
└── FCFS.cpp        ← FCFS implementation in C++
```

## Requirements

- A C++ compiler (g++ recommended)
- Works on Windows, Linux, and macOS

## How to Compile and Run

### Linux / macOS

Open a terminal in the `faris/fcfs/` directory and run:

```bash
g++ -o fcfs FCFS.cpp
./fcfs
```

### Windows

Open Command Prompt in the `faris/fcfs/` directory and run:

```bash
g++ -o fcfs.exe FCFS.cpp
fcfs.exe
```

## Usage

When the program starts, it will ask you to choose a mode:

```
Hello user, if you want to use ur own input for testing the algorothim please enter 1, else (Hardcoded test cases) enter 2:
```

### Option 1 – Custom Input

Enter your own processes at runtime. The program will ask for the number of processes, then for each process enter its ID, Arrival Time, and Burst Time separated by spaces.

**Example:**

```
Enter the number of processes: 3
Enter Process ID, Arrival Time, and Burst Time for Process (in order) 1: P1 0 5
Enter Process ID, Arrival Time, and Burst Time for Process (in order) 2: P2 2 3
Enter Process ID, Arrival Time, and Burst Time for Process (in order) 3: P3 4 8
```

### Option 2 – Hardcoded Test Cases

Runs 3 predefined test cases automatically. See the Test Cases section below for details.

## Expected Output

For each test case the program prints:

- A Gantt Chart showing the execution timeline (including idle gaps)
- A Results Table with Completion Time, Turnaround Time, and Waiting Time per process
- Average Turnaround Time and Average Waiting Time

**Example output for Test Case 3:**
 Test Case 3: CPU Idle Gaps

```
Gantt Chart:
 +----------+----------+----------+----------+----------+----------+----------+
 |  P1      |  IDLE    |  P2      |  IDLE    |  P3      |  IDLE    |  P4      |
 +----------+----------+----------+----------+----------+----------+----------+
 0          5          8          11         12         19         20         24
```

| Process | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time |
|---------|--------------|------------|-----------------|-----------------|--------------|
| P1      | 0            | 5          | 5               | 5               | 0            |
| P2      | 8            | 3          | 11              | 3               | 0            |
| P3      | 12           | 7          | 19              | 7               | 0            |
| P4      | 20           | 4          | 24              | 4               | 0            |

```
Average Turnaround Time : 4.75 ms
Average Waiting Time    : 0.00 ms
```

## Test Cases

The program includes 3 hardcoded test cases (Option 2), each demonstrating a different scenario:

| # | Description | Purpose |
|---|-------------|---------|
| 1 | General Mixed Case | Staggered arrivals with varied burst times — typical workload |
| 2 | Convoy Effect | One long process blocks several short ones |
| 3 | CPU Idle Gaps | Processes arrive late, CPU sits idle between them |

## Notes

- Processes are sorted by arrival time before scheduling begins.
- If two processes have the same arrival time, they are scheduled in the order they were entered.
- The Gantt chart explicitly shows IDLE periods where the CPU is waiting for the next process to arrive.
- If an invalid option is entered (not 1 or 2), the program will display an error message and exit.

## References

- A. Silberschatz, P. B. Galvin, and G. Gagne, Operating System Concepts, 10th ed. Hoboken, NJ: Wiley, 2018.
- W. Stallings, Operating Systems: Internals and Design Principles, 9th ed. Pearson, 2018.
- GeeksforGeeks, "First Come First Serve (FCFS) CPU Scheduling Algorithm", [Online]. Available: https://www.geeksforgeeks.org/first-come-first-serve-cpu-scheduling-non-preemptive/