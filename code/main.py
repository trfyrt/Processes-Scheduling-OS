from process import *
import pandas as pd


def run(process, quantumTime = None):
    fileName = process.upper() + '_Output'
    processes = []
    data = pd.read_excel('data/processes.xlsx')
    for i in range(0, len(data)):
        processes.append(Process(data['PID'][i], data['arrival_time'][i], data['Burst_time'][i]))
    
    results = None
    match process:
        case 'fcfs':
            print("Executing FCFS scheduling...")
            results = fcfs(processes)
        case 'sjfNone':
            print("Executing SJF Non-Preemptive scheduling...")
            results = sjfNone(processes)
        case 'sjf':
            print("Executing SJF Preemptive scheduling...")
            results = sjf(processes)
        case 'ljf':
            print("Executing LJF scheduling...")
            results = ljf(processes)
        case 'roundRobin':
            print(f"Executing Round Robin scheduling with quantum time {quantumTime}...")
            results = roundRobin(processes, quantumTime)
            
    if results is not None:
        data = {'process': [process.PID for process in processes],
        'arrivalTime': [process.arrivalTime for process in processes],
        'burstTime': [process.burstTime for process in processes],
        'remainingTime': [process.remainingTime for process in processes],
        'waitingTime': [process.waitingTime for process in processes],
        'completeTime': [process.completeTime for process in processes],
        'turnAroundTime': [process.turnAroundTime for process in processes],
        }
    
        totalWaitingTime = sum(process.waitingTime for process in processes)
        totalTurnAroundTime = sum(process.turnAroundTime for process in processes)
    
        AWT = totalWaitingTime / len(processes) if processes else 0
        ATAT = totalTurnAroundTime / len(processes) if processes else 0
        
        details = {
            'Metric': ["Total Process", "Average Waiting Time", "Total Waiting Time", 
                    "Average Turn Around Time", "Total Turn Around Time"],
            'Value': [len(processes), AWT, totalWaitingTime, ATAT, totalTurnAroundTime]
        }
        
        if quantumTime is not None:
            details['Metric'].append("Quantum Time")
            details['Value'].append(quantumTime)
            
        dfProcesses = pd.DataFrame(data)
        dfDetails = pd.DataFrame(details)

        with pd.ExcelWriter(f'data/{fileName}.xlsx') as writer:
            dfProcesses.to_excel(writer, sheet_name='Processes', index=False)
            dfDetails.to_excel(writer, sheet_name='Details', index=False)



print("Process Start!")
run('fcfs')
run('sjfNone')
run('sjf')
run('ljf')
run('roundRobin', 12)
print("Done")