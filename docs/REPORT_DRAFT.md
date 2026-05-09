# Performance Evaluation of CPU Scheduling Algorithms

---

## 1. Title Page

**Project Title:** Performance Evaluation of CPU Scheduling Algorithms  
**Course:** CS11335 – Operating Systems  
**Institution:** Princess Sumaya University for Technology  
**Department:** King Hussein School of Computing Sciences – Computer Science  
**Programming Language:** C++

| # | Student Name | Student ID | Email |
|:--|:---|:---|:---|
| 1 | Faris Asaad | 20230015 | far20230015@std.psut.edu.jo |
| 2 | Hashim Zuraiqi | 20230166 | has20230166@std.psut.edu.jo |
| 3 | Mohammad Amayreh | 20230424 | moh20230424@std.psut.edu.jo |
| 4 | Nour Al-Qatarneh | 20221067 | nou20221067@std.psut.edu.jo |
| 5 | Zina Hijazeen | 20210853 | zin20210853@std.psut.edu.jo |

---

## 2. Table of Contents

1. Introduction
   - 1.1 Statement of Purpose
   - 1.2 Background
   - 1.3 Evaluation Metrics
2. Methodology
   - 2.1 First-Come, First-Served (FCFS)
   - 2.2 Shortest Job First (SJF)
   - 2.3 Shortest Remaining Time First (SRTF)
   - 2.4 Priority Scheduling
   - 2.5 Round Robin (RR)
3. Results
   - 3.1 Test Case 1: Simple Varied Workload
   - 3.2 Test Case 2: Convoy Effect Scenario
   - 3.3 Summary Comparison
4. Analysis and Discussion
5. Conclusions
6. References

---

## 3. Introduction

### 3.1 Statement of Purpose

The purpose of this project is to implement five CPU scheduling algorithms and compare their performance in C++. The algorithms are First-Come, First-Served (FCFS), Shortest Job First (SJF), Shortest Remaining Time First (SRTF), non-preemptive Priority Scheduling, and Round Robin (RR). We use the same process sets for all algorithms so the comparison is fair. The main goal is to compare average waiting time and average turnaround time and show which algorithm works better in each case.

### 3.2 Background

CPU scheduling is one of the main jobs of an operating system. When many processes want the CPU at the same time, the scheduler decides which one runs first and for how long. This decision affects system performance, waiting time, fairness, and how fast the system responds to users [1]. If scheduling is poor, some processes may wait too long, the CPU may be used badly, or some processes may be treated unfairly.

The five algorithms in this report cover the basic types of CPU scheduling, from the simplest queue in FCFS to the preemptive methods in SRTF and RR. Each algorithm has its own idea of how the CPU should be shared. No single algorithm is best in every situation, so it is important to understand the strengths and weaknesses of each one [1][2].

All five algorithms were written from scratch in C++ and tested using the same workloads to make the comparison direct and fair.

### 3.3 Evaluation Metrics

This report uses the following metrics to measure scheduler performance:

- **Waiting Time (WT):** The time a process spends waiting in the ready queue. Formula: `WT = Turnaround Time − Burst Time`
- **Turnaround Time (TAT):** The total time from arrival until completion. Formula: `TAT = Completion Time − Arrival Time`
- **Average Waiting Time (AWT):** The average of all waiting times. A lower value is better.
- **Average Turnaround Time (ATAT):** The average of all turnaround times. A lower value is better.
- **Context Switches:** The number of times the CPU changes from one process to another. More context switches usually mean more overhead.

---

## 4. Methodology

### 4.1 First-Come, First-Served (FCFS) — Non-Preemptive
**Implemented by:** Faris Asaad

**Definition:** FCFS is the simplest CPU scheduling algorithm. Processes wait in a FIFO ready queue and run in the same order they arrive. Once a process starts, it keeps the CPU until it finishes, so there is no preemption.

**Algorithm Pseudocode:**
```
Sort processes by arrival time
currentTime = 0
For each process p in arrival order:
    if currentTime < p.arrivalTime:
        currentTime = p.arrivalTime  // CPU idle
    p.completionTime = currentTime + p.burstTime
    currentTime = p.completionTime
    p.TAT = p.completionTime - p.arrivalTime
    p.WT  = p.TAT - p.burstTime
```

**Advantages:**
- Very easy to understand and implement.
- No preemption overhead during execution.
- Every process will eventually get the CPU.

**Disadvantages:**
- It suffers from the **Convoy Effect**, where one long process blocks the shorter ones behind it.
- The average waiting time can become very high depending on the arrival order.
- It is not a good choice for interactive or time-sharing systems.

---

### 4.2 Shortest Job First (SJF) — Non-Preemptive
**Implemented by:** Zina Hijazeen

**Definition:** At each scheduling decision point, SJF chooses the ready process with the smallest CPU burst time. If two processes have the same burst time, the one that arrived earlier is chosen. After selection, the process runs until it finishes with no preemption.

**Algorithm Pseudocode:**
```
while uncompleted processes exist:
    candidates = {processes that have arrived and are not done}
    if candidates is empty:
        advance currentTime to next arrival
    else:
        p = process in candidates with minimum burstTime
        p.completionTime = currentTime + p.burstTime
        currentTime = p.completionTime
        p.TAT = p.completionTime - p.arrivalTime
        p.WT  = p.TAT - p.burstTime
        mark p as done
```

**Advantages:**
- It gives the best average waiting time among non-preemptive algorithms for a fixed set of processes [1].
- It reduces the convoy effect by running the shortest job first.
- It is simple to implement when burst times are known.

**Disadvantages:**
- Long processes may suffer from starvation if short processes keep coming.
- It needs burst-time knowledge, which is usually not known exactly in real systems. In practice, it must be estimated.
- It is non-preemptive, so a long process that starts first will block later short processes.

---

### 4.3 Shortest Remaining Time First (SRTF) — Preemptive
**Implemented by:** Hashim Zuraiqi

**Definition:** SRTF is the preemptive version of SJF. When a new process arrives, the scheduler compares its burst time with the remaining time of the running process. If the new process has a shorter remaining time, the running process is stopped and returned to the ready queue. Then the process with the shortest remaining time runs.

**Algorithm Pseudocode:**
```
completed = 0
time = 0
while completed < n:
    shortest = process with minimum remaining time that has arrived
    if no such process: time++; continue
    if shortest ≠ lastRunning: contextSwitches++
    run shortest for 1 time unit
    if shortest.remaining == 0:
        record completionTime, TAT, WT
        completed++
```

**Advantages:**
- It usually gives the lowest average waiting time among preemptive algorithms.
- Short new jobs are handled very quickly.
- It works well when short and long processes are mixed together.

**Disadvantages:**
- It can cause high context-switching overhead because the scheduler checks the remaining time often.
- Long processes may starve if short processes keep arriving.
- Like SJF, it needs burst-time estimates.

---

### 4.4 Priority Scheduling — Non-Preemptive
**Implemented by:** Mohammad Amayreh

**Definition:** Each process has an integer priority. In our implementation, a **lower number means higher priority** (priority 1 is the highest). When the CPU becomes free, the scheduler chooses the highest-priority process from the arrived ready processes. If two processes have the same priority, the earlier arrival is chosen. Once a process starts, it runs until it finishes.

**Algorithm Pseudocode:**
```
while uncompleted processes exist:
    candidates = {processes that have arrived and are not done}
    if candidates is empty:
        advance currentTime to next arrival
    else:
        p = process in candidates with minimum priority value
        p.completionTime = currentTime + p.burstTime
        currentTime = p.completionTime
        p.TAT = p.completionTime - p.arrivalTime
        p.WT  = p.TAT - p.burstTime
        mark p as done
```

**Advantages:**
- It lets the OS run important or urgent processes first.
- It is simple to understand and implement.
- The priority value can represent real system importance.

**Disadvantages:**
- Low-priority processes may starve if higher-priority processes keep coming. A common fix is **aging**, which slowly increases a waiting process's priority.
- Wrong priority values can give poor results.
- Like FCFS, the non-preemptive version cannot stop a running process.

---

### 4.5 Round Robin (RR) — Preemptive
**Implemented by:** Nour Al-Qatarneh

**Definition:** Round Robin gives each process a fixed CPU time called the **Time Quantum** (Q). The scheduler keeps a FIFO ready queue. A process runs for at most Q time units. If it does not finish, it is stopped and placed at the end of the queue. New arriving processes are added to the queue in arrival order. This continues until all processes finish.

**Algorithm Pseudocode:**
```
enqueue all processes arriving at t=0
while queue not empty or processes remaining:
    if queue empty: advance to next arrival
    idx = dequeue front process
    run = min(quantum, idx.remaining)
    execute idx for 'run' time units
    enqueue newly arrived processes (in arrival order)
    if idx.remaining > 0: re-enqueue idx
    else: record completionTime, TAT, WT
```

**Advantages:**
- It is fair because every process gets CPU time in turn.
- It does not cause starvation.
- It works well in interactive and time-sharing systems because response time is good.

**Disadvantages:**
- Its performance depends a lot on the time quantum. A very small Q causes many context switches, while a very large Q behaves like FCFS.
- It has more context-switching overhead than non-preemptive algorithms.
- Its average turnaround time is often worse than SJF because processes are interrupted many times.

---

## 5. Results

All five algorithms were tested using two standard test cases. The same process set was used for all algorithms in each case so the comparison stayed fair.

### 5.1 Test Case 1: Simple Varied Workload

**Process Set:**

| Process | Arrival Time (ms) | Burst Time (ms) | Priority |
|:---:|:---:|:---:|:---:|
| P1 | 0 | 10 | 3 |
| P2 | 1 | 4 | 1 (Highest) |
| P3 | 2 | 5 | 4 (Lowest) |
| P4 | 3 | 3 | 2 |

*Note: Round Robin uses Time Quantum = 2 ms. In Priority Scheduling, a lower number means a higher priority.*

---

#### 5.1.1 FCFS Results

**Gantt Chart:**
```
 +----------+----+-----+---+
 |    P1    | P2 |  P3 | P4|
 +----------+----+-----+---+
 0         10  14    19   22
```

**Execution Order:** P1 → P2 → P3 → P4 (arrival order)

| Process | Arrival | Burst | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 10 | 10 | 10 | 0 |
| P2 | 1 | 4 | 14 | 13 | 9 |
| P3 | 2 | 5 | 19 | 17 | 12 |
| P4 | 3 | 3 | 22 | 19 | 16 |

**AWT = 9.25 ms | ATAT = 14.75 ms | Context Switches = 0**

P1 monopolizes the CPU for the first 10 ms, forcing all subsequent processes to wait regardless of their burst length—a textbook example of the convoy effect.

---

#### 5.1.2 SJF Results

**Gantt Chart:**
```
 +----------+---+----+-----+
 |    P1    | P4| P2 |  P3 |
 +----------+---+----+-----+
 0         10  13  17    22
```

**Execution Order:** P1(burst 10, only arrival at t=0) → P4(burst 3) → P2(burst 4) → P3(burst 5)

| Process | Arrival | Burst | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 10 | 10 | 10 | 0 |
| P4 | 3 | 3 | 13 | 10 | 7 |
| P2 | 1 | 4 | 17 | 16 | 12 |
| P3 | 2 | 5 | 22 | 20 | 15 |

**AWT = 8.50 ms | ATAT = 14.00 ms | Context Switches = 0**

At t=10, all the remaining processes are ready. SJF chooses P4 first because it has the shortest burst, then P2, then P3. This gives a lower waiting time than FCFS.

---

#### 5.1.3 SRTF Results

**Gantt Chart:**
```
 +--+--------+---+-----+------------------+
 |P1|   P2   | P4|  P3 |       P1         |
 +--+--------+---+-----+------------------+
 0  1        5   8    13                 22
```

**Execution Order:** P1(0–1) → P2(1–5) → P4(5–8) → P3(8–13) → P1(13–22)

| Process | Arrival | Burst | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 10 | 22 | 22 | 12 |
| P2 | 1 | 4 | 5 | 4 | 0 |
| P3 | 2 | 5 | 13 | 11 | 6 |
| P4 | 3 | 3 | 8 | 5 | 2 |

**AWT = 5.00 ms | ATAT = 10.50 ms | Context Switches = 1**

At t=1, P2 arrives with burst 4, which is shorter than P1's remaining 9, so P1 is stopped. After that, SRTF always runs the process with the shortest remaining time. Only one preemption happens.

---

#### 5.1.4 Priority Scheduling Results

**Gantt Chart:**
```
 +----------+----+---+-----+
 |    P1    | P2 | P4|  P3 |
 +----------+----+---+-----+
 0         10  14  17    22
```

**Execution Order:** P1(priority 3, only arrival) → P2(priority 1) → P4(priority 2) → P3(priority 4)

| Process | Arrival | Burst | Priority | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 10 | 3 | 10 | 10 | 0 |
| P2 | 1 | 4 | 1 | 14 | 13 | 9 |
| P4 | 3 | 3 | 2 | 17 | 14 | 11 |
| P3 | 2 | 5 | 4 | 22 | 20 | 15 |

**AWT = 8.75 ms | ATAT = 14.25 ms | Context Switches = 0**

P1 runs first because it is the only process ready at t=0. At t=10, the scheduler chooses P2 first, then P4, then P3 based on priority. The order is similar to SJF, but it depends on priority values, not burst time.

---

#### 5.1.5 Round Robin Results (Time Quantum = 2 ms)

**Execution Sequence:**

| Time Interval | Process Running | Remaining After |
|:---:|:---:|:---:|
| 0 – 2 | P1 | P1: 8 |
| 2 – 4 | P2 | P2: 2 |
| 4 – 6 | P3 | P3: 3 |
| 6 – 8 | P1 | P1: 6 |
| 8 – 10 | P4 | P4: 1 |
| 10 – 12 | P2 | P2: 0 ✓ |
| 12 – 14 | P3 | P3: 1 |
| 14 – 16 | P1 | P1: 4 |
| 16 – 17 | P4 | P4: 0 ✓ |
| 17 – 18 | P3 | P3: 0 ✓ |
| 18 – 20 | P1 | P1: 2 |
| 20 – 22 | P1 | P1: 0 ✓ |

**Gantt Chart:**
```
 +----+----+----+----+----+----+----+----+---+---+----+----+
 | P1 | P2 | P3 | P1 | P4 | P2 | P3 | P1 |P4 |P3 | P1 | P1 |
 +----+----+----+----+----+----+----+----+---+---+----+----+
 0    2    4    6    8   10   12   14   16 17 18   20   22
```

| Process | Arrival | Burst | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 10 | 22 | 22 | 12 |
| P2 | 1 | 4 | 12 | 11 | 7 |
| P3 | 2 | 5 | 18 | 16 | 11 |
| P4 | 3 | 3 | 17 | 14 | 11 |

**AWT = 10.25 ms | ATAT = 15.75 ms | Context Switches = 10**

RR gives the CPU to each process in small time slices. This makes it fair and avoids starvation, but the many context switches and repeated stops of P1 increase waiting time and turnaround time.

---

### 5.2 Test Case 2: Convoy Effect Scenario

This test case shows how each algorithm handles one long process that blocks many short ones.

**Process Set:**

| Process | Arrival Time (ms) | Burst Time (ms) |
|:---:|:---:|:---:|
| P1 | 0 | 25 |
| P2 | 1 | 2 |
| P3 | 2 | 2 |
| P4 | 3 | 2 |

*Priority for Priority Scheduling: P1=3, P2=1, P3=4, P4=2. Round Robin Time Quantum = 2 ms.*

#### FCFS – Test Case 2

P1 uses the CPU for 25 ms. P2, P3, and P4 each wait almost the full 25 ms before they get a turn.

| Process | Arrival | Burst | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 25 | 25 | 25 | 0 |
| P2 | 1 | 2 | 27 | 26 | 24 |
| P3 | 2 | 2 | 29 | 27 | 25 |
| P4 | 3 | 2 | 31 | 28 | 26 |

**AWT = 18.75 ms | ATAT = 26.50 ms**

#### SJF – Test Case 2

At t=0, P1 is the only process that has arrived, so SJF must start it. By the time P1 finishes at t=25, the short processes are already waiting, and their waiting times are still very high. SJF gives no benefit here because P1 had to run first.

| Process | Arrival | Burst | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 25 | 25 | 25 | 0 |
| P2 | 1 | 2 | 27 | 26 | 24 |
| P3 | 2 | 2 | 29 | 27 | 25 |
| P4 | 3 | 2 | 31 | 28 | 26 |

**AWT = 18.75 ms | ATAT = 26.50 ms**

#### Priority Scheduling – Test Case 2

For this workload, Priority Scheduling behaves like FCFS and SJF. P1 is the only process available at t=0, so it runs to completion first. The priority order only starts after t=25.

| Process | Arrival | Burst | Priority | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 25 | 3 | 25 | 25 | 0 |
| P2 | 1 | 2 | 1 | 27 | 26 | 24 |
| P4 | 3 | 2 | 2 | 29 | 26 | 24 |
| P3 | 2 | 2 | 4 | 31 | 29 | 27 |

**AWT = 18.75 ms | ATAT = 26.50 ms**

#### SRTF – Test Case 2

At t=1, P2 arrives with burst 2 while P1 still has 24 ms left. SRTF stops P1 right away and runs the short processes before returning to P1. The short processes finish very quickly.

**Gantt Chart:**
```
 +--+----+----+----+----------------------------------------------+
 |P1| P2 | P3 | P4 |                    P1                        |
 +--+----+----+----+----------------------------------------------+
 0  1    3    5    7                                              31
```

| Process | Arrival | Burst | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 25 | 31 | 31 | 6 |
| P2 | 1 | 2 | 3 | 2 | 0 |
| P3 | 2 | 2 | 5 | 3 | 1 |
| P4 | 3 | 2 | 7 | 4 | 2 |

**AWT = 2.25 ms | ATAT = 10.00 ms | Context Switches = 1**

#### Round Robin – Test Case 2 (Q = 2 ms)

RR lets P2, P3, and P4 get CPU time quickly by alternating them with P1's long burst.

| Process | Arrival | Burst | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 25 | 31 | 31 | 6 |
| P2 | 1 | 2 | 4 | 3 | 1 |
| P3 | 2 | 2 | 6 | 4 | 2 |
| P4 | 3 | 2 | 10 | 7 | 5 |

**AWT = 3.50 ms | ATAT = 11.25 ms | Context Switches = 5**

---

### 5.3 Summary Comparison Tables

#### Table A: Test Case 1 — Simple Varied Workload

| Scheduling Algorithm | AWT (ms) | ATAT (ms) | Context Switches |
|:---|:---:|:---:|:---:|
| First-Come, First-Served (FCFS) | 9.25 | 14.75 | 0 |
| Shortest Job First (SJF) | 8.50 | 14.00 | 0 |
| Shortest Remaining Time First (SRTF) | **5.00** | **10.50** | 1 |
| Priority Scheduling | 8.75 | 14.25 | 0 |
| Round Robin (RR, Q=2) | 10.25 | 15.75 | 10 |

#### Table B: Test Case 2 — Convoy Effect Scenario

| Scheduling Algorithm | AWT (ms) | ATAT (ms) | Context Switches |
|:---|:---:|:---:|:---:|
| First-Come, First-Served (FCFS) | 18.75 | 26.50 | 0 |
| Shortest Job First (SJF) | 18.75 | 26.50 | 0 |
| Shortest Remaining Time First (SRTF) | **2.25** | **10.00** | 1 |
| Priority Scheduling | 18.75 | 26.50 | 0 |
| Round Robin (RR, Q=2) | 3.50 | 11.25 | 5 |

---

## 6. Analysis and Discussion

### 6.1 Performance Ranking (Test Case 1)

Ordering by Average Waiting Time from best to worst:

1. **SRTF** — 5.00 ms (best)
2. **SJF** — 8.50 ms
3. **Priority** — 8.75 ms
4. **FCFS** — 9.25 ms
5. **Round Robin** — 10.25 ms (worst for this workload)

SRTF gets the lowest AWT because it stops P1 as soon as P2 arrives. This keeps short jobs from waiting behind the long one. The single preemption lets P2, P4, and P3 finish quickly while P1 waits. This matches the theory that SRTF gives very low average waiting time in dynamic workloads [1].

SJF comes second. It cannot improve the first choice because P1 is alone at t=0, but after that it picks the shortest available job first. Its AWT is still better than FCFS, which shows that shortest-job selection helps even without preemption.

### 6.2 The Convoy Effect

Test Case 2 gives a clear example of the convoy effect. When the 25 ms process P1 starts at t=0 under FCFS, SJF, or non-preemptive Priority Scheduling, the three short processes must wait almost the full 25 ms before they run. All three non-preemptive algorithms give the same result because none of them can stop P1 once it starts.

SRTF almost removes the convoy effect. It stops P1 at t=1 when P2 arrives and reduces AWT from 18.75 ms to 2.25 ms, which is an **88% reduction**. Round Robin also handles the convoy effect well because P1 only runs for 2 ms before the CPU moves to other processes.

This experiment shows that preemption is the key factor in convoy-effect cases. Non-preemptive algorithms (FCFS, SJF, and Priority) cannot protect short jobs from one long process. Only SRTF and RR can reduce the problem.

### 6.3 Round Robin and the Time Quantum Trade-off

In Test Case 1, Round Robin gives the worst AWT (10.25 ms) and ATAT (15.75 ms), even though it is preemptive. This happens because:

1. The workload has one long process (P1 = 10 ms) that gets interrupted many times, so it finishes much later than FCFS.
2. The quantum (Q=2) is small compared to the burst times, so the scheduler makes 10 context switches and adds overhead.
3. Short processes like P2 and P4 are also interrupted before they finish, so they complete later than they do under SJF.

However, RR is still useful because it is fair and gives bounded waiting. No process waits more than (n-1)×Q = 6 ms before getting its first CPU slice. In an interactive system, this fast response can matter more than the lowest average waiting time.

The quantum choice is very important. If Q is too small, the CPU wastes time on context switches. If Q is too large, RR starts to behave like FCFS. A common guideline is to choose a quantum larger than 80% of the usual CPU burst [1].

### 6.4 Starvation and Fairness

Both SJF and Priority Scheduling can cause starvation. In SJF, a long process may wait for a very long time if short processes keep arriving. In Priority Scheduling, low-priority processes can keep getting pushed back by higher-priority ones. A common solution is **aging**, which slowly increases the priority of waiting processes [1].

FCFS and Round Robin do not starve processes by design. FCFS serves processes in arrival order, and RR serves them in a cycle. SRTF can also starve long processes if many short ones keep arriving, but this is less common in normal workloads.

---

## 7. Conclusions

This study implemented and evaluated five CPU scheduling algorithms using the same workloads. The results lead to the following conclusions:

1. **SRTF gives the best waiting time, but it has a cost.** SRTF produced the lowest AWT in both test cases (5.00 ms in TC1 and 2.25 ms in TC2). It needed only one context switch in our workloads, which is much less than Round Robin. However, SRTF still needs burst-time estimates and has more scheduling overhead than non-preemptive algorithms.

2. **Non-preemptive algorithms behave the same in convoy cases.** FCFS, SJF, and Priority Scheduling all gave AWT = 18.75 ms in Test Case 2 because P1 was the only process ready at t=0. This shows that the arrival pattern is just as important as the algorithm.

3. **Round Robin is the fairest, but not the most efficient.** RR had the highest AWT in the mixed workload (10.25 ms, 11% worse than FCFS), but it still made sure every process got CPU time after a bounded delay. This is useful in interactive systems where response time matters more than throughput.

4. **SJF is the best non-preemptive choice when it can make a difference.** In Test Case 1, SJF's AWT (8.50 ms) was better than FCFS (9.25 ms) and close to Priority Scheduling (8.75 ms). Its main problem is that it needs burst-time estimates, so it is usually only an approximation in real systems.

5. **The right algorithm depends on the system type:**
    - **Batch systems** that want high throughput: SJF or SRTF
    - **Interactive or time-sharing systems** that need good response time: Round Robin with a well-chosen quantum
    - **Real-time systems** that must prioritize important tasks: Priority Scheduling, preferably with aging
    - **Simple embedded systems**: FCFS

In short, no single algorithm is best in every case. The best choice depends on the workload, the main goal of the system, and the practical limits such as burst-time knowledge and context-switch overhead.

---

## 8. References

[1] Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). John Wiley & Sons.

[2] GeeksforGeeks. (2024). *CPU Scheduling in Operating Systems*. Retrieved from https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/

[3] Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson Education.
