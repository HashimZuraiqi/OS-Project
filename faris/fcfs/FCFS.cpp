/*
 *
 *  First-Come First-Served (FCFS) CPU Scheduling Algorithm
 *  Non-Preemptive
 * ───────────────────────────────────────────────────────
 *  How FCFS works:
 *    - Processes are executed in the order they arrive (arrival time).
 *    - Once a process starts, it runs to completion (non-preemptive).
 *    - Simple and fair in ordering, but can cause the "convoy effect"
 *      where short processes wait behind long ones.
 *
 *  Metrics calculated:
 *    - Completion Time  : when the process finishes execution
 *    - Turnaround Time  : Completion Time - Arrival Time
 *    - Waiting Time     : Turnaround Time - Burst Time
 */

#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

//Data structure representing a single process
struct Process {
    string id;           // Process identifier
    int    arrivalTime;  // Time the process enters the ready queue
    int    burstTime;    // CPU time the process needs to complete
    int    completionTime;  // Filled in by the scheduler
    int    turnaroundTime;  // Filled in by the scheduler
    int    waitingTime;     // Filled in by the scheduler
};

//FCFS Scheduler
void fcfsSchedule(vector<Process>& processes) {
    // Step 1: Sort processes by arrival time (FCFS order)
    sort(processes.begin(), processes.end(), [](const Process& a, const Process& b) {
        return a.arrivalTime < b.arrivalTime;
    });

    int currentTime = 0;

    //Step 2: Process each job in arrival order
    for (auto& p : processes) {
        //If CPU is idle before this process arrives, jump forward
        if (currentTime < p.arrivalTime) {
            currentTime = p.arrivalTime;
        }

        //Run the process to completion (non-preemptive)
        currentTime        += p.burstTime;
        p.completionTime    = currentTime;
        p.turnaroundTime    = p.completionTime - p.arrivalTime;
        p.waitingTime       = p.turnaroundTime - p.burstTime;
    }
}

//Print a Gantt Chart (Not required but for better visualization)
void printGanttChart(const vector<Process>& processes) {
    cout << "\n--- Gantt Chart ---\n";

    // Build a list of segments: each segment is either a process or an IDLE gap
    // A segment has a label, a start time, and an end time
    struct Segment {
        string label;
        int    start;
        int    end;
    };
    vector<Segment> segments;

    int clock = 0;
    for (const auto& p : processes) {
        // If there's a gap between the clock and this process's arrival → IDLE
        if (clock < p.arrivalTime) {
            segments.push_back({"IDLE", clock, p.arrivalTime});
            clock = p.arrivalTime;
        }
        // Add the process segment
        segments.push_back({p.id, clock, p.completionTime});
        clock = p.completionTime;
    }

    //Row 1: Top border
    cout << " ";
    for (const auto& s : segments)
        cout << "+----------";
    cout << "+\n";

    //Row 2: Labels
    cout << " ";
    for (const auto& s : segments)
        cout << "|  " << setw(6) << left << s.label << "  ";
    cout << "|\n";

    //Row 3: Bottom border
    cout << " ";
    for (const auto& s : segments)
        cout << "+----------";
    cout << "+\n";

    //Row 4: Time markers
    cout << " ";
    for (const auto& s : segments)
        cout << setw(11) << left << s.start;
    // Print the final end time of the last segment
    cout << segments.back().end << "\n";
}

//Print Results Table
void printResults(const vector<Process>& processes) {
    cout << "\n--- FCFS Scheduling Results ---\n";
    cout << left
         << setw(8)  << "Process"
         << setw(14) << "Arrival Time"
         << setw(12) << "Burst Time"
         << setw(18) << "Completion Time"
         << setw(18) << "Turnaround Time"
         << setw(14) << "Waiting Time"
         << "\n";
    cout << string(84, '-') << "\n";

    double totalTAT = 0, totalWT = 0;

    for (const auto& p : processes) {
        cout << left
             << setw(8)  << p.id
             << setw(14) << p.arrivalTime
             << setw(12) << p.burstTime
             << setw(18) << p.completionTime
             << setw(18) << p.turnaroundTime
             << setw(14) << p.waitingTime
             << "\n";
        totalTAT += p.turnaroundTime;
        totalWT  += p.waitingTime;
    }

    cout << string(84, '-') << "\n";
    int n = processes.size();
    cout << fixed << setprecision(2);
    cout << "\nAverage Turnaround Time : " << totalTAT / n << " ms\n";
    cout << "Average Waiting Time    : " << totalWT  / n << " ms\n";
}

//Run a single test case 
void runTestCase(int caseNum, const string& description, vector<Process> processes) {
    cout << "\n========================================\n";
    cout << " Test Case " << caseNum << ": " << description << "\n";
    cout << "========================================\n";

    fcfsSchedule(processes);
    printGanttChart(processes);
    printResults(processes);
}

//Main
int main() {
    cout << "============================================================\n";
    cout << "   First-Come First-Served (FCFS) CPU Scheduling Algorithm  \n";
    cout << "   Non-Preemptive                                           \n";
    cout << "============================================================\n";
    cout << "Hello user, if you want to use ur own input for testing the algorothim please enter 1, else (Hardcoded test cases) enter 2: " <<endl;

    int choice;
    cin >> choice;

    if (choice == 1) {
        int n;
        cout << "Enter the number of processes: ";
        cin >> n;

        vector<Process> userProcesses(n);
        for (int i = 0; i < n; ++i) {
            cout << "Enter Process ID, Arrival Time, and Burst Time for Process " << (i + 1) << ": ";
            cin >> userProcesses[i].id >> userProcesses[i].arrivalTime >> userProcesses[i].burstTime;
        }

        runTestCase(0, "User Input Test Case", userProcesses);
    } else if (choice == 2) {
    //Test Case 1: All processes arrive at time 0
    //Classic scenario: no idle time, pure burst-time execution order
    {
        vector<Process> tc1 = {
                {"P1", 0, 10},
                {"P2", 0,  5},
                {"P3", 0,  8},
                {"P4", 0,  3},
                {"P5", 0,  6},
        };
        runTestCase(1, "All processes arrive at time 0", tc1);
    }

    //Test Case 2: Processes with different arrival times
    //Demonstrates FCFS ordering based on arrival; possible idle CPU gaps
    {
        vector<Process> tc2 = {
                {"P1",  0,  6},
                {"P2",  2,  4},
                {"P3",  4,  7},
                {"P4",  6,  3},
                {"P5",  8,  5},
        };
        runTestCase(2, "Staggered arrival times", tc2);
    }

    //Test Case 3: Convoy effect demonstration
    //One very long process at the front makes short ones wait a long time
    {
        vector<Process> tc3 = {
                {"P1",  0, 30},   // Long process arriving first
                {"P2",  1,  2},
                {"P3",  2,  2},
                {"P4",  3,  2},
        };
        runTestCase(3, "Convoy effect (long process first)", tc3);
    }

    //Test Case 4: CPU idle gap between arrivals
    //Processes arrive with gaps; CPU has idle periods
    {
        vector<Process> tc4 = {
                {"P1",  0,  4},
                {"P2", 10,  3},
                {"P3", 15,  5},
        };
        runTestCase(4, "CPU idle gaps between arrivals", tc4);
    }
  }
  else {
        cout << "Invalid choice. Please run the program again and enter 1 or 2 \n";
    }
    cout << "\n============================================================\n";
    cout << "   End of FCFS Simulation\n";
    cout << "============================================================\n";
    
    return 0;
    
}