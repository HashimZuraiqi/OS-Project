# Shortest-Remaining-Time-First (SRTF) – Preemptive

**Student:** Hashim  
**Algorithm Type:** Preemptive  
**Scheduling Policy:** Process with shortest remaining burst time executes, with preemption

---

## Algorithm Description

Shortest-Remaining-Time-First (SRTF), also known as Shortest Remaining Time (SRT), is the preemptive version of Shortest-Job-First. When a new process arrives with a shorter remaining time than the currently executing process, the CPU is preempted and allocated to the new process. This algorithm minimizes average waiting and turnaround times among all preemptive algorithms.

### Characteristics
- **Preemptive:** A process can be interrupted if a shorter one arrives
- **Optimal:** Provides optimal average waiting and turnaround times
- **More Complex:** Requires tracking remaining burst time and preemption points
- **Higher Overhead:** Context switching overhead due to preemptions
- **Practical Limitation:** Requires knowledge of burst time in advance

---

## Implementation Guidelines

### Requirements
1. Implement process queue with dynamic reordering capability
2. Track the following for each process:
   - Process ID
   - Arrival Time
   - Burst Time (total CPU execution time)
   - Remaining Time (remaining burst time after preemptions)
   - Completion Time
   - Turnaround Time = Completion Time - Arrival Time
   - Waiting Time = Turnaround Time - Burst Time

### Key Differences from Non-Preemptive SJF
- When a new process arrives, compare its burst time with the currently executing process's **remaining** time
- Switch if the new process has less remaining time
- Track context switches (for analysis)

### Pseudocode

```
SRTF_Schedule(processes):
    scheduled = []
    ready_queue = []
    current_time = 0
    current_process = null
    total_processes = length(processes)
    completed = 0
    
    while completed < total_processes:
        # Add all processes that arrived at current_time
        for process in processes:
            if process.arrival_time == current_time and process not in ready_queue:
                add process to ready_queue
        
        # Check if current process should be preempted
        if current_process is not null:
            if ready_queue is not empty:
                next_process = min(ready_queue, by remaining_time)
                if next_process.remaining_time < current_process.remaining_time:
                    add current_process back to ready_queue
                    current_process = null
        
        # Select process if none is executing
        if current_process is null and ready_queue is not empty:
            current_process = min(ready_queue, by remaining_time)
            remove current_process from ready_queue
        
        # Execute for 1 time unit (or until next event)
        if current_process is not null:
            current_process.remaining_time -= 1
            current_time += 1
            
            if current_process.remaining_time == 0:
                current_process.completion_time = current_time
                calculate turnaround_time and waiting_time
                add to scheduled
                completed += 1
                current_process = null
        else:
            current_time += 1
```

---

## Folder Structure

```
hashim/srtf/
├── README.md                    # This file
├── code/
│   ├── srtf.cpp                # C++ implementation
│   ├── srtf.py                 # Python implementation (optional)
│   └── input_processes.txt      # Test input file
└── results/
    ├── output.txt              # Algorithm output
    ├── metrics.txt             # Performance metrics
    └── gantt_chart.txt         # Timeline of execution
```

---

## Running the Program

### Prerequisites
- [Your chosen language compiler/interpreter]
- Standard C++ Library / Python 3.x

### Compilation/Execution

**For C++ (example):**
```bash
cd hashim/srtf/code
g++ -o srtf srtf.cpp
./srtf input_processes.txt
```

**For Python (example):**
```bash
cd hashim/srtf/code
python srtf.py input_processes.txt
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
Total Context Switches: N
```

### Gantt Chart (Optional but Helpful)
```
Gantt Chart:
0   P1   1   P2   2   P3   4   P2   5   P4   6   P3   8   P1
|----|----|----|----|----|----|----|----|----|----|----|----|
```

---

## Testing

Create multiple test cases including:
- Processes with varying burst times to show preemption
- Test case where multiple short processes interrupt a long one
- Test case comparing with non-preemptive SJF
- Minimum 5 comprehensive test cases
- Document the number of context switches

---

## References

1. Silberschatz, A., Galvin, P., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. [Shortest job next](https://en.wikipedia.org/wiki/Shortest_job_next)

---

## Notes

- Implement time unit tracking carefully (can simulate 1 unit at a time)
- Document each preemption event in output
- Create a Gantt chart showing execution timeline
- Compare results with non-preemptive SJF to show improvement
- Discuss the trade-off between optimality and context-switching overhead
- Include detailed code comments explaining preemption logic
