#include <iostream>
#include <vector>
#include <climits>
using namespace std;

// class for process
class Process {
public:
    int id;
    int arrival;
    int burst;
    int remaining;
    int completion;
    int turnaround;
    int waiting;

    Process(int id, int arrival, int burst) {
        this->id = id;
        this->arrival = arrival;
        this->burst = burst;
        this->remaining = burst;
        this->completion = 0;
        this->turnaround = 0;
        this->waiting = 0;
    }
};

int main() {
    int n;
    cout << "Enter number of processes: ";
    cin >> n;

    vector<Process> p;

    for (int i = 0; i < n; i++) {
        int arrival, burst;
        cout << "Process " << (i + 1) << " -> Arrival Time: ";
        cin >> arrival;
        cout << "Process " << (i + 1) << " -> Burst Time: ";
        cin >> burst;
        p.push_back(Process(i + 1, arrival, burst));
    }

    // SRTF algorithm implementation
    int completed = 0;
    int time = 0;
    int contextSwitches = 0;
    int lastRunning = -1;

    while (completed < n) {
        // Find process with shortest remaining time that has arrived
        int shortest = -1;
        int minRemaining = INT_MAX;

        for (int i = 0; i < n; i++) {
            if (p[i].arrival <= time && p[i].remaining > 0) {
                if (p[i].remaining < minRemaining) {
                    minRemaining = p[i].remaining;
                    shortest = i;
                }
            }
        }

        if (shortest == -1) {
            //if the shortest is -1 then there is no process to run
            time++;
            continue;
        }

        // check if there is a context switch
        if (lastRunning != -1 && lastRunning != shortest) {
            contextSwitches++;
        }
        lastRunning = shortest;

        // Run for 1 time unit
        p[shortest].remaining--;
        time++;

        // update process info if completed
        if (p[shortest].remaining == 0) {
            p[shortest].completion  = time;
            p[shortest].turnaround  = p[shortest].completion - p[shortest].arrival;
            p[shortest].waiting     = p[shortest].turnaround - p[shortest].burst;
            completed++;
            lastRunning = -1;
        }
    }

    // print the results
    cout << endl;
    cout << "---------------------------------------------------------------" << endl;
    cout << "PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting\n";
    cout << "---------------------------------------------------------------" << endl;

    double totalTAT = 0, totalWT = 0;
    for (int i = 0; i < n; i++) {
        cout << "P" << p[i].id    << "\t"
             << p[i].arrival      << "\t"
             << p[i].burst        << "\t"
             << p[i].completion   << "\t\t"
             << p[i].turnaround   << "\t\t"
             << p[i].waiting      << "\n";
        totalTAT += p[i].turnaround;
        totalWT  += p[i].waiting;
    }

    cout << "---------------------------------------------------------------" << endl;
    cout << "Average Turnaround Time : " << totalTAT / n << "\n";
    cout << "Average Waiting Time    : " << totalWT  / n << "\n";
    cout << "Total Context Switches  : " << contextSwitches << "\n";

    return 0;
}
