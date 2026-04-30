# Comparative Analysis Template

Use this template to organize and compare results across all algorithms.

## Summary Comparison Table

| Metric | FCFS | SJF | Priority (NP) | SRTF | RR (q=4) | RR (q=8) |
|--------|------|-----|---------------|------|----------|----------|
| Average Turnaround Time | | | | | | |
| Average Waiting Time | | | | | | |
| Total Context Switches | 0 | 0 | 0 | | | |
| CPU Utilization | | | | | | |

## Test Case 1 Results

**Process Set:**
- P1: Arrival=0, Burst=5
- P2: Arrival=1, Burst=3
- P3: Arrival=2, Burst=8
- P4: Arrival=3, Burst=6
- P5: Arrival=4, Burst=2

### FCFS
- Average Turnaround Time: 
- Average Waiting Time: 

### SJF
- Average Turnaround Time: 
- Average Waiting Time: 

### Priority Scheduling (Non-Preemptive)
- Average Turnaround Time: 
- Average Waiting Time: 

### SRTF
- Average Turnaround Time: 
- Average Waiting Time: 
- Context Switches: 

### Round Robin (Time Quantum = 4)
- Average Turnaround Time: 
- Average Waiting Time: 
- Context Switches: 

### Round Robin (Time Quantum = 8)
- Average Turnaround Time: 
- Average Waiting Time: 
- Context Switches: 

## Observations

### Performance Ranking (for this test case):
1. Best: [Algorithm] - Reason?
2. Second: [Algorithm]
3. Third: [Algorithm]
4. Fourth: [Algorithm]
5. Fifth: [Algorithm]
6. Worst: [Algorithm]

### Key Insights:
- What did you observe about preemptive vs non-preemptive algorithms?
- How does time quantum affect Round Robin performance?
- What is the impact of priority levels?
- Any surprising results?

---

## Overall Analysis Across All Test Cases

### Which algorithm is best overall and why?

### Practical Recommendations:
- **For Interactive Systems:** 
- **For Batch Processing:** 
- **For Real-time Systems:** 
- **For General-Purpose OS:** 

---

## Additional Graphs/Figures

### Graph 1: Average Turnaround Time Comparison
[Description: Bar chart showing turnaround times for all algorithms across all test cases]

### Graph 2: Average Waiting Time Comparison
[Description: Bar chart showing waiting times for all algorithms across all test cases]

### Graph 3: Impact of Time Quantum on Round Robin
[Description: Line graph showing how different time quantums affect RR performance]

### Graph 4: Context Switches Analysis
[Description: Bar chart comparing context switches for preemptive algorithms]

---

## Sample Gantt Charts

### Test Case 1 - FCFS:
```
Timeline: [Visual representation]
```

### Test Case 1 - SRTF:
```
Timeline: [Visual representation]
```

### Test Case 1 - Round Robin (q=4):
```
Timeline: [Visual representation]
```
