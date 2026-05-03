# Shortest-Remaining-Time-First (SRTF) – Preemptive

**Student:** Hashim  
**Algorithm:** Shortest-Remaining-Time-First (Preemptive)  
**Course:** CS11335 Operating Systems – Princess Sumaya University  

---

## What is SRTF?

SRTF is the preemptive version of Shortest-Job-First (SJF). At every time unit, the CPU picks the process with the **shortest remaining burst time**. If a new process arrives with a shorter burst time than what's currently running, the CPU switches to it (preemption).

### Key Metrics

| Metric | Formula |
|---|---|
| Turnaround Time | Completion Time − Arrival Time |
| Waiting Time | Turnaround Time − Burst Time |

---

## Code Structure

```
srtf.cpp
├── class Process        → holds process info (id, arrival, burst, remaining, ...)
└── main()
    ├── read input        → ask user for n processes
    ├── SRTF loop         → 1 time unit at a time, pick shortest remaining
    └── print results     → table + averages + context switches
```

---

## How to Compile & Run

**Requires:** g++ compiler (MinGW on Windows)

```bash
cd hashim/srtf/code
g++ -o srtf srtf.cpp
srtf.exe
```

> **No compiler?** Paste the code into [https://www.onlinegdb.com/online_c++_compiler](https://www.onlinegdb.com/online_c++_compiler) and click Run.

---

## How to Test

When the program runs it will ask for input. Enter the number of processes, then for each process enter the arrival time and burst time.

### Test Case 1 – Basic Test

**Input to enter:**
```
5
0
5
1
3
2
8
3
6
4
2
```

**Expected Output:**
```
---------------------------------------------------------------
PID     Arrival Burst   Completion      Turnaround      Waiting
---------------------------------------------------------------
P1      0       5       10              10              5
P2      1       3       4               3               0
P3      2       8       24              22              14
P4      3       6       16              13              7
P5      4       2       6               2               0
---------------------------------------------------------------
Average Turnaround Time : 10.00
Average Waiting Time    : 5.20
Total Context Switches  : 1
```

---

### Test Case 2 – All Arrive at t=0 (Varying Burst Times)

**Input to enter:**
```
5
0
10
0
1
0
2
0
3
0
4
```

**Expected Output:**
```
---------------------------------------------------------------
PID     Arrival Burst   Completion      Turnaround      Waiting
---------------------------------------------------------------
P1      0       10      20              20              10
P2      0       1       1               1               0
P3      0       2       3               3               1
P4      0       3       6               6               3
P5      0       4       10              10              6
---------------------------------------------------------------
Average Turnaround Time : 8.00
Average Waiting Time    : 4.00
Total Context Switches  : 0
```

---

### Test Case 3 – Sequential Arrivals

**Input to enter:**
```
5
0
4
2
3
4
2
6
5
8
1
```

**Expected Output:**
```
---------------------------------------------------------------
PID     Arrival Burst   Completion      Turnaround      Waiting
---------------------------------------------------------------
P1      0       4       4               4               0
P2      2       3       9               7               4
P3      4       2       6               2               0
P4      6       5       15              9               4
P5      8       1       10              2               1
---------------------------------------------------------------
Average Turnaround Time : 4.80
Average Waiting Time    : 1.80
Total Context Switches  : 0
```

---

### Test Case 4 – All Arrive at Same Time

**Input to enter:**
```
5
0
8
0
6
0
4
0
2
0
5
```

**Expected Output:**
```
---------------------------------------------------------------
PID     Arrival Burst   Completion      Turnaround      Waiting
---------------------------------------------------------------
P1      0       8       25              25              17
P2      0       6       17              17              11
P3      0       4       6               6               2
P4      0       2       2               2               0
P5      0       5       11              11              6
---------------------------------------------------------------
Average Turnaround Time : 12.20
Average Waiting Time    : 7.20
Total Context Switches  : 0
```

---

### Test Case 5 – Random Arrivals

**Input to enter:**
```
5
1
7
0
5
3
3
2
4
4
2
```

**Expected Output:**
```
---------------------------------------------------------------
PID     Arrival Burst   Completion      Turnaround      Waiting
---------------------------------------------------------------
P1      1       7       21              20              13
P2      0       5       5               5               0
P3      3       3       10              7               4
P4      2       4       14              12              8
P5      4       2       7               3               1
---------------------------------------------------------------
Average Turnaround Time : 9.40
Average Waiting Time    : 5.20
Total Context Switches  : 0
```

---

## References

1. Silberschatz, A., Galvin, P., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. [Shortest job next – Wikipedia](https://en.wikipedia.org/wiki/Shortest_job_next)
