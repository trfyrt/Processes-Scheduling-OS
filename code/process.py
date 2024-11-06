import pandas as pd
class Process:
    def __init__(self, PID, arrivalTime, burstTime):
        self.PID = PID
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.waitingTime = 0
        self.remainingTime = burstTime
        self.completeTime = 0
        self.turnAroundTime = 0
        self.startTime = arrivalTime

def fcfs(processes): #a. first come first serve
    time = 0
    queue = []
    running = None
    finishedJob = 0

    timeline = []
    
    while finishedJob < len(processes):
        for process in processes:
            if process.arrivalTime == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                lowest = running
                for q in queue:
                    if q.arrivalTime < lowest.arrivalTime and q.remainingTime > 0:
                        lowest = q
                if lowest is not running:
                    queue.remove(lowest)
                    queue.append(running)
                    running = lowest
        else:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remainingTime > 0:
                            lowest = q
                    else:
                        if q.arrivalTime < lowest.arrivalTime and q.remainingTime > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest

        timeline.append({
            'PID': running.PID if running is not None else None,
            'Remaining Time': running.remainingTime if running is not None else None,
            'Iteration': time
        })

        if running is not None:
            running.remainingTime -= 1
            running.turnAroundTime += 1
            if running.remainingTime == 0:
                finishedJob += 1
                running.completeTime = time + 1
                running = None
        
        for q in queue:
            q.waitingTime += 1
            q.turnAroundTime += 1
        time += 1
    
    timeline_df = pd.DataFrame(timeline)
    return processes, timeline_df

def sjfNon(processes): #b. Shortest Job First (None preemptive)
    time = 0
    queue = []
    running = None
    finishedJob = 0

    timeline = []
    
    while finishedJob < len(processes):
        for process in processes:
            if process.arrivalTime == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is None:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remainingTime > 0:
                            lowest = q
                    else:
                        if q.remainingTime < lowest.remainingTime and q.remainingTime > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest
    
        timeline.append({
        'PID': running.PID if running is not None else None,
        'Remaining Time': running.remainingTime if running is not None else None,
        'Iteration': time
        })

        if running is not None:
            running.remainingTime -= 1
            running.turnAroundTime += 1
            if running.remainingTime == 0:
                finishedJob += 1
                running.completeTime = time + 1
                running = None
        
        for q in queue:
            q.waitingTime += 1
            q.turnAroundTime += 1
        time += 1
    
    timeline_df = pd.DataFrame(timeline)
    return processes, timeline_df

def sjf(processes): #c. Shortest Job First (preemptive)
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    timeline = []

    while finishedJob < len(processes):
        for process in processes:
            if process.arrivalTime == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                lowest = running
                for q in queue:
                    if q.remainingTime < lowest.remainingTime and q.remainingTime > 0:
                        lowest = q
                if lowest is not running:
                    queue.remove(lowest)
                    queue.append(running)
                    running = lowest
        else:
            if len(queue) > 0:
                lowest = None
                for q in queue:
                    if lowest is None:
                        if q.remainingTime > 0:
                            lowest = q
                    else:
                        if q.remainingTime < lowest.remainingTime and q.remainingTime > 0:
                            lowest = q
                if lowest is not None:
                    queue.remove(lowest)
                    running = lowest

        timeline.append({
        'PID': running.PID if running is not None else None,
        'Remaining Time': running.remainingTime if running is not None else None,
        'Iteration': time
        })

        if running is not None:
            running.remainingTime -= 1
            running.turnAroundTime += 1
            if running.remainingTime == 0:
                finishedJob += 1
                running.completeTime = time + 1
                running = None
        
        for q in queue:
            q.waitingTime += 1
            q.turnAroundTime += 1
        time += 1

    timeline_df = pd.DataFrame(timeline)
    return processes, timeline_df

def ljf(processes): #d. Longest Job First (preemptive)
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    timeline = []

    while finishedJob < len(processes):
        for process in processes:
            if process.arrivalTime == time:
                if running is not None:
                    queue.append(process)
                else:
                    running = process
                
        if running is not None:
            if len(queue) > 0:
                highest = running
                for q in queue:
                    if q.remainingTime > highest.remainingTime and q.remainingTime > 0:
                        highest = q
                if highest is not running:
                    queue.remove(highest)
                    queue.append(running)
                    running = highest
        else:
            if len(queue) > 0:
                highest = None
                for q in queue:
                    if highest is None:
                        if q.remainingTime > 0:
                            highest = q
                    else:
                        if q.remainingTime > highest.remainingTime and q.remainingTime > 0:
                            highest = q
                if highest is not None:
                    queue.remove(highest)
                    running = highest

        timeline.append({
        'PID': running.PID if running is not None else None,
        'Remaining Time': running.remainingTime if running is not None else None,
        'Iteration': time
        })
                
        if running is not None:
            running.remainingTime -= 1
            running.turnAroundTime += 1
            if running.remainingTime == 0:
                finishedJob += 1
                running.completeTime = time + 1
                running = None
        
        for q in queue:
            q.waitingTime += 1
            q.turnAroundTime += 1
        time += 1

    timeline_df = pd.DataFrame(timeline)
    return processes, timeline_df

def roundRobin(processes, quantumTime): 
    counter = quantumTime
    time = 0
    queue = []
    running = None
    finishedJob = 0
    
    timeline = []

    while finishedJob < len(processes):    
        if counter == 0:
            if running is not None:
                queue.append(running)
                running = None
            counter = quantumTime
            
        for process in processes:
            if process.arrivalTime == time:
                queue.append(process)
        
        if running is None and len(queue) > 0:
            running = queue.pop(0)
            if running.startTime is None:
                running.startTime = time
            counter = quantumTime  # Reset counter untuk proses yang baru mulai

        timeline.append({
            'Iteration': time,
            'PID': running.PID if running is not None else None,
            'Remaining Time': running.remainingTime if running is not None else None
        })

        if running is not None:
            running.remainingTime -= 1
            running.turnAroundTime += 1
            counter -= 1
            
            if running.remainingTime == 0:
                finishedJob += 1
                running.completeTime = time + 1
                running = None
                counter = quantumTime  # Reset counter untuk proses berikutnya

        for q in queue:
            if q.remainingTime > 0:
                q.waitingTime += 1
                q.turnAroundTime += 1
        
        time += 1

    timeline_df = pd.DataFrame(timeline)
    return processes, timeline_df