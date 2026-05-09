#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

// Structure for each process
struct Process {
    string id;
    int arrivalTime;
    int burstTime;
    int completionTime;
    int turnaroundTime;
    int waitingTime;
};

int main() {

    vector<Process> processes;

    // Sample processes
  ifstream inputFile("input_processes.txt");
  ofstream outputFile("output.txt");
  ofstream metricsFile("metrics.txt");

Process p;

while (inputFile >> p.id >> p.arrivalTime >> p.burstTime) {
    processes.push_back(p);
}

inputFile.close();

    // Print processes
    cout << "Processes Entered:\n";

    vector<Process> completed;

int currentTime = 0;

while (!processes.empty()) {

    vector<Process> available;

    // Find available processes
    for (auto p : processes) {
        if (p.arrivalTime <= currentTime) {
            available.push_back(p);
        }
    }

    // If no process available
    if (available.empty()) {
        currentTime++;
        continue;
    }

    // Find shortest burst time
    Process shortest = available[0];

    for (auto p : available) {
        if (p.burstTime < shortest.burstTime) {
            shortest = p;
        }
    }

    // Calculate times
    shortest.completionTime =
        currentTime + shortest.burstTime;

    shortest.turnaroundTime =
        shortest.completionTime - shortest.arrivalTime;

    shortest.waitingTime =
        shortest.turnaroundTime - shortest.burstTime;

    currentTime = shortest.completionTime;

    completed.push_back(shortest);

    // Remove completed process
    for (int i = 0; i < processes.size(); i++) {
        if (processes[i].id == shortest.id) {
            processes.erase(processes.begin() + i);
            break;
        }
    }
}
outputFile << "\nSJF Scheduling Result:\n";

outputFile << "Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting\n";

double totalWaiting = 0;
double totalTurnaround = 0;

for (auto p : completed) {

    outputFile << p.id << "\t"
               << p.arrivalTime << "\t"
               << p.burstTime << "\t"
               << p.completionTime << "\t\t"
               << p.turnaroundTime << "\t\t"
               << p.waitingTime << endl;

    totalWaiting += p.waitingTime;
    totalTurnaround += p.turnaroundTime;
}

metricsFile << "Average Waiting Time: "
            << totalWaiting / completed.size()
            << endl;

metricsFile << "Average Turnaround Time: "
            << totalTurnaround / completed.size()
            << endl;

outputFile.close();
metricsFile.close();

    return 0;
}