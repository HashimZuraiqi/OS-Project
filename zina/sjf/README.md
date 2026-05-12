# Shortest-Job-First (SJF) – Non-Preemptive

**Student:** Zina Hijazeen
**Algorithm Type:** Non-Preemptive
**Scheduling Policy:** Process with shortest burst time executes first

---

## Algorithm Description

Shortest Job First (SJF) is a non-preemptive CPU scheduling algorithm that selects the ready process with the smallest CPU burst time. If two processes have the same burst time, the process that arrived earlier is selected first. Once a process is selected, it executes until completion without interruption.

This algorithm minimizes average waiting time and turnaround time among all non-preemptive scheduling algorithms.

### Characteristics

* **Non-Preemptive:** Once a process starts execution, it cannot be interrupted.
* **Optimal:** Minimizes average waiting time and turnaround time.
* **Arrival Time Support:** The algorithm considers process arrival times before scheduling.
* **Practical Limitation:** Requires knowledge of burst time in advance.
* **Starvation Risk:** Long processes may starve if short processes continue arriving.

---

## Implementation Guidelines

### Requirements

1. Implement process queue and sorting mechanism by burst time.
2. Track the following for each process:

   * Process ID
   * Arrival Time
   * Burst Time
   * Completion Time
   * Turnaround Time = Completion Time - Arrival Time
   * Waiting Time = Turnaround Time - Burst Time

### Pseudocode

```text id="jlwm11"
SJF_Schedule(processes):

    completed = []
    current_time = 0

    while processes is not empty:

        available = processes with arrival_time <= current_time

        if available is empty:
            current_time++
            continue

        shortest = process with minimum burst_time

        completion_time = current_time + burst_time

        turnaround_time = completion_time - arrival_time

        waiting_time = turnaround_time - burst_time

        add process to completed list

        remove process from processes

        current_time = completion_time
```

---

## Folder Structure

```text id="jlwm12"
zina/sjf/
├── README.md
├── sjf.cpp
├── input_processes.txt
├── output.txt
└── metrics.txt
```

---

## Running the Program

### Prerequisites

* C++ Compiler (g++)
* Standard C++ Library

### Compilation

```bash id="jlwm13"
g++ sjf.cpp -o sjf
```

### Execution

```bash id="jlwm14"
.\sjf.exe
```

---

## Input Format

Create `input_processes.txt` using the following format:

```text id="jlwm15"
Process_ID Arrival_Time Burst_Time
P1 0 8
P2 1 4
P3 2 2
P4 3 1
```

---

## Output Format

The program generates scheduling results in `output.txt`.

Example:

```text id="jlwm16"
Process Arrival Burst Completion Turnaround Waiting

P1      0       8      8          8          0
P4      3       1      9          6          5
```

The average waiting time and turnaround time are stored in `metrics.txt`.

Example:

```text id="jlwm17"
Average Waiting Time: X.XX
Average Turnaround Time: X.XX
```

---

## Testing

The implementation was tested using:

* Processes with different burst times
* Convoy effect scenarios
* CPU idle gap scenarios
* Different arrival times

---

## References

1. Silberschatz, A., Galvin, P., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. Operating Systems course slides and lab materials.

---

## Notes

* The implementation considers arrival times before selecting the next process.
* The CPU remains idle if no process has arrived yet.
* Results are automatically written into output files.
* The implementation uses file input and output for testing different scheduling scenarios.
hanism
