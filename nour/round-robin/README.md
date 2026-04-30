# Round Robin (RR) – Preemptive

**Student:** Nour  
**Algorithm Type:** Preemptive  
**Scheduling Policy:** Each process gets a fixed time quantum, then is moved to the back of the queue

---

## Algorithm Description

Round Robin (RR) is a preemptive scheduling algorithm where each process is assigned a fixed time slice or time quantum (typically 10-100 milliseconds). Each process in the ready queue gets a turn to execute for its assigned time quantum. If a process doesn't complete within its time quantum, it's preempted and moved to the back of the ready queue. This algorithm is widely used in modern operating systems due to its fairness and responsiveness.

### Characteristics
- **Preemptive:** Processes are interrupted after their time quantum expires
- **Fair:** All processes get equal CPU time in the long run
- **Good for Interactive Systems:** Provides good response time
- **Time Quantum:** Critical parameter (too small = high overhead, too large = behaves like FCFS)
- **Moderate Waiting Time:** Better than FCFS, but not optimal like SJF/SRTF

---

## Implementation Guidelines

### Requirements
1. Implement a circular queue (FIFO) for process management
2. Track the following for each process:
   - Process ID
   - Arrival Time
   - Burst Time (total CPU execution time)
   - Remaining Time (remaining burst time)
   - Completion Time
   - Turnaround Time = Completion Time - Arrival Time
   - Waiting Time = Turnaround Time - Burst Time

### Time Quantum
- Typical values: 10, 20, 50, 100 milliseconds
- **Test multiple values** (e.g., 4ms, 8ms, 16ms) to show how it affects performance
- Smaller quantum = more context switches but better responsiveness
- Larger quantum = fewer switches but approaches FCFS behavior

### Pseudocode

```
RoundRobin_Schedule(processes, time_quantum):
    ready_queue = []
    scheduled = []
    current_time = 0
    
    # Add all initial processes to queue (sorted by arrival)
    for process in sort(processes, by arrival_time):
        ready_queue.enqueue(process)
    
    while ready_queue is not empty:
        # Get next process from front of queue
        process = ready_queue.dequeue()
        
        # Ensure process has arrived
        if process.arrival_time > current_time:
            current_time = process.arrival_time
        
        # Execute for minimum of (time_quantum, remaining_time)
        execution_time = min(time_quantum, process.remaining_time)
        process.remaining_time -= execution_time
        current_time += execution_time
        
        # Add newly arrived processes
        for p in processes:
            if p.arrival_time <= current_time and p not in ready_queue:
                ready_queue.enqueue(p)
        
        # If process not complete, add back to queue
        if process.remaining_time > 0:
            ready_queue.enqueue(process)
        else:
            # Process completed
            process.completion_time = current_time
            calculate turnaround_time and waiting_time
            add to scheduled
```

---

## Folder Structure

```
nour/round-robin/
├── README.md                    # This file
├── code/
│   ├── rr.cpp                  # C++ implementation
│   ├── rr.py                   # Python implementation (optional)
│   └── input_processes.txt      # Test input file
└── results/
    ├── output_q4.txt           # Results for time quantum = 4
    ├── output_q8.txt           # Results for time quantum = 8
    ├── output_q16.txt          # Results for time quantum = 16
    ├── metrics.txt             # Performance metrics
    └── gantt_charts.txt        # Execution timelines
```

---

## Running the Program

### Prerequisites
- [Your chosen language compiler/interpreter]
- Standard C++ Library / Python 3.x

### Compilation/Execution

**For C++ (example):**
```bash
cd nour/round-robin/code
g++ -o rr rr.cpp
./rr input_processes.txt 4     # Run with time quantum = 4
./rr input_processes.txt 8     # Run with time quantum = 8
./rr input_processes.txt 16    # Run with time quantum = 16
```

**For Python (example):**
```bash
cd nour/round-robin/code
python rr.py input_processes.txt 4
python rr.py input_processes.txt 8
python rr.py input_processes.txt 16
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
Time Quantum: 4

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
Gantt Chart (Time Quantum = 4):
0   P1   4   P2   8   P3  10   P4  11   P1  15   P2  19   P3
|----|----|----|----|----|----|----|----|----|----|----|----|
```

---

## Testing

Create test cases including:
- **Multiple time quantums:** Test with at least 3 different time quantum values (4, 8, 16)
- **Varying burst times:** Processes with different execution lengths
- **Test case showing impact of time quantum** on average turnaround and waiting times
- Minimum 5 comprehensive test cases
- Document context switches for each quantum value

---

## Analysis Requirements

Compare the following across different time quantums:
- Average turnaround time
- Average waiting time
- Total context switches
- Discuss the trade-offs

---

## References

1. Silberschatz, A., Galvin, P., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.
2. [Round-robin scheduling](https://en.wikipedia.org/wiki/Round-robin_scheduling)

---

## Notes

- **Time Quantum Selection:** Show how different values affect performance
- **Fairness:** Highlight Round Robin's fairness compared to priority-based algorithms
- **Context Switching:** Document and analyze the impact of context switching
- **Gantt Charts:** Create visual representations of process execution
- **Detailed Comments:** Explain queue operations and time quantum handling
- **Comparison:** Compare with FCFS and SJF to highlight differences
- **Real-world:** Discuss how modern OS (Linux, Windows) use Round Robin variants
