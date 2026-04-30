# First-Come First-Served (FCFS) – Non-Preemptive

**Student:** Faris  
**Algorithm Type:** Non-Preemptive  
**Scheduling Policy:** Processes are executed in the order they arrive in the ready queue

---

## Algorithm Description

First-Come First-Served (FCFS) is the simplest CPU scheduling algorithm. The process that arrives first in the ready queue gets the CPU first. Once a process is allocated to the CPU, it executes until it completes or enters a waiting state (I/O operation). No process can be preempted.

### Characteristics
- **Non-Preemptive:** Once CPU is allocated, it cannot be taken away until the process completes
- **Fair & Simple:** Easy to understand and implement
- **Limitations:** 
  - Suffers from the "convoy effect" (short processes wait behind long ones)
  - Average waiting time can be very high
  - Not suitable for interactive systems

---

## Implementation Guidelines

### Requirements
1. Implement a queue data structure to manage processes in FIFO order
2. Track the following for each process:
   - Process ID
   - Arrival Time
   - Burst Time (CPU execution time)
   - Completion Time
   - Turnaround Time = Completion Time - Arrival Time
   - Waiting Time = Turnaround Time - Burst Time

### Pseudocode

```
FCFS_Schedule(processes):
    ready_queue = []
    current_time = 0
    
    for each process in processes (sorted by arrival time):
        add process to ready_queue
    
    while ready_queue is not empty:
        process = dequeue from ready_queue
        
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        
        process.start_time = current_time
        current_time += process.burst_time
        process.completion_time = current_time
        
        calculate turnaround_time and waiting_time
        store results
```

---

## Folder Structure

```
faris/fcfs/
├── README.md                    # This file
├── code/
│   ├── fcfs.cpp                # C++ implementation
│   ├── fcfs.py                 # Python implementation (optional)
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
cd faris/fcfs/code
g++ -o fcfs fcfs.cpp
./fcfs input_processes.txt
```

**For Python (example):**
```bash
cd faris/fcfs/code
python fcfs.py input_processes.txt
```

---

## Input Format

Create `input_processes.txt` with the following format:
```
Process_ID Arrival_Time Burst_Time
P1 0 5
P2 1 3
P3 2 8
P4 3 6
```

---

## Output Format

Your program should produce output in this format:
```
Process | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time
P1      | 0            | 5          | 5               | 5               | 0
P2      | 1            | 3          | 8               | 7               | 4
...

Average Turnaround Time: X.XX
Average Waiting Time: X.XX
```

---

## Testing

Create multiple test cases with:
- Processes arriving in different orders
- Varying burst times
- Different number of processes (minimum 5 test cases)

---

## References

1. Silberschatz, A., Galvin, P., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. [Operating System Scheduling](https://en.wikipedia.org/wiki/Scheduling_(computing))

---

## Notes

- Document your code with comments explaining the logic
- Include a brief explanation of how FCFS handles the test cases
- Prepare to discuss the convoy effect in your results
