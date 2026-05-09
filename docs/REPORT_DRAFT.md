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

The purpose of this project is to implement and conduct a formal performance evaluation of five core CPU scheduling algorithms: First-Come, First-Served (FCFS), Shortest Job First (SJF), Shortest Remaining Time First (SRTF), non-preemptive Priority Scheduling, and Round Robin (RR). By simulating all five algorithms in C++ under identical, standardized workloads, this study aims to quantitatively measure and compare their efficiency in terms of average turnaround time and average waiting time. The overarching goal is to identify the trade-offs between algorithmic simplicity, system throughput, process fairness, and responsiveness, so that informed recommendations can be made for different classes of computing environments.

### 3.2 Background

CPU scheduling is one of the most fundamental responsibilities of an operating system. When multiple processes compete for a single CPU, the scheduler determines which process receives CPU time and for how long. The selection strategy has a direct and measurable impact on system performance, user experience, and resource utilization [1]. Poor scheduling can lead to excessive waiting, low CPU utilization, or unfair treatment of certain processes—problems that become critically visible in real-time, interactive, and batch-processing systems alike.

The five algorithms studied in this report represent the foundational spectrum of scheduling strategies: from the simplest non-preemptive queue (FCFS) to dynamic preemptive policies (SRTF and RR). Each algorithm embodies a different design philosophy, and no single algorithm is universally optimal. Understanding when each excels and where each falls short is therefore essential knowledge in operating systems design [1][2].

All five algorithms were implemented from scratch in C++ and tested against a common set of process workloads to enable a direct, fair comparison.

### 1.3 Evaluation Metrics

The following standard metrics are used throughout this report to evaluate scheduler performance:

- **Waiting Time (WT):** The total time a process spends in the ready queue waiting for the CPU. Calculated as: `WT = Turnaround Time − Burst Time`
- **Turnaround Time (TAT):** The total elapsed time from process submission to process completion. Calculated as: `TAT = Completion Time − Arrival Time`
- **Average Waiting Time (AWT):** The arithmetic mean of waiting times across all processes. Lower AWT indicates better scheduling efficiency.
- **Average Turnaround Time (ATAT):** The arithmetic mean of turnaround times across all processes. Lower ATAT indicates faster overall process throughput.
- **Context Switches:** For preemptive algorithms, the number of times the CPU switches from one process to another. Frequent context switching increases scheduling overhead.

---

## 4. Methodology

### 4.1 First-Come, First-Served (FCFS) — Non-Preemptive
**Implemented by:** Faris Asaad

**Definition:** FCFS is the simplest CPU scheduling algorithm. Processes are placed in a FIFO (First-In, First-Out) ready queue and are executed strictly in the order in which they arrive. Once a process starts executing, it continues until it completes—there is no preemption.

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
- Extremely simple to understand and implement.
- Zero preemption overhead; no context switches during execution.
- Fair in the sense that every process eventually gets the CPU.

**Disadvantages:**
- Suffers severely from the **Convoy Effect**: a single long-burst process blocks all shorter processes behind it, dramatically inflating their waiting times.
- Average waiting time is highly sensitive to arrival order and can be very large.
- Not suitable for interactive or time-sharing systems where responsiveness matters.

---

### 4.2 Shortest Job First (SJF) — Non-Preemptive
**Implemented by:** Zina Hijazeen

**Definition:** At each scheduling decision point (when the CPU becomes free), SJF selects the process from the ready queue with the smallest CPU burst time. If two processes have equal burst times, the one that arrived earlier is chosen. Once selected, the process runs to completion without preemption.

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
- **Provably optimal** for minimizing average waiting time among non-preemptive algorithms for any given set of processes [1].
- Significantly reduces the convoy effect by always selecting short jobs when available.
- Simple to implement once burst times are known.

**Disadvantages:**
- **Starvation risk:** Long processes may wait indefinitely if short processes keep arriving.
- Requires prior knowledge of burst times, which is generally unavailable in real-world systems. In practice, burst time must be estimated (e.g., using exponential averaging of past behavior).
- Non-preemptive: a long process that starts when no other is ready will still block shorter processes that arrive later.

---

### 4.3 Shortest Remaining Time First (SRTF) — Preemptive
**Implemented by:** Hashim Zuraiqi

**Definition:** SRTF is the preemptive counterpart of SJF. At every moment a new process arrives, the scheduler compares that process's burst time with the remaining burst time of the currently running process. If the new process has a shorter remaining time, the current process is immediately preempted and placed back in the ready queue. The algorithm then runs the process with the globally shortest remaining time.

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
- Minimizes average waiting time among all preemptive algorithms—a direct extension of SJF's optimality to dynamic environments.
- Highly responsive to newly arriving short jobs; they are serviced almost immediately.
- Excellent throughput in systems with mixed short and long processes.

**Disadvantages:**
- **High context-switching overhead:** The scheduler checks remaining times at every time unit, which is computationally expensive.
- Long processes can suffer severe starvation in workloads with continuous short-job arrivals.
- Like SJF, requires knowledge of burst times, which must be estimated in practice.

---

### 4.4 Priority Scheduling — Non-Preemptive
**Implemented by:** Mohammad Amayreh

**Definition:** Each process is assigned an integer priority. In our implementation, a **lower integer value corresponds to higher priority** (priority 1 is the highest). When the CPU becomes free, the scheduler selects the highest-priority process from all arrived, ready processes. Ties in priority are broken by arrival time. Once a process starts, it runs to completion.

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
- Allows the OS to prioritize critical system processes and time-sensitive tasks over background jobs.
- Simple to implement and reason about in systems with well-defined priority levels.
- Flexible: priority can encode real-world importance (e.g., I/O-bound vs. CPU-bound).

**Disadvantages:**
- **Starvation:** Low-priority processes may never execute if high-priority processes keep arriving. This is mitigated in practice using **aging**, where priority gradually increases the longer a process waits.
- Priority assignment can be arbitrary; incorrect priorities lead to poor system behavior.
- Like FCFS, the non-preemptive variant cannot interrupt a running low-priority process even when a high-priority process arrives.

---

### 4.5 Round Robin (RR) — Preemptive
**Implemented by:** Nour Al-Qatarneh

**Definition:** Round Robin assigns each process a fixed, maximum unit of CPU time called the **Time Quantum** (Q). The scheduler maintains a FIFO ready queue. A process runs for at most Q time units; if it does not finish, it is preempted and added to the end of the ready queue. New processes that arrive during a running quantum are enqueued before the preempted process. This continues until all processes complete.

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
- **Fairness:** Every process is guaranteed CPU time within a bounded wait of (n-1)×Q time units.
- No starvation: every process eventually reaches the front of the queue.
- Excellent for interactive and time-sharing systems; provides good response times for short processes.

**Disadvantages:**
- **Performance depends critically on the time quantum.** A very small Q causes excessive context switching; a very large Q degenerates to FCFS behavior.
- Context-switching overhead is inherently higher than non-preemptive algorithms.
- Average turnaround time is often worse than SJF because short processes are interrupted repeatedly.

---

## 5. Results

All five algorithms were evaluated using two standardized test cases. Each test case was run with identical process sets across all algorithms to ensure a fair comparison.

### 5.1 Test Case 1: Simple Varied Workload

**Process Set:**

| Process | Arrival Time (ms) | Burst Time (ms) | Priority |
|:---:|:---:|:---:|:---:|
| P1 | 0 | 10 | 3 |
| P2 | 1 | 4 | 1 (Highest) |
| P3 | 2 | 5 | 4 (Lowest) |
| P4 | 3 | 3 | 2 |

*Note: Round Robin uses Time Quantum = 2 ms. Priority: lower number = higher priority.*

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

At t=10 all three remaining processes have arrived. SJF selects P4 (shortest burst = 3), then P2 (burst = 4), then P3 (burst = 5). This reordering reduces AWT by 8% compared to FCFS.

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

At t=1, P2 arrives with burst 4 < P1's remaining 9, so P1 is preempted. From t=1, SRTF always runs the globally shortest remaining job. Only one preemption occurs; all other transitions happen at natural completions.

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

P1 runs first (only arrived process). At t=10, priority ordering selects P2 (priority 1), then P4 (priority 2), then P3 (priority 4). The result is similar to SJF in structure but driven by assigned priority rather than burst length.

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

RR distributes the CPU among all processes in small slices. While this guarantees fairness and no starvation, the frequent context switching and the repeated interruption of P1 result in the highest AWT and ATAT among all algorithms for this workload.

---

### 5.2 Test Case 2: Convoy Effect Scenario

This test case is designed to expose how each algorithm handles a single long-burst process blocking many short ones.

**Process Set:**

| Process | Arrival Time (ms) | Burst Time (ms) |
|:---:|:---:|:---:|
| P1 | 0 | 25 |
| P2 | 1 | 2 |
| P3 | 2 | 2 |
| P4 | 3 | 2 |

*Priority for Priority Scheduling: P1=3, P2=1, P3=4, P4=2. Round Robin Time Quantum = 2 ms.*

#### FCFS – Test Case 2

P1 occupies the CPU for 25 ms. P2, P3, and P4 each wait the entire 25 ms before even starting.

| Process | Arrival | Burst | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 25 | 25 | 25 | 0 |
| P2 | 1 | 2 | 27 | 26 | 24 |
| P3 | 2 | 2 | 29 | 27 | 25 |
| P4 | 3 | 2 | 31 | 28 | 26 |

**AWT = 18.75 ms | ATAT = 26.50 ms**

#### SJF – Test Case 2

At t=0, P1 is the only arrived process, so SJF must start it. By the time P1 finishes at t=25, all short processes are ready—but they have already waited 24–22 ms. SJF provides no benefit here because the long process was unavoidable.

| Process | Arrival | Burst | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 25 | 25 | 25 | 0 |
| P2 | 1 | 2 | 27 | 26 | 24 |
| P3 | 2 | 2 | 29 | 27 | 25 |
| P4 | 3 | 2 | 31 | 28 | 26 |

**AWT = 18.75 ms | ATAT = 26.50 ms**

#### Priority Scheduling – Test Case 2

Same as SJF and FCFS for this workload: P1 (priority 3) is the only available process at t=0 and must run non-preemptively to completion. Priority ordering takes effect at t=25.

| Process | Arrival | Burst | Priority | Completion | TAT | WT |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| P1 | 0 | 25 | 3 | 25 | 25 | 0 |
| P2 | 1 | 2 | 1 | 27 | 26 | 24 |
| P4 | 3 | 2 | 2 | 29 | 26 | 24 |
| P3 | 2 | 2 | 4 | 31 | 29 | 27 |

**AWT = 18.75 ms | ATAT = 26.50 ms**

#### SRTF – Test Case 2

At t=1, P2 arrives with burst 2 vs. P1's remaining 24. SRTF immediately preempts P1 and runs P2 through P4 before returning to P1. The short processes complete in just 3–5 ms.

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

RR allows P2, P3, and P4 to be serviced almost immediately by interleaving with P1's long burst.

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

SRTF achieves the lowest AWT by dynamically preempting P1 the moment P2 arrives, ensuring short jobs are never blocked behind long ones. The single preemption (P1 → P2 at t=1) enables P2, P4, and P3 to complete rapidly while P1 waits. This result aligns with the theoretical proof that SRTF minimizes average waiting time in dynamic environments [1].

SJF ranks second. It cannot improve on the first scheduling decision (P1 runs at t=0 because it is alone), but once P1 completes, it correctly prioritizes P4 over P2 and P3. The 8% improvement in AWT over FCFS (9.25 → 8.50 ms) illustrates the value of shortest-job prioritization even in non-preemptive form.

### 6.2 The Convoy Effect

Test Case 2 provides a controlled demonstration of the convoy effect. When a 25 ms process (P1) occupies the CPU at t=0 under FCFS, SJF, or non-preemptive Priority Scheduling, all three short processes (2 ms each) are forced to wait approximately 24 ms before their first execution. All three non-preemptive algorithms produce identical results (AWT = 18.75 ms) because none can interrupt P1 once it starts.

SRTF eliminates the convoy effect almost entirely: it preempts P1 at t=1 when P2 arrives, reducing AWT from 18.75 ms to 2.25 ms—an **88% reduction**. Round Robin also handles the convoy effect well, limiting P1's uninterrupted run to only 2 ms before yielding to other processes, yielding AWT = 3.50 ms.

This experiment reveals that preemption is the key differentiator for convoy-effect scenarios. Non-preemptive algorithms (FCFS, SJF, Priority) offer no protection against a single long-burst process; only SRTF and RR can mitigate it.

### 6.3 Round Robin and the Time Quantum Trade-off

In Test Case 1, Round Robin performs worst in AWT (10.25 ms) and ATAT (15.75 ms), despite being preemptive. This counterintuitive result arises because:

1. The workload contains one very long process (P1 = 10 ms) that is repeatedly interrupted, causing it to run in six separate segments over 22 ms instead of completing quickly.
2. The quantum (Q=2) is small relative to the burst times, generating 10 context switches and significant scheduling overhead.
3. Shorter processes (P2, P4) are also interrupted mid-burst, delaying their completion compared to SJF.

However, RR's advantage is **fairness and bounded waiting**. No process waits more than (n-1)×Q = 6 ms before receiving its first CPU slice. In an interactive multi-user system, this responsiveness matters far more than minimizing AWT.

The choice of quantum is critical: a Q that is too small wastes CPU time on context switches, while a Q that is too large degenerates to FCFS. Empirical guidelines suggest Q should be larger than 80% of typical CPU bursts [1].

### 6.4 Starvation and Fairness

Both SJF and Priority Scheduling carry starvation risk. In SJF, a process with a very long burst time may never be scheduled if short processes continuously arrive. In Priority Scheduling, low-priority processes (e.g., P3 with priority 4 in our test) are always deferred in favor of higher-priority ones. The standard remedy is **aging**: incrementally increasing the effective priority of waiting processes over time to ensure eventual service [1].

FCFS and Round Robin are immune to starvation by design. FCFS guarantees service in arrival order; RR guarantees service in cyclic order. SRTF can starve long processes in adversarial workloads but is unlikely to do so in typical distributions.

---

## 7. Conclusions

This study implemented and evaluated five CPU scheduling algorithms under standardized workloads. The results support several original conclusions:

1. **SRTF achieves the best throughput but at a design cost.** SRTF produced the lowest AWT in both test cases (5.00 ms in TC1, 2.25 ms in TC2). It requires only one context switch in our test workloads—far fewer than Round Robin—because most transitions occur at natural completions rather than forced preemptions. However, SRTF requires burst-time knowledge and has higher per-unit-time scheduling overhead than non-preemptive algorithms.

2. **Non-preemptive algorithms are indistinguishable in convoy scenarios.** FCFS, SJF, and Priority Scheduling all produced AWT = 18.75 ms in Test Case 2 because the convoy-causing process (P1) was unavoidably the only arrived process at t=0. This demonstrates that the arrival pattern—not just the algorithm—determines whether non-preemptive scheduling suffers from the convoy effect.

3. **Round Robin is the fairest but not the most efficient.** RR provided the highest AWT for our mixed workload (10.25 ms, 11% worse than FCFS) but ensured every process received CPU time within a bounded delay. Its advantage grows in workloads with many interactive processes where responsiveness is prioritized over throughput.

4. **SJF offers the best non-preemptive performance when it can act.** In Test Case 1, SJF's AWT (8.50 ms) was 8% better than FCFS (9.25 ms) and close to Priority Scheduling (8.75 ms). SJF's limitation—requiring burst-time estimates—prevents direct deployment in most real-world schedulers, though many modern OS schedulers use variations of burst-time prediction (exponential averaging) to approximate SJF behavior.

5. **Algorithm selection should match system requirements:**
   - **Batch systems** (maximize throughput): SJF or SRTF
   - **Interactive / time-sharing systems** (minimize response time): Round Robin with a well-tuned quantum
   - **Real-time systems** (prioritize critical tasks): Priority Scheduling (preferably preemptive with aging)
   - **Simplicity-first embedded systems**: FCFS

In summary, no single algorithm dominates in all scenarios. The most effective scheduling strategy is determined by the nature of the workload, the system's primary performance objective (throughput vs. responsiveness vs. fairness), and the operational constraints (availability of burst-time information, acceptable context-switch overhead).

---

## 8. References

[1] Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). John Wiley & Sons.

[2] GeeksforGeeks. (2024). *CPU Scheduling in Operating Systems*. Retrieved from https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/

[3] Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson Education.
