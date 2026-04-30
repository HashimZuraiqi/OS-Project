# Shortest-Job-First (SJF) – Non-Preemptive

**Student:** Zina  
**Algorithm Type:** Non-Preemptive  
**Scheduling Policy:** Process with shortest burst time executes first

---

## Algorithm Description

Shortest-Job-First (SJF) is a scheduling algorithm that selects the process with the shortest burst time for execution. Once a process is selected, it runs to completion without being preempted. This algorithm minimizes average waiting time and turnaround time among all non-preemptive algorithms.

### Characteristics
- **Non-Preemptive:** Once a process starts, it cannot be interrupted
- **Optimal:** Minimizes average waiting and turnaround times
- **Practical Limitation:** Requires knowledge of burst time in advance (not always available)
- **Starvation Risk:** Long processes may starve if short processes keep arriving

---

## Implementation Guidelines

### Requirements
1. Implement process queue and sorting mechanism by burst time
2. Track the following for each process:
   - Process ID
   - Arrival Time
   - Burst Time (CPU execution time)
   - Completion Time
   - Turnaround Time = Completion Time - Arrival Time
   - Waiting Time = Turnaround Time - Burst Time

### Pseudocode

```
SJF_Schedule(processes):
    scheduled = []
    current_time = 0
    remaining_processes = sort(processes, by arrival_time)
    
    while remaining_processes is not empty:
        # Find processes that have arrived by current_time
        available = [p for p in remaining_processes if p.arrival_time <= current_time]
        
        if available is empty and remaining_processes is not empty:
            # No process has arrived yet, jump to next arrival
            current_time = min(remaining_processes).arrival_time
            continue
        
        # Select process with shortest burst time
        next_process = min(available, by burst_time)
        
        current_time = max(current_time, next_process.arrival_time)
        next_process.completion_time = current_time + next_process.burst_time
        
        calculate turnaround_time and waiting_time
        add to scheduled
        remove from remaining_processes
        
        current_time = next_process.completion_time
```

---

## Folder Structure

```
zina/sjf/
├── README.md                    # This file
├── code/
│   ├── sjf.cpp                 # C++ implementation
│   ├── sjf.py                  # Python implementation (optional)
│   └── input_processes.txt      # Test input file
└── results/
    ├── output.txt              # Algorithm output
    └── metrics.txt             # Performance metrics
```

---

## Running the Program

### Prerequisites
- [Your chosen language compiler/interpreter]
- Standard C++ Library / Python 3.x

### Compilation/Execution

**For C++ (example):**
```bash
cd zina/sjf/code
g++ -o sjf sjf.cpp
./sjf input_processes.txt
```

**For Python (example):**
```bash
cd zina/sjf/code
python sjf.py input_processes.txt
```

---

## Input Format

Create `input_processes.txt` with the following format:
```
Process_ID Arrival_Time Burst_Time
P1 0 8
P2 1 4
P3 2 2
P4 3 1
```

---

## Output Format

Your program should produce output in this format:
```
Process | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time
P4      | 3            | 1          | 4               | 1               | 0
P3      | 2            | 2          | 6               | 4               | 2
...

Average Turnaround Time: X.XX
Average Waiting Time: X.XX
```

---

## Testing

Create multiple test cases including:
- Processes with varying burst times
- Test cases to demonstrate optimality vs. FCFS
- Test cases showing starvation potential
- Minimum 5 comprehensive test cases

---

## References

1. Silberschatz, A., Galvin, P., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. [Shortest Job First Scheduling](https://en.wikipedia.org/wiki/Shortest_job_next)

---

## Notes

- Compare your results with FCFS to demonstrate optimality
- Document the assumption that burst time is known in advance
- Include discussion on starvation and how it could be mitigated
- Add comments explaining the sorting and selection mechanism
