# Priority Scheduling – Non-Preemptive

**Student:** Mohammad  
**Algorithm Type:** Non-Preemptive  
**Scheduling Policy:** Process with highest priority executes first

---

## Algorithm Description

Priority Scheduling is an algorithm where each process is assigned a priority, and the CPU is allocated to the process with the highest priority. In the non-preemptive version, once a process starts execution, it runs to completion even if a higher priority process arrives.

### Characteristics
- **Non-Preemptive:** Once a process starts, it cannot be interrupted
- **Flexible:** Can assign priorities based on various criteria
- **Priority Types:** 
  - Higher number = higher priority (or vice versa, define your convention)
  - Static or dynamic priorities
- **Starvation:** Low-priority processes may starve if high-priority processes continuously arrive
- **Real-world Use:** Widely used in real operating systems

---

## Implementation Guidelines

### Requirements
1. Implement process queue and sorting mechanism by priority
2. Track the following for each process:
   - Process ID
   - Arrival Time
   - Burst Time (CPU execution time)
   - Priority Level (define your scale, e.g., 1-10, where 1 is highest or lowest)
   - Completion Time
   - Turnaround Time = Completion Time - Arrival Time
   - Waiting Time = Turnaround Time - Burst Time

### Priority Convention
**Define clearly:** Are higher numbers = higher priority or lower priority?
Example: 1 (Highest Priority) to 10 (Lowest Priority)

### Pseudocode

```
PriorityScheduling_NonPreemptive(processes):
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
        
        # Select process with highest priority
        next_process = max(available, by priority)  # Adjust based on your priority scheme
        
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
mohammad/priority-scheduling/
├── README.md                    # This file
├── code/
│   ├── priority.cpp            # C++ implementation
│   ├── priority.py             # Python implementation (optional)
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
cd mohammad/priority-scheduling/code
g++ -o priority priority.cpp
./priority input_processes.txt
```

**For Python (example):**
```bash
cd mohammad/priority-scheduling/code
python priority.py input_processes.txt
```

---

## Input Format

Create `input_processes.txt` with the following format:
```
Process_ID Arrival_Time Burst_Time Priority
P1 0 5 2
P2 1 3 5
P3 2 8 1
P4 3 6 3
```

*(Where 1 = Highest Priority, 5 = Lowest Priority — adjust your scale)*

---

## Output Format

Your program should produce output in this format:
```
Process | Arrival Time | Burst Time | Priority | Completion Time | Turnaround Time | Waiting Time
P3      | 2            | 8          | 1        | 10              | 8               | 0
P1      | 0            | 5          | 2        | 5               | 5               | 0
...

Average Turnaround Time: X.XX
Average Waiting Time: X.XX
```

---

## Testing

Create multiple test cases including:
- Processes with different priorities
- Test case showing starvation (low-priority process never executes)
- Test case with inverted priorities (low-priority arrives first)
- At least 5 comprehensive test cases

---

## References

1. Silberschatz, A., Galvin, P., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. [Priority Scheduling](https://en.wikipedia.org/wiki/Scheduling_(computing)#Priority_scheduling)

---

## Notes

- Clearly document your priority scheme (1 = highest or 10 = highest)
- Discuss starvation problems and potential solutions (aging)
- Include test cases that demonstrate priority-based scheduling behavior
- Compare results with FCFS and SJF algorithms
- Add comprehensive code comments
