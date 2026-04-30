# Standard Test Cases for CPU Scheduling Algorithms

Use these test cases to ensure consistency across all algorithm implementations.

## Test Case 1: Basic Test
```
Process_ID Arrival_Time Burst_Time Priority(optional)
P1 0 5 1
P2 1 3 2
P3 2 8 3
P4 3 6 4
P5 4 2 5
```

## Test Case 2: Varying Burst Times
```
Process_ID Arrival_Time Burst_Time Priority(optional)
P1 0 10 1
P2 0 1 2
P3 0 2 3
P4 0 3 4
P5 0 4 5
```

## Test Case 3: Sequential Arrivals
```
Process_ID Arrival_Time Burst_Time Priority(optional)
P1 0 4 1
P2 2 3 2
P3 4 2 3
P4 6 5 4
P5 8 1 5
```

## Test Case 4: All Arrive at Same Time
```
Process_ID Arrival_Time Burst_Time Priority(optional)
P1 0 8 3
P2 0 6 1
P3 0 4 2
P4 0 2 5
P5 0 5 4
```

## Test Case 5: Random Arrivals
```
Process_ID Arrival_Time Burst_Time Priority(optional)
P1 1 7 2
P2 0 5 1
P3 3 3 4
P4 2 4 3
P5 4 2 5
```

## Notes:
- Priority column: Use 1 = Highest, 5 = Lowest (for Priority Scheduling)
- Time Quantum for Round Robin: Test with values 2, 4, 8
- All time values are in arbitrary time units (can be milliseconds, quanta, etc.)
- The burst times are realistic for CPU scheduling (typically 1-100 time units)

## Expected Output Template:
```
Test Case: X
Algorithm: [Algorithm Name]
[Additional Parameters: Time Quantum, Priority Scheme, etc.]

Execution Schedule:
Process | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time
[Results for each process]

Aggregate Metrics:
Average Turnaround Time: X.XX
Average Waiting Time: X.XX
[Additional metrics like context switches, if applicable]

Gantt Chart (optional):
[Timeline visualization]
```
